# encoding: utf-8
from nsbaseresource import NSBaseResource


class NSGSLBVServerGSLBServiceBinding(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSGSLBVServerGSLBServiceBinding, self).__init__()

        self.options = {
            'name': '',
            'weight': '',
            'servicename': '',
            'domainname': '',
            # --- Read-only options ---
            'cnameentry': '',
            'gslbthreshold': '',
            'port': '',
            'iscname': '',
            'curstate': '',
            'preferredlocation': '',
            'svreffgslbstate': '',
            'dynamicconfwt': '',
            'sitepersistence': '',
            'thresholdvalue': '',
            'servicetype': '',
            'ipaddress': '',
            'cumulativeweight': '',
            '__count': ''
        }

        self.resourcetype = NSGSLBVServerGSLBServiceBinding.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "gslbvserver_gslbservice_binding"

    def set_name(self, name):
        """
        """
        self.options['name'] = name

    def get_name(self):
        """
        """
        return self.options['name']

    def get_ipaddress(self):
        """
        """
        return self.options['ipaddress']

    @staticmethod
    def get(nitro, gslbservice_binding):
        """
        Use this API to fetch csvserver resource of given name.
        """
        __gslbservice_binding = NSGSLBVServerGSLBServiceBinding()
        __gslbservice_binding.set_name(gslbservice_binding.get_name())
        __gslbservice_binding.get_resource(nitro)
        return __gslbservice_binding
