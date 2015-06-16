from nsbaseresource import NSBaseResource

__author__ = 'vlazarenko'


class NSCSPolicyCSPolicylabelBinding(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSCSPolicyCSPolicylabelBinding, self).__init__()
        self.options = {'policyname': '',
                        'priority': 0,
                        'targetvserver': '',
                        'gotopriorityexpression': '',
                        'invoke': False,
                        'labeltype': '',
                        'invoke_labelname': '',
                        'labelname': ''}

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

        self.resourcetype = NSCSPolicyCSPolicylabelBinding.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        return "cspolicylabel_cspolicy_binding"

    def set_policyname(self, policyname):
        """
        Bound classic (Compression/Authorization/Filter/Audit) policies to this vserver.

        Default value: 0
        """
        self.options['policyname'] = policyname

    def get_policyname(self):
        """
        Bound classic (Compression/Authorization/Filter/Audit) policies to this vserver.

        Default value: 0
        """
        return self.options['policyname']

    def set_priority(self, priority):
        """
        Priority for the policy.

        Default value: 0
        """
        self.options['priority'] = priority

    def get_priority(self):
        """
        Priority for the policy.

        Default value: 0
        """
        return self.options['priority']

    def set_gotopriorityexpression(self, gotopriorityexpression):
        """
        Expression specifying the priority of the next policy
        which will get evaluated if the current policy rule
        evaluates to TRUE.

        Default value: 0
        """
        self.options['gotopriorityexpression'] = gotopriorityexpression

    def get_gotopriorityexpression(self):
        """
        Expression specifying the priority of the next policy which
        will get evaluated if the current policy rule
        evaluates to TRUE.

        Default value: 0
        """
        return self.options['gotopriorityexpression']

    def set_bindpoint(self, bindpoint):
        """
        The bindpoint to which the policy is bound.

        Default value: 0
        """
        self.options['bindpoint'] = bindpoint

    def get_bindpoint(self):
        """
        The bindpoint to which the policy is bound.

        Default value: 0
        """
        return self.options['bindpoint']

    def set_invoke(self, invoke):
        """
        Invoke flag.

        Default value: 0
        """
        self.options['invoke'] = invoke

    def get_invoke(self):
        """
        Invoke flag.

        Default value: 0
        """
        return self.options['invoke']

    def get_invoke_labelname(self):
        """
        Invoke flag labelname.

        Default value: ''
        """
        return self.options['invoke_labelname']

    def set_invoke_labelname(self, labelname):
        """
        Set the invoke labelname.
        """
        self.options['invoke_labelname'] = labelname

    def set_labeltype(self, labeltype):
        """
        The invocation type.

        Default value: 0
        """
        self.options['labeltype'] = labeltype

    def get_labeltype(self):
        """
        The invocation type.

        Default value: 0
        """
        return self.options['labeltype']

    def set_labelname(self, labelname):
        """
        Name of the label invoked.

        Default value: 0
        """
        self.options['labelname'] = labelname

    def get_labelname(self):
        """
        Name of the label invoked.

        Default value: 0
        """
        return self.options['labelname']

    def set_name(self, name):
        """
        The virtual server name (created with the add cs vserver or add cr vserver command)
        for which the content switching policy will be set.

        Default value: 0
        Minimum length =  1.
        """
        self.options['name'] = name

    def get_name(self):
        """
        The virtual server name (created with the add cs vserver or add cr vserver command)
        for which the content switching policy will be set.

        Default value: 0
        Minimum length =  1.
        """
        return self.options['name']

    def set_targetvserver(self, targetvserver):
        """
        Target vserver name.

        Default value: 0
        """
        self.options['targetvserver'] = targetvserver

    def get_targetvserver(self):
        """
        Target vserver name.

        Default value: 0
        """
        return self.options['targetvserver']

    def get_hits(self):
        """
        Number of hits.

        Default value: 0
        """
        return self.options['hits']

    def get_rule(self):
        """
        Rule.

        Default value: 0
        """
        return self.options['rule']

    # Operations methods
    @staticmethod
    def get(nitro, csvserver_cspolicy_binding):
        """
        Use this API to fetch all configured csvserver_cspolicy_binding resources.
        """
        __url = (nitro.get_url() + NSCSPolicyCSPolicylabelBinding.get_resourcetype() +
                 "/" +
                 csvserver_cspolicy_binding.get_name())
        __json_resources = nitro.get(__url).get_response_field(NSCSPolicyCSPolicylabelBinding.get_resourcetype())
        __resources = []
        for json_resource in __json_resources:
            __resources.append(NSCSPolicyCSPolicylabelBinding(json_resource))
        return __resources

    @staticmethod
    def add(nitro, csvserver_cspolicy_binding):
        """
        Use this API to add csvserver_cspolicy_binding.
        """
        __csvserver_cspolicy_binding = NSCSPolicyCSPolicylabelBinding()
        __csvserver_cspolicy_binding.set_labelname(csvserver_cspolicy_binding.get_labelname())
        __csvserver_cspolicy_binding.set_policyname(csvserver_cspolicy_binding.get_policyname())
        __csvserver_cspolicy_binding.set_priority(csvserver_cspolicy_binding.get_priority())
        __csvserver_cspolicy_binding.set_targetvserver(csvserver_cspolicy_binding.get_targetvserver())
        __csvserver_cspolicy_binding.set_gotopriorityexpression(csvserver_cspolicy_binding.get_gotopriorityexpression())
        __csvserver_cspolicy_binding.set_invoke(csvserver_cspolicy_binding.get_invoke())
        __csvserver_cspolicy_binding.set_labeltype(csvserver_cspolicy_binding.get_labeltype())
        __csvserver_cspolicy_binding.set_invoke_labelname(csvserver_cspolicy_binding.get_invoke_labelname())
        return __csvserver_cspolicy_binding.update_resource(nitro)

    @staticmethod
    def delete(nitro, csvserver_cspolicy_binding):
        """
        Use this API to delete csvserver_cspolicy_binding of a given name.
        """
        __csvserver_cspolicy_binding = NSCSPolicyCSPolicylabelBinding()
        __csvserver_cspolicy_binding.set_name(csvserver_cspolicy_binding.get_name())
        __csvserver_cspolicy_binding.set_policyname(csvserver_cspolicy_binding.get_policyname())
        __csvserver_cspolicy_binding.set_priority(csvserver_cspolicy_binding.get_priority())
        __csvserver_cspolicy_binding.set_bindpoint(csvserver_cspolicy_binding.get_bindpoint())
        nsresponse = __csvserver_cspolicy_binding.delete_resource(nitro)
        return nsresponse
