from nsbaseresource import NSBaseResource
__author__ = 'timl'


class NSResponderPolicyLabelBinding(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSResponderPolicyLabelBinding, self).__init__()
        self.options = {
            'labelname': '',
            'policyname': '',
            'priority': '',
            'gotopriorityexpression': '',
            'flags': '',
            'labeltype': '',
            'invoke_labelname': '',
        }

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

        self.resourcetype = NSResponderPolicyLabelBinding.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        return "responderpolicylabel_responderpolicy_binding"

    def set_labelname(self, labelname):
        """
        Responder policy label.

        Default value: 0
        """
        self.options['labelname'] = labelname

    def get_labelname(self):
        """
        Responder policy label.

        Default value: 0
        """
        return self.options['labelname']

    def set_policyname(self, policyname):
        """
        Bound responder policies to this responder policy label.

        Default value: 0
        """
        self.options['policyname'] = policyname

    def get_policyname(self):
        """
        Bound responder policies to this responder policy label.

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
        Expression specifying the priority of the next policy which will get evaluated if the current policy rule
        evaluates to TRUE.

        Default value: 0
        """
        self.options['gotopriorityexpression'] = gotopriorityexpression

    def get_gotopriorityexpression(self):
        """
        Expression specifying the priority of the next policy which will get evaluated if the current policy rule
        evaluates to TRUE.

        Default value: 0
        """
        return self.options['gotopriorityexpression']

    def set_flags(self, flags):
        """
        Bind flags.

        Default value: 0
        """
        self.options['flags'] = flags

    def get_flags(self):
        """
        Bind flags.

        Default value: 0
        """
        return self.options['flags']

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

    def set_invoke_labelname(self, invoke_labelname):
        """
        Name of the label invoked.

        Default value: 0
        """
        self.options['invoke_labelname'] = invoke_labelname

    def get_invoke_labelname(self):
        """
        Name of the label invoked.

        Default value: 0
        """
        return self.options['invoke_labelname']

    # Operations methods
    @staticmethod
    def get(nitro, responderpolicylabel_binding):
        """
        Use this API to fetch all configured responderpolicylabel_binding resources.
        """
        __url = nitro.get_url() + NSResponderPolicyLabelBinding.get_resourcetype() + "/" + responderpolicylabel_binding.get_labelname()
        __json_resources = nitro.get(__url).get_response_field(NSResponderPolicyLabelBinding.get_resourcetype())
        __resources = []
        for json_resource in __json_resources:
            __resources.append(NSResponderPolicyLabelBinding(json_resource))
        return __resources

    @staticmethod
    def add(nitro, responderpolicylabel_binding):
        """
        Use this API to add responderpolicylabel_binding.
        """
        __responderpolicylabel_binding = NSResponderPolicyLabelBinding()
        __responderpolicylabel_binding.set_labelname(responderpolicylabel_binding.get_labelname())
        __responderpolicylabel_binding.set_policyname(responderpolicylabel_binding.get_policyname())
        __responderpolicylabel_binding.set_priority(responderpolicylabel_binding.get_priority())
        __responderpolicylabel_binding.set_gotopriorityexpression(responderpolicylabel_binding.get_gotopriorityexpression())
        __responderpolicylabel_binding.set_flags(responderpolicylabel_binding.get_flags())
        __responderpolicylabel_binding.set_labeltype(responderpolicylabel_binding.get_labeltype())
        __responderpolicylabel_binding.set_invoke_labelname(responderpolicylabel_binding.get_invoke_labelname())
        return __responderpolicylabel_binding.update_resource(nitro)

    @staticmethod
    def delete(nitro, responderpolicylabel_binding):
        """
        Use this API to delete responderpolicylabel_binding of a given name.
        """
        __responderpolicylabel_binding = NSResponderPolicyLabelBinding()
        __name = responderpolicylabel_binding.get_labelname()
        __responderpolicylabel_binding.set_labelname(__name)
        __responderpolicylabel_binding.set_policyname(responderpolicylabel_binding.get_policyname())
        nsresponse = __responderpolicylabel_binding.delete_resource(nitro, __name)
        return nsresponse
