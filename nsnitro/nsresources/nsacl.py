from nsbaseresource import NSBaseResource


class NSAcl(NSBaseResource):

    # Configuration for ACL entry resource.

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSAcl, self).__init__()
        self.options = {
            'aclname': '',
            'aclaction': '',
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
            'destportop': '',
            'destportval': '',
            'ttl': '',
            'srcmac': '',
            'protocol': '',
            'protocolnumber': '',
            'vlan': '',
            'Interface': '',
            'established': '',
            'icmptype': '',
            'icmpcode': '',
            'priority': '',
            'state': '',
            'logstate': '',
            'ratelimit': '',
            'hits': '',
            'kernelstate': '',
            '__count': ''
        }

        self.resourcetype = NSAcl.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "nsacl"

    def set_aclname(self, aclname):
        """
        The alphanumeric name of the ACL.
        Default value: 0
        Minimum length =  1.
        """
        self.options['aclname'] = aclname

    def get_aclname(self):
        """
        The action associated with the ACL.
        Default value: 0
        """
        return self.options['aclname']

    def set_aclaction(self, aclaction):
        """
        The action associated with the ACL.
        Default value: 0
        """
        self.options['aclaction'] = aclaction

    def get_aclaction(self):
        """
        The action associated with the ACL.
        Default value: 0
        """
        return self.options['aclaction']

    def set_srcip(self, srcip):
        """
        The source IP address (range).
        Default value: 0
        """
        self.options['srcip'] = srcip

    def get_srcip(self):
        """
        The source IP address (range).
        Default value: 0
        """
        return self.options['srcip']

    def set_srcipop(self, srcipop):
        """
        Logical operator.
        Default value: 0
        """
        self.options['srcipop'] = srcipop

    def get_srcipop(self):
        """
        Logical operator.
        Default value: 0
        """
        return self.options['srcipop']

    def set_srcipval(self, srcipval):
        """
        The source IP address (range).
        Default value: 0
        """
        self.options['srcipval'] = srcipval

    def get_srcipval(self):
        """
        The source IP address (range).
        Default value: 0
        """
        return self.options['srcipval']

    def set_srcport(self, srcport):
        """
        The source Port (range).
        Default value: 0
        """
        self.options['srcport'] = srcport

    def get_srcport(self):
        """
        The source Port (range).
        Default value: 0
        """
        return self.options['srcport']

    def set_srcportop(self, srcportop):
        """
        Logical operator.
        Default value: 0
        """
        self.options['srcportop'] = srcportop

    def get_srcportop(self):
        """
        Logical operator.
        Default value: 0
        """
        return self.options['srcportop']

    def set_srcportval(self, srcportval):
        """
        The source Port (range).
        Default value: 0
        Maximum length =  65535.
        """
        self.options['srcportval'] = srcportval

    def get_srcportval(self):
        """
        The source Port (range).
        Default value: 0
        Maximum length =  65535.
        """
        return self.options['srcportval']

    def set_destip(self, destip):
        """
        The destination IP address (range).
        Default value: 0
        """
        self.options['destip'] = destip

    def get_destip(self):
        """
        The destination IP address (range).
        Default value: 0
        """
        return self.options['destip']

    def set_destipop(self, destipop):
        """
        Logical operator.
        Default value: 0
        """
        self.options['destipop'] = destipop

    def get_destipop(self):
        """
        Logical operator.
        Default value: 0
        """
        return self.options['destipop']

    def set_destipval(self, destipval):
        """
        The destination IP address (range).
        Default value: 0
        """
        self.options['destipval'] = destipval

    def get_destipval(self):
        """
        The destination IP address (range).
        Default value: 0
        """
        return self.options['destipval']

    def set_destport(self, destport):
        """
        The destination Port (range).
        Default value: 0
        """
        self.options['destport'] = destport

    def get_destport(self):
        """
        The destination Port (range).
        Default value: 0
        """
        return self.options['destport']

    def set_destportop(self, destportop):
        """
        Logical operator.
        Default value: 0
        """
        self.options['destportop'] = destportop

    def get_destportop(self):
        """
        Logical operator.
        Default value: 0
        """
        return self.options['destportop']

    def set_destportval(self, destportval):
        """
        The destination Port (range).
        Default value: 0
        Maximum length =  65535.
        """
        self.options['destportval'] = destportval

    def get_destportval(self):
        """
        The destination Port (range).
        Default value: 0
        Maximum length =  65535.
        """
        return self.options['destportval']

    def set_ttl(self, ttl):
        """
        The time to expire this ACL(in seconds).
        Default value: 0
        Minimum value =  1
        Maximum value =  0x7FFFFFFF
        """
        self.options['ttl'] = ttl

    def get_ttl(self):
        """
        The time to expire this ACL(in seconds).
        Default value: 0
        Minimum value =  1
        Maximum value =  0x7FFFFFFF
        """
        return self.options['ttl']

    def set_srcmac(self, srcmac):
        """
        The source MAC address.
        Default value: 0
        """
        self.options['srcmac'] = srcmac

    def get_srcmac(self):
        """
        The source MAC address.
        Default value: 0
        """
        return self.options['srcmac']

    def set_protocol(self, protocol):
        """
        The IP protocol name.
        Default value: 0
        """
        self.options['protocol'] = protocol

    def get_protocol(self):
        """
        The IP protocol name.
        Default value: 0
        """
        return self.options['protocol']

    def set_protocolnumber(self, protocolnumber):
        """
        The IP protocol number (decimal).
        Default value: 0
        Minimum value =  1
        Maximum value =  255
        """
        self.options['protocolnumber'] = protocolnumber

    def get_protocolnumber(self):
        """
        The IP protocol number (decimal).
        Default value: 0
        Minimum value =  1
        Maximum value =  255
        """
        return self.options['protocolnumber']

    def set_vlan(self, vlan):
        """
        The VLAN number.
        Default value: 0
        Minimum value =  1
        Maximum value =  4094
        """
        self.options['vlan'] = vlan

    def get_vlan(self):
        """
        The VLAN number.
        Default value: 0
        Minimum value =  1
        Maximum value =  4094
        """
        return self.options['vlan']

    def set_Interface(self, Interface):
        """
        The physical interface.
        Default value: 0
        """
        self.options['Interface'] = Interface

    def get_Interface(self):
        """
        The physical interface.
        Default value: 0
        """
        return self.options['Interface']

    def set_established(self, established):
        """
        This argument indicates that the ACL should be used for TCP response traffic only.
        """
        self.options['established'] = established

    def get_established(self):
        """
        This argument indicates that the ACL should be used for TCP response traffic only.
        """
        return self.options['established']

    def set_icmptype(self, icmptype):
        """
        The ICMP message type.
        Default value: 65536
        Minimum value =  0
        Maximum value =  255
        """
        self.options['icmptype'] = icmptype

    def get_icmptype(self):
        """
        The ICMP message type.
        Default value: 65536
        Minimum value =  0
        Maximum value =  255
        """
        return self.options['icmptype']

    def set_icmpcode(self, icmpcode):
        """
        The ICMP message code.
        Default value: 65536
        Minimum value =  0
        Maximum value =  255
        """
        self.options['icmpcode'] = icmpcode

    def get_icmpcode(self):
        """
        The ICMP message code.
        Default value: 65536
        Minimum value =  0
        Maximum value =  255
        """
        return self.options['icmpcode']

    def set_priority(self, priority):
        """
        The priority of the ACL.
        Default value: 0
        Minimum value =  1
        Maximum value =  10240
        """
        self.options['priority'] = priority

    def get_priority(self):
        """
        The priority of the ACL.
        Default value: 0
        Minimum value =  1
        Maximum value =  10240
        """
        return self.options['priority']

    def set_state(self, state):
        """
        The state of the ACL.
        Default value: ENABLED
        """
        self.options['state'] = state

    def get_state(self):
        """
        The state of the ACL.
        Default value: ENABLED
        """
        return self.options['state']

    def set_logstate(self, logstate):
        """
        The logging state of the ACL.
        Default value: DISABLED
        """
        self.options['logstate'] = logstate

    def get_logstate(self):
        """
        The logging state of the ACL.
        Default value: DISABLED
        """
        return self.options['logstate']

    def set_ratelimit(self, ratelimit):
        """
        log message rate limit for acl rule.
        Default value: 100
        Minimum value =  1
        Maximum value =  10000
        """
        self.options['ratelimit'] = ratelimit

    def get_ratelimit(self):
        """
        log message rate limit for acl rule.
        Default value: 100
        Minimum value =  1
        Maximum value =  10000
        """
        return self.options['ratelimit']

    def get_hits(self):
        """
        The hits of this ACL.
        Default value: 0
        """
        return self.options['hits']

    def get_kernelstate(self):
        """
        The commit status of the ACL.
        Default value: 0
        """
        return self.options['kernelstate']

    # Operations methods

    @staticmethod
    def add(nitro, nsacl):
        """
        Use this API to add nsacl resources.
        """
        __nsacl = NSAcl()
        __nsacl.set_aclname(nsacl.get_aclname())
        __nsacl.set_aclaction(nsacl.get_aclaction())
        __nsacl.set_srcip(nsacl.get_srcip())
        __nsacl.set_srcipop(nsacl.get_srcipop())
        __nsacl.set_srcipval(nsacl.get_srcipval())
        __nsacl.set_srcport(nsacl.get_srcport())
        __nsacl.set_srcportop(nsacl.get_srcportop())
        __nsacl.set_srcportval(nsacl.get_srcportval())
        __nsacl.set_destip(nsacl.get_destip())
        __nsacl.set_destipop(nsacl.get_destipop())
        __nsacl.set_destipval(nsacl.get_destipval())
        __nsacl.set_destport(nsacl.get_destport())
        __nsacl.set_destportop(nsacl.get_destportop())
        __nsacl.set_destportval(nsacl.get_destportval())
        __nsacl.set_ttl(nsacl.get_ttl())
        __nsacl.set_srcmac(nsacl.get_srcmac())
        __nsacl.set_protocol(nsacl.get_protocol())
        __nsacl.set_protocolnumber(nsacl.get_protocolnumber())
        __nsacl.set_vlan(nsacl.get_vlan())
        __nsacl.set_Interface(nsacl.get_Interface())
        __nsacl.set_established(nsacl.get_established())
        __nsacl.set_icmptype(nsacl.get_icmptype())
        __nsacl.set_icmpcode(nsacl.get_icmpcode())
        __nsacl.set_priority(nsacl.get_priority())
        __nsacl.set_state(nsacl.get_state())
        __nsacl.set_logstate(nsacl.get_logstate())
        __nsacl.set_ratelimit(nsacl.get_ratelimit())
        return __nsacl.add_resource(nitro)

    @staticmethod
    def delete(nitro, nsacl):
        """
        Use this API to delete nsacl resources.
        """
        __nsacl = NSAcl()
        __nsacl.set_aclname(nsacl.get_aclname())
        nsresponse = __nsacl.delete_resource(nitro, nsacl.get_aclname())
        return nsresponse

    @staticmethod
    def update(nitro, nsacl):
        """
        Use this API to update nsacl resources.
        """
        __nsacl = NSAcl()
        __nsacl.set_aclname(nsacl.get_aclname())
        __nsacl.set_aclaction(nsacl.get_aclaction())
        __nsacl.set_srcip(nsacl.get_srcip())
        __nsacl.set_srcipop(nsacl.get_srcipop())
        __nsacl.set_srcipval(nsacl.get_srcipval())
        __nsacl.set_srcport(nsacl.get_srcport())
        __nsacl.set_srcportop(nsacl.get_srcportop())
        __nsacl.set_srcportval(nsacl.get_srcportval())
        __nsacl.set_destip(nsacl.get_destip())
        __nsacl.set_destipop(nsacl.get_destipop())
        __nsacl.set_destipval(nsacl.get_destipval())
        __nsacl.set_destport(nsacl.get_destport())
        __nsacl.set_destportop(nsacl.get_destportop())
        __nsacl.set_destportval(nsacl.get_destportval())
        __nsacl.set_srcmac(nsacl.get_srcmac())
        __nsacl.set_protocol(nsacl.get_protocol())
        __nsacl.set_protocolnumber(nsacl.get_protocolnumber())
        __nsacl.set_icmptype(nsacl.get_icmptype())
        __nsacl.set_icmpcode(nsacl.get_icmpcode())
        __nsacl.set_vlan(nsacl.get_vlan())
        __nsacl.set_Interface(nsacl.get_Interface())
        __nsacl.set_priority(nsacl.get_priority())
        __nsacl.set_state(nsacl.get_state())
        __nsacl.set_logstate(nsacl.get_logstate())
        __nsacl.set_ratelimit(nsacl.get_ratelimit())
        return __nsacl.update_resource(nitro)

#    @staticmethod
#    def unset(nitro, nsacl):
#        """ generated source for method unset """
#        unsetresource = nsacl()
#        unsetresource.aclname = aclname
#        return unsetresource.unset_resource(client, args)

    @staticmethod
    def enable(nitro, nsacl):
        """
        Use this API to enable a acl of given name.
        """
        __nsacl = NSAcl()
        __nsacl.set_aclname(nsacl.get_aclname())
        return __nsacl.perform_operation(nitro, "enable")

    @staticmethod
    def disable(nitro, nsacl):
        """
        Use this API to disable a acl of given name.
        """
        __nsacl = NSAcl()
        __nsacl.set_aclname(nsacl.get_aclname())
        return __nsacl.perform_operation(nitro, "disable")

    @staticmethod
    def get(nitro, nsacl):
        """
        Use this API to fetch nsacl resource of given name.
        """
        __nsacl = NSAcl()
        __nsacl.set_aclname(nsacl.get_aclname())
        __nsacl.get_resource(nitro, object_name=__nsacl.get_aclname())
        return __nsacl

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured nsacl resources.
        """
        __url = nitro.get_url() + NSAcl.get_resourcetype()
        __json_nsacls = nitro.get(__url).get_response_field(NSAcl.get_resourcetype())
        __nsacls = []
        for json_nsacl in __json_nsacls:
            __nsacls.append(NSAcl(json_nsacl))
        return __nsacls
