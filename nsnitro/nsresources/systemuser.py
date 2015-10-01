from nsbaseresource import NSBaseResource

__author__ = 'ivanxx@gmail.com'


class SystemUser(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(SystemUser, self).__init__()

        self.options = {'username': '',
                        'password': '',
                        'priority': '',
                        'externalauth': '',
                        'promptstring': '',
                        'timeout': '',
                        'logging': ''}

        self.resourcetype = SystemUser.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "systemuser"

    def set_username(self, username):
        self.options['username'] = username

    def get_username(self):
        return self.options['username']

    def set_password(self, password):
        self.options['password'] = password

    def get_password(self):
        return self.options['password']

    def set_priority(self, password):
        # The priority, when submitted to the Nitro API, is ignored by the Nitro API
        # and it is always zero
        self.options['priority'] = password

    def get_priority(self):
        # The priority, when retrieve from the Nitro API, is always zero
        return self.options['priority']

    def set_externalauth(self, externalauth):
        self.options['externalauth'] = externalauth

    def get_externalauth(self):
        return self.options['externalauth']

    def set_promptstring(self, promptstring):
        self.options['promptstring'] = promptstring

    def get_promptstring(self):
        return self.options['promptstring']

    def set_timeout(self, timeout):
        self.options['timeout'] = timeout

    def get_timeout(self):
        return self.options['timeout']

    def set_logging(self, logging):
        self.options['logging'] = logging

    def get_logging(self):
        return self.options['logging']

    @staticmethod
    def add(nitro, systemuser):
        __systemuser = SystemUser()
        __systemuser.set_username(systemuser.get_username())
        __systemuser.set_password(systemuser.get_password())
        __systemuser.set_externalauth(systemuser.get_externalauth())
        __systemuser.set_promptstring(systemuser.get_promptstring())
        __systemuser.set_timeout(systemuser.get_timeout())
        __systemuser.set_logging(systemuser.get_logging())
        return __systemuser.add_resource(nitro)

    @staticmethod
    def get(nitro, systemuser):
        __systemuser = SystemUser()
        __systemuser.set_username(systemuser.get_username())
        __systemuser.get_resource(nitro, object_name=__systemuser.get_username())
        return __systemuser

    @staticmethod
    def update(nitro, systemuser):
        __systemuser = SystemUser()
        __systemuser.set_username(systemuser.get_username())
        __systemuser.set_password(systemuser.get_password())
        __systemuser.set_externalauth(systemuser.get_externalauth())
        __systemuser.set_promptstring(systemuser.get_promptstring())
        __systemuser.set_timeout(systemuser.get_timeout())
        __systemuser.set_logging(systemuser.get_logging())
        return __systemuser.update_resource(nitro)

    @staticmethod
    def delete(nitro, systemuser):
        __systemuser = SystemUser()
        __systemuser.set_username(systemuser.get_username())
        return __systemuser.delete_resource(nitro)

    @staticmethod
    def get_all(nitro):
        __url = nitro.get_url() + SystemUser.get_resourcetype()
        __json_systemusers = nitro.get(__url).get_response_field(SystemUser.get_resourcetype())

        return [SystemUser(u) for u in __json_systemusers]
