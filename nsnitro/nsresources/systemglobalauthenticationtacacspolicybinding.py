from nsbaseresource import NSBaseResource

__author__ = 'ndenev@gmail.com'


class SystemGlobalAuthTacacsPolicyBinding(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(SystemGlobalAuthTacacsPolicyBinding, self).__init__()

        self.options = {'priority': '',
                        'builtin': '',
                        'policyname': ''}

        self.resourcetype = SystemGlobalAuthTacacsPolicyBinding.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "systemglobal_authenticationtacacspolicy_binding"

    def set_priority(self, priority):
        """
        The priority of the command policy.
        """
        self.options['priority'] = priority

    def get_priority(self):
        return self.options['priority']

    def set_builtin(self, builtin):
        """
        Indicates that a variable is a built-in (SYSTEM INTERNAL) type.
        Possible values = MODIFIABLE, DELETABLE, IMMUTABLE
        """
        self.options['builtin'] = builtin

    def get_builtin(self):
        return self.options['builtin']

    def set_policyname(self, policyname):
        """
        The name of the command policy.
        """
        self.options['policyname'] = policyname

    def get_policyname(self):
        return self.options['policyname']

    # Operations methods
    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch the configured systemglobal_authenticationtacacspolicy_binding resources.
        """
        __url = nitro.get_url() + SystemGlobalAuthTacacsPolicyBinding.get_resourcetype()
        __json_policybindings = nitro.get(__url).get_response_field(SystemGlobalAuthTacacsPolicyBinding.get_resourcetype())
        __policybindings = []
        for json_policybinding in __json_policybindings:
            __policybindings.append(SystemGlobalAuthTacacsPolicyBinding(json_policybinding))
        return __policybindings

    @staticmethod
    def add(nitro, policybinding):
        """
        Use this API to add systemglobal_authenticationtacacspolicy_binding.
        """
        __policybinding = SystemGlobalAuthTacacsPolicyBinding()
        __policybinding.set_policyname(policybinding.get_policyname())
        __policybinding.set_priority(policybinding.get_priority())
        __policybinding.set_builtin(policybinding.get_builtin())
        return __policybinding.add_resource(nitro)

    @staticmethod
    def delete(nitro, policybinding):
        """
        Use this API to delete systemglobal_authenticationtacacspolicy_binding of a given name.
        """
        __policybinding = SystemGlobalAuthTacacsPolicyBinding()
        __policybinding.set_policyname(policybinding.get_policyname())
        nsresponse = __policybinding.delete_resource(nitro)
        return nsresponse
