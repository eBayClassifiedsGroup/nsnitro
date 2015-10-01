from nsbaseresource import NSBaseResource

__author__ = 'md2k@md2k.net'


class SystemGroup(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(SystemGroup, self).__init__()

        self.options = {'groupname': '',
                        'promptstring': '',
                        'timeout': ''}

        self.resourcetype = SystemGroup.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "systemgroup"

    def set_groupname(self, groupname):
        """Name for the group. Must begin with a letter, number, or the underscore (_) character, and must contain only alphanumeric, hyphen (-), period (.), hash (#), space ( ), at (@), equal (=), colon (:), and underscore characters. Cannot be changed after the group is created.
        CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my group" or 'my group').<br/>Minimum length =  1.
        """
        self.options["groupname"] = groupname

    def get_groupname(self):
        """Name for the group. Must begin with a letter, number, or the underscore (_) character, and must contain only alphanumeric, hyphen (-), period (.), hash (#), space ( ), at (@), equal (=), colon (:), and underscore characters. Cannot be changed after the group is created.
        CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my group" or 'my group').<br/>Minimum length =  1.
        """
        return self.options["groupname"]

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

    def set_timeout(self, timeout):
        """CLI session inactivity timeout, in seconds.If Restrictedtimeout argument of system parameter is enabled, Timeout can have values in the range [300-86400] seconds.
        If Restrictedtimeout argument of system parameter is disabled, Timeout can have values in the range [0, 10-100000000] seconds. Default value is 900 seconds.
        """
        self.options["timeout"] = timeout

    def get_timeout(self):
        """CLI session inactivity timeout, in seconds.If Restrictedtimeout argument of system parameter is enabled, Timeout can have values in the range [300-86400] seconds.
        If Restrictedtimeout argument of system parameter is disabled, Timeout can have values in the range [0, 10-100000000] seconds. Default value is 900 seconds.
        """
        return self.options["timeout"]

    @staticmethod
    def add(nitro, systemgroup):
        """ Use this API to add systemgroup.
        """
        __systemgroup = SystemGroup()
        __systemgroup.set_groupname(systemgroup.get_groupname())
        __systemgroup.set_promptstring(systemgroup.get_promptstring())
        __systemgroup.set_timeout(systemgroup.get_timeout())
        return __systemgroup.add_resource(nitro)

    @staticmethod
    def update(nitro, systemgroup):
        """ Use this API to update systemgroup.
        """
        __systemgroup = SystemGroup()
        __systemgroup.set_groupname(systemgroup.get_groupname())
        __systemgroup.set_promptstring(systemgroup.get_promptstring())
        __systemgroup.set_timeout(systemgroup.get_timeout())
        return __systemgroup.update_resource(nitro)

    @staticmethod
    def delete(nitro, systemgroup):
        """ Use this API to delete systemgroup.
        """
        __systemgroup = SystemGroup()
        __systemgroup.set_groupname(systemgroup.get_groupname())
        return __systemgroup.delete_resource(nitro)

    @staticmethod
    def get(nitro, systemgroup):
        """ Use this API to fetch specific systemgroup resource that are configured on netscaler.
        """
        __systemgroup = SystemGroup()
        __systemgroup.set_groupname(systemgroup.get_groupname())
        return __systemgroup.get_resource(nitro)

    @staticmethod
    def get_all(nitro):
        """ Use this API to fetch all the systemgroup resources that are configured on netscaler.
        """
        __url = nitro.get_url() + SystemGroup.get_resourcetype()
        __json_systemgroup = nitro.get(__url).get_response_field(SystemGroup.get_resourcetype())
        __systemgroup = []
        for json_systemgroup in __json_systemgroup:
            __systemgroup.append(SystemGroup(json_systemgroup))
        return
