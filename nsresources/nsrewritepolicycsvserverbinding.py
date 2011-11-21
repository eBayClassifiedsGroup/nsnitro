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
                        'boundto' : '',
                        'priority' : '',
                        'activepolicy' : '',
                        'gotopriorityexpression' : '',
                        'labeltype' : '',
                        'labelname' : '',
                        'name' : '',
                }

                self.resourcetype = NSRewritePolicyCSVServerBinding.get_resourcetype()

                if not (json_data is None):
                        for key in json_data.keys():
                                if self.options.has_key(key):
                                        self.options[key] = json_data[key]


        @staticmethod
        def get_resourcetype():
                return "rewritepolicy_csvserver_binding"

        def set_boundto(self, boundto):
                self.options['boundto'] = boundto

        def get_boundto(self):
                return self.options['boundto']

        def set_priority(self, priority):
                self.options['priority'] = priority

        def get_priority(self):
                return self.options['priority']

        def set_activepolicy(self, activepolicy):
                self.options['activepolicy'] = activepolicy

        def get_activepolicy(self):
                return self.options['activepolicy']

        def set_gotopriorityexpression(self, gotopriorityexpression):
                self.options['gotopriorityexpression'] = gotopriorityexpression

        def get_gotopriorityexpression(self):
                return self.options['gotopriorityexpression']

        def set_labeltype(self, labeltype):
                self.options['labeltype'] = labeltype

        def get_labeltype(self):
                return self.options['labeltype']

        def set_labelname(self, labelname):
                self.options['labelname'] = labelname

        def get_labelname(self):
                return self.options['labelname']

        def set_name(self, name):
                self.options['name'] = name

        def get_name(self):
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