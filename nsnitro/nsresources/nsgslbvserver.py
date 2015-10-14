# encoding: utf-8
from nsbaseresource import NSBaseResource


class NSGSLBVServer(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSGSLBVServer, self).__init__()

        self.options = {
            'name': '',
            'servicetype': '',
            'iptype': '',
            'dnsrecordtype': '',
            'lbmethod': '',
            'backupsessiontimeout': '',
            'backuplbmethod': '',
            'netmask': '',
            'v6netmasklen': '',
            'tolerance': '',
            'persistencetype': '',
            'persistenceid': '',
            'persistmask': '',
            'v6persistmasklen': '',
            'timeout': '',
            'edr': '',
            'mir': '',
            'disableprimaryondown': '',
            'dynamicweight': '',
            'state': '',
            'considereffectivestate': '',
            'comment': '',
            'somethod': '',
            'sopersistence': '',
            'sopersistencetimeout': '',
            'sothreshold': '',
            'sobackupaction': '',
            'appflowlog': '',
            'backupvserver': '',
            'servicename': '',
            'weight': '',
            'domainname': '',
            'ttl': '',
            'backupip': '',
            'cookie_domain': '',
            'cookietimeout': '',
            'sitedomainttl': '',
            'newname': '',

            # read only properties
            'curstate': '',
            'status': '',
            'lbrrreason': '',
            'iscname': '',
            'totalservices': '',
            'activeservices': '',
            'statechangetimesec': '',
            'statechangetimemsec': '',
            'tickssincelaststatechange': '',
            'health': '',
            'policyname': '',
            'priority': '',
            'gotopriorityexpression': '',
            'type': ''
        }

        self.resourcetype = NSGSLBVServer.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "gslbvserver"

    def set_name(self, name):
        """
        The gslb virtual name
        """
        self.options['name'] = name

    def get_name(self):
        """
        """
        return self.options['name']

    def set_lbmethod(self, lbmethod):
        """
        The gslb virtual name
        """
        self.options['lbmethod'] = lbmethod

    def get_lbmethod(self):
        """
        """
        return self.options['lbmethod']

    def set_weight(self, weight):
        """
        The gslb virtual name
        """
        self.options['weight'] = weight

    def get_weight(self):
        """
        """
        return self.options['weight']

    def set_servicename(self, servicename):
        """
        The gslb virtual name
        """
        self.options['servicename'] = servicename

    def get_servicename(self):
        """
        """
        return self.options['servicename']

    # Operations methods
    @staticmethod
    def get(nitro, gslbvserver):
        """
        Use this API to fetch gslbvserver resource of given name.
        """
        __gslbvserver = NSGSLBVServer()
        __gslbvserver.set_name(gslbvserver.get_name())
        __gslbvserver.get_resource(nitro)
        return __gslbvserver

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured gslbvserver resources.
        """
        __url = nitro.get_url() + NSGSLBVServer.get_resourcetype()
        __json_gslbvservers = nitro.get(__url).get_response_field(
            NSGSLBVServer.get_resourcetype())
        __gslbvservers = []
        for json_gslbvserver in __json_gslbvservers:
            __gslbvservers.append(NSGSLBVServer(json_gslbvserver))
        return __gslbvservers

    @staticmethod
    def update(nitro, gslbvs):
        """
        Use this API to update gslbvserver of a given name.
        """
        __gslbvs = NSGSLBVServer()
        __gslbvs.set_name(gslbvs.get_name())
        __gslbvs.set_servicename(gslbvs.get_servicename())
        __gslbvs.set_weight(gslbvs.get_weight())

        return __gslbvs.update_resource(nitro)
