import os
from setuptools import setup,find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "nsnitro",
    version = "1.0.34",
    author = "Vladimir Lazarenko",
    author_email = "vllazarenko@ebay.com",
    description = ("A simple library to control Citrix Netscaler 9.2+ with NITRO API."),
    license = "GPL",
    keywords = "citrix netscaler nitro api nsnitro",
    url = "http://pypi.python.org/pypi/nsnitro",
    packages=["nsnitro"] + [os.path.join("nsnitro",a) for a in find_packages("nsnitro")],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: Python Software Foundation License",
    ],
    install_requires=[
        "httplib2",
        "argparse",
    ],
    scripts=[
        'bin/nsnitrocmd.py'
    ],
)
