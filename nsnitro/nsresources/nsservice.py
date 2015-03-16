from nsbaseresource import NSBaseResource

__author__ = 'vlazarenko'


class NSService(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSService, self).__init__()

        self.options = {
            # Read-write values
            'cachetype': '',
            'servername': '',
            'downstateflush': '',
            'maxreq': '',
            'maxbandwidth': '',
            'svrtimeout': '',
            'port': '',
            'clttimeout': '',
            'servicetype': '',
            'cacheable': '',
            'maxclient': '',
            'ipaddress': '',
            'delay': '',
            'graceful': '',
            'usip': '',
            'rtspsessionidremap': '',
            'cleartextport': '',
            'monthreshold': '',
            'accessdown': '',
            'serverid': '',
            'cka': '',
            'name': '',
            'newname': '',
            'sp': '',
            'weight': '',
            'cip': '',
            'monitor_name_svc': '',
            'cipheader': '',
            'useproxyport': '',
            'sc': '',
            'cmp': '',
            'tcpb': '',
            'state': '',
            'httpprofilename': '',
            'tcpprofilename': '',
            'comment': '',

            # Readonly values
            'policyname': '',
            'monstatparam2': '',
            'monstatparam3': '',
            'stateupdatereason': '',
            'serviceconftype': '',
            'gslb': '',
            'svrstate': '',
            'monstatcode': '',
            'timesincelaststatechange': '',
            'tickssincelaststatechange': '',
            'responsetime': '',
            'statechangetimesec': '',
            'statechangetimemsec': '',
            'failedprobes': '',
            'totalfailedprobes': '',
            'totalprobes': '',
        }

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options:
                    self.options[key] = json_data[key]

        self.resourcetype = NSService.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        return "service"

    # Getters and setters for configurable options
    def get_name(self):
        """
        The name of the service.
        Default value: 0
        Minimum length =  1.
        """
        return self.options['name']

    def set_name(self, name):
        """
        The name of the service.
        Default value: 0
        Minimum length =  1.
        """
        self.options['name'] = name

    def get_newname(self):
        """
        The new name of the service.
        Default value: 0
        Minimum length =  1.
        """
        return self.options['newname']

    def set_newname(self, name):
        """
        The new name of the service.
        Default value: 0
        Minimum length =  1.
        """
        self.options['newname'] = name

    def get_cachetype(self):
        """
        The cache type option supported by the cache server.
        Default value: 0
        """
        return self.options['cachetype']

    def set_cachetype(self, cachetype):
        """
        The cache type option supported by the cache server.
        Default value: 0
        """
        self.options['cachetype'] = cachetype

    def get_servername(self):
        """
        The name of the server for which a service will be added.
        Default value: 0
        Minimum length =  1.
        """
        return self.options['servername']

    def set_servername(self, servername):
        """
        The name of the server for which a service will be added.
        Default value: 0
        Minimum length =  1.
        """
        self.options['servername'] = servername

    def get_downstateflush(self):
        """
        Perform delayed clean up of connections on this service.
        Default value: ENABLED
        """
        return self.options['downstateflush']

    def set_downstateflush(self, downstateflush):
        """
        Perform delayed clean up of connections on this service.
        Default value: ENABLED
        """
        self.options['downstateflush'] = downstateflush

    def get_maxreq(self):
        """
        The maximum number of requests that can be sent on a persistent connection to the service.
        Minimum value =  0
        Maximum value =  65535
        """
        return self.options['maxreq']

    def set_maxreq(self, maxreq):
        """
        The maximum number of requests that can be sent on a persistent connection to the service.
        Minimum value =  0
        Maximum value =  65535
        """
        self.options['maxreq'] = maxreq

    def get_maxbandwidth(self):
        """
        The maximum bandwidth in kbps allowed for the service.
        Default value: 0
        Minimum value =  0
        Maximum value =  4294967287
        """
        return self.options['maxbandwidth']

    def set_maxbandwidth(self, maxbandwidth):
        """
        The maximum bandwidth in kbps allowed for the service.
        Default value: 0
        Minimum value =  0
        Maximum value =  4294967287
        """
        self.options['maxbandwidth'] = maxbandwidth

    def get_svrtimeout(self):
        """
        The idle time (in seconds) after which the server connection is terminated.
        Minimum value =  0
        Maximum value =  31536000
        """
        return self.options['svrtimeout']

    def set_svrtimeout(self, svrtimeout):
        """
        The idle time (in seconds) after which the server connection is terminated.
        Minimum value =  0
        Maximum value =  31536000
        """
        self.options['svrtimeout'] = svrtimeout

    def get_port(self):
        """
        The port number to be used for the service.
        Default value: 0
        Range 1 - 65535.
        """
        return self.options['port']

    def set_port(self, port):
        """
        The port number to be used for the service.
        Default value: 0
        Range 1 - 65535.
        """
        self.options['port'] = port

    def get_weight(self):
        """
        The weight for the specified monitor.
        Default value: 0
        Minimum value =  1
        Maximum value =  100
        """
        return self.options['weight']

    def set_weight(self, weight):
        """
        The weight for the specified monitor.
        Default value: 0
        Minimum value =  1
        Maximum value =  100
        """
        self.options['weight'] = weight

    def get_monitor_name_svc(self):
        """
        The monitor name bound to the selected service.
        Default value: 0
        Minimum length =  1.
        """
        return self.options['monitor_name_svc']

    def set_monitor_name_svc(self, monitornamesvc):
        """
        The monitor name bound to the selected service.
        Default value: 0
        Minimum length =  1.
        """
        self.options['monitor_name_svc'] = monitornamesvc

    def get_clttimeout(self):
        """
        The idle time (in seconds) after which the client connection is terminated.
        Minimum value =  0
        Maximum value =  31536000
        """
        return self.options['clttimeout']

    def set_clttimeout(self, clttimeout):
        """
        The idle time (in seconds) after which the client connection is terminated.
        Minimum value =  0
        Maximum value =  31536000
        """
        self.options['clttimeout'] = clttimeout

    def get_servicetype(self):
        """
        The type of service. The supported protocols are:
        HTTP - To load balance web servers and provide connection multiplexing, latency improvement, and other content and TCP protection benefits for HTTP traffic.
        FTP - To load balance FTP servers. In FTP mode, the system provides TCP protection benefits, protection against SYN attacks, and surge protection.
        TCP - To host any other TCP protocols that are not HTTP, FTP, NNTP, or SSL. In TCP mode, the system provides TCPprotection benefits, protection against SYN attack, and surge protection.
        UDP - To load balance servers with UDP-based services (other than DNS).
        SSL - To provide end-to-end encryption and SSL acceleration.
        SSL_BRIDGE - To load balance SSL servers.
        SSL_TCP - To offload SSL traffic for TCP applications.
        NNTP - To load balance NNTP servers.
        DNS - To load balance DNS servers.
        ADNS: To create an authoritative DNS service.
        ANY - To load balance a service type not listed above (for example, for IP traffic when load balancing firewalls).
        Note:  The NNTP service is for cache redirection.

        Default value: 0
        """
        return self.options['servicetype']

    def set_servicetype(self, servicetype):
        """
        The type of service. The supported protocols are:
        HTTP - To load balance web servers and provide connection multiplexing, latency improvement, and other content and TCP protection benefits for HTTP traffic.
        FTP - To load balance FTP servers. In FTP mode, the system provides TCP protection benefits, protection against SYN attacks, and surge protection.
        TCP - To host any other TCP protocols that are not HTTP, FTP, NNTP, or SSL. In TCP mode, the system provides TCPprotection benefits, protection against SYN attack, and surge protection.
        UDP - To load balance servers with UDP-based services (other than DNS).
        SSL - To provide end-to-end encryption and SSL acceleration.
        SSL_BRIDGE - To load balance SSL servers.
        SSL_TCP - To offload SSL traffic for TCP applications.
        NNTP - To load balance NNTP servers.
        DNS - To load balance DNS servers.
        ADNS: To create an authoritative DNS service.
        ANY - To load balance a service type not listed above (for example, for IP traffic when load balancing firewalls).
        Note:  The NNTP service is for cache redirection.

        Default value: 0
        """
        self.options['servicetype'] = servicetype

    def get_cacheable(self):
        """
        The virtual server (used in load balancing or content switching) routes a request to the virtual server
        (used in transparent cache redirection) on the same system before sending it to the configured servers.
        The virtual server used for transparent cache redirection determines if the request is directed to the
        cache servers or configured servers.
        Note:  This argument is disabled by default. Do not specify this argument if a -cacheType cacheType is specified.

        Default value: NO
        """
        return self.options['cacheable']

    def set_cacheable(self, cacheable):
        """
        The virtual server (used in load balancing or content switching) routes a request to the virtual server
        (used in transparent cache redirection) on the same system before sending it to the configured servers.
        The virtual server used for transparent cache redirection determines if the request is directed to the
        cache servers or configured servers.
        Note:  This argument is disabled by default. Do not specify this argument if a -cacheType cacheType is specified.

        Default value: NO
        """
        self.options['cacheable'] = cacheable

    def get_maxclient(self):
        """
        The maximum number of open connections to the service.
        Minimum value =  0
        Maximum value =  4294967294
        """
        return self.options['maxclient']

    def set_maxclient(self, maxclient):
        """
        The maximum number of open connections to the service.
        Minimum value =  0
        Maximum value =  4294967294
        """
        self.options['maxclient'] = maxclient

    def get_ipaddress(self):
        """
        The new IP address of the service.
        Default value: 0
        """
        return self.options['ipaddress']

    def set_ipaddress(self, ipaddress):
        """
        The new IP address of the service.
        Default value: 0
        """
        self.options['ipaddress'] = ipaddress

    def get_delay(self):
        """
        The time allowed (in seconds) for a graceful shutdown. During this period, new connections and requests
        continue to be sent to the service for clients who already have persistent sessions on the system.
        Connections or requests from fresh or new clients who do not yet have a persistence sessions on the
        NetScaler system are not sent to the service. Instead, they are load balanced among other available
        services. After the delay time has passed, no new requests or connections are sent to the service.

        Default value: 0
        """
        return self.options['delay']

    def set_delay(self, delay):
        """
        The time allowed (in seconds) for a graceful shutdown. During this period, new connections and requests
        continue to be sent to the service for clients who already have persistent sessions on the system.
        Connections or requests from fresh or new clients who do not yet have a persistence sessions on the
        NetScaler system are not sent to the service. Instead, they are load balanced among other available
        services. After the delay time has passed, no new requests or connections are sent to the service.

        Default value: 0
        """
        self.options['delay'] = delay

    def set_graceful(self, graceful):
        """
        Indicates graceful shutdown of the service. System will wait for all outstanding
        connections to this service to be closed before disabling the service.
        Default value: NO
        """
        self.options['graceful'] = graceful

    def get_graceful(self):
        """
        Indicates graceful shutdown of the service. System will wait for all outstanding
        connections to this service to be closed before disabling the service.
        Default value: NO
        """
        return self.options['graceful']

    def get_usip(self):
        """
        The use of client's IP Address option to the source IP Address while connecting to this server.
        By default, the system uses a mapped IP address for its server connection; however, you can use this
        option to tell the system to use the client's IP address when it communicates with the server.
        """
        return self.options['usip']

    def set_usip(self, usip):
        """
        The use of client's IP Address option to the source IP Address while connecting to this server.
        By default, the system uses a mapped IP address for its server connection; however, you can use this
        option to tell the system to use the client's IP address when it communicates with the server.
        """
        self.options['usip'] = usip

    def get_rtspsessionidremap(self):
        """
        Use this parameter to enable mapping of RTSP sessionid.
        Default value: OFF
        """
        return self.options['rtspsessionidremap']

    def set_rtspsessionidremap(self, rtspsessionidremap):
        """
        Use this parameter to enable mapping of RTSP sessionid.
        Default value: OFF
        """
        self.options['rtspsessionidremap'] = rtspsessionidremap

    def get_cleartextport(self):
        """
        The clear text port number where clear text data is sent. Used with SSL offload service.
        Default value: 0
        Minimum value =  1
        """
        return self.options['cleartextport']

    def set_cleartextport(self, cleartextport):
        """
        The clear text port number where clear text data is sent. Used with SSL offload service.
        Default value: 0
        Minimum value =  1
        """
        self.options['cleartextport'] = cleartextport

    def get_monthreshold(self):
        """
        The monitoring threshold.
        Default value: 0
        Minimum value =  0
        Maximum value =  65535
        """
        return self.options['monthreshold']

    def set_monthreshold(self, monthreshold):
        """
        The monitoring threshold.
        Default value: 0
        Minimum value =  0
        Maximum value =  65535
        """
        self.options['monthreshold'] = monthreshold

    def get_accessdown(self):
        """
        The option to allow access to disabled or down services. If enabled, all packets to this service are
        bridged.  If disabled, they are dropped.
        Default value: NO
        """
        return self.options['accessdown']

    def set_accessdown(self, accessdown):
        """
        The option to allow access to disabled or down services. If enabled, all packets to this service are
        bridged.  If disabled, they are dropped.
        Default value: NO
        """
        self.options['accessdown'] = accessdown

    def get_serverid(self):
        """
        The  identifier for the service. This is used when the persistency type is set to Custom Server ID.
        Default value: 0
        """
        return self.options['serverid']

    def set_serverid(self, serverid):
        """
        The  identifier for the service. This is used when the persistency type is set to Custom Server ID.
        Default value: 0
        """
        self.options['serverid'] = serverid

    def get_state(self):
        """
        The state of the service after it is added.
        Default value: ENABLED
        """
        return self.options['state']

    def set_state(self, state):
        """
        The state of the service after it is added.
        Default value: ENABLED
        """
        self.options['state'] = state

    def get_cka(self):
        """
        The state of the Client Keep-Alive feature for the service.
        """
        return self.options['cka']

    def set_cka(self, cka):
        """
        The state of the Client Keep-Alive feature for the service.
        """
        self.options['cka'] = cka

    def get_sp(self):
        """
        The state of Surge protection for the the service.
        """
        return self.options['sp']

    def set_sp(self, sp):
        """
        The state of Surge protection for the the service.
        """
        self.options['sp'] = sp

    def get_cip(self):
        """
        The Client IP header insertion option for the service.
        """
        return self.options['cip']

    def set_cip(self, cip):
        """
        The Client IP header insertion option for the service.
        """
        self.options['cip'] = cip

    def get_cipheader(self):
        """
        The client IP header. If client IP insertion is enabled and the client IP header is not specified,
        then the value set by the ###set ns config### command will be used as the Client IP header.
        Default value: 0
        Minimum length =  1.
        """
        return self.options['cipheader']

    def set_cipheader(self, cipheader):
        """
        The client IP header. If client IP insertion is enabled and the client IP header is not specified,
        then the value set by the ###set ns config### command will be used as the Client IP header.
        Default value: 0
        Minimum length =  1.
        """
        self.options['cipheader'] = cipheader

    def get_useproxyport(self):
        """
        When USIP is enabled, based on the setting of this variable proxy port or the client port will be used
        as the source port for the backend connection.
        """
        return self.options['useproxyport']

    def set_useproxyport(self, useproxyport):
        """
        When USIP is enabled, based on the setting of this variable proxy port or the client port will be used
        as the source port for the backend connection.
        """
        self.options['useproxyport'] = useproxyport

    def get_sc(self):
        """
        The state of SureConnect for the service.
        Note:  This parameter is supported for legacy purposes only. It has no effect on this system, and its
        only valid value is OFF.
        Default value: OFF
        """
        return self.options['sc']

    def set_sc(self, sc):
        """
        The state of SureConnect for the service.
        Note:  This parameter is supported for legacy purposes only. It has no effect on this system, and its
        only valid value is OFF.
        Default value: OFF
        """
        self.options['sc'] = sc

    def get_cmp(self):
        """
        The state of the HTTP Compression feature for the service.
        """
        return self.options['cmp']

    def set_cmp(self, cmp):
        """
        The state of the HTTP Compression feature for the service.
        """
        self.options['cmp'] = cmp

    def get_tcpb(self):
        """
        The state of the TCP Buffering feature for the service.
        """
        return self.options['tcpb']

    def set_tcpb(self, tcpb):
        """
        The state of the TCP Buffering feature for the service.
        """
        self.options['tcpb'] = tcpb

    def set_tcpprofilename(self, tcpprofilename):
        """
        The name of the TCP profile.
        Default value: 0
        Minimum length =  1.
        Maximum length =  127.
        """
        self.options['tcpprofilename'] = tcpprofilename

    def get_tcpprofilename(self):
        """
        The name of the TCP profile.
        Default value: 0
        Minimum length =  1.
        Maximum length =  127.
        """
        return self.options['tcpprofilename']

    def set_httpprofilename(self, httpprofilename):
        """
        Name of the HTTP profile.
        Default value: 0
        Minimum length =  1.
        Maximum length =  127.
        """
        self.options['httpprofilename'] = httpprofilename

    def get_httpprofilename(self):
        """
        Name of the HTTP profile.
        Default value: 0
        Minimum length =  1.
        Maximum length =  127.
        """
        return self.options['httpprofilename']

    def set_comment(self, comment):
        """
        Comments associated with this server.
        Default value: 0
        """
        self.options['comment'] = comment

    def get_comment(self):
        """
        Comments associated with this server.
        Default value: 0
        """
        return self.options['comment']

    # Read-only option getters
    def get_svrstate(self):
        """
        The state of the service.
        Default value: 0
        """
        return self.options['svrstate']

    def get_policyname(self):
        """
        The name of the policyname for which this service is bound.
        Default value: 0
        """
        return self.options['policyname']

    def get_monstatparam(self):
        """
        First parameter for use with message code.
        Default value: 0
        """
        return self.options['monstatparam2']

    def get_monstatparam2(self):
        """
        Second parameter for use with message code.
        Default value: 0
        """
        return self.options['monstatparam2']

    def get_monstatparam3(self):
        """
        Third parameter for use with message code.
        Default value: 0
        """
        return self.options['monstatparam3']

    def get_stateupdatereason(self):
        """
        Checks state update reason on the secondary node.
        Default value: 0
        """
        return self.options['stateupdatereason']

    def get_serviceconftype(self):
        """
        The configuration type of the service.
        Default value: 0
        """
        return self.options['serviceconftype']

    def get_gslb(self):
        """
        The GSLB option for the corresponding virtual server.
        Default value: 0
        """
        return self.options['gslb']

    def get_monstatcode(self):
        """
        The code indicating the monitor response.
        Default value: 0
        """
        return self.options['monstatcode']

    def get_timesincelaststatechange(self):
        """
        Time in milliseconds since the last state change.
        Default value: 0
        """
        return self.options['timesincelaststatechange']

    def get_tickssincelaststatechange(self):
        """
        Time in 10 millisecond ticks since the last state change.
        Default value: 0
        """
        return self.options['tickssincelaststatechange']

    def get_responsetime(self):
        """
        Response time of this monitor.
        Default value: 0
        """
        return self.options['responsetime']

    def get_statechangetimesec(self):
        """
        Time when last state change happened. Seconds part.
        Default value: 0
        """
        return self.options['statechangetimesec']

    def get_statechangetimemsec(self):
        """
        Time at which last state change happened. Milliseconds part.
        Default value: 0
        """
        return self.options['statechangetimemsec']

    # Operations methods
    @staticmethod
    def disable(nitro, service):
        """
        Use this API to disable service.
        """
        __service = NSService()
        __service.set_name(service.get_name())
        __service.set_delay(service.get_delay())
        __service.set_graceful(service.get_graceful())
        return __service.perform_operation(nitro, "disable")

    @staticmethod
    def enable(nitro, service):
        """
        Use this API to enable service.
        """
        __service = NSService()
        __service.set_name(service.get_name())
        return __service.perform_operation(nitro, "enable")

    @staticmethod
    def rename(nitro, service):
        """
        Use this API to rename service.
        """
        __service = NSService()
        __service.set_name(service.get_name())
        __service.set_newname(service.get_newname())
        return __service.perform_operation(nitro, "rename")

    @staticmethod
    def get(nitro, service):
        """
        Use this API to fetch service resource of given name.
        """
        __service = NSService()
        __service.set_name(service.get_name())
        __service.get_resource(nitro)
        return __service

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured service resources.
        """
        __url = nitro.get_url() + NSService.get_resourcetype()
        __json_services = nitro.get(__url).get_response_field(NSService.get_resourcetype())
        __services = []
        for json_service in __json_services:
            __services.append(NSService(json_service))
        return __services

    @staticmethod
    def add(nitro, service):
        """
        Use this API to add service.
        """
        __service = NSService()
        __service.set_name(service.get_name())
        __service.set_ipaddress(service.get_ipaddress())
        __service.set_servername(service.get_servername())
        __service.set_servicetype(service.get_servicetype())
        __service.set_port(service.get_port())
        __service.set_cleartextport(service.get_cleartextport())
        __service.set_cachetype(service.get_cachetype())
        __service.set_maxclient(service.get_maxclient())
        __service.set_maxreq(service.get_maxreq())
        __service.set_cacheable(service.get_cacheable())
        __service.set_cip(service.get_cip())
        __service.set_cipheader(service.get_cipheader())
        __service.set_usip(service.get_usip())
        __service.set_useproxyport(service.get_useproxyport())
        __service.set_sc(service.get_sc())
        __service.set_sp(service.get_sp())
        __service.set_rtspsessionidremap(service.get_rtspsessionidremap())
        __service.set_clttimeout(service.get_clttimeout())
        __service.set_svrtimeout(service.get_svrtimeout())
        __service.set_serverid(service.get_serverid())
        __service.set_cka(service.get_cka())
        __service.set_tcpb(service.get_tcpb())
        __service.set_maxbandwidth(service.get_maxbandwidth())
        __service.set_accessdown(service.get_accessdown())
        __service.set_monthreshold(service.get_monthreshold())
        __service.set_state(service.get_state())
        __service.set_downstateflush(service.get_downstateflush())
        __service.set_tcpprofilename(service.get_tcpprofilename())
        __service.set_httpprofilename(service.get_httpprofilename())
        __service.set_comment(service.get_comment())
        return __service.add_resource(nitro)

    @staticmethod
    def update(nitro, service):
        """
        Use this API to add service.
        """
        __service = NSService()
        __service.set_name(service.get_name())
        __service.set_ipaddress(service.get_ipaddress())
        __service.set_maxclient(service.get_maxclient())
        __service.set_maxreq(service.get_maxreq())
        __service.set_cacheable(service.get_cacheable())
        __service.set_cip(service.get_cip())
        __service.set_cipheader(service.get_cipheader())
        __service.set_usip(service.get_usip())
        __service.set_useproxyport(service.get_useproxyport())
        __service.set_sc(service.get_sc())
        __service.set_sp(service.get_sp())
        __service.set_rtspsessionidremap(service.get_rtspsessionidremap())
        __service.set_clttimeout(service.get_clttimeout())
        __service.set_svrtimeout(service.get_svrtimeout())
        __service.set_serverid(service.get_serverid())
        __service.set_cka(service.get_cka())
        __service.set_tcpb(service.get_tcpb())
        __service.set_cmp(service.get_cmp())
        __service.set_maxbandwidth(service.get_maxbandwidth())
        __service.set_accessdown(service.get_accessdown())
        __service.set_monthreshold(service.get_monthreshold())
        __service.set_weight(service.get_weight())
        __service.set_monitor_name_svc(service.get_monitor_name_svc())
        __service.set_downstateflush(service.get_downstateflush())
        __service.set_tcpprofilename(service.get_tcpprofilename())
        __service.set_httpprofilename(service.get_httpprofilename())
        __service.set_comment(service.get_comment())
        return __service.update_resource(nitro)

    @staticmethod
    def delete(nitro, service):
        """
        Use this API to delete service of a given name.
        """
        __service = NSService()
        __service.set_name(service.get_name())
        nsresponse = __service.delete_resource(nitro)
        return nsresponse
