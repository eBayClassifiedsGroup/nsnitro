from nsbaseresource import NSBaseResource
__author__ = 'vlazarenko'


class NSRewritePolicyCSVServerBinding(NSBaseResource):

    # Binding class showing the csvserver that can be bound to rewritepolicy

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSRewritePolicyCSVServerBinding, self).__init__()
        self.options = {
            'boundto': '',
            'priority': '',
            'activepolicy': '',
            'gotopriorityexpression': '',
            'labeltype': '',
            'labelname': '',
            'name': '',
        }

        self.resourcetype = NSRewritePolicyCSVServerBinding.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "rewritepolicy_csvserver_binding"

    def set_boundto(self, boundto):
        """
        Location where policy is bound.

        Default value: 0
        """
        self.options['boundto'] = boundto

    def get_boundto(self):
        """
        Location where policy is bound.

        Default value: 0
        """
        return self.options['boundto']

    def get_priority(self):
        """
        Specifies the priority of the policy.

        Default value: 0
        """
        return self.options['priority']

    def get_activepolicy(self):
        """
        Indicates whether policy is bound or not.

        Default value: 0
        """
        return self.options['activepolicy']

    def get_gotopriorityexpression(self):
        """
        Expression specifying the priority of the next policy which will get evaluated if the current policy
        rule evaluates to TRUE.

        Default value: 0
        """
        return self.options['gotopriorityexpression']

    def get_labeltype(self):
        """
        Type of policy label invocation.

        Default value: 0
        """
        return self.options['labeltype']

    def get_labelname(self):
        """
        Name of the label to invoke if the current policy rule evaluates to TRUE.

        Default value: 0
        """
        return self.options['labelname']

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

    @staticmethod
    def get(nitro, rewritepolicy_csvserver_binding):
        """
        Use this API to fetch all configured rewritepolicy_csvserver_binding resources.
        """
        __url = nitro.get_url() + NSRewritePolicyCSVServerBinding.get_resourcetype() + "/" + rewritepolicy_csvserver_binding.get_name()
        __json_resources = nitro.get(__url).get_response_field(NSRewritePolicyCSVServerBinding.get_resourcetype())
        __resources = []
        for json_resource in __json_resources:
            __resources.append(NSRewritePolicyCSVServerBinding(json_resource))
        return __resources
