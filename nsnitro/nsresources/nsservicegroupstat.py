# encoding: utf-8
from nsbaseresource import NSBaseResource


class NSServiceGroupStat(NSBaseResource):

    def __init__(self, json_data=None):
        super(NSServiceGroupStat, self).__init__()
        self.options = {
            'servicegroupname': '',     # Name of the service group for which to display settings.
            'clearstats': '',           # Clear the statsistics / counters.Possible values = basic, full

            # ---- read-only options -----
            'state': '',                # Current state of the server. Possible values are UP, DOWN, UNKNOWN,
                                        # OFS(Out of Service), TROFS(Transition Out of Service), TROFS_DOWN
                                        # (Down When going Out of Service)
            'servicetype': '',          # The service type of this service.Possible values are ADNS, DNS, MYSQL,
                                        # RTSP, SSL_DIAMETER, ADNS_TCP, DNS_TCP, NNTP, SIP_UDP, SSL_TCP, ANY, 
                                        # FTP, RADIUS, SNMP, TCP, DHCPRA, HTTP, RDP, SSL, TFTP, DIAMETER, MSSQL,
                                        # RPCSVR, SSL_BRIDGE, UDP
        }
        self.resourcetype = NSServiceGroupStat.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return 'servicegroup'

    def set_servicegroupname(self, name):
        self.options['servicegroupname'] = name

    def get_servicegroupname(self):
        return self.options['servicegroupname']

    def get_state(self):
        return self.options['state']

    def get_servicetype(self):
        return self.options['servicetype']

    @staticmethod
    def get(nitro, servicegroupst):
        __servicegroupst = NSServiceGroupStat()
        __servicegroupst.set_servicegroupname(
            servicegroupst.get_servicegroupname())
        __servicegroupst.get_resource(
            nitro, 'stat', __servicegroupst.get_servicegroupname())
        return __servicegroupst

    @staticmethod
    def get_all(nitro):
        __url = nitro.get_url('stat') + NSServiceGroupStat.get_resourcetype()
        __json_sgstat = nitro.get(__url).get_response_field(
            NSServiceGroupStat.get_resourcetype())
        __sgstats = []
        for json_sgstat in __json_sgstat:
            __sgstats.append(NSServiceGroupStat(json_sgstat))
        return __sgstats
