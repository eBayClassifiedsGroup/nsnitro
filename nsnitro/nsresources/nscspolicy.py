from nsbaseresource import NSBaseResource

__author__ = 'vlazarenko'


class NSCSPolicy(NSBaseResource):

    # Configuration for content-switching policy resource.

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSCSPolicy, self).__init__()
        self.options = {'policyname': '',
                        'url': '',
                        'rule': '',
                        'domain': '',
                        'vstype': '',
                        'hits': '',
                        'bindhits': '',
                        'labelname': '',
                        'labeltype': '',
                        'target': '',
                        'priority': '',
                        '__count': ''}

        self.resourcetype = NSCSPolicy.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "cspolicy"

    def set_policyname(self, policyname):
        """
        The name of the new content switching policy.

        Default value: 0
        Minimum length =  1.
        """
        self.options['policyname'] = policyname

    def get_policyname(self):
        """
        The name of the new content switching policy.

        Default value: 0
        Minimum length =  1.
        """
        return self.options['policyname']

    def set_url(self, url):
        """
        The URL, with wildcards.
        Specify the string value in this format:
        // [[prefix ] [*]] [.suffix].

        Default value: 0
        Minimum length =  1.
        Maximum length =  208.
        """
        self.options['url'] = url

    def get_url(self):
        """
        The URL, with wildcards.
        Specify the string value in this format:
        // [[prefix ] [*]] [.suffix].

        Default value: 0
        Minimum length =  1.
        Maximum length =  208.
        """
        return self.options['url']

    def set_rule(self, rule):
        """
        The condition for applying this policy.
        Expression logic is as follows:
                - Expression names separated by the logical operators || and &&.
                - Expression names may be grouped using parenthesis.
                - If the expression contains blanks (e.g., between an expression name and a logical operator),
                        then the entire argument must be enclosed in double quotes.
        The following example shows valid expression logic:
                ns_ext_cgi||ns_ext_asp
                "ns_non_get && (ns_header_cookie||ns_header_pragma)".

        Default value: 0
        """
        self.options['rule'] = rule

    def get_rule(self):
        """
        The condition for applying this policy.
        Expression logic is as follows:
                - Expression names separated by the logical operators || and &&.
                - Expression names may be grouped using parenthesis.
                - If the expression contains blanks (e.g., between an expression name and a logical operator),
                        then the entire argument must be enclosed in double quotes.
        The following example shows valid expression logic:
                ns_ext_cgi||ns_ext_asp
                "ns_non_get && (ns_header_cookie||ns_header_pragma)".

        Default value: 0
        """
        return self.options['rule']

    def set_domain(self, domain):
        """
        The domain name. The string value can range to 63 characters.

        Default value: 0
        Minimum length =  1.
        """
        self.options['domain'] = domain

    def get_domain(self):
        """
        The domain name. The string value can range to 63 characters.

        Default value: 0
        Minimum length =  1.
        """
        return self.options['domain']

    def get_vstype(self):
        """
        Virtual server type.

        Default value: 0
        """
        return self.options['vstype']

    def get_hits(self):
        """
        Total number of hits.

        Default value: 0
        """
        return self.options['hits']

    def get_bindhits(self):
        """
        Total number of hits.

        Default value: 0
        """
        return self.options['bindhits']

    def get_labelname(self):
        """
        Name of the label invoked.

        Default value: 0
        """
        return self.options['labelname']

    def get_labeltype(self):
        """
        The invocation type.

        Default value: 0
        """
        return self.options['labeltype']

    def get_target(self):
        """
        Target flag.

        Default value: 0
        """
        return self.options['target']

    def get_priority(self):
        """
        Priority of bound policy.

        Default value: 0
        """
        return self.options['priority']

    # Operations methods
    @staticmethod
    def get(nitro, cspolicy):
        """
        Use this API to fetch cspolicy resource of given name.
        """
        __cspolicy = NSCSPolicy()
        __cspolicy.set_policyname(cspolicy.get_policyname())
        __cspolicy.get_resource(nitro)
        return __cspolicy

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured cspolicy resources.
        """
        __url = nitro.get_url() + NSCSPolicy.get_resourcetype()
        __json_cspolicies = nitro.get(__url).get_response_field(NSCSPolicy.get_resourcetype())
        __cspolicies = []
        for json_cspolicy in __json_cspolicies:
            __cspolicies.append(NSCSPolicy(json_cspolicy))
        return __cspolicies

    @staticmethod
    def add(nitro, cspolicy):
        """
        Use this API to add cspolicy.
        """
        __cspolicy = NSCSPolicy()
        __cspolicy.set_policyname(cspolicy.get_policyname())
        __cspolicy.set_url(cspolicy.get_url())
        __cspolicy.set_rule(cspolicy.get_rule())
        __cspolicy.set_domain(cspolicy.get_domain())
        return __cspolicy.add_resource(nitro)

    @staticmethod
    def delete(nitro, cspolicy):
        """
        Use this API to delete cspolicy of a given name.
        """
        __cspolicy = NSCSPolicy()
        __cspolicy.set_policyname(cspolicy.get_policyname())
        nsresponse = __cspolicy.delete_resource(nitro)
        return nsresponse

    @staticmethod
    def update(nitro, cspolicy):
        """
        Use this API to update a cspolicy of a given name.
        """
        __cspolicy = NSCSPolicy()
        __cspolicy.set_policyname(cspolicy.get_policyname())
        __cspolicy.set_url(cspolicy.get_url())
        __cspolicy.set_rule(cspolicy.get_rule())
        __cspolicy.set_domain(cspolicy.get_domain())
        return __cspolicy.update_resource(nitro)


    # No unset functionality for now.
