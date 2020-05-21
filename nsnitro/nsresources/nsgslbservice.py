# encoding: utf-8
from .nsbaseresource import NSBaseResource
from .nsservice import NSService

class NSGSLBService(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSGSLBService, self).__init__()

        self.options = {
            'servicename': '',
            'cnameentry': '',
            'ip': '',
            'servername': '',
            'servicetype': '',
            'port': '',
            'publicip': '',
            'healthmonitor': '',
            'sitename': '',
            'state': '',
            'cip': '',
            'sitepersistence': '',
            'ipaddress': '',
            'weight': '',
        }

        self.resourcetype = NSGSLBService.get_resourcetype()
        if not (json_data is None):
            for key in list(json_data.keys()):
                if key in list(self.options.keys()):
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "gslbservice"

    def set_servicename(self, servicename):
        """
        The gslb virtual name
        """
        self.options['servicename'] = servicename

    def get_servicename(self):
        """
        """
        return self.options['servicename']

    def set_servername(self, servername):
        """
        The gslb virtual name
        """
        self.options['servername'] = servername

    def get_servername(self):
        """
        """
        return self.options['servername']

    def set_servicetype(self, servicetype):
        """
        The gslb virtual name
        """
        self.options['servicetype'] = servicetype

    def get_servicetype(self):
        """
        """
        return self.options['servicetype']

    def set_sitename(self, sitename):
        """
        The gslb virtual name
        """
        self.options['sitename'] = sitename

    def get_sitename(self):
        """
        """
        return self.options['sitename']

    def get_publicip(self):
        """
        """
        return self.options['publicip']

    def set_ip(self, ip):
        """
        """
        self.options['ip'] = ip

    def get_ip(self):
        """
        """
        return self.options['ip']

    def set_port(self, port):
        """
        """
        self.options['port'] = port

    def get_port(self):
        """
        """
        return self.options['port']

    def set_state(self, state):
        """
        """
        self.options['state'] = state

    def get_state(self):
        """
        """
        return self.options['state']

    @staticmethod
    def disable(nitro, service):
        """
        Use this API to disable service.
        """
        __service = NSService()
        __service.set_name(service.get_servicename())
        return __service.perform_operation(nitro, "disable")

    @staticmethod
    def enable(nitro, service):
        """
        Use this API to enable service.
        """
        __service = NSService()
        __service.set_name(service.get_servicename())
        return __service.perform_operation(nitro, "enable")

    @staticmethod
    def get(nitro, service):
        """
        Use this API to fetch service resource of given name.
        """
        __service = NSGSLBService()
        __service.set_servicename(service.get_servicename())
        __service.get_resource(nitro, service.get_servicename())
        return __service

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured gslbservice resources.
        """
        __url = nitro.get_url() + NSGSLBService.get_resourcetype()
        __json_gslbvservers = nitro.get(__url).get_response_field(
            NSGSLBService.get_resourcetype())
        __gslbvservers = []
        for json_gslbvserver in __json_gslbvservers:
            __gslbvservers.append(NSGSLBService(json_gslbvserver))
        return __gslbvservers

    @staticmethod
    def add(nitro, service):
        """
        Use this API to add service.
        """
        __service = NSGSLBService()
        __service.set_ip(service.get_ip())
        __service.set_servicetype(service.get_servicetype())
        __service.set_servicename(service.get_servicename())
        __service.set_port(service.get_port())
        __service.set_sitename(service.get_sitename())
        __service.set_state(service.get_state())
        return __service.add_resource(nitro)

    @staticmethod
    def delete(nitro, service):
        """
        Use this API to delete service of a given name.
        """
        __service = NSGSLBService()
        __service.set_servicename(service.get_servicename())
        nsresponse = __service.delete_resource(nitro)
        return nsresponse