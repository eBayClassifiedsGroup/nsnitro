from nsbaseresource import NSBaseResource


class NSSimpleacl(NSBaseResource):

    # Configuration for ACL entry resource.

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSSimpleacl, self).__init__()
        self.options = {
            'aclname': '',
            'aclaction': '',
            'srcip': '',
            'destport': '',
            'ttl': '',
            'protocol': '',
            'hits': '',
            '__count': '',
            'estSessions': ''
        }

        self.resourcetype = NSSimpleacl.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "nssimpleacl"

    def set_aclname(self, aclname):
        """
        The alphanumeric name of the ACL.
        Default value: 0
        Minimum length =  1.
        """
        self.options['aclname'] = aclname

    def get_aclname(self):
        """
        The action associated with the ACL.
        Default value: 0
        """
        return self.options['aclname']

    def set_aclaction(self, aclaction):
        """
        The action associated with the ACL.
        Default value: 0
        """
        self.options['aclaction'] = aclaction

    def get_aclaction(self):
        """
        The action associated with the ACL.
        Default value: 0
        """
        return self.options['aclaction']

    def set_srcip(self, srcip):
        """
        The source IP address (range).
        Default value: 0
        """
        self.options['srcip'] = srcip

    def get_srcip(self):
        """
        The source IP address (range).
        Default value: 0
        """
        return self.options['srcip']

    def set_destport(self, destport):
        """
        The destination Port (range).
        Default value: 0
        """
        self.options['destport'] = destport

    def get_destport(self):
        """
        The destination Port (range).
        Default value: 0
        """
        return self.options['destport']


    def set_ttl(self, ttl):
        """
        The time to expire this ACL(in seconds).
        Default value: 0
        Minimum value =  4
        Maximum value =  2147483647
        """
        self.options['ttl'] = ttl

    def get_ttl(self):
        """
        The time to expire this ACL(in seconds).
        Default value: 0
        Minimum value =  4
        Maximum value =  2147483647
        """
        return self.options['ttl']

    def set_protocol(self, protocol):
        """
        The IP protocol name.
        Default value: 0
        """
        self.options['protocol'] = protocol

    def get_protocol(self):
        """
        The IP protocol name.
        Default value: 0
        """
        return self.options['protocol']

    def get_hits(self):
        """
        The hits of this ACL.
        Default value: 0
        """
        return self.options['hits']

    def set_estSessions(self, estSessions):
        """
        The IP protocol name.
        Default value: 0
        """
        self.options['estSessions'] = estSessions

    def get_estSessions(self):
        """
        The IP protocol name.
        Default value: 0
        """
        return self.options['estSessions']


    # Operations methods

    @staticmethod
    def add(nitro, nssimpleacl):
        """
        Use this API to add nssimpleacl resources.
        """
        __nssimpleacl = NSSimpleacl()
        __nssimpleacl.set_aclname(nssimpleacl.get_aclname())
        __nssimpleacl.set_aclaction(nssimpleacl.get_aclaction())
        __nssimpleacl.set_srcip(nssimpleacl.get_srcip())
        __nssimpleacl.set_destport(nssimpleacl.get_destport())
        __nssimpleacl.set_ttl(nssimpleacl.get_ttl())
        __nssimpleacl.set_protocol(nssimpleacl.get_protocol())
        return __nssimpleacl.add_resource(nitro)

    @staticmethod
    def delete(nitro, nssimpleacl):
        """
        Use this API to delete nssimpleacl resources.
        """
        __nssimpleacl = NSSimpleacl()
        __nssimpleacl.set_aclname(nssimpleacl.get_aclname())
        nsresponse = __nssimpleacl.delete_resource(nitro, nssimpleacl.get_aclname())
        return nsresponse


    @staticmethod
    def get(nitro, nssimpleacl):
        """
        Use this API to fetch nssimpleacl resource of given name.
        """
        __nssimpleacl = NSSimpleacl()
        __nssimpleacl.set_aclname(nssimpleacl.get_aclname())
        __nssimpleacl.get_resource(nitro, object_name=__nssimpleacl.get_aclname())
        return __nssimpleacl

    @staticmethod
    def clear(nitro):
        """
        Use this API to clear nssimpleacl resources.
        """
        __nssimpleacl = NSSimpleacl()
        return __nssimpleacl.perform_operation(nitro, "clear")

    @staticmethod
    def flush(nitro):
        """
        Use this API to clear nssimpleacl resources.
        """
        __nssimpleacl = NSSimpleacl()
        __nssimpleacl.set_estSessions(True)
        return __nssimpleacl.perform_operation(nitro, "flush")


    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured nssimpleacl resources.
        """
        __url = nitro.get_url() + NSSimpleacl.get_resourcetype()
        __json_nssimpleacls = nitro.get(__url).get_response_field(NSSimpleacl.get_resourcetype())
        __nssimpleacls = []
        for json_nssimpleacl in __json_nssimpleacls:
            __nssimpleacls.append(NSSimpleacl(json_nssimpleacl))
        return __nssimpleacls
