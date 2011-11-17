from nsbaseresource import NSBaseResource
__author__ = 'vlazarenko'

class NSLBVServerServiceBinding(NSBaseResource):

        def __init__(self, json_data=None):
                options = {
                        'servicename' : '',
                        'ipv46' : '',
                        'port' : '',
                        'servicetype' : '',
                        'curstate' : '',
                        'weight' : '',
                        'dynamicweight' : '',
                        'cookieipport' : '',
                        'vserverid' : '',
                        'name' : '',
                        'servicegroupname' : '',
                }


                if not (json_data is None):
                        for key in json_data.keys():
                                if self.options.has_key(key):
                                        self.options[key]=json_data[key]

                self.resourcetype = NSLBVServerServiceBinding.get_resourcetype()

        @staticmethod
        def get_resourcetype():
                return "lbvserver_service_binding"


        # Getters and setters for configurable options
        def set_servicename(self, servicename):
                self.options['servicename'] = servicename

        def get_servicename(self):
                return self.options['servicename']

        def set_ipv46(self, ipv46):
                self.options['ipv46'] = ipv46

        def get_ipv46(self):
                return self.options['ipv46']

        def set_port(self, port):
                self.options['port'] = port

        def get_port(self):
                return self.options['port']

        def set_servicetype(self, servicetype):
                self.options['servicetype'] = servicetype

        def get_servicetype(self):
                return self.options['servicetype']

        def set_curstate(self, curstate):
                self.options['curstate'] = curstate

        def get_curstate(self):
                return self.options['curstate']

        def set_weight(self, weight):
                self.options['weight'] = weight

        def get_weight(self):
                return self.options['weight']

        def set_dynamicweight(self, dynamicweight):
                self.options['dynamicweight'] = dynamicweight

        def get_dynamicweight(self):
                return self.options['dynamicweight']

        def set_cookieipport(self, cookieipport):
                self.options['cookieipport'] = cookieipport

        def get_cookieipport(self):
                return self.options['cookieipport']

        def set_vserverid(self, vserverid):
                self.options['vserverid'] = vserverid

        def get_vserverid(self):
                return self.options['vserverid']

        def set_name(self, name):
                self.options['name'] = name

        def get_name(self):
                return self.options['name']

        def set_servicegroupname(self, servicegroupname):
                self.options['servicegroupname'] = servicegroupname

        def get_servicegroupname(self):
                return self.options['servicegroupname']


        # Operations methods

        @staticmethod
        def get(nitro, vserver_service_binding):
                """
                Use this API to fetch vserver_service_binding resource of given name.
                """
                __vserver_service_binding = NSLBVServerServiceBinding()
                __vserver_service_binding.set_name(vserver_service_binding.get_name())
                __vserver_service_binding.get_resource(nitro)
                return __vserver_service_binding

        @staticmethod
        def get_all(nitro):
                """
                Use this API to fetch all configured vserver_service_binding resources.
                """
                __url = nitro.get_url() + NSLBVServerServiceBinding.get_resourcetype()
                __json_vserver_service_bindings = nitro.get(__url).get_response_field(NSLBVServerServiceBinding.get_resourcetype())
                __vserver_service_bindings = []
                for json_vserver_service_binding in __json_vserver_service_bindings:
                        __vserver_service_bindings.append(NSLBVServerServiceBinding(json_vserver_service_binding))
                return __vserver_service_bindings

        @staticmethod
        def add(nitro, vserver_service_binding):
                """
                Use this API to add vserver_service_binding.
                """
                __vserver_service_binding = NSLBVServerServiceBinding()
                __vserver_service_binding.set_name(vserver_service_binding.get_name())
                __vserver_service_binding.set_servicename(vserver_service_binding.get_servicename())
                __vserver_service_binding.set_weight(vserver_service_binding.get_weight())
                __vserver_service_binding.set_servicegroupname(vserver_service_binding.get_servicegroupname())
                return __vserver_service_binding.update_resource(nitro)

        @staticmethod
        def delete(nitro, vserver_service_binding):
                """
                Use this API to delete vserver_service_binding of a given name.
                """
                __vserver_service_binding = NSLBVServerServiceBinding()
                __vserver_service_binding.set_name(vserver_service_binding.get_name())
                nsresponse = __vserver_service_binding.delete_resource(nitro)
                return nsresponse