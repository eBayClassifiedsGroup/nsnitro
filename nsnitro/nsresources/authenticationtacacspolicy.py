from nsbaseresource import NSBaseResource

__author__ = 'ndenev@gmail.com'


class AuthTacacsPolicy(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(AuthTacacsPolicy, self).__init__()

        self.options = {'name': '',
                        'rule': '',
                        'reqaction': ''}

        self.resourcetype = AuthTacacsPolicy.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "authenticationtacacspolicy"

    def set_name(self, name):
        """
        Name for the TACACS+ policy. Must begin with a letter, number, or the underscore character (_), and must contain only letters,
        numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
        Cannot be changed after TACACS+ policy is created.
        Minimum length = 1
        """
        self.options['name'] = name

    def get_name(self):
        return self.options['name']

    def set_rule(self, rule):
        """
        Name of the NetScaler named rule, or a default syntax expression, that the policy uses to determine whether to attempt to authenticate the user with the TACACS+ server.
        Minimum length = 1
        """
        self.options['rule'] = rule

    def get_rule(self):
        return self.options['rule']

    def set_reqaction(self, reqaction):
        """
        Name of the TACACS+ action to perform if the policy matches.
        Minimum length = 1
        """
        self.options['reqaction'] = reqaction

    def get_reqaction(self):
        return self.options['reqaction']

    # Operations methods
    @staticmethod
    def get(nitro, tacacspolicy):
        """
        Use this API to fetch a configured authenticationtacacspolicy resource by name.
        """
        __tacacspolicy = AuthTacacsPolicy()
        __tacacspolicy.set_name(tacacspolicy.get_name())
        __tacacspolicy.get_resource(nitro)
        return __tacacspolicy

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured authenticationtacacspolicy resources.
        """
        __url = nitro.get_url() + AuthTacacsPolicy.get_resourcetype()
        __json_tacacspolicies = nitro.get(__url).get_response_field(AuthTacacsPolicy.get_resourcetype())
        __tacacspolicies = []
        for json_tacacspolicy in __json_tacacspolicies:
            __tacacspolicies.append(AuthTacacsPolicy(json_tacacspolicy))
        return __tacacspolicies

    @staticmethod
    def add(nitro, tacacspolicy):
        """
        Use this API to add authenticationtacacspolicy.
        """
        __tacacspolicy = AuthTacacsPolicy()
        __tacacspolicy.set_name(tacacspolicy.get_name())
        __tacacspolicy.set_rule(tacacspolicy.get_rule())
        __tacacspolicy.set_reqaction(tacacspolicy.get_reqaction())
        return __tacacspolicy.add_resource(nitro)

    @staticmethod
    def delete(nitro, tacacspolicy):
        """
        Use this API to delete authenticationtacacspolicy of a given name.
        """
        __tacacspolicy = AuthTacacsPolicy()
        __tacacspolicy.set_name(tacacspolicy.get_name())
        nsresponse = __tacacspolicy.delete_resource(nitro)
        return nsresponse

    @staticmethod
    def update(nitro, tacacspolicy):
        """
        Use this API to update a rewritepolicy of a given name.
        """
        __tacacspolicy = AuthTacacsPolicy()
        __tacacspolicy.set_name(tacacspolicy.get_name())
        __tacacspolicy.set_rule(tacacspolicy.get_rule())
        __tacacspolicy.set_reqaction(tacacspolicy.get_reqaction())
        return __tacacspolicy.update_resource(nitro)

    # No unset functionality for now.
