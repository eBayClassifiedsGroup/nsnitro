from nsbaseresource import NSBaseResource

__author__ = 'vlazarenko'


class NSConfig(NSBaseResource):

    # General Netscaler configuration object

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """

        super(NSConfig, self).__init__()

        self.options = {'force': '',
                        'level': '',
                        'ipaddress': '',
                        'netmask': '',
                        'nsvlan': '',
                        'ifnum': '',
                        'httpport': '',
                        'maxconn': '',
                        'maxreq': '',
                        'cip': '',
                        'cipheader': '',
                        'cookieversion': '',
                        'securecookie': '',
                        'pmtumin': '',
                        'pmtutimeout': '',
                        'ftpportrange': '',
                        'timezone': '',
                        'grantquotamaxclient': '',
                        'exclusivequotamaxclient': '',
                        'grantquotaspillover': '',
                        'exclusivequotaspillover': '',
                        'config1': '',
                        'config2': '',
                        'outtype': '',
                        'template': '',
                        'message': '',
                        'range': '',
                        'failover': '',
                        'primaryip': '',
                        'flags': '',
                        'lastconfigchangedtime': '',
                        'systemtime': ''}

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

        self.resourcetype = NSConfig.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        return "nsconfig"

    def set_force(self, force):
        """
        Clear the configuration without prompting confirmation.

        Default value: 0
        """
        self.options['force'] = force

    def get_force(self):
        """
        Clear the configuration without prompting confirmation.

        Default value: 0
        """
        return self.options['force']

    def set_level(self, level):
        """
        Clear the configuration according to the levels.

        Default value: 0
        """
        self.options['level'] = level

    def get_level(self):
        """
        Clear the configuration according to the levels.

        Default value: 0
        """
        return self.options['level']

    def set_ipaddress(self, ipaddress):
        """
        The IP address of the system.

        Default value: 0
        Minimum length =  1.
        """
        self.options['ipaddress'] = ipaddress

    def get_ipaddress(self):
        """
        The IP address of the system.

        Default value: 0
        Minimum length =  1.
        """
        return self.options['ipaddress']

    def set_netmask(self, netmask):
        """
        The netmask corresponding to the IP address.

        Default value: 0
        """
        self.options['netmask'] = netmask

    def get_netmask(self):
        """
        The netmask corresponding to the IP address.

        Default value: 0
        """
        return self.options['netmask']

    def set_nsvlan(self, nsvlan):
        """
        The VLAN (NSVLAN) for the subnet on which the IP resides.

        Default value: 0
        Minimum value =  2
        Maximum value =  4094
        """
        self.options['nsvlan'] = nsvlan

    def get_nsvlan(self):
        """
        The VLAN (NSVLAN) for the subnet on which the IP resides.

        Default value: 0
        Minimum value =  2
        Maximum value =  4094
        """
        return self.options['nsvlan']

    def set_ifnum(self, ifnum):
        """
        Bind the given ports to the NSVLAN.

        Default value: 0
        Minimum length =  1.
        """
        self.options['ifnum'] = ifnum

    def get_ifnum(self):
        """
        Bind the given ports to the NSVLAN.

        Default value: 0
        Minimum length =  1.
        """
        return self.options['ifnum']

    def set_httpport(self, httpport):
        """
        The HTTP ports on the Web server. This allows the system to perform connection off-load for any client
        request that has a destination port matching one of these configured ports.

        Default value: 0
        Minimum value =  1
        """
        self.options['httpport'] = httpport

    def get_httpport(self):
        """
        The HTTP ports on the Web server. This allows the system to perform connection off-load for any client
        request that has a destination port matching one of these configured ports.

        Default value: 0
        Minimum value =  1
        """
        return self.options['httpport']

    def set_maxconn(self, maxconn):
        """
        The maximum number of connections that will be made from the system to the web server(s) attached to it.
        The value entered here is applied globally to all attached servers.

        Default value: 0
        Minimum value =  0
        Maximum value =  4294967294
        """
        self.options['maxconn'] = maxconn

    def get_maxconn(self):
        """
        The maximum number of connections that will be made from the system to the web server(s) attached to it.
        The value entered here is applied globally to all attached servers.

        Default value: 0
        Minimum value =  0
        Maximum value =  4294967294
        """
        return self.options['maxconn']

    def set_maxreq(self, maxreq):
        """
        The maximum number of requests that the system can pass on a particular connection between the system
        and a server attached to it. Setting this value to 0 allows an unlimited number of requests to be
        passed.

        Default value: 0
        Minimum value =  0
        Maximum value =  65535
        """
        self.options['maxreq'] = maxreq

    def get_maxreq(self):
        """
        The maximum number of requests that the system can pass on a particular connection between the system
        and a server attached to it. Setting this value to 0 allows an unlimited number of requests to be
        passed.

        Default value: 0
        Minimum value =  0
        Maximum value =  65535
        """
        return self.options['maxreq']

    def set_cip(self, cip):
        """
        The option to control (enable or disable) the insertion of the actual client IP address into the HTTP
        header request passed from the client to one, some, or all servers attached to the system.

        The passed address can then be accessed through a minor modification to the server.
                If cipHeader is specified, it will be used as the client IP header.

                If it is not specified, then the value that has been set by the set ns config CLI command will
                be used as the client IP header.

        Default value: 0
        """
        self.options['cip'] = cip

    def get_cip(self):
        """
        The option to control (enable or disable) the insertion of the actual client IP address into the HTTP
        header request passed from the client to one, some, or all servers attached to the system.

        The passed address can then be accessed through a minor modification to the server.
                If cipHeader is specified, it will be used as the client IP header.

                If it is not specified, then the value that has been set by the set ns config CLI command will
                be used as the client IP header.

        Default value: 0
        """
        return self.options['cip']

    def set_cipheader(self, cipheader):
        """
        The text that will be used as the client IP header.

        Default value: 0
        Minimum length =  1.
        """
        self.options['cipheader'] = cipheader

    def get_cipheader(self):
        """
        The text that will be used as the client IP header.

        Default value: 0
        Minimum length =  1.
        """
        return self.options['cipheader']

    def set_cookieversion(self, cookieversion):
        """
        The version of the cookie inserted by system.

        Default value: 0
        """
        self.options['cookieversion'] = cookieversion

    def get_cookieversion(self):
        """
        The version of the cookie inserted by system.

        Default value: 0
        """
        return self.options['cookieversion']

    def set_securecookie(self, securecookie):
        """
        enable/disable secure flag for persistence cookie.

        Default value: ENABLED
        """
        self.options['securecookie'] = securecookie

    def get_securecookie(self):
        """
        enable/disable secure flag for persistence cookie.

        Default value: ENABLED
        """
        return self.options['securecookie']

    def set_pmtumin(self, pmtumin):
        """
        The minimum Path MTU.

        Default value: 576
        Minimum value =  168
        Maximum value =  1500
        """
        self.options['pmtumin'] = pmtumin

    def get_pmtumin(self):
        """
        The minimum Path MTU.

        Default value: 576
        Minimum value =  168
        Maximum value =  1500
        """
        return self.options['pmtumin']

    def set_pmtutimeout(self, pmtutimeout):
        """
        The timeout value in minutes.

        Default value: 10
        Minimum value =  1
        Maximum value =  1440
        """
        self.options['pmtutimeout'] = pmtutimeout

    def get_pmtutimeout(self):
        """
        The timeout value in minutes.

        Default value: 10
        Minimum value =  1
        Maximum value =  1440
        """
        return self.options['pmtutimeout']

    def set_ftpportrange(self, ftpportrange):
        """
        Port range configured for FTP services.

        Default value: 0
        Minimum length =  1024.
        Maximum length =  64000.
        """
        self.options['ftpportrange'] = ftpportrange

    def get_ftpportrange(self):
        """
        Port range configured for FTP services.

        Default value: 0
        Minimum length =  1024.
        Maximum length =  64000.
        """
        return self.options['ftpportrange']

    def set_timezone(self, timezone):
        """
        Name of the timezone.

        Default value: 0
        """
        self.options['timezone'] = timezone

    def get_timezone(self):
        """
        Name of the timezone.

        Default value: 0
        """
        return self.options['timezone']

    def set_grantquotamaxclient(self, grantquotamaxclient):
        """
        The percentage of shared quota to be granted at a time for maxClient.

        Default value: 10
        Minimum value =  0
        Maximum value =  100
        """
        self.options['grantquotamaxclient'] = grantquotamaxclient

    def get_grantquotamaxclient(self):
        """
        The percentage of shared quota to be granted at a time for maxClient.

        Default value: 10
        Minimum value =  0
        Maximum value =  100
        """
        return self.options['grantquotamaxclient']

    def set_exclusivequotamaxclient(self, exclusivequotamaxclient):
        """
        The percentage of maxClient to be given to PEs.

        Default value: 80
        Minimum value =  0
        Maximum value =  100
        """
        self.options['exclusivequotamaxclient'] = exclusivequotamaxclient

    def get_exclusivequotamaxclient(self):
        """
        The percentage of maxClient to be given to PEs.

        Default value: 80
        Minimum value =  0
        Maximum value =  100
        """
        return self.options['exclusivequotamaxclient']

    def set_grantquotaspillover(self, grantquotaspillover):
        """
        The percentage of shared quota to be granted at a time for spillover.

        Default value: 10
        Minimum value =  0
        Maximum value =  100
        """
        self.options['grantquotaspillover'] = grantquotaspillover

    def get_grantquotaspillover(self):
        """
        The percentage of shared quota to be granted at a time for spillover.

        Default value: 10
        Minimum value =  0
        Maximum value =  100
        """
        return self.options['grantquotaspillover']

    def set_exclusivequotaspillover(self, exclusivequotaspillover):
        """
        The percentage of max limit to be given to PEs.

        Default value: 80
        Minimum value =  0
        Maximum value =  100
        """
        self.options['exclusivequotaspillover'] = exclusivequotaspillover

    def get_exclusivequotaspillover(self):
        """
        The percentage of max limit to be given to PEs.

        Default value: 80
        Minimum value =  0
        Maximum value =  100
        """
        return self.options['exclusivequotaspillover']

    def set_config1(self, config1):
        """
        Config options.

        Default value: 0
        """
        self.options['config1'] = config1

    def get_config1(self):
        """
        Config options.

        Default value: 0
        """
        return self.options['config1']

    def set_config2(self, config2):
        """
        Config options.

        Default value: 0
        """
        self.options['config2'] = config2

    def get_config2(self):
        """
        Config options.

        Default value: 0
        """
        return self.options['config2']

    def set_outtype(self, outtype):
        """
        The format in which result is desired.

        Default value: 0
        """
        self.options['outtype'] = outtype

    def get_outtype(self):
        """
        The format in which result is desired.

        Default value: 0
        """
        return self.options['outtype']

    def set_template(self, template):
        """
        Enable template diff. This will only compare commands given in template file.

        Default value: 0
        """
        self.options['template'] = template

    def get_template(self):
        """
        Enable template diff. This will only compare commands given in template file.

        Default value: 0
        """
        return self.options['template']

    def get_message(self):
        """
        Default value: 0
        """
        return self.options['message']

    def get_range(self):
        """
        The range of Mapped IP addresses to be configured.

        Default value: 0
        """
        return self.options['range']

    def get_failover(self):
        """
        Standalone node.

        Default value: 0
        """
        return self.options['failover']

    def get_primaryip(self):
        """
        HA Master Node IP address.

        Default value: 0
        """
        return self.options['primaryip']

    def get_flags(self):
        """
        The flags for this entry.

        Default value: 0
        """
        return self.options['flags']

    def get_lastconfigchangedtime(self):
        """
        Time when the configuration was last modified.

        Default value: 0
        """
        return self.options['lastconfigchangedtime']

    def get_systemtime(self):
        """
        Current system time.

        Default value: 0
        """
        return self.options['systemtime']

    @staticmethod
    def save(nitro):
        """
        Use this API to save Netscaler configuration.
        """
        __config = NSConfig()
        return __config.perform_operation(nitro, "save")

    @staticmethod
    def clear(nitro, config):
        __config = NSConfig()
        __config.set_force(config.get_force())
        __config.set_level(config.get_level())
        return __config.perform_operation(nitro, "clear")

    @staticmethod
    def update(nitro, config):
        __config = NSConfig()
        __config.set_ipaddress(config.get_ipaddress())
        __config.set_netmask(config.get_netmask())
        __config.set_nsvlan(config.get_nsvlan())
        __config.set_ifnum(config.get_ifnum())
        __config.set_httpport(config.get_httpport())
        __config.set_maxconn(config.get_maxconn())
        __config.set_maxreq(config.get_maxreq())
        __config.set_cip(config.get_cip())
        __config.set_cipheader(config.get_cipheader())
        __config.set_cookieversion(config.get_cookieversion())
        __config.set_securecookie(config.get_securecookie())
        __config.set_pmtumin(config.get_pmtumin())
        __config.set_pmtutimeout(config.get_pmtutimeout())
        __config.set_ftpportrange(config.get_ftpportrange())
        __config.set_timezone(config.get_timezone())
        __config.set_grantquotamaxclient(config.get_grantquotamaxclient())
        __config.set_exclusivequotamaxclient(config.get_exclusivequotamaxclient())
        __config.set_grantquotaspillover(config.get_grantquotaspillover())
        __config.set_exclusivequotaspillover(config.get_exclusivequotaspillover())
        return __config.update_resource(nitro)

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all nsconfig resources that are configured on netscaler.
        """
        __url = nitro.get_url() + NSConfig.get_resourcetype()
        __json_configs = nitro.get(__url).get_response_field(NSConfig.get_resourcetype())
        return NSConfig(__json_configs)
