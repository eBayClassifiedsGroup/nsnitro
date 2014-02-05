#!/opt/local/bin/python

"""
    Autogenerate Nsnitro exception classes from NITRO API Docs.
    Author: ndenev@amazon.com January, 2014

    Requires: BeautifulSoup for the html parsing

"""

from collections import OrderedDict
import argparse
import bs4
import os
import re
import string
import sys
import textwrap




""" location of the netscaler /var/netscaler/nitro/nitro-rest.tgz """
DOC = '/Users/ndenev/Netscaler/doc/html/errorlisting.html'

""" NSNitroError class definition at the beginning of the file """
HEADER = '''\
from collections import defaultdict


class NSNitroError(Exception):
    """ Custom exception class """
    def __init__(self, value, code=0):
        self.message = value
        self.code = code

    def __str__(self):
        return repr(self.message)


'''

""" Template for specific exception classes """
SPEC_EXC = string.Template('''\
class $exc($err_cls):
    """
        Nitro error code $errc
        $desc
    """
    pass


''')


""" Template for base exception classes """
BASE_EXC = string.Template('''\
class $err_cls(NSNitroError):
    """
        Base exception class $err_cls
    """
    pass


''')


def gen_exception_lookup_dict(exceptions):
    """ generate the exceptions lookup dictionary in nsexceptions/nsexceptions.py """
    lines = []
    lines.append("NSNitroExceptionClassMap = defaultdict(lambda: NSNitroError)")
    lines.append("NSNitroExceptions = {")
    for code, exception in exceptions.iteritems():
        lines.append("    {}: {},".format(code, exception))
    lines.append("}")
    lines.append("NSNitroExceptionClassMap.update(NSNitroExceptions)")
    lines.append("")
    return "\n".join(lines)

def gen__init__(exceptions):
    """ generate nsexceptions/__init__.py file """
    lines = []
    lines.append("from nsexceptions import NSNitroError")
    lines.append("from nsexceptions import NSNitroExceptionClassMap")
    for exception in exceptions.values():
        lines.append("from nsexceptions import {}".format(exception))
    lines.append("")
    lines.append("__all__ = ['NSNitroError',")
    lines.append("           'NSNitroExceptionClassMap',")
    for exception in exceptions.values():
        lines.append("           '{}',".format(exception))
    lines.append("          ]")
    lines.append("")
    return "\n".join(lines)

def parse_arguments():
    """ parse command line arguments """
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--errorlist", dest='html_errors', default=DOC, action='store',
        help="path to errorlisting.html file")
    arg_parser.add_argument("--write-files", dest='write_files', default=False, action='store_true',
        help="If specified writes __init__.py and nsexceptions.py files in the current directory")
    return arg_parser.parse_args()

def main():
    nsnitro_dir = os.path.dirname(os.path.realpath(__file__))
    args = parse_arguments()

    if args.write_files:
        init_file = open(os.path.join(nsnitro_dir, 'nsnitro/nsexceptions/__init__.py'), 'w')
        exceptions_file = open(os.path.join(nsnitro_dir, 'nsnitro/nsexceptions/nsexceptions.py'), 'w')
    else:
        init_file = exceptions_file = sys.stdout

    sys.stderr.write("printing header...\n")
    exceptions_file.write(HEADER)

    sys.stderr.write("opening HTML doc file.\n")
    with open(args.html_errors, 'r') as doc:
        html_doc = doc.read()

    sys.stderr.write("parsing HTML doc file...")
    soup = bs4.BeautifulSoup(html_doc)
    sys.stderr.write("done.\n")

    error_class = ""
    exceptions = OrderedDict()
 
    sys.stderr.write("generating exception classes...")
    rows = soup.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        """
            If we have one cell, use regex to check if the text ends on ERRORS,
            and capture it to be used as the name of the exception base class.
        """
        if len(cells) == 1:
            m = re.search("^\s*(.*\s+ERRORS)$", cells[0].get_text())
            if m:
                error_class = m.group(1)
                error_class = string.capwords(error_class)
                error_class = re.sub("\s", "", error_class)
                error_class = "NSNitro{}".format(error_class)
                exceptions_file.write(BASE_EXC.substitute(err_cls=error_class))
                next
        """
            If we have four cells, then this is a description of NITRO error:
            cell[0] : error name
            cell[1] : decimal error code
            cell[2] : hexadecimal error code
            cell[3] : error description
        """
        if len(cells) == 4:
            m1 = re.search("\d+", cells[1].get_text())
            m2 = re.search("0x[a-f0-9]+", cells[2].get_text())
            if m1 and m2:
                error_name = cells[0].get_text()
                error_code = cells[1].get_text()
                error_desc = cells[3].get_text()
                """ CamelCase error name to be used as exception class name """
                exception = string.capwords(error_name, "_")
                exception = re.sub("[_\s]", "", exception)
                exception = "NSNitro{}".format(exception)
                """ Just in case raise an exception if we see duplicate error code """
                if error_code in exceptions:
                    raise
                exceptions[error_code] = exception
                """ wrap long descriptions """
                desc = "\n        ".join(textwrap.wrap(error_desc,64))
                exceptions_file.write(SPEC_EXC.substitute(exc=exception, err_cls=error_class, errc=error_code, desc=desc))
    sys.stderr.write("done.\n")

    sys.stderr.write("generating exception lookup dictionary...")
    exceptions_file.write(gen_exception_lookup_dict(exceptions))
    sys.stderr.write("done.\n")

    sys.stderr.write("generating __init__.py file...")
    init_file.write(gen__init__(exceptions))
    sys.stderr.write("done.\n")

    exceptions_file.close()
    init_file.close()

if __name__ == "__main__":
    main()
