from nsbaseresource import NSBaseResource
__author__ = 'Aleksandar Topuzovic'


class NSSSLVServerSSLPolicyBinding(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSSSLVServerSSLPolicyBinding, self).__init__()
        self.options = {'priority': '',
                        'policyname': '',
                        'vservername': '',
                        'polinherit': ''}

        self.resourcetype = NSSSLVServerSSLPolicyBinding.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        """
        Binding object showing the lbmonitor that can be bound to service.
        """
        return "sslvserver_sslpolicy_binding"

    # Read/write properties
    def set_priority(self, priority):
        """
        The priority of the policies bound to this SSL service.
        """
        self.options['priority'] = priority

    def get_priority(self):
        """
        The priority of the policies bound to this SSL service.
        """
        return self.options['priority']

    def set_policyname(self, policyname):
        """
        The name of the SSL policy binding.
        """
        self.options['policyname'] = policyname

    def get_policyname(self):
        """
        The name of the SSL policy binding.
        """
        return self.options['policyname']

    def set_vservername(self, vservername):
        """
        The name of the SSL virtual server to which the SSL policy needs to be bound.
        Minimum length = 1
        """
        self.options['vservername'] = vservername

    def get_vservername(self):
        """
        The name of the SSL virtual server to which the SSL policy needs to be bound.
        Minimum length = 1
        """
        return self.options['vservername']

    # Read only properties
    def get_polinherit(self):
        """
        Whether the bound policy is a inherited policy or not.
        """
        return self.options['polinherit']

    @staticmethod
    def get(nitro, resource):
        """
        Use this API to fetch sslvserver resource of given name.
        """
        __url = nitro.get_url() + NSSSLVServerSSLPolicyBinding.get_resourcetype() + \
            "/" + resource.get_vservername()
        __json_resources = nitro.get(__url).get_response_field(
            NSSSLVServerSSLPolicyBinding.get_resourcetype())
        __resources = []
        for json_resource in __json_resources:
            __resources.append(NSSSLVServerSSLPolicyBinding(json_resource))
        return __resources

    @staticmethod
    def add(nitro, resource):
        """
        Use this API to add resource.
        """
        __resource = NSSSLVServerSSLPolicyBinding()
        __resource.set_vservername(resource.get_vservername())
        __resource.set_policyname(resource.get_policyname())
        __resource.set_priority(resource.get_priority())
        return __resource.add_resource(nitro)

    @staticmethod
    def delete(nitro, resource):
        """
        Use this API to delete server of a given name.
        """
        __resource = NSSSLVServerSSLPolicyBinding()
        __resource.set_vservername(resource.get_vservername())
        return __resource.delete_resource(nitro)
