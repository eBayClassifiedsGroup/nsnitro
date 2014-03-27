from nsbaseresource import NSBaseResource
__author__ = 'ndenev'


class NSPbr(NSBaseResource):

    # Configuration for PBR entry resource.

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSPbr, self).__init__()
        self.options = {'name': '',
                        'action': '',
                        'td': '',
                        'srcip': '',
                        'srcipop': '',
                        'srcipval': '',
                        'srcport': '',
                        'srcportop': '',
                        'srcportval': '',
                        'destip': '',
                        'destipop': '',
                        'destipval': '',
                        'destport': '',
                        'destportval': '',
                        'nexthop': '',
                        'nexthopval': '',
                        'iptunnel': '',
                        'iptunnelname': '',
                        'srcmac': '',
                        'protocol': '',
                        'protocolnumber': '',
                        'vlan': '',
                        'Interface': '',
                        'priority': '',
                        'msr': '',
                        'monitor': '',
                        'state': '',
                        'detail': '',
                        'hits': '',
                        'kernelstate': '',
                        'curstate': '',
                        'totalprobes': '',
                        'totalfailedprobes': '',
                        'failedprobes': '',
                        'monstatcode': '',
                        'monstatparam1': '',
                        'monstatparam2': '',
                        'monstatparam3': '',
                        'data': '',
                        '__count': ''
                        }

        self.resourcetype = NSPbr.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "nspbr"

    def set_name(self, name):
        self.options['name'] = name

    def get_name(self):
        return self.options['name']

    def set_action(self, action):
        self.options['action'] = action

    def get_action(self):
        return self.options['action']

    def set_td(self, td):
        self.options['td'] = td

    def get_td(self):
        return self.options['td']

    def set_srcip(self, srcip):
        self.options['srcip'] = srcip

    def get_srcip(self):
        return self.options['srcip']

    def set_srcipop(self, srcipop):
        self.options['srcipop'] = srcipop

    def get_srcipop(self):
        return self.options['srcipop']

    def set_srcipval(self, srcipval):
        self.options['srcipval'] = srcipval

    def get_srcipval(self):
        return self.options['srcipval']

    def set_srcport(self, srcport):
        self.options['srcport'] = srcport

    def get_srcport(self):
        return self.options['srcport']

    def set_srcportop(self, srcportop):
        self.options['srcportop'] = srcportop

    def get_srcportop(self):
        return self.options['srcportop']

    def set_srcportval(self, srcportval):
        self.options['srcportval'] = srcportval

    def get_srcportval(self):
        return self.options['srcportval']

    def set_destip(self, destip):
        self.options['destip'] = destip

    def get_destip(self):
        return self.options['destip']

    def set_destipop(self, destipop):
        self.options['destipop'] = destipop

    def get_destipop(self):
        return self.options['destipop']

    def set_destipval(self, destipval):
        self.options['destipval'] = destipval

    def get_destipval(self):
        return self.options['destipval']

    def set_destport(self, destport):
        self.options['destport'] = destport

    def get_destport(self):
        return self.options['destport']

    def set_destportval(self, destportval):
        self.options['destportval'] = destportval

    def get_destportval(self):
        return self.options['destportval']

    def set_nexthop(self, nexthop):
        self.options['nexthop'] = nexthop

    def get_nexthop(self):
        return self.options['nexthop']

    def set_nexthopval(self, nexthopval):
        self.options['nexthopval'] = nexthopval

    def get_nexthopval(self):
        return self.options['nexthopval']

    def set_iptunnel(self, iptunnel):
        self.options['iptunnel'] = iptunnel

    def get_iptunnel(self):
        return self.options['iptunnel']

    def set_iptunnelname(self, iptunnelname):
        self.options['iptunnelname'] = iptunnelname

    def get_iptunnelname(self):
        return self.options['iptunnelname']

    def set_srcmac(self, srcmac):
        self.options['srcmac'] = srcmac

    def get_srcmac(self):
        return self.options['srcmac']

    def set_protocol(self, protocol):
        self.options['protocol'] = protocol

    def get_protocol(self):
        return self.options['protocol']

    def set_protocolnumber(self, protocolnumber):
        self.options['protocolnumber'] = protocolnumber

    def get_protocolnumber(self):
        return self.options['protocolnumber']

    def set_vlan(self, vlan):
        self.options['vlan'] = vlan

    def get_vlan(self):
        return self.options['vlan']

    def set_interface(self, interface):
        self.options['Interface'] = interface

    def get_interface(self):
        return self.options['Interface']

    def set_priority(self, priority):
        self.options['priority'] = priority

    def get_priority(self):
        return self.options['priority']

    def set_msr(self, msr):
        self.options['msr'] = msr

    def get_msr(self):
        return self.options['msr']

    def set_monitor(self, monitor):
        self.options['monitor'] = monitor

    def get_monitor(self):
        return self.options['monitor']

    def set_state(self, state):
        self.options['state'] = state

    def get_state(self):
        return self.options['state']

    def set_detail(self, detail):
        self.options['detail'] = detail

    def get_detail(self):
        return self.options['detail']

    # ReadOnly
    def get_hits(self):
        return self.options['hits']

    def get_kernelstate(self):
        return self.options['kernelstate']

    def get_curstate(self):
        return self.options['curstate']

    def get_totalprobes(self):
        return self.options['totalprobes']

    def get_totalfailedprobes(self):
        return self.options['totalfailedprobes']

    def get_failedprobes(self):
        return self.options['failedprobes']

    def get_monstatcode(self):
        return self.options['monstatcode']

    def get_monstatparam1(self):
        return self.options['monstatparam1']

    def get_monstatparam2(self):
        return self.options['monstatparam2']

    def get_monstatparam3(self):
        return self.options['monstatparam3']

    def get_data(self):
        return self.options['data']

    # Operations methods

    @staticmethod
    def add(nitro, nspbr):
        """
        Use this API to add NSPbr resources.
        """
        __NSPbr = NSPbr()
        __NSPbr.set_name(nspbr.get_name())
        __NSPbr.set_action(nspbr.get_action())
        __NSPbr.set_td(nspbr.get_td())
        __NSPbr.set_srcip(nspbr.get_srcip())
        __NSPbr.set_srcipop(nspbr.get_srcipop())
        __NSPbr.set_srcipval(nspbr.get_srcipval())
        __NSPbr.set_srcport(nspbr.get_srcport())
        __NSPbr.set_srcportop(nspbr.get_srcportop())
        __NSPbr.set_srcportval(nspbr.get_srcportval())
        __NSPbr.set_destip(nspbr.get_destip())
        __NSPbr.set_destipop(nspbr.get_destipop())
        __NSPbr.set_destipval(nspbr.get_destipval())
        __NSPbr.set_destport(nspbr.get_destport())
        __NSPbr.set_destportop(nspbr.get_destportop())
        __NSPbr.set_destportval(nspbr.get_destportval())
        __NSPbr.set_nexthop(nspbr.get_nexthop())
        __NSPbr.set_nexthopval(nspbr.get_nexthopval())
        __NSPbr.set_iptunnel(nspbr.get_iptunnel())
        __NSPbr.set_iptunnelname(nspbr.get_iptunnelname())
        __NSPbr.set_srcmac(nspbr.get_srcmac())
        __NSPbr.set_protocol(nspbr.get_protocol())
        __NSPbr.set_protocolnumber(nspbr.get_protocolnumber())
        __NSPbr.set_vlan(nspbr.get_vlan())
        __NSPbr.set_Interface(nspbr.get_Interface())
        __NSPbr.set_priority(nspbr.get_priority())
        __NSPbr.set_msr(nspbr.get_msr())
        __NSPbr.set_monitor(nspbr.get_monitor())
        __NSPbr.set_state(nspbr.get_state())
        return __NSPbr.add_resource(nitro)

    @staticmethod
    def delete(nitro, nspbr):
        """
        Use this API to delete NSPbr resources.
        """
        __NSPbr = NSPbr()
        __NSPbr.set_name(nspbr.get_name())
        nsresponse = __NSPbr.delete_resource(nitro)
        return nsresponse

    @staticmethod
    def update(nitro, nspbr):
        """
        Use this API to update NSPbr resources.
        """
        __NSPbr = NSPbr()
        __NSPbr.set_name(nspbr.get_name())
        __NSPbr.set_action(nspbr.get_action())
        __NSPbr.set_srcip(nspbr.get_srcip())
        __NSPbr.set_srcipop(nspbr.get_srcipop())
        __NSPbr.set_srcipval(nspbr.get_srcipval())
        __NSPbr.set_srcport(nspbr.get_srcport())
        __NSPbr.set_srcportop(nspbr.get_srcportop())
        __NSPbr.set_srcportval(nspbr.get_srcportval())
        __NSPbr.set_destip(nspbr.get_destip())
        __NSPbr.set_destipop(nspbr.get_destipop())
        __NSPbr.set_destipval(nspbr.get_destipval())
        __NSPbr.set_destport(nspbr.get_destport())
        __NSPbr.set_destportop(nspbr.get_destportop())
        __NSPbr.set_destportval(nspbr.get_destportval())
        __NSPbr.set_nexthop(nspbr.get_nexthop())
        __NSPbr.set_nexthopval(nspbr.get_nexthopval())
        __NSPbr.set_iptunnel(nspbr.get_iptunnel())
        __NSPbr.set_iptunnelname(nspbr.get_iptunnelname())
        __NSPbr.set_srcmac(nspbr.get_srcmac())
        __NSPbr.set_protocol(nspbr.get_protocol())
        __NSPbr.set_protocolnumber(nspbr.get_protocolnumber())
        __NSPbr.set_vlan(nspbr.get_vlan())
        __NSPbr.set_interface(nspbr.get_interface())
        __NSPbr.set_priority(nspbr.get_priority())
        __NSPbr.set_msr(nspbr.get_msr())
        __NSPbr.set_monitor(nspbr.get_monitor())
        return __NSPbr.update_resource(nitro)

#    @staticmethod
#    def unset(nitro, NSPbr):
#        """ generated source for method unset """
#        unsetresource = NSPbr()
#        unsetresource.name = pbrname
#        return unsetresource.unset_resource(client, args)

    @staticmethod
    def enable(nitro, nspbr):
        """
        Use this API to enable a acl of given name.
        """
        __NSPbr = NSPbr()
        __NSPbr.set_name(nspbr.get_name())
        return __NSPbr.perform_operation(nitro, "enable")

    @staticmethod
    def disable(nitro, nspbr):
        """
        Use this API to disable a acl of given name.
        """
        __NSPbr = NSPbr()
        __NSPbr.set_name(nspbr.get_name())
        return __NSPbr.perform_operation(nitro, "disable")

    @staticmethod
    def get(nitro, nspbr):
        """
        Use this API to fetch NSPbr resource of given name.
        """
        __NSPbr = NSPbr()
        __NSPbr.set_name(nspbr.get_name())
        __NSPbr.get_resource(nitro, object_name=__NSPbr.get_name())
        return __NSPbr

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured NSPbr resources.
        """
        __url = nitro.get_url() + NSPbr.get_resourcetype()
        __json_NSPbrs = nitro.get(__url).get_response_field(NSPbr.get_resourcetype())
        __NSPbrs = []
        for json_NSPbr in __json_NSPbrs:
            __NSPbrs.append(NSPbr(json_NSPbr))
        return __NSPbrs
