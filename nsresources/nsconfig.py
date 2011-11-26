from nsbaseresource import NSBaseResource

__author__ = 'vlazarenko'

class NSConfig(NSBaseResource):

        # General Netscaler configuration object

        def __init__(self, json_data = None):
                """
                Supplied with json_data the object can be pre-filled
                """

                super(NSConfig, self).__init__()

                self.options = {
                        'force' : '',
                        'level' : '',
                        'ipaddress' : '',
                        'netmask' : '',
                        'nsvlan' : '',
                        'ifnum' : '',
                        'httpport' : '',
                        'maxconn' : '',
                        'maxreq' : '',
                        'cip' : '',
                        'cipheader' : '',
                        'cookieversion' : '',
                        'securecookie' : '',
                        'pmtumin' : '',
                        'pmtutimeout' : '',
                        'ftpportrange' : '',
                        'timezone' : '',
                        'grantquotamaxclient' : '',
                        'exclusivequotamaxclient' : '',
                        'grantquotaspillover' : '',
                        'exclusivequotaspillover' : '',
                        'config1' : '',
                        'config2' : '',
                        'outtype' : '',
                        'template' : '',
                        'message' : '',
                        'range' : '',
                        'failover' : '',
                        'primaryip' : '',
                        'flags' : '',
                        'lastconfigchangedtime' : '',
                        'systemtime' : '',
                }

                if not (json_data is None):
                        for key in json_data.keys():
                                if self.options.has_key(key):
                                        self.options[key]=json_data[key]

                self.resourcetype = NSConfig.get_resourcetype()

        @staticmethod
        def get_resourcetype():
                return "nsconfig"

        def set_force(self, force):
                self.options['force'] = force

        def get_force(self):
                return self.options['force']

        def set_level(self, level):
                self.options['level'] = level

        def get_level(self):
                return self.options['level']

        def set_ipaddress(self, ipaddress):
                self.options['ipaddress'] = ipaddress

        def get_ipaddress(self):
                return self.options['ipaddress']

        def set_netmask(self, netmask):
                self.options['netmask'] = netmask

        def get_netmask(self):
                return self.options['netmask']

        def set_nsvlan(self, nsvlan):
                self.options['nsvlan'] = nsvlan

        def get_nsvlan(self):
                return self.options['nsvlan']

        def set_ifnum(self, ifnum):
                self.options['ifnum'] = ifnum

        def get_ifnum(self):
                return self.options['ifnum']

        def set_httpport(self, httpport):
                self.options['httpport'] = httpport

        def get_httpport(self):
                return self.options['httpport']

        def set_maxconn(self, maxconn):
                self.options['maxconn'] = maxconn

        def get_maxconn(self):
                return self.options['maxconn']

        def set_maxreq(self, maxreq):
                self.options['maxreq'] = maxreq

        def get_maxreq(self):
                return self.options['maxreq']

        def set_cip(self, cip):
                self.options['cip'] = cip

        def get_cip(self):
                return self.options['cip']

        def set_cipheader(self, cipheader):
                self.options['cipheader'] = cipheader

        def get_cipheader(self):
                return self.options['cipheader']

        def set_cookieversion(self, cookieversion):
                self.options['cookieversion'] = cookieversion

        def get_cookieversion(self):
                return self.options['cookieversion']

        def set_securecookie(self, securecookie):
                self.options['securecookie'] = securecookie

        def get_securecookie(self):
                return self.options['securecookie']

        def set_pmtumin(self, pmtumin):
                self.options['pmtumin'] = pmtumin

        def get_pmtumin(self):
                return self.options['pmtumin']

        def set_pmtutimeout(self, pmtutimeout):
                self.options['pmtutimeout'] = pmtutimeout

        def get_pmtutimeout(self):
                return self.options['pmtutimeout']

        def set_ftpportrange(self, ftpportrange):
                self.options['ftpportrange'] = ftpportrange

        def get_ftpportrange(self):
                return self.options['ftpportrange']

        def set_timezone(self, timezone):
                self.options['timezone'] = timezone

        def get_timezone(self):
                return self.options['timezone']

        def set_grantquotamaxclient(self, grantquotamaxclient):
                self.options['grantquotamaxclient'] = grantquotamaxclient

        def get_grantquotamaxclient(self):
                return self.options['grantquotamaxclient']

        def set_exclusivequotamaxclient(self, exclusivequotamaxclient):
                self.options['exclusivequotamaxclient'] = exclusivequotamaxclient

        def get_exclusivequotamaxclient(self):
                return self.options['exclusivequotamaxclient']

        def set_grantquotaspillover(self, grantquotaspillover):
                self.options['grantquotaspillover'] = grantquotaspillover

        def get_grantquotaspillover(self):
                return self.options['grantquotaspillover']

        def set_exclusivequotaspillover(self, exclusivequotaspillover):
                self.options['exclusivequotaspillover'] = exclusivequotaspillover

        def get_exclusivequotaspillover(self):
                return self.options['exclusivequotaspillover']

        def set_config1(self, config1):
                self.options['config1'] = config1

        def get_config1(self):
                return self.options['config1']

        def set_config2(self, config2):
                self.options['config2'] = config2

        def get_config2(self):
                return self.options['config2']

        def set_outtype(self, outtype):
                self.options['outtype'] = outtype

        def get_outtype(self):
                return self.options['outtype']

        def set_template(self, template):
                self.options['template'] = template

        def get_template(self):
                return self.options['template']

        def get_message(self):
                return self.options['message']

        def get_range(self):
                return self.options['range']

        def get_failover(self):
                return self.options['failover']

        def get_primaryip(self):
                return self.options['primaryip']

        def get_flags(self):
                return self.options['flags']

        def get_lastconfigchangedtime(self):
                return self.options['lastconfigchangedtime']

        def get_systemtime(self):
                return self.options['systemtime']

        @staticmethod
        def save(nitro):
                """
                Use this API to save Netscaler configuration.
                """
                __config = NSConfig()
                return __config.perform_operation(nitro, "save")