from nsbaseresource import NSBaseResource
__author__ = 'Aleksandar Topuzovic'


class NSSSLCertLink(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSSSLCertLink, self).__init__()
        self.options = {'certkeyname': '',
                        'linkcertkeyname': ''}

        self.resourcetype = NSSSLCertLink.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        """
        Binding object showing the lbmonitor that can be bound to service.
        """
        return "sslcertlink"

    # Read only properties
    def get_certkeyname(self):
        """
        Certificate key name.
        """
        return self.options['certkeyname']

    def get_linkcertkeyname(self):
        """
        Name of the Certificate-Authority.
        """
        return self.options['linkcertkeyname']

    @staticmethod
    def get(nitro, resource):
        """
        Use this API to fetch resource resource of given name.
        """
        __resource = NSSSLCertLink()
        __resource.get_resource(nitro, resource.get_name())
        return __resource

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured resource resources.
        """
        __url = nitro.get_url() + NSSSLCertLink.get_resourcetype()
        __json_resources = nitro.get(__url).get_response_field(NSSSLCertLink.get_resourcetype())
        __resources = []
        for json_resource in __json_resources:
            __resources.append(NSSSLCertLink(json_resource))
        return __resources
