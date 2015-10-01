from nsbaseresource import NSBaseResource

__author__ = 'md2k@md2k.net'


class SystemGlobalAuthLdapPolicyBinding(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(SystemGlobalAuthLdapPolicyBinding, self).__init__()

        self.options = {'policyname': '',
                        'builtin': '',
                        'priority': ''}

        self.resourcetype = SystemGlobalAuthLdapPolicyBinding.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "systemglobal_authenticationldappolicy_binding"

    def set_builtin(self, builtin):
        """
        Indicates that a variable is a built-in (SYSTEM INTERNAL) type.
        Possible values = MODIFIABLE, DELETABLE, IMMUTABLE
        """
        self.options['builtin'] = builtin

    def get_builtin(self):
        return self.options['builtin']

    def set_policyname(self, policyname):
        """The name of the  command policy.
        """
        self.options["policyname"] = policyname

    def get_policyname(self):
        """The name of the  command policy.
        """
        return self.options["policyname"]

    def set_priority(self, priority):
        """The priority of the command policy.
        """
        self.options["priority"] = priority

    def get_priority(self):
        """The priority of the command policy.
        """
        return self.options["priority"]

    @staticmethod
    def add(nitro, policybinding):
        __policybinding = SystemGlobalAuthLdapPolicyBinding()
        __policybinding.set_policyname(policybinding.get_policyname())
        __policybinding.set_priority(policybinding.get_priority())
        __policybinding.set_builtin(policybinding.get_builtin())
        return __policybinding.add_resource(nitro)

    @staticmethod
    def delete(nitro, policybinding):
        __policybinding = SystemGlobalAuthLdapPolicyBinding()
        __policybinding.set_policyname(policybinding.get_policyname())
        return __policybinding.delete_resource(nitro)

    @staticmethod
    def get(nitro, policybinding):
        __policybinding = SystemGlobalAuthLdapPolicyBinding()
        __policybinding.set_policyname(policybinding.get_policyname())
        return __policybinding.get_resource(nitro)

    @staticmethod
    def get_all(nitro):
        __url = nitro.get_url() + SystemGlobalAuthLdapPolicyBinding.get_resourcetype()
        __json_policybinding = nitro.get(__url).get_response_field(SystemGlobalAuthLdapPolicyBinding.get_resourcetype())
        __policybinding = []
        for json_policybinding in __json_policybinding:
            __policybinding.append(SystemGlobalAuthLdapPolicyBinding(json_policybinding))
        return __policybinding
