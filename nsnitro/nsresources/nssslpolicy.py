from nsbaseresource import NSBaseResource
__author__ = 'Aleksandar Topuzovic'


class NSSSLPolicy(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSSSLPolicy, self).__init__()
        self.options = {'name': '',
                        'rule': '',
                        'reqaction': '',
                        'action': '',
                        'hits': ''}

        self.resourcetype = NSSSLPolicy.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        """
        Binding object showing the lbmonitor that can be bound to service.
        """
        return "sslpolicy"

    # Read/write properties
    def set_name(self, name):
        """
        The name for the new SSL policy. Maximum Length: 32.
        Minimum length = 1
        """
        self.options['name'] = name

    def get_name(self):
        """
        The name for the new SSL policy. Maximum Length: 32.
        Minimum length = 1
        """
        return self.options['name']

    def set_rule(self, rule):
        """
        The expression that sets the condition for application of the SSL policy. Maximum Length:1500.
        """
        self.options['rule'] = rule

    def get_rule(self):
        """
        The expression that sets the condition for application of the SSL policy. Maximum Length:1500.
        """
        return self.options['rule']

    def set_reqaction(self, reqaction):
        """
        The name of the action to be performed on the request. Refer to 'add ssl action' command to add a new action.
        Minimum length = 1
        """
        self.options['reqaction'] = reqaction

    def get_reqaction(self):
        """
        The name of the action to be performed on the request. Refer to 'add ssl action' command to add a new action.
        Minimum length = 1
        """
        return self.options['reqaction']

    # Read only properties
    def get_action(self):
        """
        The name of the action to be performed on the request.
        """
        return self.options['action']

    def get_hits(self):
        """
        Number of hits for this policy.
        """
        return self.options['hits']

    @staticmethod
    def get(nitro, sslpolicy):
        """
        Use this API to fetch sslpolicy resource of given name.
        """
        __sslpolicy = NSSSLPolicy()
        __sslpolicy.get_resource(nitro, sslpolicy.get_name())
        return __sslpolicy

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured sslpolicy resources.
        """
        __url = nitro.get_url() + NSSSLPolicy.get_resourcetype()
        __json_sslpolicies = nitro.get(__url).get_response_field(NSSSLPolicy.get_resourcetype())
        __sslpolicies = []
        for json_sslpolicy in __json_sslpolicies:
            __sslpolicies.append(NSSSLPolicy(json_sslpolicy))
        return __sslpolicies

    @staticmethod
    def add(nitro, resource):
        """
        Use this API to add resource.
        """
        __resource = NSSSLPolicy()
        __resource.set_name(resource.get_name())
        __resource.set_rule(resource.get_rule())
        __resource.set_reqaction(resource.get_reqaction())
        return __resource.add_resource(nitro)

    @staticmethod
    def delete(nitro, resource):
        """
        Use this API to delete server of a given name.
        """
        __resource = NSSSLPolicy()
        __resource.set_name(resource.get_name())
        return __resource.delete_resource(nitro)