from nsbaseresource import NSBaseResource


class NSServiceGroupServerBinding(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSServiceGroupServerBinding, self).__init__()
        self.options = {
            'servicegroupname': '',
            'ip': '',
            'servername': '',
            'port': '',
            'weight': '',
            'state': '',
            'serverid': '',
            'hashid': '',
            'svrstate': ''
        }

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options:
                    self.options[key] = json_data[key]

        self.resourcetype = NSServiceGroupServerBinding.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        return "servicegroup_servicegroupmember_binding"

    # Getters and setters for configurable options
    def set_ip(self, ip):
        """
        The IP address of the server that needs to be binded.
        Default value: 0
        """
        self.options['ip'] = ip

    def get_ip(self):
        """
        The IP address of the server.
        Default value: 0
        """
        return self.options['ip']

    def set_port(self, port):
        """
        The port of the server.
        """
        self.options['port'] = port

    def get_port(self):
        """
        The port of the server that its binded to.
        """
        return self.options['port']

    def set_state(self, state):
        """
        The state of the server.
        """
        self.options['state'] = state

    def get_state(self):
        """
        The state of the server that its binded to.
        """
        return self.options['state']

    def get_svrstate(self):
        """
        The svrstate of the server that its binded to.
        """
        return self.options['svrstate']

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

    def set_hashid(self, hashid):
        """
        hash Id.
        Default value: 0
        """
        self.options['hashid'] = hashid

    def get_hashid(self):
        """
        hash Id.
        Default value: 0
        """
        return self.options['hashid']

    def set_serverid(self, serverid):
        """
        server Id.
        Default value: 0
        """
        self.options['serverid'] = serverid

    def get_serverid(self):
        """
        server Id.
        Default value: 0
        """
        return self.options['serverid']

    def set_servername(self, servername):
        """
        The server name to which the service is bound.
        """
        self.options['servername'] = servername

    def get_servername(self):
        """
        The server name to which the service is bound.
        """
        return self.options['servername']

    def set_servicegroupname(self, servicegroupname):
        """
        The name of the service group that is bound.
        """
        self.options['servicegroupname'] = servicegroupname

    def get_servicegroupname(self):
        """
        The name of the service group that is bound.
        """
        return self.options['servicegroupname']

    # Operations methods
    @staticmethod
    def get(nitro, servicegroup_server_binding):
        """
        Use this API to fetch configured servicegroup_server_binding
        """
        __url = nitro.get_url() + NSServiceGroupServerBinding.get_resourcetype() + "/" + servicegroup_server_binding.get_servicegroupname()
        __json_services = nitro.get(__url).get_response_field(NSServiceGroupServerBinding.get_resourcetype())
        __services = []
        for json_service in __json_services:
            __services.append(NSServiceGroupServerBinding(json_service))
        return __services

    @staticmethod
    def get_server(nitro, servicegroup_server_binding):
        """
        Use this API to fetch a server configured to a servicegroup_server_binding
        """
        __servicegroup_server_binding = NSServiceGroupServerBinding()
        __servicegroup_server_binding.set_servicegroupname(servicegroup_server_binding.get_servicegroupname())
        __servicegroup_server_binding.set_servername(servicegroup_server_binding.get_servername())
        __filter = servicegroup_server_binding.get_servicegroupname() + "?filter=servername:" + servicegroup_server_binding.get_servername()
        __servicegroup_server_binding.get_resource(nitro, __filter)
        return __servicegroup_server_binding

    @staticmethod
    def add(nitro, servicegroup_server_binding):
        """
        Use this API to add a server to servergroup through servicegroup_server_binding.
        """
        __servicegroup_server_binding = NSServiceGroupServerBinding()
        __servicegroup_server_binding.set_servername(servicegroup_server_binding.get_servername())
        __servicegroup_server_binding.set_ip(servicegroup_server_binding.get_ip())
        __servicegroup_server_binding.set_port(servicegroup_server_binding.get_port())
        __servicegroup_server_binding.set_servicegroupname(servicegroup_server_binding.get_servicegroupname())
        __servicegroup_server_binding.set_weight(servicegroup_server_binding.get_weight())
        __servicegroup_server_binding.set_serverid(servicegroup_server_binding.get_serverid())
        __servicegroup_server_binding.set_state(servicegroup_server_binding.get_state())
        __servicegroup_server_binding.set_hashid(servicegroup_server_binding.get_hashid())
        return __servicegroup_server_binding.update_resource(nitro)

    @staticmethod
    def delete(nitro, servicegroup_server_binding):
        """
        Use this API to delete a server from servicegroup_server_binding of a given name.
        """
        __servicegroup_server_binding = NSServiceGroupServerBinding()
        __servicegroup_server_binding.set_servicegroupname(servicegroup_server_binding.get_servicegroupname())
        __servicegroup_server_binding.set_servername(servicegroup_server_binding.get_servername())
        __servicegroup_server_binding.set_ip(servicegroup_server_binding.get_ip())
        __servicegroup_server_binding.set_port(servicegroup_server_binding.get_port())
        __filter = servicegroup_server_binding.get_servicegroupname() + "/" + servicegroup_server_binding.get_servername()
        return __servicegroup_server_binding.delete_resource(nitro, __filter)
