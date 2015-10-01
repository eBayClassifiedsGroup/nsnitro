from nsbaseresource import NSBaseResource

__author__ = 'md2k@md2k.net'


class AuthLdapPolicy(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(AuthLdapPolicy, self).__init__()

        self.options = {'name': '',
                        'rule': '',
                        'reqaction': ''}

        self.resourcetype = AuthLdapPolicy.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "authenticationldappolicy"

    def set_name(self, name):
        """Name for the LDAP policy.
        Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after LDAP policy is created.
        The following requirement applies only to the NetScaler CLI:
        If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication policy" or 'my authentication policy').<br/>Minimum length =  1.
        """
        self.options["name"] = name

    def get_name(self):
        """Name for the LDAP policy.
        Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after LDAP policy is created.
        The following requirement applies only to the NetScaler CLI:
        If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication policy" or 'my authentication policy').<br/>Minimum length =  1.
        """
        return self.options["name"]

    def set_rule(self, rule):
        """Name of the NetScaler named rule, or a default syntax expression, that the policy uses to determine whether to attempt to authenticate the user with the LDAP server.<br/>Minimum length =  1.
        """
        self.options["rule"] = rule

    def get_rule(self):
        """Name of the NetScaler named rule, or a default syntax expression, that the policy uses to determine whether to attempt to authenticate the user with the LDAP server.<br/>Minimum length =  1.
        """
        return self.options["rule"]

    def set_reqaction(self, reqaction):
        """Name of the LDAP action to perform if the policy matches.<br/>Minimum length =  1.
        """
        self.options["reqaction"] = reqaction

    def get_reqaction(self):
        """Name of the LDAP action to perform if the policy matches.<br/>Minimum length =  1.
        """
        return self.options["reqaction"]

    @staticmethod
    def add(nitro, ldappolicy):
        __ldappolicy = AuthLdapPolicy()
        __ldappolicy.set_name(ldappolicy.get_name())
        __ldappolicy.set_rule(ldappolicy.get_rule())
        __ldappolicy.set_reqaction(ldappolicy.get_reqaction())
        return __ldappolicy.add_resource(nitro)

    @staticmethod
    def update(nitro, ldappolicy):
        __ldappolicy = AuthLdapPolicy()
        __ldappolicy.set_name(ldappolicy.get_name())
        __ldappolicy.set_rule(ldappolicy.get_rule())
        __ldappolicy.set_reqaction(ldappolicy.get_reqaction())
        return __ldappolicy.update_resource(nitro)

    @staticmethod
    def delete(nitro, ldappolicy):
        __ldappolicy = AuthLdapPolicy()
        __ldappolicy.set_name(ldappolicy.get_name())
        return __ldappolicy.delete_resource(nitro)

    @staticmethod
    def get(nitro, ldappolicy):
        __ldappolicy = AuthLdapPolicy()
        __ldappolicy.set_name(ldappolicy.get_name())
        return __ldappolicy.get_resource(nitro)

    @staticmethod
    def get_all(nitro):
        __url = nitro.get_url() + AuthLdapPolicy.get_resourcetype()
        __json_ldappolicy = nitro.get(__url).get_response_field(AuthLdapPolicy.get_resourcetype())
        __ldappolicy = []
        for json_ldappolicy in __json_ldappolicy:
            __ldappolicy.append(AuthLdapPolicy(json_ldappolicy))
        return __ldappolicy
