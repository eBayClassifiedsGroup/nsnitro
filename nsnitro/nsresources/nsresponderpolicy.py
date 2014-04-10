from nsbaseresource import NSBaseResource

__author__ = 'timl'


class NSResponderPolicy(NSBaseResource):

    # Configuration for content-switching policy resource.

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSResponderPolicy, self).__init__()
        self.options = {
            'name': '',
            'rule': '',
            'action': '',
            'hits': '',
            'undefhits': '',
            'newname': '',
            'activepolicy': '',
            'priority': '',
        }

        self.resourcetype = NSResponderPolicy.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "responderpolicy"

    def set_name(self, name):
        """
        Name of the responder policy.

        Default value: 0
        """
        self.options['name'] = name

    def get_name(self):
        """
        Name of the responder policy.

        Default value: 0
        """
        return self.options['name']

    def set_rule(self, rule):
        """
        Expression to be used by responder policy. It has to be a boolean PI rule expression.

        Default value: 0
        """
        self.options['rule'] = rule

    def get_rule(self):
        """
        Expression to be used by responder policy. It has to be a boolean PI rule expression.

        Default value: 0
        """
        return self.options['rule']

    def set_action(self, action):
        """
        Responder action to be used by the policy.

        Default value: 0
        """
        self.options['action'] = action

    def get_action(self):
        """
        Responder action to be used by the policy.

        Default value: 0
        """
        return self.options['action']

    def set_newname(self, newname):
        """
        The new name of the responder policy.

        Default value: 0
        Minimum length =  1.
        """
        self.options['newname'] = newname

    def get_newname(self):
        """
        The new name of the responder policy.

        Default value: 0
        Minimum length =  1.
        """
        return self.options['newname']

    def get_hits(self):
        """
        Number of hits.

        Default value: 0
        """
        return self.options['hits']

    def get_undefhits(self):
        """
        Number of undef hits.

        Default value: 0
        """
        return self.options['undefhits']

    def get_activepolicy(self):
        """
        Policy is in use.

        Default value: 0
        """
        return self.options['activepolicy']

    def set_priority(self, priority):
        """
        Set the priority for the responder policy.

        Default value: 0
        """
        self.options['priority'] = priority

    def get_priority(self):
        """
        Priority of the responder policy.

        Default value: 0
        """
        return self.options['priority']

    # Operations methods
    @staticmethod
    def get(nitro, responderpolicy):
        """
        Use this API to fetch responderpolicy resource of given name.
        """
        __responderpolicy = NSResponderPolicy()
        __responderpolicy.set_name(responderpolicy.get_name())
        __responderpolicy.get_resource(nitro)
        return __responderpolicy

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured responderpolicy resources.
        """
        __url = nitro.get_url() + NSResponderPolicy.get_resourcetype()
        __json_cspolicies = nitro.get(__url).get_response_field(NSResponderPolicy.get_resourcetype())
        __responderpolicies = []
        for json_responderpolicy in __json_cspolicies:
            __responderpolicies.append(NSResponderPolicy(json_responderpolicy))
        return __responderpolicies

    @staticmethod
    def add(nitro, responderpolicy):
        """
        Use this API to add responderpolicy.
        """
        __responderpolicy = NSResponderPolicy()
        __responderpolicy.set_name(responderpolicy.get_name())
        __responderpolicy.set_rule(responderpolicy.get_rule())
        __responderpolicy.set_action(responderpolicy.get_action())
        __responderpolicy.set_priority(responderpolicy.get_priority())
        return __responderpolicy.add_resource(nitro)

    @staticmethod
    def delete(nitro, responderpolicy):
        """
        Use this API to delete responderpolicy of a given name.
        """
        __responderpolicy = NSResponderPolicy()
        __responderpolicy.set_name(responderpolicy.get_name())
        nsresponse = __responderpolicy.delete_resource(nitro)
        return nsresponse

    @staticmethod
    def update(nitro, responderpolicy):
        """
        Use this API to update a responderpolicy of a given name.
        """
        __responderpolicy = NSResponderPolicy()
        __responderpolicy.set_name(responderpolicy.get_name())
        __responderpolicy.set_rule(responderpolicy.get_rule())
        __responderpolicy.set_action(responderpolicy.get_action())
        __responderpolicy.set_priority(responderpolicy.get_priority())
        return __responderpolicy.update_resource(nitro)

    # No unset functionality for now.
    @staticmethod
    def rename(nitro, responderpolicy):
        """
        Use this API to rename responderpolicy.
        """
        __responderpolicy = NSResponderPolicy()
        __responderpolicy.set_name(responderpolicy.get_name())
        __responderpolicy.set_newname(responderpolicy.get_newname())
        return __responderpolicy.perform_operation(nitro, "rename")
