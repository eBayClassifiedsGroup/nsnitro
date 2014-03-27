from nsbaseresource import NSBaseResource
__author__ = 'Aleksandar Topuzovic'


class NSLBVServerCSVserverBinding(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSLBVServerCSVserverBinding, self).__init__()
        self.options = {'priority': '',
                        'policyname': '',
                        'name': '',
                        'cachevserver': '',
                        'cachetype': '',
                        'hits': ''}

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

        self.resourcetype = NSLBVServerCSVserverBinding.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        """
        Binding object showing the csvserver that can be bound to lbvserver.
        """
        return "lbvserver_csvserver_binding"

    # Read/write properties
    def set_priority(self, priority):
        """
        Priority.
        """
        self.options['priority'] = priority

    def get_priority(self):
        """
        Priority.
        """
        return self.options['priority']

    def set_policyname(self, policyname):
        """
        Name of the policy bound to the LB vserver.
        """
        self.options['policyname'] = policyname

    def get_policyname(self):
        """
        Name of the policy bound to the LB vserver.
        """
        return self.options['policyname']

    def set_name(self, name):
        """
        The virtual server name to which the service is bound.
        Minimum length = 1
        """
        self.options['name'] = name

    def get_name(self):
        """
        The virtual server name to which the service is bound.
        Minimum length = 1
        """
        return self.options['name']

    def set_cachevserver(self, cachevserver):
        """
        Cache virtual server.
        """
        self.options['cachevserver'] = cachevserver

    def get_cachevserver(self):
        """
        Cache virtual server.
        """
        return self.options['cachevserver']

    # Read only properties
    def get_cachetype(self):
        """
        Cache type.
        """
        return self.options['cachetype']

    def get_hits(self):
        """
        Number of hits.
        """
        return self.options['hits']

    @staticmethod
    def get(nitro, lbvservercsvserverbinding):
        """
        Use this API to fetch lb vserver cs vserver binding resource of given name.
        """
        __url = nitro.get_url() + NSLBVServerCSVserverBinding.get_resourcetype() + "/" + lbvservercsvserverbinding.get_name()
        __json_csvservers = nitro.get(__url).get_response_field(NSLBVServerCSVserverBinding.get_resourcetype())
        __csvservers = []
        for json_csvserver in __json_csvservers:
            __csvservers.append(NSLBVServerCSVserverBinding(json_csvserver))
        return __csvservers
