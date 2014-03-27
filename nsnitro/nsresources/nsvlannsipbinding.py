from nsbaseresource import NSBaseResource

__author__ = 'vlazarenko'


class NSVLANNSIPBinding(NSBaseResource):

    # General Netscaler configuration object

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """

        super(NSVLANNSIPBinding, self).__init__()

        self.options = {
            'ipaddress': '',
            'netmask': '',
            'rnat': '',
            'id': '',
        }

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

        self.resourcetype = NSVLANNSIPBinding.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        return "vlan_nsip_binding"

    def set_ipaddress(self, ipaddress):
        self.options['ipaddress'] = ipaddress

    def get_ipaddress(self):
        return self.options['ipaddress']

    def set_netmask(self, netmask):
        self.options['netmask'] = netmask

    def get_netmask(self):
        return self.options['netmask']

    def set_rnat(self, rnat):
        self.options['rnat'] = rnat

    def get_rnat(self):
        return self.options['rnat']

    def set_id(self, id):
        self.options['id'] = id

    def get_id(self):
        return self.options['id']

    @staticmethod
    def add(nitro, resource):
        __resource = NSVLANNSIPBinding()
        __resource.set_id(resource.get_id())
        __resource.set_ipaddress(resource.get_ipaddress())
        __resource.set_netmask(resource.get_netmask())
        return __resource.add_resource(nitro)

    @staticmethod
    def delete(nitro, resource):
        __resource = NSVLANNSIPBinding()
        __resource.set_id(resource.get_id())
        __resource.set_ipaddress(resource.get_ipaddress())
        __resource.set_netmask(resource.get_netmask())
        nsresponse = __resource.delete_resource(nitro, object_name=__resource.get_id())
        return nsresponse

    @staticmethod
    def get(nitro, resource):
        """
        Use this API to fetch service resource of given name.
        """
        __resource = NSVLANNSIPBinding()
        __resource.set_id(resource.get_id())
        __resource.get_resource(nitro, object_name=resource.get_id())
        return __resource
