# encoding: utf-8
from nsbaseresource import NSBaseResource


class NSGSLBService(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSGSLBService, self).__init__()

        self.options = {
            'servicename': '',
            'cnameentry': '',
            'ip': '',
            'servername': '',
            'servicetype': '',
            'port': '',
            'publicip': '',
            'healthmonitor': '',
            'sitename': '',
            'state': '',
            'cip': '',
            'sitepersistence': '',
            'ipaddress': '',
            'weight': '',
        }

        self.resourcetype = NSGSLBService.get_resourcetype()
        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "gslbservice"

    def set_servicename(self, servicename):
        """
        The gslb virtual name
        """
        self.options['servicename'] = servicename

    def get_servicename(self):
        """
        """
        return self.options['servicename']

    def set_servername(self, servername):
        """
        The gslb virtual name
        """
        self.options['servername'] = servername

    def get_servername(self):
        """
        """
        return self.options['servername']

    def set_servicetype(self, servicetype):
        """
        The gslb virtual name
        """
        self.options['servicetype'] = servicetype

    def get_servicetype(self):
        """
        """
        return self.options['servicetype']

    def set_sitename(self, sitename):
        """
        The gslb virtual name
        """
        self.options['sitename'] = sitename

    def get_sitename(self):
        """
        """
        return self.options['sitename']

    def get_publicip(self):
        """
        """
        return self.options['publicip']

    def get_ip(self):
        """
        """
        return self.options['ip']

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured gslbservice resources.
        """
        __url = nitro.get_url() + NSGSLBService.get_resourcetype()
        __json_gslbvservers = nitro.get(__url).get_response_field(
            NSGSLBService.get_resourcetype())
        __gslbvservers = []
        for json_gslbvserver in __json_gslbvservers:
            __gslbvservers.append(NSGSLBService(json_gslbvserver))
        return __gslbvservers
