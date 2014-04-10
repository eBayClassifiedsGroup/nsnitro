from nsbaseresource import NSBaseResource
__author__ = 'vlazarenko'


class NSCSVServerRewritePolicyBinding(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSCSVServerRewritePolicyBinding, self).__init__()
        self.options = {'policyname': '',
                        'priority': '',
                        'gotopriorityexpression': '',
                        'bindpoint': '',
                        'invoke': '',
                        'labeltype': '',
                        'labelname': '',
                        'name': ''}

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

        self.resourcetype = NSCSVServerRewritePolicyBinding.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        return "csvserver_rewritepolicy_binding"

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
        Expression specifying the priority of the next policy
        which will get evaluated if the current policy rule
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
        The virtual server name (created with the add cs vserver or
        add cr vserver command) for which the content
        switching policy will be set.

        Default value: 0
        Minimum length =  1.
        """
        self.options['name'] = name

    def get_name(self):
        """
        The virtual server name (created with the add cs vserver or
        add cr vserver command) for which the content
        switching policy will be set.

        Default value: 0
        Minimum length =  1.
        """
        return self.options['name']

    # Operations methods
    @staticmethod
    def get(nitro, csvserver_rewritepolicy_binding):
        """
        Use this API to fetch all configured csvserver_rewritepolicy_binding resources.
        """
        __url = nitro.get_url() + NSCSVServerRewritePolicyBinding.get_resourcetype() + "/" + csvserver_rewritepolicy_binding.get_name()
        __json_resources = nitro.get(__url).get_response_field(NSCSVServerRewritePolicyBinding.get_resourcetype())
        __resources = []
        for json_resource in __json_resources:
            __resources.append(NSCSVServerRewritePolicyBinding(json_resource))
        return __resources

    @staticmethod
    def add(nitro, csvserver_rewritepolicy_binding):
        """
        Use this API to add csvserver_rewritepolicy_binding.
        """
        __csvserver_rewritepolicy_binding = NSCSVServerRewritePolicyBinding()
        __csvserver_rewritepolicy_binding.set_name(csvserver_rewritepolicy_binding.get_name())
        __csvserver_rewritepolicy_binding.set_policyname(csvserver_rewritepolicy_binding.get_policyname())
        __csvserver_rewritepolicy_binding.set_priority(csvserver_rewritepolicy_binding.get_priority())
        __csvserver_rewritepolicy_binding.set_gotopriorityexpression(csvserver_rewritepolicy_binding.get_gotopriorityexpression())
        __csvserver_rewritepolicy_binding.set_bindpoint(csvserver_rewritepolicy_binding.get_bindpoint())
        __csvserver_rewritepolicy_binding.set_invoke(csvserver_rewritepolicy_binding.get_invoke())
        __csvserver_rewritepolicy_binding.set_labeltype(csvserver_rewritepolicy_binding.get_labeltype())
        __csvserver_rewritepolicy_binding.set_labelname(csvserver_rewritepolicy_binding.get_labelname())
        return __csvserver_rewritepolicy_binding.update_resource(nitro)

    @staticmethod
    def delete(nitro, csvserver_rewritepolicy_binding):
        """
        Use this API to delete csvserver_rewritepolicy_binding of a given name.
        """
        __csvserver_rewritepolicy_binding = NSCSVServerRewritePolicyBinding()
        __csvserver_rewritepolicy_binding.set_name(csvserver_rewritepolicy_binding.get_name())
        __csvserver_rewritepolicy_binding.set_policyname(csvserver_rewritepolicy_binding.get_policyname())
        __csvserver_rewritepolicy_binding.set_priority(csvserver_rewritepolicy_binding.get_priority())
        __csvserver_rewritepolicy_binding.set_bindpoint(csvserver_rewritepolicy_binding.get_bindpoint())
        nsresponse = __csvserver_rewritepolicy_binding.delete_resource(nitro)
        return nsresponse
