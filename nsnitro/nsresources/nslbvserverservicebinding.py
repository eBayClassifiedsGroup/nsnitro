from nsbaseresource import NSBaseResource
__author__ = 'vlazarenko'


class NSLBVServerServiceBinding(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSLBVServerServiceBinding, self).__init__()
        self.options = {
            'servicename': '',
            'ipv46': '',
            'port': '',
            'servicetype': '',
            'curstate': '',
            'weight': '',
            'dynamicweight': '',
            'cookieipport': '',
            'vserverid': '',
            'name': '',
            'servicegroupname': ''
        }

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

        self.resourcetype = NSLBVServerServiceBinding.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        return "lbvserver_service_binding"

    # Getters and setters for configurable options
    def set_servicename(self, servicename):
        """
        The service name bound to the selected load balancing virtual server.
        Default value: 0
        Minimum length =  1.
        """
        self.options['servicename'] = servicename

    def get_servicename(self):
        """
        The service name bound to the selected load balancing virtual server.
        Default value: 0
        Minimum length =  1.
        """
        return self.options['servicename']

    def get_ipv46(self):
        """
        The IP address of the virtual server.
        Default value: 0
        """
        return self.options['ipv46']

    def get_port(self):
        """
        The IP address of the virtual server.
        Default value: 0
        """
        return self.options['port']

    def get_servicetype(self):
        """
        The service type.
        Default value: 0
        """
        return self.options['servicetype']

    def get_curstate(self):
        """
        Current LB vserver state.
        Default value: 0
        """
        return self.options['curstate']

    def set_weight(self, weight):
        """
        The weight for the specified service.
        Default value: 0
        Minimum value =  1
        Maximum value =  100
        """
        self.options['weight'] = weight

    def get_weight(self):
        """
        The weight for the specified service.
        Default value: 0
        Minimum value =  1
        Maximum value =  100
        """
        return self.options['weight']

    def get_dynamicweight(self):
        """
        Dynamic weight.
        Default value: 0
        """
        return self.options['dynamicweight']

    def get_cookieipport(self):
        """
        Encryped Ip address and port of the service that is inserted into the set-cookie http header.
        Default value: 0
        """
        return self.options['cookieipport']

    def get_vserverid(self):
        """
        Vserver Id.
        Default value: 0
        """
        return self.options['vserverid']

    def set_name(self, name):
        """
        The virtual server name to which the service is bound.
        Default value: 0
        Minimum length =  1.
        """
        self.options['name'] = name

    def get_name(self):
        """
        The virtual server name to which the service is bound.
        Default value: 0
        Minimum length =  1.
        """
        return self.options['name']

    def set_servicegroupname(self, servicegroupname):
        """
        The name of the service group that is bound.
        Default value: 0
        Minimum length =  1.
        """
        self.options['servicegroupname'] = servicegroupname

    def get_servicegroupname(self):
        """
        The name of the service group that is bound.
        Default value: 0
        Minimum length =  1.
        """
        return self.options['servicegroupname']

    # Operations methods
    @staticmethod
    def get(nitro, vserver_service_binding):
        """
        Use this API to fetch configured vserver_service_binding resources of a given name.
        """
        __url = nitro.get_url() + NSLBVServerServiceBinding.get_resourcetype() + \
            "/" + vserver_service_binding.get_name()
        __json_services = nitro.get(__url).get_response_field(
            NSLBVServerServiceBinding.get_resourcetype())
        __services = []
        for json_service in __json_services:
            __services.append(NSLBVServerServiceBinding(json_service))
        return __services


    @staticmethod
    def add(nitro, vserver_service_binding):
        """
        Use this API to add vserver_service_binding.
        """
        __vserver_service_binding = NSLBVServerServiceBinding()
        __vserver_service_binding.set_name(vserver_service_binding.get_name())
        __vserver_service_binding.set_servicename(
            vserver_service_binding.get_servicename())
        __vserver_service_binding.set_weight(
            vserver_service_binding.get_weight())
        __vserver_service_binding.set_servicegroupname(
            vserver_service_binding.get_servicegroupname())
        return __vserver_service_binding.update_resource(nitro)

    @staticmethod
    def delete(nitro, vserver_service_binding):
        """
        Use this API to delete vserver_service_binding of a given name.
        """
        __vserver_service_binding = NSLBVServerServiceBinding()
        __vserver_service_binding.set_name(vserver_service_binding.get_name())
        __vserver_service_binding.set_servicename(
            vserver_service_binding.get_servicename())
        __vserver_service_binding.set_servicegroupname(
            vserver_service_binding.get_servicegroupname())
        nsresponse = __vserver_service_binding.delete_resource(nitro)
        return nsresponse
