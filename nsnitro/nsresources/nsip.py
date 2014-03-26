from nsbaseresource import NSBaseResource

__author__ = 'vlazarenko'


class NSIP(NSBaseResource):

    # General Netscaler configuration object

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """

        super(NSIP, self).__init__()

        self.options = {'ipaddress': '',
                        'netmask': '',
                        'type': '',
                        'arp': '',
                        'icmp': '',
                        'vserver': '',
                        'telnet': '',
                        'ftp': '',
                        'gui': '',
                        'ssh': '',
                        'snmp': '',
                        'mgmtaccess': '',
                        'restrictaccess': '',
                        'dynamicrouting': '',
                        'ospf': '',
                        'bgp': '',
                        'rip': '',
                        'hostroute': '',
                        'hostrtgw': '',
                        'metric': '',
                        'vserverrhilevel': '',
                        'ospflsatype': '',
                        'ospfarea': '',
                        'state': '',
                        'vrid': '',
                        'flags': '',
                        'ospfareaval': '',
                        'viprtadv2bsd': '',
                        'vipvsercount': '',
                        'vipvserdowncount': '',
                        'freeports': '',
                        'iptype': '',
                        'count': ''}

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

        self.resourcetype = NSIP.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        return "nsip"

    def set_ipaddress(self, ipaddress):
        self.options['ipaddress'] = ipaddress

    def get_ipaddress(self):
        return self.options['ipaddress']

    def set_netmask(self, netmask):
        self.options['netmask'] = netmask

    def get_netmask(self):
        return self.options['netmask']

    def set_type(self, mytype):
        self.options['type'] = mytype

    def get_type(self):
        return self.options['type']

    def set_arp(self, arp):
        self.options['arp'] = arp

    def get_arp(self):
        return self.options['arp']

    def set_icmp(self, icmp):
        self.options['icmp'] = icmp

    def get_icmp(self):
        return self.options['icmp']

    def set_vserver(self, vserver):
        self.options['vserver'] = vserver

    def get_vserver(self):
        return self.options['vserver']

    def set_telnet(self, telnet):
        self.options['telnet'] = telnet

    def get_telnet(self):
        return self.options['telnet']

    def set_ftp(self, ftp):
        self.options['ftp'] = ftp

    def get_ftp(self):
        return self.options['ftp']

    def set_gui(self, gui):
        self.options['gui'] = gui

    def get_gui(self):
        return self.options['gui']

    def set_ssh(self, ssh):
        self.options['ssh'] = ssh

    def get_ssh(self):
        return self.options['ssh']

    def set_snmp(self, snmp):
        self.options['snmp'] = snmp

    def get_snmp(self):
        return self.options['snmp']

    def set_mgmtaccess(self, mgmtaccess):
        self.options['mgmtaccess'] = mgmtaccess

    def get_mgmtaccess(self):
        return self.options['mgmtaccess']

    def set_restrictaccess(self, restrictaccess):
        self.options['restrictaccess'] = restrictaccess

    def get_restrictaccess(self):
        return self.options['restrictaccess']

    def set_dynamicrouting(self, dynamicrouting):
        self.options['dynamicrouting'] = dynamicrouting

    def get_dynamicrouting(self):
        return self.options['dynamicrouting']

    def set_ospf(self, ospf):
        self.options['ospf'] = ospf

    def get_ospf(self):
        return self.options['ospf']

    def set_bgp(self, bgp):
        self.options['bgp'] = bgp

    def get_bgp(self):
        return self.options['bgp']

    def set_rip(self, rip):
        self.options['rip'] = rip

    def get_rip(self):
        return self.options['rip']

    def set_hostroute(self, hostroute):
        self.options['hostroute'] = hostroute

    def get_hostroute(self):
        return self.options['hostroute']

    def set_hostrtgw(self, hostrtgw):
        self.options['hostrtgw'] = hostrtgw

    def get_hostrtgw(self):
        return self.options['hostrtgw']

    def set_metric(self, metric):
        self.options['metric'] = metric

    def get_metric(self):
        return self.options['metric']

    def set_vserverrhilevel(self, vserverrhilevel):
        self.options['vserverrhilevel'] = vserverrhilevel

    def get_vserverrhilevel(self):
        return self.options['vserverrhilevel']

    def set_ospflsatype(self, ospflsatype):
        self.options['ospflsatype'] = ospflsatype

    def get_ospflsatype(self):
        return self.options['ospflsatype']

    def set_ospfarea(self, ospfarea):
        self.options['ospfarea'] = ospfarea

    def get_ospfarea(self):
        return self.options['ospfarea']

    def set_state(self, state):
        self.options['state'] = state

    def get_state(self):
        return self.options['state']

    def set_vrid(self, vrid):
        self.options['vrid'] = vrid

    def get_vrid(self):
        return self.options['vrid']

    def get_flags(self):
        return self.options['flags']

    def get_ospfareaval(self):
        return self.options['ospfareaval']

    def get_viprtadv2bsd(self):
        return self.options['viprtadv2bsd']

    def get_vipvsercount(self):
        return self.options['vipvsercount']

    def get_vipvserdowncount(self):
        return self.options['vipvserdowncount']

    def get_freeports(self):
        return self.options['freeports']

    def get_iptype(self):
        return self.options['iptype']

    def get_count(self):
        return self.options['count']

    @staticmethod
    def add(nitro, ip):
        __ip = NSIP()
        __ip.set_ipaddress(ip.get_ipaddress())
        __ip.set_netmask(ip.get_netmask())
        __ip.set_type(ip.get_type())
        __ip.set_arp(ip.get_arp())
        __ip.set_icmp(ip.get_icmp())
        __ip.set_vserver(ip.get_vserver())
        __ip.set_telnet(ip.get_telnet())
        __ip.set_ftp(ip.get_ftp())
        __ip.set_gui(ip.get_gui())
        __ip.set_ssh(ip.get_ssh())
        __ip.set_snmp(ip.get_snmp())
        __ip.set_mgmtaccess(ip.get_mgmtaccess())
        __ip.set_restrictaccess(ip.get_restrictaccess())
        __ip.set_dynamicrouting(ip.get_dynamicrouting())
        __ip.set_ospf(ip.get_ospf())
        __ip.set_bgp(ip.get_bgp())
        __ip.set_rip(ip.get_rip())
        __ip.set_hostroute(ip.get_hostroute())
        __ip.set_hostrtgw(ip.get_hostrtgw())
        __ip.set_metric(ip.get_metric())
        __ip.set_vserverrhilevel(ip.get_vserverrhilevel())
        __ip.set_ospflsatype(ip.get_ospflsatype())
        __ip.set_ospfarea(ip.get_ospfarea())
        __ip.set_state(ip.get_state())
        __ip.set_vrid(ip.get_vrid())
        return __ip.add_resource(nitro)

    @staticmethod
    def update(nitro, ip):
        __ip = NSIP()
        __ip.set_ipaddress(ip.get_ipaddress())
        __ip.set_netmask(ip.get_netmask())
        __ip.set_arp(ip.get_arp())
        __ip.set_icmp(ip.get_icmp())
        __ip.set_vserver(ip.get_vserver())
        __ip.set_telnet(ip.get_telnet())
        __ip.set_ftp(ip.get_ftp())
        __ip.set_gui(ip.get_gui())
        __ip.set_ssh(ip.get_ssh())
        __ip.set_snmp(ip.get_snmp())
        __ip.set_mgmtaccess(ip.get_mgmtaccess())
        __ip.set_restrictaccess(ip.get_restrictaccess())
        __ip.set_dynamicrouting(ip.get_dynamicrouting())
        __ip.set_ospf(ip.get_ospf())
        __ip.set_bgp(ip.get_bgp())
        __ip.set_rip(ip.get_rip())
        __ip.set_hostroute(ip.get_hostroute())
        __ip.set_hostrtgw(ip.get_hostrtgw())
        __ip.set_metric(ip.get_metric())
        __ip.set_vserverrhilevel(ip.get_vserverrhilevel())
        __ip.set_ospflsatype(ip.get_ospflsatype())
        __ip.set_ospfarea(ip.get_ospfarea())
        __ip.set_vrid(ip.get_vrid())
        return __ip.update_resource(nitro)

    @staticmethod
    def delete(nitro, ip):
        __ip = NSIP()
        __ip.set_ipaddress(ip.get_ipaddress())
        nsresponse = __ip.delete_resource(nitro, object_name=ip.get_ipaddress())
        return nsresponse

    @staticmethod
    def enable(nitro, ip):
        __ip = NSIP()
        __ip.set_ipaddress(ip.get_ipaddress())
        return __ip.perform_operation(nitro, "enable")

    @staticmethod
    def disable(nitro, ip):
        __ip = NSIP()
        __ip.set_ipaddress(ip.get_ipaddress())
        return __ip.perform_operation(nitro, "disable")

    @staticmethod
    def get(nitro, ip):
        __url = nitro.get_url() + NSIP.get_resourcetype() + "/" + ip.get_ipaddress()
        return nitro.get(__url).get_response_field(NSIP.get_resourcetype())[0]

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all nsip resources that are configured on netscaler.
        """
        __url = nitro.get_url() + NSIP.get_resourcetype()
        __json_ips = nitro.get(__url).get_response_field(NSIP.get_resourcetype())
        __ips = []
        for json_ip in __json_ips:
            __ips.append(NSIP(json_ip))
        return __ips
