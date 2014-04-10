from nsbaseresource import NSBaseResource

__author__ = 'vlazarenko'


class NSRewritePolicy(NSBaseResource):

    # Configuration for content-switching policy resource.

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSRewritePolicy, self).__init__()
        self.options = {
            'name': '',
            'rule': '',
            'action': '',
            'undefaction': '',
            'comment': '',
            'logaction': '',
            'newname': '',
            'hits': '',
            'undefhits': '',
            'description': '',
        }

        self.resourcetype = NSRewritePolicy.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "rewritepolicy"

    def set_name(self, name):
        """
        Name of the rewrite policy.

        Default value: 0
        """
        self.options['name'] = name

    def get_name(self):
        """
        Name of the rewrite policy.

        Default value: 0
        """
        return self.options['name']

    def set_rule(self, rule):
        """
        Expression to be used by rewrite policy. It has to be a boolean PI rule expression.

        Default value: 0
        """
        self.options['rule'] = rule

    def get_rule(self):
        """
        Expression to be used by rewrite policy. It has to be a boolean PI rule expression.

        Default value: 0
        """
        return self.options['rule']

    def set_action(self, action):
        """
        Rewrite action to be used by the policy.

        Default value: 0
        """
        self.options['action'] = action

    def get_action(self):
        """
        Rewrite action to be used by the policy.

        Default value: 0
        """
        return self.options['action']

    def set_undefaction(self, undefaction):
        """
        A rewrite action, to be used by the policy when the rule evaluation turns out to be undefined.
        The undef action can be NOREWRITE, RESET or DROP.

        Default value: 0
        """
        self.options['undefaction'] = undefaction

    def get_undefaction(self):
        """
        A rewrite action, to be used by the policy when the rule evaluation turns out to be undefined.
        The undef action can be NOREWRITE, RESET or DROP.

        Default value: 0
        """
        return self.options['undefaction']

    def set_comment(self, comment):
        """
        Comments associated with this rewrite policy.

        Default value: 0
        """
        self.options['comment'] = comment

    def get_comment(self):
        """
        Comments associated with this rewrite policy.

        Default value: 0
        """
        return self.options['comment']

    def set_logaction(self, logaction):
        """
        The log action associated with the rewrite policy.

        Default value: 0
        """
        self.options['logaction'] = logaction

    def get_logaction(self):
        """
        The log action associated with the rewrite policy.

        Default value: 0
        """
        return self.options['logaction']

    def set_newname(self, newname):
        """
        The new name of the rewrite policy.

        Default value: 0
        Minimum length =  1.
        """
        self.options['newname'] = newname

    def get_newname(self):
        """
        The new name of the rewrite policy.

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

    def get_description(self):
        """
        Description of the policy.

        Default value: 0
        """
        return self.options['description']

    # Operations methods
    @staticmethod
    def get(nitro, rewritepolicy):
        """
        Use this API to fetch rewritepolicy resource of given name.
        """
        __rewritepolicy = NSRewritePolicy()
        __rewritepolicy.set_name(rewritepolicy.get_name())
        __rewritepolicy.get_resource(nitro)
        return __rewritepolicy

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured rewritepolicy resources.
        """
        __url = nitro.get_url() + NSRewritePolicy.get_resourcetype()
        __json_cspolicies = nitro.get(__url).get_response_field(NSRewritePolicy.get_resourcetype())
        __rewritepolicies = []
        for json_rewritepolicy in __json_cspolicies:
            __rewritepolicies.append(NSRewritePolicy(json_rewritepolicy))
        return __rewritepolicies

    @staticmethod
    def add(nitro, rewritepolicy):
        """
        Use this API to add rewritepolicy.
        """
        __rewritepolicy = NSRewritePolicy()
        __rewritepolicy.set_name(rewritepolicy.get_name())
        __rewritepolicy.set_rule(rewritepolicy.get_rule())
        __rewritepolicy.set_action(rewritepolicy.get_action())
        __rewritepolicy.set_undefaction(rewritepolicy.get_undefaction())
        __rewritepolicy.set_comment(rewritepolicy.get_comment())
        __rewritepolicy.set_logaction(rewritepolicy.get_logaction())
        return __rewritepolicy.add_resource(nitro)

    @staticmethod
    def delete(nitro, rewritepolicy):
        """
        Use this API to delete rewritepolicy of a given name.
        """
        __rewritepolicy = NSRewritePolicy()
        __rewritepolicy.set_name(rewritepolicy.get_name())
        nsresponse = __rewritepolicy.delete_resource(nitro)
        return nsresponse

    @staticmethod
    def update(nitro, rewritepolicy):
        """
        Use this API to update a rewritepolicy of a given name.
        """
        __rewritepolicy = NSRewritePolicy()
        __rewritepolicy.set_name(rewritepolicy.get_name())
        __rewritepolicy.set_rule(rewritepolicy.get_rule())
        __rewritepolicy.set_action(rewritepolicy.get_action())
        __rewritepolicy.set_undefaction(rewritepolicy.get_undefaction())
        __rewritepolicy.set_comment(rewritepolicy.get_comment())
        __rewritepolicy.set_logaction(rewritepolicy.get_logaction())
        return __rewritepolicy.update_resource(nitro)

    # No unset functionality for now.
    @staticmethod
    def rename(nitro, rewritepolicy):
        """
        Use this API to rename rewritepolicy.
        """
        __rewritepolicy = NSRewritePolicy()
        __rewritepolicy.set_name(rewritepolicy.get_name())
        __rewritepolicy.set_newname(rewritepolicy.get_newname())
        return __rewritepolicy.perform_operation(nitro, "rename")
