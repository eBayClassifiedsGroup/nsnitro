from nsbaseresource import NSBaseResource


class NSLBVServer(NSBaseResource):

    # Configuration for Load Balancing Virtual Server resource.

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSLBVServer, self).__init__()
        self.options = {'name': '',
                        'servicetype': '',
                        'ipv46': '',
                        'ippattern': '',
                        'ipmask': '',
                        'port': '',
                        'range': '',
                        'persistencetype': '',
                        'timeout': '',
                        'persistencebackup': '',
                        'backuppersistencetimeout': '',
                        'lbmethod': '',
                        'hashlength': '',
                        'netmask': '',
                        'v6netmasklen': '',
                        'rule': '',
                        'listenpolicy': '',
                        'listenpriority': '',
                        'resrule': '',
                        'persistmask': '',
                        'v6persistmasklen': '',
                        'pq': '',
                        'sc': '',
                        'rtspnat': '',
                        'm': '',
                        'tosid': '',
                        'datalength': '',
                        'dataoffset': '',
                        'sessionless': '',
                        'state': '',
                        'connfailover': '',
                        'redirurl': '',
                        'cacheable': '',
                        'clttimeout': '',
                        'somethod': '',
                        'sopersistence': '',
                        'sopersistencetimeout': '',
                        'sothreshold': '',
                        'redirectportrewrite': '',
                        'downstateflush': '',
                        'backupvserver': '',
                        'disableprimaryondown': '',
                        'insertvserveripport': '',
                        'vipheader': '',
                        'authenticationhost': '',
                        'authentication': '',
                        'authn401': '',
                        'authnvsname': '',
                        'push': '',
                        'pushvserver': '',
                        'pushlabel': '',
                        'pushmulticlients': '',
                        'tcpprofilename': '',
                        'httpprofilename': '',
                        'comment': '',
                        'weight': '',
                        'servicename': '',
                        'redirurlflags': '',
                        'newname': '',
                        'value': '',
                        'ipmapping': '',
                        'type': '',
                        'curstate': '',
                        'effectivestate': '',
                        'status': '',
                        'lbrrreason': '',
                        'redirect': '',
                        'precedence': '',
                        'homepage': '',
                        'dnsvservername': '',
                        'domain': '',
                        'cachevserver': '',
                        'health': '',
                        'gotopriorityexpression': '',
                        'ruletype': '',
                        'groupname': '',
                        'cookiedomain': '',
                        'map': '',
                        'gt2gb': '',
                        'thresholdvalue': '',
                        'bindpoint': '',
                        'invoke': '',
                        'labeltype': '',
                        'labelname': '',
                        'version': '',
                        'totalservices': '',
                        'activeservices': '',
                        'statechangetimeseconds': '',
                        'statechangetimemsec': '',
                        'tickssincelaststatechange': '',
                        '__count': ''}

        self.resourcetype = NSLBVServer.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "lbvserver"

    def set_name(self, name):
        """
        The name of the load balancing virtual server being added.
        Default value: 0
        Minimum length =  1.
        """
        self.options['name'] = name

    def get_name(self):
        """
        The name of the load balancing virtual server being added.
        Default value: 0
        Minimum length =  1.
        """
        return self.options['name']

    def set_servicetype(self, servicetype):
        """
        The service type.
        Default value: 0
        """
        self.options['servicetype'] = servicetype

    def get_servicetype(self):
        """
        The service type.
        Default value: 0
        """
        return self.options['servicetype']

    def set_ipv46(self, ipv46):
        """
        The IP address of the virtual server.
        Default value: 0
        """
        self.options['ipv46'] = ipv46

    def get_ipv46(self):
        """
        The IP address of the virtual server.
        Default value: 0
        """
        return self.options['ipv46']

    def set_ippattern(self, ippattern):
        """
        The IP Pattern of the virtual server.
        Default value: 0
        """
        self.options['ippattern'] = ippattern

    def get_ippattern(self):
        """
        The IP Pattern of the virtual server.
        Default value: 0
        """
        return self.options['ippattern']

    def set_ipmask(self, ipmask):
        """
        The IP Mask of the virtual server IP Pattern.
        """
        self.options['ipmask'] = ipmask

    def get_ipmask(self):
        """
        The IP Mask of the virtual server IP Pattern.
        """
        return self.options['ipmask']

    def set_port(self, port):
        """
        A port number for the virtual server.
        Default value: 0
        Range 1 - 65535.
        """
        self.options['port'] = port

    def get_port(self):
        """
        A port number for the virtual server.
        Default value: 0
        Range 1 - 65535.
        """
        return self.options['port']

    def set_range(self, myrange):
        """
        The IP range for the network vserver.
        Default value: 1
        Minimum value =  1
        Maximum value =  254
        """
        self.options['range'] = myrange

    def get_range(self):
        """
        The IP range for the network vserver.
        Default value: 1
        Minimum value =  1
        Maximum value =  254
        """
        return self.options['range']

    def set_persistencetype(self, persistencetype):
        self.options['persistencetype'] = persistencetype

    def get_persistencetype(self):
        return self.options['persistencetype']

    def set_timeout(self, timeout):
        """
        The time period for which the persistence is in effect for a specific client.
        The value ranges from 2 to 1440 minutes.
        Default value: 2
        Minimum value =  0
        Maximum value =  1440
        """
        self.options['timeout'] = timeout

    def get_timeout(self):
        """
        The time period for which the persistence is in effect for a specific client.
        The value ranges from 2 to 1440 minutes.
        Default value: 2
        Minimum value =  0
        Maximum value =  1440
        """
        return self.options['timeout']

    def set_persistencebackup(self, persistencebackup):
        """
        Use this parameter to specify a backup persistence type for the virtual server.
        The Backup persistence option is used when the primary configured persistence
        mechanism on virtual server fails.
        The <persistenceBacup> parameter can take one of the following options:
           SOURCEIP
           NONE.
        Default value: 0
        """
        self.options['persistencebackup'] = persistencebackup

    def get_persistencebackup(self):
        """
        Use this parameter to specify a backup persistence type for the virtual server.
        The Backup persistence option is used when the primary configured persistence
        mechanism on virtual server fails.
        The <persistenceBacup> parameter can take one of the following options:
           SOURCEIP
           NONE.
        Default value: 0
        """
        return self.options['persistencebackup']

    def set_backuppersistencetimeout(self, backuppersistencetimeout):
        """
        The maximum time backup persistence is in effect for a specific client.
        Default value: 2
        Minimum value =  2
        Maximum value =  1440
        """
        self.options['backuppersistencetimeout'] = backuppersistencetimeout

    def get_backuppersistencetimeout(self):
        """
        The maximum time backup persistence is in effect for a specific client.
        Default value: 2
        Minimum value =  2
        Maximum value =  1440
        """
        return self.options['backuppersistencetimeout']

    def set_lbmethod(self, lbmethod):
        """
        The load balancing method for the virtual server. The valid options for this parameter are:
        ROUNDROBIN, LEASTCONNECTION, LEASTRESPONSETIME, URLHASH, DOMAINHASH, DESTINATIONIPHASH, SOURCEIPHASH,
        SRCIPDESTIPHASH,LEASTBANDWIDTH, LEASTPACKETS, TOKEN, SRCIPDESTIPHASH, CUSTOMLOAD, SRCIPSRCPORTHASH,
        LRTM, CALLIDHASSH.
        When the load balancing policy is configured as:
             ROUNDROBIN - When configured, the system distributes incoming requests to each server in rotation,
               regardless of the load. When different weights are assigned to services then weighted round robin
               occurs and requests go to services according to how much weighting has been set.

             LEASTCONNECTION (default value)- When configured, the system selects the service that has the least
               number of connections. For TCP, HTTP, HTTPS and SSL_TCP services the least number of connections
                includes:
               Established, active connections to a service. Connection reuse applies to HTTP and HTTPS.
               Hence the count
               includes only those connections which have outstanding HTTP or HTTPS requests, and does
               not include inactive, reusable connections.
               Connections to a service waiting in the Surge Queue, which exists only if the Surge Protection
                feature is enabled.
        For UDP services the least number of connections includes:
               The number of sessions between client and a physical service. These sessions are the logical,
               time-based entities, created on first arriving UDP packet. If configured, weights are taken into
               account when server selection is performed.

             LEASTRESPONSETIME - When configured, the system selects the service with the minimum average
               response time. The response time is the time interval taken when a request is sent to a service
                and
               first response packet comes back from the service, that is Time to First Byte (TTFB).
             URLHASH - The system selects the service based on the hashed value of the incoming URL.
               To specify the number of bytes of the URL that is used to calculate the hash value use the
                optional
               argument [-hashLength <positive_integer>] in either the add lb vserver or set lb vserver CLI
                command.
               The default value is 80.

             DOMAINHASH - When configured with this load balancing method, the system selects the service
                based on
               the hashed value of the domain name in the HTTP request. The domain name is taken either from
               the incoming URL or from the Host header of the HTTP request.
        Note:   The system defaults to LEASTCONNECTION if the request does not contain a domain name.
        If the domain name appears in both the URL and the host header, the system gives preference to
         the URL domain.
        #
               DESTINATIONIPHASH - The system selects the service based on the hashed value of the destination
                IP address in the TCP IP header.
               SOURCEIPHASH - The system selects the service based on the hashed value of the client's
                IP address in the IP header.
               LEASTBANDWIDTH - The system selects the service that is currently serving the least traffic,
                measured in megabits per second.
               LEASTPACKETS - The system selects the service that is currently serving the lowest
                number of packets per second.
               Token -The system selects the service based on the value, calculated from a token, extracted
                from the client's request
               (location and size of the token is configurable). For subsequent requests with the same token,
                the systems will select the same physical server.
               SRCIPDESTIPHASH - The system selects the service based on the hashed value of the client's
                SOURCE IP and DESTINATION IP address in the TCP IP header.
               CUSTOMLOAD - The system selects the service based on the it load which was determined by the
                LOAD monitors bound to the service.
               SRCIPSRCPORTHASH - The system selects the service based on the hashed value of the client's
               SOURCE IP and SOURCE PORT in the TCP/UDP+IP header.
               LRTM - When configured, the system selects the service with least response time learned through
                probing(number of active
               connections taken into account in addition to the response time).
               CALLIDHASSH - The system selects the service based on the hashed value of SIP callid.
        Default value: LEASTCONNECTION
        """
        self.options['lbmethod'] = lbmethod

    def get_lbmethod(self):
        """
        The load balancing method for the virtual server. The valid options for this parameter are:
        ROUNDROBIN, LEASTCONNECTION, LEASTRESPONSETIME, URLHASH, DOMAINHASH, DESTINATIONIPHASH, SOURCEIPHASH,
        SRCIPDESTIPHASH,LEASTBANDWIDTH, LEASTPACKETS, TOKEN, SRCIPDESTIPHASH, CUSTOMLOAD, SRCIPSRCPORTHASH,
        LRTM, CALLIDHASSH.
        When the load balancing policy is configured as:
               ROUNDROBIN - When configured, the system distributes incoming requests to each server
               in rotation, regardless of the load. When different weights are assigned to services then
               weighted round robin occurs and requests go to services according to how much
               weighting has been set.
               LEASTCONNECTION (default value)- When configured, the system selects the service that has the
               least number of connections. For TCP, HTTP, HTTPS and SSL_TCP services the least number of
               connections includes:
               Established, active connections to a service. Connection reuse applies to HTTP and HTTPS. Hence
               the count includes only those connections which have outstanding HTTP or HTTPS requests,
               and does not include inactive, reusable connections.
               Connections to a service waiting in the Surge Queue, which exists only if the Surge Protection
                feature is enabled.
        For UDP services the least number of connections includes:
               The number of sessions between client and a physical service. These sessions are the logical,
                time-based entities, created on first arriving UDP packet. If configured, weights are taken
                 into account when server selection is performed.
               LEASTRESPONSETIME - When configured, the system selects the service with the minimum average
                response time. The response time is the time interval taken when a request is sent to a service
                 and first response packet comes back from the service, that is Time to First Byte (TTFB).
               URLHASH - The system selects the service based on the hashed value of the incoming URL.To specify
                the number of bytes of the URL that is used to calculate the hash value use the optional
                argument [-hashLength <positive_integer>] in either the add lb vserver or set lb vserver
                CLI command. The default value is 80.
               DOMAINHASH - When configured with this load balancing method, the system selects the service
               based on the hashed value of the domain name in the HTTP request. The domain name is taken
               either from the incoming URL or from the Host header of the HTTP request.
        Note:   The system defaults to LEASTCONNECTION if the request does not contain a domain name.
        If the domain name appears in both the URL and the host header, the system gives preference to
        the URL domain.
        #
               DESTINATIONIPHASH - The system selects the service based on the hashed value of the destination
                IP address in the TCP IP header.
               SOURCEIPHASH - The system selects the service based on the hashed value of the client's IP
               address in the IP header.
               LEASTBANDWIDTH - The system selects the service that is currently serving the least traffic,
               measured in megabits per second.
               LEASTPACKETS - The system selects the service that is currently serving the lowest number of
               packets per second.
               Token -The system selects the service based on the value, calculated from a token, extracted
               from the client's request (location and size of the token is configurable). For subsequent
               requests with the same token, the systems will select the same physical server.
               SRCIPDESTIPHASH - The system selects the service based on the hashed value of the client's
               SOURCE IP and DESTINATION IP address in the TCP IP header.
               CUSTOMLOAD - The system selects the service based on the it load which was determined by
               the LOAD monitors bound to the service.
               SRCIPSRCPORTHASH - The system selects the service based on the hashed value of
               the client's SOURCE IP and SOURCE PORT in the TCP/UDP+IP header.
               LRTM - When configured, the system selects the service with least response time learned through
               probing(number of active connections taken into account in addition to the response time).
               CALLIDHASSH - The system selects the service based on the hashed value of SIP callid.
        Default value: LEASTCONNECTION
        """
        return self.options['lbmethod']

    def set_hashlength(self, hashlength):
        """
        This parameter is used when the URLHASH or DOMAINHASH policy is set. Enter the number of bytes
        that will be hashed in the URL or DOMAIN name. Valid values are from 1 to 4096 bytes.
        Default value: 80
        Minimum value =  1
        Maximum value =  4096
        """
        self.options['hashlength'] = hashlength

    def get_hashlength(self):
        """
        This parameter is used when the URLHASH or DOMAINHASH policy is set. Enter the number of bytes
        that will be hashed in the URL or DOMAIN name. Valid values are from 1 to 4096 bytes.
        Default value: 80
        Minimum value =  1
        Maximum value =  4096
        """
        return self.options['hashlength']

    def set_netmask(self, netmask):
        """
        Use this parameter to set the DESTINATIONIPHASH or SOURCEIPHASH policy.
        Enter the netmask to be used in modifying the destination or source IP address or network.
        Minimum length =  1.
        """
        self.options['netmask'] = netmask

    def get_netmask(self):
        """
        Use this parameter to set the DESTINATIONIPHASH or SOURCEIPHASH policy.
        Enter the netmask to be used in modifying the destination or source IP address or network.
        Minimum length =  1.
        """
        return self.options['netmask']

    def set_v6netmasklen(self, v6netmasklen):
        """
        The Network mask. Use this parameter if you are setting the DESTINATIONIPHASH or SOURCEIPHASH policy.
        Enter the netmask to be used in modifying the destination or source IP address or network.
        Default value: 128
        Minimum value =  1
        Maximum value =  128
        """
        self.options['v6netmasklen'] = v6netmasklen

    def get_v6netmasklen(self):
        """
        The Network mask. Use this parameter if you are setting the DESTINATIONIPHASH or SOURCEIPHASH policy.
        Enter the netmask to be used in modifying the destination or source IP address or network.
        Default value: 128
        Minimum value =  1
        Maximum value =  128
        """
        return self.options['v6netmasklen']

    def set_rule(self, rule):
        """
        Use this parameter to specify the string value used to set the RULE persistence type.
        The string can be either an existing rule name (configured using add rule command) or else it can be
        an in-line expression with a maximum of 256 characters.
        Default value: "none"
        """
        self.options['rule'] = rule

    def get_rule(self):
        """
        Use this parameter to specify the string value used to set the RULE persistence type.
        The string can be either an existing rule name (configured using add rule command) or else it can be
        an in-line expression with a maximum of 256 characters.
        Default value: "none"
        """
        return self.options['rule']

    def set_listenpolicy(self, listenpolicy):
        """
        Use this parameter to specify the listen policy for LB Vserver.
        The string can be either an existing expression name (configured using add policy expression command)
        or else it can be an in-line expression with a maximum of 1500 characters.
        Default value: "none"
        """
        self.options['listenpolicy'] = listenpolicy

    def get_listenpolicy(self):
        """
        Use this parameter to specify the listen policy for LB Vserver.
        The string can be either an existing expression name (configured using add policy expression command)
        or else it can be an in-line expression with a maximum of 1500 characters.
        Default value: "none"
        """
        return self.options['listenpolicy']

    def set_listenpriority(self, listenpriority):
        """
        Use this parameter to specify the priority for listen policy of LB Vserver.
        Default value: 101
        Minimum value =  0
        Maximum value =  100
        """
        self.options['listenpriority'] = listenpriority

    def get_listenpriority(self):
        """
        Use this parameter to specify the priority for listen policy of LB Vserver.
        Default value: 101
        Minimum value =  0
        Maximum value =  100
        """
        return self.options['listenpriority']

    def set_resrule(self, resrule):
        """
        Use this parameter to specify the expression to be used in response for RULE persistence type.
        The string  is an in-line expression with a maximum of 1500 characters.
        Default value: "none"
        """
        self.options['resrule'] = resrule

    def get_resrule(self):
        """
        Use this parameter to specify the expression to be used in response for RULE persistence type.
        The string  is an in-line expression with a maximum of 1500 characters.
        Default value: "none"
        """
        return self.options['resrule']

    def set_persistmask(self, persistmask):
        """
        Use this parameter to specify if the persistency is IP based. This parameter is Optional.
        Minimum length =  1.
        """
        self.options['persistmask'] = persistmask

    def get_persistmask(self):
        """
        Use this parameter to specify if the persistency is IP based. This parameter is Optional.
        Minimum length =  1.
        """
        return self.options['persistmask']

    def set_v6persistmasklen(self, v6persistmasklen):
        """
        The persistence mask. Use this parameter if you are using IP based persistence type on a ipv6 vserver.
        Default value: 128
        Minimum value =  1
        Maximum value =  128
        """
        self.options['v6persistmasklen'] = v6persistmasklen

    def get_v6persistmasklen(self):
        """
        The persistence mask. Use this parameter if you are using IP based persistence type on a ipv6 vserver.
        Default value: 128
        Minimum value =  1
        Maximum value =  128
        """
        return self.options['v6persistmasklen']

    def set_pq(self, pq):
        """
        Use this parameter to enable priority queuing on the specified virtual server.
        Default value: OFF
        """
        self.options['pq'] = pq

    def get_pq(self):
        """
        Use this parameter to enable priority queuing on the specified virtual server.
        Default value: OFF
        """
        return self.options['pq']

    def set_sc(self, sc):
        """
        Use this parameter to enable SureConnect on the specified virtual server.
        Default value: OFF
        """
        self.options['sc'] = sc

    def get_sc(self):
        """
        Use this parameter to enable SureConnect on the specified virtual server.
        Default value: OFF
        """
        return self.options['sc']

    def set_rtspnat(self, rtspnat):
        """
        Use this parameter to enable natting for RTSP data connection.
        Default value: OFF
        """
        self.options['rtspnat'] = rtspnat

    def get_rtspnat(self):
        """
        Use this parameter to enable natting for RTSP data connection.
        Default value: OFF
        """
        return self.options['rtspnat']

    def set_m(self, m):
        """
        Use this parameter to specify the LB mode. If the value is specified as IP then the traffic
        is sent to the physical servers by changing the destination IP address to that of the physical server.
        If the value is MAC then the traffic is sent to the physical servers , by changing
        the destination MAC address to that of one of the physical servers, the destination IP is not changed.
        MAC mode is used mostly in Firewall Load Balancing scenario.
        Default value: IP
        """
        self.options['m'] = m

    def get_m(self):
        """
        Use this parameter to specify the LB mode. If the value is specified as IP then the traffic
        is sent to the physical servers by changing the destination IP address to that of the physical server.
        If the value is MAC then the traffic is sent to the physical servers , by changing
        the destination MAC address to that of one of the physical servers, the destination IP is not changed.
        MAC mode is used mostly in Firewall Load Balancing scenario.
        Default value: IP
        """
        return self.options['m']

    def set_tosid(self, tosid):
        """
        Use this parameter to specify the TOS ID of this vserver. Applicable only when the LB mode is TOS.
        Default value: 0
        Minimum value =  1
        Maximum value =  63
        """
        self.options['tosid'] = tosid

    def get_tosid(self):
        """
        Use this parameter to specify the TOS ID of this vserver. Applicable only when the LB mode is TOS.
        Default value: 0
        Minimum value =  1
        Maximum value =  63
        """
        return self.options['tosid']

    def set_datalength(self, datalength):
        """
        Use this parameter to specify the length of the token in bytes. Applicable to
        TCP virtual servers, when Token Load Balancing method is selected.
        The datalength should not be more than 24k.
        Default value: 0
        Minimum value =  0
        Maximum value =  100
        """
        self.options['datalength'] = datalength

    def get_datalength(self):
        """
        Use this parameter to specify the length of the token in bytes. Applicable to
        TCP virtual servers, when Token Load Balancing method is selected.
        The datalength should not be more than 24k.
        Default value: 0
        Minimum value =  0
        Maximum value =  100
        """
        return self.options['datalength']

    def set_dataoffset(self, dataoffset):
        """
        Use this parameter to specifies offset of the data to be taken as token. Applicable to
        the TCP type virtual servers, when Token load balancing method is used.
        Must be within the first 24k of the client TCP data.
        Default value: 0
        Minimum value =  0
        Maximum value =  25400
        """
        self.options['dataoffset'] = dataoffset

    def get_dataoffset(self):
        """
        Use this parameter to specifies offset of the data to be taken as token. Applicable to
        the TCP type virtual servers, when Token load balancing method is used.
        Must be within the first 24k of the client TCP data.
        Default value: 0
        Minimum value =  0
        Maximum value =  25400
        """
        return self.options['dataoffset']

    def set_sessionless(self, sessionless):
        """
        Use this parameter to enable sessionless load balancing.
        Default value: DISABLED
        """
        self.options['sessionless'] = sessionless

    def get_sessionless(self):
        """
        Use this parameter to enable sessionless load balancing.
        Default value: DISABLED
        """
        return self.options['sessionless']

    def set_state(self, state):
        """
        The state of the load balancing virtual server.
        Default value: ENABLED
        """
        self.options['state'] = state

    def get_state(self):
        """
        The state of the load balancing virtual server.
        Default value: ENABLED
        """
        return self.options['state']

    def set_connfailover(self, connfailover):
        """
        Specifies the connection failover mode of the virtual server.
        Default value: DISABLED
        """
        self.options['connfailover'] = connfailover

    def get_connfailover(self):
        """
        Specifies the connection failover mode of the virtual server.
        Default value: DISABLED
        """
        return self.options['connfailover']

    def set_redirurl(self, redirurl):
        """
        The URL where traffic is redirected if the virtual server in the system becomes unavailable.
        You can enter up to 127 characters as the URL argument.
        WARNING!        Make sure that the domain you specify in the URL does not match the domain specified
        in the -d domainName argument of the add cs policy CLI command. If the same domain is specified
        in both arguments, the request will be
        continuously redirected to the same unavailable virtual server in the system  -  then the user
        may not get the requested content.
        Default value: 0
        Minimum length =  1.
        """
        self.options['redirurl'] = redirurl

    def get_redirurl(self):
        """
        The URL where traffic is redirected if the virtual server in the system becomes unavailable.
        You can enter up to 127 characters as the URL argument.
        WARNING!        Make sure that the domain you specify in the URL does not match the domain specified
        in the -d domainName argument of the add cs policy CLI command. If the same domain is specified
        in both arguments, the request will be
        continuously redirected to the same unavailable virtual server in the system  -  then the user
        may not get the requested content.
        Default value: 0
        Minimum length =  1.
        """
        return self.options['redirurl']

    def set_cacheable(self, cacheable):
        """
        Use this option to specify whether a virtual server, used for load balancing or content switching,
        routes requests to the cache redirection virtual server before sending it to the configured servers.
        Default value: NO
        """
        self.options['cacheable'] = cacheable

    def get_cacheable(self):
        """
        Use this option to specify whether a virtual server, used for load balancing or content switching,
        routes requests to the cache redirection virtual server before sending it to the configured servers.
        Default value: NO
        """
        return self.options['cacheable']

    def set_clttimeout(self, clttimeout):
        """
        The timeout value in seconds for idle client connection.
        Default value: 0
        Minimum value =  0
        Maximum value =  31536000
        """
        self.options['clttimeout'] = clttimeout

    def get_clttimeout(self):
        """
        The timeout value in seconds for idle client connection.
        Default value: 0
        Minimum value =  0
        Maximum value =  31536000
        """
        return self.options['clttimeout']

    def set_somethod(self, somethod):
        """
        The spillover factor based on which the traffic will be given to the backupvserver
        once the main virtual server reaches the spillover threshold.
        Default value: 0
        """
        self.options['somethod'] = somethod

    def get_somethod(self):
        """
        The spillover factor based on which the traffic will be given to the backupvserver
        once the main virtual server reaches the spillover threshold.
        Default value: 0
        """
        return self.options['somethod']

    def set_sopersistence(self, sopersistence):
        """
        The state of the spillover persistence.
        Default value: DISABLED
        """
        self.options['sopersistence'] = sopersistence

    def get_sopersistence(self):
        """
        The state of the spillover persistence.
        Default value: DISABLED
        """
        return self.options['sopersistence']

    def set_sopersistencetimeout(self, sopersistencetimeout):
        """
        The spillover persistency entry timeout.
        Default value: 2
        Minimum value =  2
        Maximum value =  1440
        """
        self.options['sopersistencetimeout'] = sopersistencetimeout

    def get_sopersistencetimeout(self):
        """
        The spillover persistency entry timeout.
        Default value: 2
        Minimum value =  2
        Maximum value =  1440
        """
        return self.options['sopersistencetimeout']

    def set_sothreshold(self, sothreshold):
        """
        In case of CONNECTION (or) DYNAMICCONNECTION type spillover method this value is treated
        as Maximum number of connections an lb vserver will handle before spillover takes place.
        In case of BANDWIDTH type spillover method this value is treated as the amount
        of incoming and outgoing traffic (in Kbps) a Vserver will handle before spillover takes place.
        In case of HEALTH type spillover method if the percentage of active services
        (by weight) becomes lower than this value, spillover takes place .
        Default value: 0
        Minimum value =  1
        Maximum value =  4294967287
        """
        self.options['sothreshold'] = sothreshold

    def get_sothreshold(self):
        """
        In case of CONNECTION (or) DYNAMICCONNECTION type spillover method this value is treated
        as Maximum number of connections an lb vserver will handle before spillover takes place.
        In case of BANDWIDTH type spillover method this value is treated as the amount
        of incoming and outgoing traffic (in Kbps) a Vserver will handle before spillover takes place.
        In case of HEALTH type spillover method if the percentage of active services
        (by weight) becomes lower than this value, spillover takes place .
        Default value: 0
        Minimum value =  1
        Maximum value =  4294967287
        """
        return self.options['sothreshold']

    def set_redirectportrewrite(self, redirectportrewrite):
        """
        The state of port rewrite while performing HTTP redirect.
        Default value: DISABLED
        """
        self.options['redirectportrewrite'] = redirectportrewrite

    def get_redirectportrewrite(self):
        """
        The state of port rewrite while performing HTTP redirect.
        Default value: DISABLED
        """
        return self.options['redirectportrewrite']

    def set_downstateflush(self, downstateflush):
        """
        Perform delayed clean up of connections on this vserver.
        Default value: ENABLED
        """
        self.options['downstateflush'] = downstateflush

    def get_downstateflush(self):
        """
        Perform delayed clean up of connections on this vserver.
        Default value: ENABLED
        """
        return self.options['downstateflush']

    def set_backupvserver(self, backupvserver):
        """
        The Backup Virtual Server.
        Default value: 0
        Minimum length =  1.
        """
        self.options['backupvserver'] = backupvserver

    def get_backupvserver(self):
        """
        The Backup Virtual Server.
        Default value: 0
        Minimum length =  1.
        """
        return self.options['backupvserver']

    def set_disableprimaryondown(self, disableprimaryondown):
        """
        When this argument is enabled, traffic will continue reaching backup vservers
        even after primary comes UP from DOWN state.
        Default value: DISABLED
        """
        self.options['disableprimaryondown'] = disableprimaryondown

    def get_disableprimaryondown(self):
        """
        When this argument is enabled, traffic will continue reaching backup vservers
        even after primary comes UP from DOWN state.
        Default value: DISABLED
        """
        return self.options['disableprimaryondown']

    def set_insertvserveripport(self, insertvserveripport):
        """
        The virtual IP and port header insertion option for the vserver.
               VIPADDR      - Header contains the vserver's IP address and port number without any translation.
               OFF             - The virtual IP and port header insertion option is disabled.
               V6TOV4MAPPING   - Header contains the mapped IPv4 address corresponding to the IPv6 address
               of the vserver and the port number. An IPv6 address can be mapped to
               a user-specified IPv4 address using the set ns ip6 command.
        Default value: OFF
        """
        self.options['insertvserveripport'] = insertvserveripport

    def get_insertvserveripport(self):
        """
        The virtual IP and port header insertion option for the vserver.
               VIPADDR      - Header contains the vserver's IP address and port number without any translation.
               OFF             - The virtual IP and port header insertion option is disabled.
               V6TOV4MAPPING   - Header contains the mapped IPv4 address corresponding to the IPv6 address
               of the vserver and the port number. An IPv6 address can be mapped to
        a user-specified IPv4 address using the set ns ip6 command.
        Default value: OFF
        """
        return self.options['insertvserveripport']

    def set_vipheader(self, vipheader):
        """
        The name of virtual IP and port header.
        Default value: 0
        Minimum length =  1.
        """
        self.options['vipheader'] = vipheader

    def get_vipheader(self):
        """
        The name of virtual IP and port header.
        Default value: 0
        Minimum length =  1.
        """
        return self.options['vipheader']

    def set_authenticationhost(self, authenticationhost):
        """
        FQDN of authentication vserver.
        Default value: 0
        Minimum length =  3.
        Maximum length =  252.
        """
        self.options['authenticationhost'] = authenticationhost

    def get_authenticationhost(self):
        """
        FQDN of authentication vserver.
        Default value: 0
        Minimum length =  3.
        Maximum length =  252.
        """
        return self.options['authenticationhost']

    def set_authentication(self, authentication):
        """
        This option toggles on or off the application of authentication of incoming users to the vserver.
        Default value: OFF
        """
        self.options['authentication'] = authentication

    def get_authentication(self):
        """
        This option toggles on or off the application of authentication of incoming users to the vserver.
        Default value: OFF
        """
        return self.options['authentication']

    def set_authn401(self, authn401):
        """
        This option toggles on or off the HTTP 401 response based authentication.
        Default value: OFF
        """
        self.options['authn401'] = authn401

    def get_authn401(self):
        """
        This option toggles on or off the HTTP 401 response based authentication.
        Default value: OFF
        """
        return self.options['authn401']

    def set_authnvsname(self, authnvsname):
        """
        Name of authentication vserver.
        Default value: 0
        Minimum length =  1.
        Maximum length =  252.
        """
        self.options['authnvsname'] = authnvsname

    def get_authnvsname(self):
        """
        Name of authentication vserver.
        Default value: 0
        Minimum length =  1.
        Maximum length =  252.
        """
        return self.options['authnvsname']

    def set_push(self, push):
        """
        Process traffic on bound Push vserver.
        Default value: DISABLED
        """
        self.options['push'] = push

    def get_push(self):
        """
        Process traffic on bound Push vserver.
        Default value: DISABLED
        """
        return self.options['push']

    def set_pushvserver(self, pushvserver):
        """
        The lb vserver of type PUSH/SSL_PUSH to which server pushes
        the updates received on the client facing non-push lb vserver.
        Default value: 0
        Minimum length =  1.
        """
        self.options['pushvserver'] = pushvserver

    def get_pushvserver(self):
        """
        The lb vserver of type PUSH/SSL_PUSH to which server pushes the updates received
        on the client facing non-push lb vserver.
        Default value: 0
        Minimum length =  1.
        """
        return self.options['pushvserver']

    def set_pushlabel(self, pushlabel):
        """
        Use this parameter to specify the expression to extract the label in response from server.
        The string can be either a named expression (configured using add policy expression command) or
        else it can be an in-line expression with a maximum of 63 characters.
        Default value: "none"
        """
        self.options['pushlabel'] = pushlabel

    def get_pushlabel(self):
        """
        Use this parameter to specify the expression to extract the label in response from server.
        The string can be either a named expression (configured using add policy expression command) or
        else it can be an in-line expression with a maximum of 63 characters.
        Default value: "none"
        """
        return self.options['pushlabel']

    def set_pushmulticlients(self, pushmulticlients):
        """
        Specify if multiple web 2.0 connections from the same client can connect
        to this vserver and expect updates.
        Default value: NO
        """
        self.options['pushmulticlients'] = pushmulticlients

    def get_pushmulticlients(self):
        """
        Specify if multiple web 2.0 connections from the same client can connect
        to this vserver and expect updates.
        Default value: NO
        """
        return self.options['pushmulticlients']

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
        Comments associated with this virtual server.
        Default value: 0
        """
        self.options['comment'] = comment

    def get_comment(self):
        """
        Comments associated with this virtual server.
        Default value: 0
        """
        return self.options['comment']

    def set_weight(self, weight):
        """
        The weight for the specified service.
        Default value: 0
        Minimum value =  1
        Maximum value =  100
        """
        self.options['weight'] = weight

    def get_weight(self):
        """
        The weight for the specified service.
        Default value: 0
        Minimum value =  1
        Maximum value =  100
        """
        return self.options['weight']

    def set_servicename(self, servicename):
        """
        The service name bound to the selected load balancing virtual server.
        Default value: 0
        Minimum length =  1.
        """
        self.options['servicename'] = servicename

    def get_servicename(self):
        """
        The service name bound to the selected load balancing virtual server.
        Default value: 0
        Minimum length =  1.
        """
        return self.options['servicename']

    def set_redirurlflags(self, redirurlflags):
        """
        The redirect URL to be unset.
        """
        self.options['redirurlflags'] = redirurlflags

    def get_redirurlflags(self):
        """
        The redirect URL to be unset.
        """
        return self.options['redirurlflags']

    def set_newname(self, newname):
        """
        The new name of the virtual server.
        Default value: 0
        Minimum length =  1.
        """
        self.options['newname'] = newname

    def get_newname(self):
        """
        The new name of the virtual server.
        Default value: 0
        Minimum length =  1.
        """
        return self.options['newname']

    def get_value(self):
        """
        SSL status.
        Default value: 0
        """
        return self.options['value']

    def get_ipmapping(self):
        """
        The permanent mapping for the V6 Address.
        Default value: 0
        """
        return self.options['ipmapping']

    def get_type(self):
        """
        Type of LB vserver.
        Default value: 0
        """
        return self.options['type']

    def get_curstate(self):
        """
        Current LB vserver state.
        Default value: 0
        """
        return self.options['curstate']

    def get_effectivestate(self):
        """
        Effective state of the LB vserver , based on the state of backup vservers.
        Default value: 0
        """
        return self.options['effectivestate']

    def get_status(self):
        """
        Current status of the lb vserver. During the initial phase if the configured lb method is not
        round robin , the vserver will adopt round robin to distribute
        traffic for a predefined number of requests.
        Default value: 0
        """
        return self.options['status']

    def get_lbrrreason(self):
        """
        Reason why a vserver is in RR. The following are the reasons:
        1  - MEP is DOWN (GSLB)
        2  - LB method has changed
        3  - Bound service's state changed to UP
        4  - A new service is bound
        5  - Startup RR factor has changed
        6  - LB feature is enabled
        7  - Load monitor is not active on a service
        8  - Vserver is Enabled
        9  - SSL feature is Enabled
        10 - All bound services have reached threshold. Using effective state to load balance (GSLB)
        11 - Primary state of bound services are not UP. Using effective state to load balance (GSLB)
        12 - No LB decision can be made as all bound services have either reached threshold or are not UP (GSLB)
        13 - All load monitors are active
        .
        Default value: 0
        """
        return self.options['lbrrreason']

    def get_redirect(self):
        """
        Cache redirect type.
        Default value: 0
        """
        return self.options['redirect']

    def get_precedence(self):
        """
        Precedence.
        Default value: 0
        """
        return self.options['precedence']

    def get_homepage(self):
        """
        Home page.
        Default value: 0
        """
        return self.options['homepage']

    def get_dnsvservername(self):
        """
        DNS vserver name.
        Default value: 0
        """
        return self.options['dnsvservername']

    def get_domain(self):
        """
        Domain.
        Default value: 0
        """
        return self.options['domain']

    def get_cachevserver(self):
        """
        Cache virtual server.
        Default value: 0
        """
        return self.options['cachevserver']

    def get_health(self):
        """
        Health of vserver based on percentage of weights of active svcs/all svcs.
        This does not consider administratively disabled svcs.
        Default value: 0
        """
        return self.options['health']

    def get_gotopriorityexpression(self):
        """
        Expression specifying the priority of the next policy which will get evaluated
        if the current policy rule evaluates to TRUE.
        Default value: 0
        """
        return self.options['gotopriorityexpression']

    def get_ruletype(self):
        """
        Rule type.
        Default value: 0
        """
        return self.options['ruletype']

    def get_groupname(self):
        """
        LB group to which the lb vserver is to be bound.
        Default value: 0
        """
        return self.options['groupname']

    def get_cookiedomain(self):
        """
        Domain name to be used in the set cookie header in case of cookie persistence.
        Default value: 0
        """
        return self.options['cookiedomain']

    def get_map(self):
        """
        Map.
        Default value: 0
        """
        return self.options['map']

    def get_gt2gb(self):
        """
        Allow for greater than 2 GB transactions on this vserver.
        Default value: 0
        """
        return self.options['gt2gb']

    def get_thresholdvalue(self):
        """
        Tells whether threshold exceeded for this service participating in CUSTOMLB.
        Default value: 0
        """
        return self.options['thresholdvalue']

    def get_bindpoint(self):
        """
        The bindpoint to which the policy is bound.
        Default value: 0
        """
        return self.options['bindpoint']

    def get_invoke(self):
        """
        Invoke flag.
        Default value: 0
        """
        return self.options['invoke']

    def get_labeltype(self):
        """
        The invocation type.
        Default value: 0
        """
        return self.options['labeltype']

    def get_labelname(self):
        """
        Name of the label invoked.
        Default value: 0
        """
        return self.options['labelname']

    def get_version(self):
        """
        Cookie version.
        Default value: 0
        """
        return self.options['version']

    def get_totalservices(self):
        """
        Total number of services bound to the vserver.
        Default value: 0
        """
        return self.options['totalservices']

    def get_activeservices(self):
        """
        Total number of active services bound to the vserver.
        Default value: 0
        """
        return self.options['activeservices']

    def get_statechangetimeseconds(self):
        """
        Time when last state change happened. Seconds part.
        Default value: 0
        """
        return self.options['statechangetimeseconds']

    def get_statechangetimemsec(self):
        """
        Time at which last state change happened. Milliseconds part.
        Default value: 0
        """
        return self.options['statechangetimemsec']

    def get_tickssincelaststatechange(self):
        """
        Time in 10 millisecond ticks since the last state change.
        Default value: 0
        """
        return self.options['tickssincelaststatechange']

    # Operations methods
    @staticmethod
    def disable(nitro, lbvserver):
        """
        Use this API to disable lbvserver.
        """
        __lbvserver = NSLBVServer()
        __lbvserver.set_name(lbvserver.get_name())
        return __lbvserver.perform_operation(nitro, "disable")

    @staticmethod
    def enable(nitro, lbvserver):
        """
        Use this API to enable lbvserver.
        """
        __lbvserver = NSLBVServer()
        __lbvserver.set_name(lbvserver.get_name())
        return __lbvserver.perform_operation(nitro, "enable")

    @staticmethod
    def rename(nitro, lbvserver):
        """
        Use this API to rename lbvserver.
        """
        __lbvserver = NSLBVServer()
        __lbvserver.set_name(lbvserver.get_name())
        __lbvserver.set_newname(lbvserver.get_newname())
        return __lbvserver.perform_operation(nitro, "rename")

    @staticmethod
    def get(nitro, lbvserver):
        """
        Use this API to fetch lbvserver resource of given name.
        """
        __lbvserver = NSLBVServer()
        __lbvserver.set_name(lbvserver.get_name())
        __lbvserver.get_resource(nitro)
        return __lbvserver

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured lbvserver resources.
        """
        __url = nitro.get_url() + NSLBVServer.get_resourcetype()
        __json_lbvservers = nitro.get(__url).get_response_field(NSLBVServer.get_resourcetype())
        __lbvservers = []
        for json_lbvserver in __json_lbvservers:
            __lbvservers.append(NSLBVServer(json_lbvserver))
        return __lbvservers

    @staticmethod
    def add(nitro, lbvserver):
        """
        Use this API to add lbvserver.
        """
        __lbvserver = NSLBVServer()
        __lbvserver.set_name(lbvserver.get_name())
        __lbvserver.set_servicetype(lbvserver.get_servicetype())
        __lbvserver.set_ipv46(lbvserver.get_ipv46())
        __lbvserver.set_ippattern(lbvserver.get_ippattern())
        __lbvserver.set_ipmask(lbvserver.get_ipmask())
        __lbvserver.set_port(lbvserver.get_port())
        __lbvserver.set_range(lbvserver.get_range())
        __lbvserver.set_persistencetype(lbvserver.get_persistencetype())
        __lbvserver.set_timeout(lbvserver.get_timeout())
        __lbvserver.set_persistencebackup(lbvserver.get_persistencebackup())
        __lbvserver.set_backuppersistencetimeout(lbvserver.get_backuppersistencetimeout())
        __lbvserver.set_lbmethod(lbvserver.get_lbmethod())
        __lbvserver.set_hashlength(lbvserver.get_hashlength())
        __lbvserver.set_netmask(lbvserver.get_netmask())
        __lbvserver.set_v6netmasklen(lbvserver.get_v6netmasklen())
        __lbvserver.set_rule(lbvserver.get_rule())
        __lbvserver.set_listenpolicy(lbvserver.get_listenpolicy())
        __lbvserver.set_listenpriority(lbvserver.get_listenpriority())
        __lbvserver.set_resrule(lbvserver.get_resrule())
        __lbvserver.set_persistmask(lbvserver.get_persistmask())
        __lbvserver.set_v6persistmasklen(lbvserver.get_v6persistmasklen())
        __lbvserver.set_pq(lbvserver.get_pq())
        __lbvserver.set_sc(lbvserver.get_sc())
        __lbvserver.set_rtspnat(lbvserver.get_rtspnat())
        __lbvserver.set_m(lbvserver.get_m())
        __lbvserver.set_tosid(lbvserver.get_tosid())
        __lbvserver.set_datalength(lbvserver.get_datalength())
        __lbvserver.set_dataoffset(lbvserver.get_dataoffset())
        __lbvserver.set_sessionless(lbvserver.get_sessionless())
        __lbvserver.set_state(lbvserver.get_state())
        __lbvserver.set_connfailover(lbvserver.get_connfailover())
        __lbvserver.set_redirurl(lbvserver.get_redirurl())
        __lbvserver.set_cacheable(lbvserver.get_cacheable())
        __lbvserver.set_clttimeout(lbvserver.get_clttimeout())
        __lbvserver.set_somethod(lbvserver.get_somethod())
        __lbvserver.set_sopersistence(lbvserver.get_sopersistence())
        __lbvserver.set_sopersistencetimeout(lbvserver.get_sopersistencetimeout())
        __lbvserver.set_sothreshold(lbvserver.get_sothreshold())
        __lbvserver.set_redirectportrewrite(lbvserver.get_redirectportrewrite())
        __lbvserver.set_downstateflush(lbvserver.get_downstateflush())
        __lbvserver.set_backupvserver(lbvserver.get_backupvserver())
        __lbvserver.set_disableprimaryondown(lbvserver.get_disableprimaryondown())
        __lbvserver.set_insertvserveripport(lbvserver.get_insertvserveripport())
        __lbvserver.set_vipheader(lbvserver.get_vipheader())
        __lbvserver.set_authenticationhost(lbvserver.get_authenticationhost())
        __lbvserver.set_authentication(lbvserver.get_authentication())
        __lbvserver.set_authn401(lbvserver.get_authn401())
        __lbvserver.set_authnvsname(lbvserver.get_authnvsname())
        __lbvserver.set_push(lbvserver.get_push())
        __lbvserver.set_pushvserver(lbvserver.get_pushvserver())
        __lbvserver.set_pushlabel(lbvserver.get_pushlabel())
        __lbvserver.set_pushmulticlients(lbvserver.get_pushmulticlients())
        __lbvserver.set_tcpprofilename(lbvserver.get_tcpprofilename())
        __lbvserver.set_httpprofilename(lbvserver.get_httpprofilename())
        __lbvserver.set_comment(lbvserver.get_comment())
        return __lbvserver.add_resource(nitro)

    @staticmethod
    def delete(nitro, lbvserver):
        """
        Use this API to delete lbvserver of a given name.
        """
        __lbvserver = NSLBVServer()
        __lbvserver.set_name(lbvserver.get_name())
        nsresponse = __lbvserver.delete_resource(nitro)
        return nsresponse

    @staticmethod
    def update(nitro, lbvserver):
        """
        Use this API to update lbvserver of a given name.
        """
        __lbvserver = NSLBVServer()
        __lbvserver.set_name(lbvserver.get_name())
        __lbvserver.set_ipv46(lbvserver.get_ipv46())
        __lbvserver.set_ippattern(lbvserver.get_ippattern())
        __lbvserver.set_ipmask(lbvserver.get_ipmask())
        __lbvserver.set_weight(lbvserver.get_weight())
        __lbvserver.set_servicename(lbvserver.get_servicename())
        __lbvserver.set_persistencetype(lbvserver.get_persistencetype())
        __lbvserver.set_timeout(lbvserver.get_timeout())
        __lbvserver.set_persistencebackup(lbvserver.get_persistencebackup())
        __lbvserver.set_backuppersistencetimeout(lbvserver.get_backuppersistencetimeout())
        __lbvserver.set_lbmethod(lbvserver.get_lbmethod())
        __lbvserver.set_hashlength(lbvserver.get_hashlength())
        __lbvserver.set_netmask(lbvserver.get_netmask())
        __lbvserver.set_v6netmasklen(lbvserver.get_v6netmasklen())
        __lbvserver.set_rule(lbvserver.get_rule())
        __lbvserver.set_resrule(lbvserver.get_resrule())
        __lbvserver.set_persistmask(lbvserver.get_persistmask())
        __lbvserver.set_v6persistmasklen(lbvserver.get_v6persistmasklen())
        __lbvserver.set_pq(lbvserver.get_pq())
        __lbvserver.set_sc(lbvserver.get_sc())
        __lbvserver.set_rtspnat(lbvserver.get_rtspnat())
        __lbvserver.set_m(lbvserver.get_m())
        __lbvserver.set_tosid(lbvserver.get_tosid())
        __lbvserver.set_datalength(lbvserver.get_datalength())
        __lbvserver.set_dataoffset(lbvserver.get_dataoffset())
        __lbvserver.set_sessionless(lbvserver.get_sessionless())
        __lbvserver.set_connfailover(lbvserver.get_connfailover())
        __lbvserver.set_backupvserver(lbvserver.get_backupvserver())
        __lbvserver.set_redirurl(lbvserver.get_redirurl())
        __lbvserver.set_cacheable(lbvserver.get_cacheable())
        __lbvserver.set_clttimeout(lbvserver.get_clttimeout())
        __lbvserver.set_somethod(lbvserver.get_somethod())
        __lbvserver.set_sothreshold(lbvserver.get_sothreshold())
        __lbvserver.set_sopersistence(lbvserver.get_sopersistence())
        __lbvserver.set_sopersistencetimeout(lbvserver.get_sopersistencetimeout())
        __lbvserver.set_redirectportrewrite(lbvserver.get_redirectportrewrite())
        __lbvserver.set_downstateflush(lbvserver.get_downstateflush())
        __lbvserver.set_insertvserveripport(lbvserver.get_insertvserveripport())
        __lbvserver.set_vipheader(lbvserver.get_vipheader())
        __lbvserver.set_disableprimaryondown(lbvserver.get_disableprimaryondown())
        __lbvserver.set_authenticationhost(lbvserver.get_authenticationhost())
        __lbvserver.set_authentication(lbvserver.get_authentication())
        __lbvserver.set_authn401(lbvserver.get_authn401())
        __lbvserver.set_authnvsname(lbvserver.get_authnvsname())
        __lbvserver.set_push(lbvserver.get_push())
        __lbvserver.set_pushvserver(lbvserver.get_pushvserver())
        __lbvserver.set_pushlabel(lbvserver.get_pushlabel())
        __lbvserver.set_pushmulticlients(lbvserver.get_pushmulticlients())
        __lbvserver.set_listenpolicy(lbvserver.get_listenpolicy())
        __lbvserver.set_listenpriority(lbvserver.get_listenpriority())
        __lbvserver.set_tcpprofilename(lbvserver.get_tcpprofilename())
        __lbvserver.set_httpprofilename(lbvserver.get_httpprofilename())
        __lbvserver.set_comment(lbvserver.get_comment())
        return __lbvserver.update_resource(nitro)
