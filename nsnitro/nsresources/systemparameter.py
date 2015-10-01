""" Class tested only for update resources """

from nsbaseresource import NSBaseResource

__author__ = 'md2k@md2k.net'


class SystemParameter(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(SystemParameter, self).__init__()

        self.options = {'rbaonresponse': '',
                        'promptstring': '',
                        'natpcbforceflushlimit': '',
                        'natpcbrstontimeout': '',
                        'timeout': '',
                        'localauth': '',
                        'restrictedtimeout': ''}

        self.resourcetype = SystemParameter.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "systemparameter"

    def set_rbaonresponse(self, rbaonresponse):
        """Enable or disable Role-Based Authentication (RBA) on responses.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
        """
        self.options["rbaonresponse"] = rbaonresponse

    def get_rbaonresponse(self):
        """Enable or disable Role-Based Authentication (RBA) on responses.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
        """
        return self.options["rbaonresponse"]

    def set_promptstring(self, promptstring):
        """String to display at the command-line prompt. Can consist of letters, numbers, hyphen (-), period (.), hash (#), space ( ), at (@), equal (=), colon (:), underscore (_), and the following variables:
        * %u - Will be replaced by the user name.
        * %h - Will be replaced by the hostname of the NetScaler appliance.
        * %t - Will be replaced by the current time in 12-hour format.
        * %T - Will be replaced by the current time in 24-hour format.
        * %d - Will be replaced by the current date.
        * %s - Will be replaced by the state of the NetScaler appliance.
        Note: The 63-character limit for the length of the string does not apply to the characters that replace the variables.<br/>Minimum length =  1.
        """
        self.options["promptstring"] = promptstring

    def get_promptstring(self):
        """String to display at the command-line prompt. Can consist of letters, numbers, hyphen (-), period (.), hash (#), space ( ), at (@), equal (=), colon (:), underscore (_), and the following variables:
        * %u - Will be replaced by the user name.
        * %h - Will be replaced by the hostname of the NetScaler appliance.
        * %t - Will be replaced by the current time in 12-hour format.
        * %T - Will be replaced by the current time in 24-hour format.
        * %d - Will be replaced by the current date.
        * %s - Will be replaced by the state of the NetScaler appliance.
        Note: The 63-character limit for the length of the string does not apply to the characters that replace the variables.<br/>Minimum length =  1.
        """
        return self.options["promptstring"]

    def set_natpcbforceflushlimit(self, natpcbforceflushlimit):
        """Flush the system if the number of Network Address Translation Protocol Control Blocks (NATPCBs) exceeds this value.<br/>Default value: 2147483647<br/>Minimum length =  1000.
        """
        self.options["natpcbforceflushlimit"] = natpcbforceflushlimit

    def get_natpcbforceflushlimit(self):
        """Flush the system if the number of Network Address Translation Protocol Control Blocks (NATPCBs) exceeds this value.<br/>Default value: 2147483647<br/>Minimum length =  1000.
        """
        return self.options["natpcbforceflushlimit"]

    def set_natpcbrstontimeout(self, natpcbrstontimeout):
        """Send a reset signal to client and server connections when their NATPCBs time out. Avoids the buildup of idle TCP connections on both the sides.
        <br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
        """
        self.options["natpcbrstontimeout"] = natpcbrstontimeout

    def get_natpcbrstontimeout(self):
        """Send a reset signal to client and server connections when their NATPCBs time out. Avoids the buildup of idle TCP connections on both the sides.
        <br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
        """
        return self.options["natpcbrstontimeout"]

    def set_timeout(self, timeout):
        """CLI session inactivity timeout, in seconds. If Restrictedtimeout argument of system parameter is enabled, Timeout can have values in the range [300-86400] seconds.
        If Restrictedtimeout argument of system parameter is disabled, Timeout can have values in the range [0, 10-100000000] seconds. Default value is 900 seconds.
        """
        self.options["timeout"] = timeout

    def get_timeout(self):
        """CLI session inactivity timeout, in seconds. If Restrictedtimeout argument of system parameter is enabled, Timeout can have values in the range [300-86400] seconds.
        If Restrictedtimeout argument of system parameter is disabled, Timeout can have values in the range [0, 10-100000000] seconds. Default value is 900 seconds.
        """
        return self.options["timeout"]

    def set_localauth(self, localauth):
        """When enabled, local users can access NetScaler even when external authentication is configured. When disabled, local users are not allowed to access the NetScaler,
        Local users can access the NetScaler only when the configured external authentication servers are unavailable.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
        """
        self.options["localauth"] = localauth

    def get_localauth(self):
        """When enabled, local users can access NetScaler even when external authentication is configured. When disabled, local users are not allowed to access the NetScaler,
        Local users can access the NetScaler only when the configured external authentication servers are unavailable.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
        """
        return self.options["localauth"]

    def set_restrictedtimeout(self, restrictedtimeout):
        """Enable/Disable the restricted timeout behaviour. When enabled, timeout cannot be configured beyond admin configured timeout and also it will have\
        the [minimum - maximum] range check. When disabled, timeout will have the old behaviour. By default the value is disabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
        """
        self.options["restrictedtimeout"] = restrictedtimeout

    def get_restrictedtimeout(self):
        """Enable/Disable the restricted timeout behaviour. When enabled, timeout cannot be configured beyond admin configured timeout and also it will have\
        the [minimum - maximum] range check. When disabled, timeout will have the old behaviour. By default the value is disabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
        """
        return self.options["restrictedtimeout"]

    @staticmethod
    def update(nitro, systemparameter):
        __systemparameter = SystemParameter()
        __systemparameter.set_rbaonresponse(systemparameter.get_rbaonresponse())
        __systemparameter.set_promptstring(systemparameter.get_promptstring())
        __systemparameter.set_natpcbforceflushlimit(systemparameter.get_natpcbforceflushlimit())
        __systemparameter.set_natpcbrstontimeout(systemparameter.get_natpcbrstontimeout())
        __systemparameter.set_timeout(systemparameter.get_timeout())
        __systemparameter.set_localauth(systemparameter.get_localauth())
        __systemparameter.set_restrictedtimeout(systemparameter.get_restrictedtimeout())
        return __systemparameter.update_resource(nitro)

    @staticmethod
    def get_all(nitro):
        __url = nitro.get_url() + SystemParameter.get_resourcetype()
        __json_systemparameter = nitro.get(__url).get_response_field(SystemParameter.get_resourcetype())
        __systemparameter = []
        for json_systemparameter in __json_systemparameter:
            __systemparameter.append(SystemParameter(json_systemparameter))
        return __systemparameter
