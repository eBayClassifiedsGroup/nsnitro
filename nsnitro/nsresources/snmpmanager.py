from nsbaseresource import NSBaseResource

__author__ = 'ndenev@gmail.com'


class SNMPManager(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(SNMPManager, self).__init__()

        self.options = {'ipaddress': '',
                        'netmask': '',
                        'domainresolveretry': '',
                        # ReadOnly
                        'ip': '',
                        'domain': ''}

        self.resourcetype = SNMPManager.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "snmpmanager"

    def set_ipaddress(self, ipaddress):
        self.options['ipaddress'] = ipaddress

    def get_ipaddress(self):
        return self.options['ipaddress']

    def set_netmask(self, netmask):
        self.options['netmask'] = netmask

    def get_netmask(self):
        return self.options['netmask']

    def set_domainresolveretry(self, domainresolveretry):
        self.options['domainresolveretry'] = domainresolveretry

    def get_domainresolveretry(self):
        return self.options['domainresolveretry']

    def get_ip(self):
        return self.options['ip']

    def get_domain(self):
        return self.options['domain']

    @staticmethod
    def add(nitro, snmpmanager):
        __snmpmanager = SNMPManager()
        __snmpmanager.set_ipaddress(snmpmanager.get_ipaddress())
        __snmpmanager.set_netmask(snmpmanager.get_netmask())
        __snmpmanager.set_domainresolveretry(snmpmanager.get_domainresolveretry())
        return __snmpmanager.add_resource(nitro)

    @staticmethod
    def delete(nitro, snmpmanager):
        __snmpmanager = SNMPManager()
        __snmpmanager.set_ipaddress(snmpmanager.get_ipaddress())
        return __snmpmanager.delete_resource(nitro)

    @staticmethod
    def update(nitro, snmpmanager):
        __snmpmanager = SNMPManager()
        __snmpmanager.set_ipaddress(snmpmanager.get_ipaddress())
        __snmpmanager.set_netmask(snmpmanager.get_netmask())
        __snmpmanager.set_domainresolveretry(snmpmanager.get_domainresolveretry())
        return __snmpmanager.update_resource(nitro)

    @staticmethod
    def get(nitro, snmpmanager):
        __snmpmanager = SNMPManager()
        __snmpmanager.set_ipaddress(snmpmanager.get_ipaddress())
        __snmpmanager.get_resource(nitro, object_name=__snmpmanager.get_ipaddress())
        return __snmpmanager

    @staticmethod
    def get_all(nitro):
        __url = nitro.get_url() + SNMPManager.get_resourcetype()
        __json_snmpmanagers = nitro.get(__url).get_response_field(SNMPManager.get_resourcetype())
        __snmpmanagers = []
        for json_snmpmanager in __json_snmpmanagers:
            __snmpmanagers.append(SNMPManager(json_snmpmanager))
        return __snmpmanagers

