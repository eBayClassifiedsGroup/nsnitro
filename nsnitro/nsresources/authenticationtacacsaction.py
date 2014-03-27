from nsbaseresource import NSBaseResource

__author__ = 'ndenev@gmail.com'


class AuthTacacsAction(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(AuthTacacsAction, self).__init__()

        self.options = {'name': '',
                        'serverip': '',
                        'serverport': '',
                        'authtimeout': '',
                        'tacacssecret': '',
                        'authorization': '',
                        'accounting': '',
                        'auditfailedcmds': '',
                        'defaultauthenticationgroup': '',
                        # ReadOnly
                        'success': '',
                        'failure': ''}

        self.resourcetype = AuthTacacsAction.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "authenticationtacacsaction"

    def set_name(self, name):
        """
        Name for the TACACS+ profile (action). Must begin with a letter, number, or the underscore character (_), and must contain only letters,
        numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
        Cannot be changed after TACACS profile is created.
        Minimum length = 1
        """
        self.options['name'] = name

    def get_name(self):
        return self.options['name']

    def set_serverip(self, serverip):
        """
        IP address assigned to the TACACS+ server.
        """
        self.options['serverip'] = serverip

    def get_serverip(self):
        return self.options['serverip']

    def set_serverport(self, serverport):
        """
        Port number on which the TACACS+ server listens for connections.
        Default value: 49
        """
        self.options['serverport'] = serverport

    def get_serverport(self):
        return self.options['serverport']

    def set_authtimeout(self, authtimeout):
        """
        Number of seconds the NetScaler appliance waits for a response from the TACACS+ server.
        Default value: 3
        """
        self.options['authtimeout'] = authtimeout

    def get_authtimeout(self):
        return self.options['authtimeout']

    def set_tacacssecret(self, tacacssecret):
        """
        Key shared between the TACACS+ server and the NetScaler appliance. Required for allowing the NetScaler appliance to communicate with the TACACS+ server.
        Minimum length = 1
        """
        self.options['tacacssecret'] = tacacssecret

    def get_tacacssecret(self):
        return self.options['tacacssecret']

    def set_authorization(self, authorization):
        """
        Use streaming authorization on the TACACS+ server.
        """
        self.options['authorization'] = authorization

    def get_authorization(self):
        return self.options['authorization']

    def set_accounting(self, accounting):
        """
        Whether the TACACS+ server is currently accepting accounting messages.
        """
        self.options['accounting'] = accounting

    def get_accounting(self):
        return self.options['accounting']

    def set_auditfailedcmds(self, auditfailedcmds):
        """
        The state of the TACACS+ server that will receive accounting messages.
        """
        self.options['auditfailedcmds'] = auditfailedcmds

    def get_auditfailedcmds(self):
        return self.options['auditfailedcmds']

    def set_defaultauthenticationgroup(self, defaultauthenticationgroup):
        """
        This is the default group that is chosen when the authentication succeeds in addition to extracted groups.
        """
        self.options['defaultauthenticationgroup'] = defaultauthenticationgroup

    def get_defaultauthenticationgroup(self):
        return self.options['defaultauthenticationgroup']

    def get_success(self):
        return self.options['success']

    def get_failure(self):
        return self.options['failure']

    # Operations methods
    @staticmethod
    def get(nitro, tacacsaction):
        """
        Use this API to fetch a configured authenticationtacacsaction resource by name.
        """
        __tacacsaction = AuthTacacsAction()
        __tacacsaction.set_name(tacacsaction.get_name())
        __tacacsaction.get_resource(nitro)
        return __tacacsaction

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured authenticationtacacsaction resources.
        """
        __url = nitro.get_url() + AuthTacacsAction.get_resourcetype()
        __json_tacacsactions = nitro.get(__url).get_response_field(AuthTacacsAction.get_resourcetype())
        __tacacsactions = []
        for json_tacacsaction in __json_tacacsactions:
            __tacacsactions.append(AuthTacacsAction(json_tacacsaction))
        return __tacacsactions

    @staticmethod
    def add(nitro, tacacsaction):
        """
        Use this API to add authenticationtacacsaction.
        """
        __tacacsaction = AuthTacacsAction()
        __tacacsaction.set_name(tacacsaction.get_name())
        __tacacsaction.set_serverip(tacacsaction.get_serverip())
        __tacacsaction.set_serverport(tacacsaction.get_serverport())
        __tacacsaction.set_authtimeout(tacacsaction.get_authtimeout())
        __tacacsaction.set_tacacssecret(tacacsaction.get_tacacssecret())
        __tacacsaction.set_authorization(tacacsaction.get_authorization())
        __tacacsaction.set_accounting(tacacsaction.get_accounting())
        __tacacsaction.set_auditfailedcmds(tacacsaction.get_auditfailedcmds())
        __tacacsaction.set_defaultauthenticationgroup(tacacsaction.get_defaultauthenticationgroup())
        return __tacacsaction.add_resource(nitro)

    @staticmethod
    def delete(nitro, tacacsaction):
        """
        Use this API to delete authenticationtacacsaction of a given name.
        """
        __tacacsaction = AuthTacacsAction()
        __tacacsaction.set_name(tacacsaction.get_name())
        nsresponse = __tacacsaction.delete_resource(nitro)
        return nsresponse

    @staticmethod
    def update(nitro, tacacsaction):
        """
        Use this API to update a rewriteaction of a given name.
        """
        __tacacsaction = AuthTacacsAction()
        __tacacsaction.set_name(tacacsaction.get_name())
        __tacacsaction.set_serverip(tacacsaction.get_serverip())
        __tacacsaction.set_serverport(tacacsaction.get_serverport())
        __tacacsaction.set_authtimeout(tacacsaction.get_authtimeout())
        __tacacsaction.set_tacacssecret(tacacsaction.get_tacacssecret())
        __tacacsaction.set_authorization(tacacsaction.get_authorization())
        __tacacsaction.set_accounting(tacacsaction.get_accounting())
        __tacacsaction.set_auditfailedcmds(tacacsaction.get_auditfailedcmds())
        __tacacsaction.set_defaultauthenticationgroup(tacacsaction.get_defaultauthenticationgroup())
        return __tacacsaction.update_resource(nitro)

    # No unset functionality for now.
