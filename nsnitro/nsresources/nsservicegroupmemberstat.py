# encoding: utf-8
from nsbaseresource import NSBaseResource


class NSServiceGroupMemberStat(NSBaseResource):

    def __init__(self, json_data=None):
        super(NSServiceGroupMemberStat, self).__init__()
        self.options = {
            'servicegroupname': '',     # Name of the service group.
            'ip': '',                   # IP address of the service group. Mutually exclusive with the server name parameter.
            'servername': '',           # Name of the server. Mutually exclusive with the IP address parameter.
            'port': '',                 # Port number of the service group member.
            'clearstats': '',           # Clear the statsistics / counters.Possible values = basic, full

            # ---- read-only options -----
            'avgsvrttfb': '',           # Average TTFB between the NetScaler appliance and the server.TTFB is the time interval
                                        # between sending the request packet to a service and receiving the first response from
                                        # the service
            'primaryipaddress': '',     # The IP address on which the service is running.
            'primaryport': '',          # The port on which the service is running.
            'servicetype': '',          # The service type of this service.Possible values are ADNS, DNS, MYSQL, RTSP,
                                        # SSL_DIAMETER, ADNS_TCP, DNS_TCP, NNTP, SIP_UDP, SSL_TCP, ANY, FTP, RADIUS, SNMP,
                                        # TCP, DHCPRA, HTTP, RDP, SSL, TFTP, DIAMETER, MSSQL, RPCSVR, SSL_BRIDGE, UDP
            'state': '',                # Current state of the server. Possible values are UP, DOWN, UNKNOWN,
                                        # OFS(Out of Service), TROFS(Transition Out of Service), TROFS_DOWN
                                        # (Down When going Out of Service)
            'totalrequests': '',        # Total number of requests received on this service or virtual server.
                                        # (This applies to HTTP/SSL services and servers.)
            'requestsrate': '',         # Rate (/s) counter for totalrequests
            'totalresponses': '',       # Number of responses received on this service or virtual server.
                                        #(This applies to HTTP/SSL services and servers.)
            'responsesrate': '',        # Rate (/s) counter for totalresponses
            'totalrequestbytes': '',    # Total number of request bytes received on this service or virtual server.
            'requestbytesrate': '',     # Rate (/s) counter for totalrequestbytes
            'totalresponsebytes': '',   # Number of response bytes received by this service or virtual server.
            'responsebytesrate': '',    # Rate (/s) counter for totalresponsebytes
            'curclntconnections': '',   # Number of current client connections.
            'surgecount': '',           # Number of requests in the surge queue.
            'cursrvrconnections': '',   # Number of current connections to the actual servers behind the virtual server.
            'svrestablishedconn': '',   # Number of server connections in ESTABLISHED state.
            'curreusepool': '',         # Number of requests in the idle queue/reuse pool.
            'maxclients': '',           # Maximum open connections allowed on this service.
        }

        self.resourcetype = NSServiceGroupMemberStat.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if self.options.has_key(key):
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return 'servicegroupmember'

    def set_servicegroupname(self, name):
        self.options['servicegroupname'] = name

    def get_servicegroupname(self):
        return self.options['servicegroupname']

    def set_ip(self, ip):
        self.options['ip'] = ip

    def get_ip(self):
        return self.options['ip']

    def set_servername(self, name):
        self.options['servername'] = name

    def get_servername(self):
        return self.options['servername']

    def set_port(self, port):
        self.options['port'] = port

    def get_port(self):
        return self.options['port']

    def get_primaryipaddress(self):
        return self.options['primaryipaddress']

    def get_primaryport(self):
        return self.options['primaryport']

    def get_state(self):
        return self.options['state']

    def get_cursrvrconnections(self):
        return self.options['cursrvrconnections']

    @staticmethod
    def get(nitro, sgmember):
        __sgmember = NSServiceGroupMemberStat()
        __sgmember.set_servicegroupname(sgmember.get_servicegroupname())
        __sgmember.set_ip(sgmember.get_ip())
        __sgmember.set_servername(sgmember.get_servername())
        __sgmember.set_port(sgmember.get_port())
        #__sgmember.get_resource(nitro)
        __url = nitro.get_url(
            'stat') + NSServiceGroupMemberStat.get_resourcetype()+__sgmember.get_stat_args()
        # print __url
        __json_sgmemberst = nitro.get(__url).get_response_field(
            NSServiceGroupMemberStat.get_resourcetype())
        __sgmembers = []
        for json_sgmember in __json_sgmemberst:
            __sgmembers.append(NSServiceGroupMemberStat(json_sgmember))

        return __sgmembers
