from nsbaseresource import NSBaseResource

__author__ = 'vlazarenko'


class NSSSLVServerSSLCertKeyBinding(NSBaseResource):

    # General Netscaler configuration object

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """

        super(NSSSLVServerSSLCertKeyBinding, self).__init__()

        self.options = {'certkeyname': '',
                        'cleartextport': '',
                        'crlcheck': '',
                        'ocspcheck': '',
                        'vservername': '',
                        'ca': '',
                        'snicert': ''}

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

        self.resourcetype = NSSSLVServerSSLCertKeyBinding.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        return "sslvserver_sslcertkey_binding"

    def set_certkeyname(self, certkeyname):
        self.options['certkeyname'] = certkeyname

    def get_certkeyname(self):
        return self.options['certkeyname']

    def set_cleartextport(self, cleartextport):
        self.options['cleartextport'] = cleartextport

    def get_cleartextport(self):
        return self.options['cleartextport']

    def set_crlcheck(self, crlcheck):
        self.options['crlcheck'] = crlcheck

    def get_crlcheck(self):
        return self.options['crlcheck']

    def set_ocspcheck(self, ocspcheck):
        self.options['ocspcheck'] = ocspcheck

    def get_ocspcheck(self):
        return self.options['ocspcheck']

    def set_vservername(self, vservername):
        self.options['vservername'] = vservername

    def get_vservername(self):
        return self.options['vservername']

    def set_ca(self, ca):
        self.options['ca'] = ca

    def get_ca(self):
        return self.options['ca']

    def set_snicert(self, snicert):
        self.options['snicert'] = snicert

    def get_snicert(self):
        return self.options['snicert']

    @staticmethod
    def get(nitro, resource):
        """
        Use this API to fetch SSL certkey resource of given name.
        """
        __url = nitro.get_url() + NSSSLVServerSSLCertKeyBinding.get_resourcetype() + "/" + resource.get_vservername()
        __json_resources = nitro.get(__url).get_response_field(NSSSLVServerSSLCertKeyBinding.get_resourcetype())
        __resources = []
        for json_resource in __json_resources:
            __resources.append(NSSSLVServerSSLCertKeyBinding(json_resource))
        return __resources

    @staticmethod
    def add(nitro, resource):
        """
        Use this API to add resource.
        """
        __resource = NSSSLVServerSSLCertKeyBinding()
        __resource.set_vservername(resource.get_vservername())
        __resource.set_certkeyname(resource.get_certkeyname())
        __resource.set_ca(resource.get_ca())
        __resource.set_crlcheck(resource.get_crlcheck())
        __resource.set_snicert(resource.get_snicert())
        __resource.set_ocspcheck(resource.get_ocspcheck())
        return __resource.add_resource(nitro)

    @staticmethod
    def delete(nitro, resource):
        """
        Use this API to delete server of a given name.
        """
        __resource = NSSSLVServerSSLCertKeyBinding()
        __resource.set_vservername(resource.get_vservername())
        __resource.set_certkeyname(resource.get_certkeyname())
        __resource.set_ca(resource.get_ca())
        __resource.set_crlcheck(resource.get_crlcheck())
        __resource.set_snicert(resource.get_snicert())
        nsresponse = __resource.delete_resource(nitro)
        return nsresponse
