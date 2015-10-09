# encoding: utf-8
from nsbaseresource import NSBaseResource


class NSGSLBVServerBinding(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSGSLBVServerBinding, self).__init__()

        self.options = {
            'name': '',
            # --- read-only options ---
            'gslbvserver_spilloverpolicy_binding': '',
            'gslbvserver_gslbservice_binding': '',
            'gslbvserver_domain_binding': ''
        }

        self.resourcetype = NSGSLBVServerBinding.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "gslbvserver_binding"

    def set_name(self, name):
        """
        """
        self.options['name'] = name

    def get_name(self):
        """
        """
        return self.options['name']

    def set_gslbservice_binding(self, binding):
        """
        """
        self.options['gslbvserver_gslbservice_binding'] = binding

    def get_gslbservice_binding(self):
        """
        """
        return self.options['gslbvserver_gslbservice_binding']

    def set_spilloverpolicy_binding(self, binding):
        """
        """
        self.options['gslbvserver_spilloverpolicy_binding'] = binding

    def get_spilloverpolicy_binding(self):
        """
        """
        return self.options['gslbvserver_spilloverpolicy_binding']

    def set_domain_binding(self, binding):
        """
        """
        self.options['gslbvserver_domain_binding'] = binding

    def get_domain_binding(self):
        """
        """
        return self.options['gslbvserver_domain_binding']

    @staticmethod
    def get(nitro, gslbvserver_binding):
        """
        Use this API to fetch csvserver resource of given name.
        """
        __gslbvserver_binding = NSGSLBVServerBinding()
        __gslbvserver_binding.set_name(gslbvserver_binding.get_name())
        __gslbvserver_binding.get_resource(nitro)
        return __gslbvserver_binding
