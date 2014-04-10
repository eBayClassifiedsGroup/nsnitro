from nsbaseresource import NSBaseResource

__author__ = 'vlazarenko'


class NSCSVServer(NSBaseResource):

    # Configuration for Content Switching Virtual Server resource.

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSCSVServer, self).__init__()

        self.options = {'name': '',
                        'servicetype': '',
                        'ipv46': '',
                        'ippattern': '',
                        'ipmask': '',
                        'range': '',
                        'port': '',
                        'state': '',
                        'stateupdate': '',
                        'cacheable': '',
                        'redirecturl': '',
                        'clttimeout': '',
                        'precedence': '',
                        'casesensitive': '',
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
                        'rtspnat': '',
                        'authenticationhost': '',
                        'authentication': '',
                        'listenpolicy': '',
                        'listenpriority': '',
                        'authn401': '',
                        'authnvsname': '',
                        'push': '',
                        'pushvserver': '',
                        'pushlabel': '',
                        'pushmulticlients': '',
                        'tcpprofilename': '',
                        'httpprofilename': '',
                        'comment': '',
                        'newname': '',

                        # --- Read-only options ---

                        'ip': '',
                        'value': '',
                        'type': '',
                        'curstate': '',
                        'status': '',
                        'cachetype': '',
                        'redirect': '',
                        'homepage': '',
                        'dnsvservername': '',
                        'domain': '',
                        'servicename': '',
                        'weight': '',
                        'cachevserver': '',
                        'targetvserver': '',
                        'url': '',
                        'gotopriorityexpression': '',
                        'bindpoint': '',
                        'invoke': '',
                        'labeltype': '',
                        'labelname': '',
                        'gt2gb': '',
                        'statechangetimesec': '',
                        'statechangetimemsec': '',
                        'tickssincelaststatechange': ''}

        self.resourcetype = NSCSVServer.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "csvserver"

    def set_name(self, name):
        """
        The content switching virtual server name.
        Default value: 0<
        Minimum length =  1.
        """
        self.options['name'] = name

    def get_name(self):
        """
        The content switching virtual server name.
        Default value: 0<
        Minimum length =  1.
        """
        return self.options['name']

    def set_servicetype(self, servicetype):
        """
        The service type of the virtual server.
        Default value: 0
        """
        self.options['servicetype'] = servicetype

    def get_servicetype(self):
        """
        The service type of the virtual server.
        Default value: 0
        """
        return self.options['servicetype']

    def set_ipv46(self, ipv46):
        """
        The IP address of the virtual server.
        Default value: 0
        Minimum length =  1.
        """
        self.options['ipv46'] = ipv46

    def get_ipv46(self):
        """
        The IP address of the virtual server.
        Default value: 0
        Minimum length =  1.
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

    def set_range(self, myrange):
        """
        An IP address range.
        Default value: 1
        Minimum value =  1
        """
        self.options['range'] = myrange

    def get_range(self):
        """
        An IP address range.
        Default value: 1
        Minimum value =  1
        """
        return self.options['range']

    def set_port(self, port):
        """
        A port number for the virtual server.
        Default value: 0
        Minimum value =  1
        Range 1 - 65535.
        """
        self.options['port'] = port

    def get_port(self):
        """
        A port number for the virtual server.
        Default value: 0
        Minimum value =  1
        Range 1 - 65535.
        """
        return self.options['port']

    def set_state(self, state):
        """
        The initial state, enabled or disabled, of the virtual server.
        Default value: ENABLED
        """
        self.options['state'] = state

    def get_state(self):
        """
        The initial state, enabled or disabled, of the virtual server.
        Default value: ENABLED
        """
        return self.options['state']

    def set_stateupdate(self, stateupdate):
        """
        To enable the state update for a CSW vserver.
        Default value: DISABLED
        """
        self.options['stateupdate'] = stateupdate

    def get_stateupdate(self):
        """
        To enable the state update for a CSW vserver.
        Default value: DISABLED
        """
        return self.options['stateupdate']

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

    def set_redirecturl(self, redirecturl):
        """
        The URL where traffic is redirected if the virtual server in the system becomes unavailable.
        You can enter up to 127 characters as the URL argument.

        WARNING!

        Make sure that the domain you specify in URL does not match the domain specified in the -d domainName
        argument of the add cs policy CLI command. If the same domain is specified in both arguments,
        the request will be continuously redirected to the same unavailable virtual server in the system  -
        then the user may not get the requested content.

        Default value: 0
        Minimum length =  1.
        """
        self.options['redirecturl'] = redirecturl

    def get_redirecturl(self):
        """
        The URL where traffic is redirected if the virtual server in the system becomes unavailable.
        You can enter up to 127 characters as the URL argument.

        WARNING!

        Make sure that the domain you specify in URL does not match the domain specified in the -d domainName
        argument of the add cs policy CLI command. If the same domain is specified in both arguments,
        the request will be continuously redirected to the same unavailable virtual server in the system  -
        then the user may not get the requested content.

        Default value: 0
        Minimum length =  1.
        """
        return self.options['redirecturl']

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

    def set_precedence(self, precedence):
        """
        This sets the precedence between RULE-based and URL-based policies on the content switching
        virtual server. The default precedence is RULE.
        With the precedence set to RULE, incoming requests are evaluated against the content switching policies
        created with the -rule argument (using the add cs policy CLI command).
        If none of the rules match, the URL in the request is evaluated against the content switching policies
        created with the -url argument (using the add cs policy CLI command).

        Default value: RULE
        """
        self.options['precedence'] = precedence

    def get_precedence(self):
        """
        This sets the precedence between RULE-based and URL-based policies on the content switching
        virtual server. The default precedence is RULE.
        With the precedence set to RULE, incoming requests are evaluated against the content switching policies
        created with the -rule argument (using the add cs policy CLI command).
        If none of the rules match, the URL in the request is evaluated against the content switching policies
        created with the -url argument (using the add cs policy CLI command).

        Default value: RULE
        """
        return self.options['precedence']

    def set_casesensitive(self, casesensitive):
        """
        The URL lookup case option on the content switching vserver.
        If the case sensitivity of a content switching virtual server is set to 'ON', the URLs
        /a/1.html and /A/1.HTML are treated differently, and can be switched to different targets
        with appropriate content switching policies.
        If the case sensitivity is set to 'OFF', the URLs /a/1.html and /A/1.HTML are treated the same, and
        are switched to the same target.

        Default value: ON
        """
        self.options['casesensitive'] = casesensitive

    def get_casesensitive(self):
        """
        The URL lookup case option on the content switching vserver.
        If the case sensitivity of a content switching virtual server is set to 'ON', the URLs
        /a/1.html and /A/1.HTML are treated differently, and can be switched to different targets
        with appropriate content switching policies.
        If the case sensitivity is set to 'OFF', the URLs /a/1.html and /A/1.HTML are treated the same, and
        are switched to the same target.

        Default value: ON
        """
        return self.options['casesensitive']

    def set_somethod(self, somethod):
        """
        The spillover factor based on which the traffic will be given to the backupvserver once the main virtual
        server reaches the spillover threshold.

        Default value: 0
        """
        self.options['somethod'] = somethod

    def get_somethod(self):
        """
        The spillover factor based on which the traffic will be given to the backupvserver once the main virtual
        server reaches the spillover threshold.

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
        Default value: 2
        Minimum value =  2
        Maximum value =  1440
        """
        self.options['sopersistencetimeout'] = sopersistencetimeout

    def get_sopersistencetimeout(self):
        """
        Default value: 2
        Minimum value =  2
        Maximum value =  1440
        """
        return self.options['sopersistencetimeout']

    def set_sothreshold(self, sothreshold):
        """
        If the spillover method is set to CONNECTION or DYNAMICCONNECTION, this value is treated as the maximum
        number of connections a lb vserver will handle before spillover takes place. If the spillover method is
        set to BANDWIDTH, this value is treated as the amount of incoming and outgoing traffic (in Kbps)
        a vserver will handle before spillover takes place.

        Default value: 0
        Minimum value =  1
        Maximum value =  4294967287
        """
        self.options['sothreshold'] = sothreshold

    def get_sothreshold(self):
        """
        If the spillover method is set to CONNECTION or DYNAMICCONNECTION, this value is treated as the maximum
        number of connections a lb vserver will handle before spillover takes place. If the spillover method is
        set to BANDWIDTH, this value is treated as the amount of incoming and outgoing traffic (in Kbps)
        a vserver will handle before spillover takes place.

        Default value: 0
        Minimum value =  1
        Maximum value =  4294967287
        """
        return self.options['sothreshold']

    def set_redirectportrewrite(self, redirectportrewrite):
        """
        Enable port rewrite while performing HTTP redirect.

        Default value: DISABLED
        """
        self.options['redirectportrewrite'] = redirectportrewrite

    def get_redirectportrewrite(self):
        """
        Enable port rewrite while performing HTTP redirect.

        Default value: DISABLED
        """
        return self.options['redirectportrewrite']

    def set_downstateflush(self, downstateflush):
        """
        Perform delayed cleanup of connections on this vserver.

        Default value: ENABLED
        """
        self.options['downstateflush'] = downstateflush

    def get_downstateflush(self):
        """
        Perform delayed cleanup of connections on this vserver.

        Default value: ENABLED
        """
        return self.options['downstateflush']

    def set_backupvserver(self, backupvserver):
        """
        The backup virtual server for content switching.

        Default value: 0
        Minimum length =  1.
        """
        self.options['backupvserver'] = backupvserver

    def get_backupvserver(self):
        """
        The backup virtual server for content switching.

        Default value: 0
        Minimum length =  1.
        """
        return self.options['backupvserver']

    def set_disableprimaryondown(self, disableprimaryondown):
        """
        When this argument is enabled, traffic will continue reaching backup vservers even after primary
        comes UP from DOWN state.

        Default value: DISABLED
        """
        self.options['disableprimaryondown'] = disableprimaryondown

    def get_disableprimaryondown(self):
        """
        When this argument is enabled, traffic will continue reaching backup vservers even after primary
        comes UP from DOWN state.

        Default value: DISABLED
        """
        return self.options['disableprimaryondown']

    def set_insertvserveripport(self, insertvserveripport):
        """
        The virtual IP and port header insertion option for the vserver.
        VIPADDR - Header contains the vserver's IP address and port number without any translation.
        OFF - The virtual IP and port header insertion option is disabled.
        V6TOV4MAPPING - Header contains the mapped IPv4 address corresponding to the IPv6 address of the vserver
        and the port number. An IPv6 address can be mapped to a user-specified IPv4 address using
        the set ns ip6 command.

        Default value: OFF
        """
        self.options['insertvserveripport'] = insertvserveripport

    def get_insertvserveripport(self):
        """
        The virtual IP and port header insertion option for the vserver.
        VIPADDR - Header contains the vserver's IP address and port number without any translation.
        OFF - The virtual IP and port header insertion option is disabled.
        V6TOV4MAPPING - Header contains the mapped IPv4 address corresponding to the IPv6 address of the vserver
        and the port number. An IPv6 address can be mapped to a user-specified IPv4 address using
        the set ns ip6 command.

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

    def set_listenpolicy(self, listenpolicy):
        """
        Use this parameter to specify the listen policy for CS Vserver.
        The string can be either an existing expression name (configured using add policy expression command)
        or else it can be an in-line expression with a maximum of 1500 characters.

        Default value: "none"
        """
        self.options['listenpolicy'] = listenpolicy

    def get_listenpolicy(self):
        """
        Use this parameter to specify the listen policy for CS Vserver.
        The string can be either an existing expression name (configured using add policy expression command)
        or else it can be an in-line expression with a maximum of 1500 characters.

        Default value: "none"
        """
        return self.options['listenpolicy']

    def set_listenpriority(self, listenpriority):
        """
        Use this parameter to specify the priority for listen policy of CS Vserver.

        Default value: 101
        Minimum value =  0
        Maximum value =  100
        """
        self.options['listenpriority'] = listenpriority

    def get_listenpriority(self):
        """
        Use this parameter to specify the priority for listen policy of CS Vserver.

        Default value: 101
        Minimum value =  0
        Maximum value =  100
        """
        return self.options['listenpriority']

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
        The lb vserver of type PUSH/SSL_PUSH to which server pushes the updates received on the client facing
        non-push lb vserver.

        Default value: 0
        Minimum length =  1.
        """
        self.options['pushvserver'] = pushvserver

    def get_pushvserver(self):
        """
        The lb vserver of type PUSH/SSL_PUSH to which server pushes the updates received on the client facing
        non-push lb vserver.

        Default value: 0
        Minimum length =  1.
        """
        return self.options['pushvserver']

    def set_pushlabel(self, pushlabel):
        """
        Use this parameter to specify the expression to extract the label in response from server.
        The string can be either a named expression (configured using add policy expression command) or else it
        can be an in-line expression with a maximum of 63 characters.

        Default value: "none"
        """
        self.options['pushlabel'] = pushlabel

    def get_pushlabel(self):
        """
        Use this parameter to specify the expression to extract the label in response from server.
        The string can be either a named expression (configured using add policy expression command) or else it
        can be an in-line expression with a maximum of 63 characters.

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

    def get_ip(self):
        """
        The IP address of the virtual server.

        Default value: 0
        """
        return self.options['ip']

    def get_value(self):
        """
        The ssl card status for the transparent ssl cs vserver.

        Default value: 0
        """
        return self.options['value']

    def get_type(self):
        """
        Virtual server type.

        Default value: 0
        """
        return self.options['type']

    def get_curstate(self):
        """
        The state of the cs vserver.

        Default value: 0
        """
        return self.options['curstate']

    def get_status(self):
        """
        Status.

        Default value: 0
        """
        return self.options['status']

    def get_cachetype(self):
        """
        Cache type.

        Default value: 0
        """
        return self.options['cachetype']

    def get_redirect(self):
        """
        Redirect UTL string.

        Default value: 0
        """
        return self.options['redirect']

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

    def get_servicename(self):
        """
        Service name.

        Default value: 0
        """
        return self.options['servicename']

    def get_weight(self):
        """
        Weight for this service.

        Default value: 0
        """
        return self.options['weight']

    def get_cachevserver(self):
        """
        Cache vserver name.

        Default value: 0
        """
        return self.options['cachevserver']

    def get_targetvserver(self):
        """
        Target vserver name.

        Default value: 0
        """
        return self.options['targetvserver']

    def get_url(self):
        """
        URL string.

        Default value: 0
        """
        return self.options['url']

    def get_gotopriorityexpression(self):
        """
        Expression specifying the priority of the next policy which will get evaluated if the current policy
        rule evaluates to TRUE.

        Default value: 0
        """
        return self.options['gotopriorityexpression']

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

    def get_gt2gb(self):
        """
        This argument has no effect.

        Default value: 0
        """
        return self.options['gt2gb']

    def get_statechangetimesec(self):
        """
        Time when last state change happened. Seconds part.

        Default value: 0
        """
        return self.options['statechangetimesec']

    def get_statechangetimemsec(self):
        """
        Time when last state change happened. Milliseconds part.

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
    def disable(nitro, csvserver):
        """
        Use this API to disable csvserver.
        """
        __csvserver = NSCSVServer()
        __csvserver.set_name(csvserver.get_name())
        return __csvserver.perform_operation(nitro, "disable")

    @staticmethod
    def enable(nitro, csvserver):
        """
        Use this API to enable csvserver.
        """
        __csvserver = NSCSVServer()
        __csvserver.set_name(csvserver.get_name())
        return __csvserver.perform_operation(nitro, "enable")

    @staticmethod
    def rename(nitro, csvserver):
        """
        Use this API to rename csvserver.
        """
        __csvserver = NSCSVServer()
        __csvserver.set_name(csvserver.get_name())
        __csvserver.set_newname(csvserver.get_newname())
        return __csvserver.perform_operation(nitro, "rename")

    @staticmethod
    def get(nitro, csvserver):
        """
        Use this API to fetch csvserver resource of given name.
        """
        __csvserver = NSCSVServer()
        __csvserver.set_name(csvserver.get_name())
        __csvserver.get_resource(nitro)
        return __csvserver

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured csvserver resources.
        """
        __url = nitro.get_url() + NSCSVServer.get_resourcetype()
        __json_csvservers = nitro.get(__url).get_response_field(NSCSVServer.get_resourcetype())
        __csvservers = []
        for json_csvserver in __json_csvservers:
            __csvservers.append(NSCSVServer(json_csvserver))
        return __csvservers

    @staticmethod
    def add(nitro, csvserver):
        """
        Use this API to add csvserver.
        """
        __csvserver = NSCSVServer()
        __csvserver.set_name(csvserver.get_name())
        __csvserver.set_servicetype(csvserver.get_servicetype())
        __csvserver.set_ipv46(csvserver.get_ipv46())
        __csvserver.set_ippattern(csvserver.get_ippattern())
        __csvserver.set_ipmask(csvserver.get_ipmask())
        __csvserver.set_range(csvserver.get_range())
        __csvserver.set_port(csvserver.get_port())
        __csvserver.set_state(csvserver.get_state())
        __csvserver.set_stateupdate(csvserver.get_stateupdate())
        __csvserver.set_cacheable(csvserver.get_cacheable())
        __csvserver.set_redirecturl(csvserver.get_redirecturl())
        __csvserver.set_clttimeout(csvserver.get_clttimeout())
        __csvserver.set_precedence(csvserver.get_precedence())
        __csvserver.set_casesensitive(csvserver.get_casesensitive())
        __csvserver.set_somethod(csvserver.get_somethod())
        __csvserver.set_sopersistence(csvserver.get_sopersistence())
        __csvserver.set_sopersistencetimeout(csvserver.get_sopersistencetimeout())
        __csvserver.set_sothreshold(csvserver.get_sothreshold())
        __csvserver.set_redirectportrewrite(csvserver.get_redirectportrewrite())
        __csvserver.set_downstateflush(csvserver.get_downstateflush())
        __csvserver.set_backupvserver(csvserver.get_backupvserver())
        __csvserver.set_disableprimaryondown(csvserver.get_disableprimaryondown())
        __csvserver.set_insertvserveripport(csvserver.get_insertvserveripport())
        __csvserver.set_vipheader(csvserver.get_vipheader())
        __csvserver.set_rtspnat(csvserver.get_rtspnat())
        __csvserver.set_authenticationhost(csvserver.get_authenticationhost())
        __csvserver.set_authentication(csvserver.get_authentication())
        __csvserver.set_listenpolicy(csvserver.get_listenpolicy())
        __csvserver.set_listenpriority(csvserver.get_listenpriority())
        __csvserver.set_authn401(csvserver.get_authn401())
        __csvserver.set_authnvsname(csvserver.get_authnvsname())
        __csvserver.set_push(csvserver.get_push())
        __csvserver.set_pushvserver(csvserver.get_pushvserver())
        __csvserver.set_pushlabel(csvserver.get_pushlabel())
        __csvserver.set_pushmulticlients(csvserver.get_pushmulticlients())
        __csvserver.set_tcpprofilename(csvserver.get_tcpprofilename())
        __csvserver.set_httpprofilename(csvserver.get_httpprofilename())
        __csvserver.set_comment(csvserver.get_comment())
        return __csvserver.add_resource(nitro)

    @staticmethod
    def delete(nitro, csvserver):
        """
        Use this API to delete csvserver of a given name.
        """
        __csvserver = NSCSVServer()
        __csvserver.set_name(csvserver.get_name())
        nsresponse = __csvserver.delete_resource(nitro)
        return nsresponse

    @staticmethod
    def update(nitro, csvserver):
        """
        Use this API to update csvserver of a given name.
        """
        __csvserver = NSCSVServer()
        __csvserver.set_name(csvserver.get_name())
        __csvserver.set_ipv46(csvserver.get_ipv46())
        __csvserver.set_ippattern(csvserver.get_ippattern())
        __csvserver.set_ipmask(csvserver.get_ipmask())
        __csvserver.set_stateupdate(csvserver.get_stateupdate())
        __csvserver.set_precedence(csvserver.get_precedence())
        __csvserver.set_casesensitive(csvserver.get_casesensitive())
        __csvserver.set_backupvserver(csvserver.get_backupvserver())
        __csvserver.set_redirecturl(csvserver.get_redirecturl())
        __csvserver.set_cacheable(csvserver.get_cacheable())
        __csvserver.set_clttimeout(csvserver.get_clttimeout())
        __csvserver.set_somethod(csvserver.get_somethod())
        __csvserver.set_sopersistence(csvserver.get_sopersistence())
        __csvserver.set_sopersistencetimeout(csvserver.get_sopersistencetimeout())
        __csvserver.set_sothreshold(csvserver.get_sothreshold())
        __csvserver.set_redirectportrewrite(csvserver.get_redirectportrewrite())
        __csvserver.set_downstateflush(csvserver.get_downstateflush())
        __csvserver.set_disableprimaryondown(csvserver.get_disableprimaryondown())
        __csvserver.set_insertvserveripport(csvserver.get_insertvserveripport())
        __csvserver.set_vipheader(csvserver.get_vipheader())
        __csvserver.set_rtspnat(csvserver.get_rtspnat())
        __csvserver.set_authenticationhost(csvserver.get_authenticationhost())
        __csvserver.set_authentication(csvserver.get_authentication())
        __csvserver.set_listenpolicy(csvserver.get_listenpolicy())
        __csvserver.set_listenpriority(csvserver.get_listenpriority())
        __csvserver.set_authn401(csvserver.get_authn401())
        __csvserver.set_authnvsname(csvserver.get_authnvsname())
        __csvserver.set_push(csvserver.get_push())
        __csvserver.set_pushvserver(csvserver.get_pushvserver())
        __csvserver.set_pushlabel(csvserver.get_pushlabel())
        __csvserver.set_pushmulticlients(csvserver.get_pushmulticlients())
        __csvserver.set_tcpprofilename(csvserver.get_tcpprofilename())
        __csvserver.set_httpprofilename(csvserver.get_httpprofilename())
        __csvserver.set_comment(csvserver.get_comment())
        return __csvserver.update_resource(nitro)
