from nsbaseresource import NSBaseResource

__author__ = 'zojoncj'


class NSSystemCMDPolicy(NSBaseResource):

    # General Netscaler configuration object

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """

        super(NSSystemCMDPolicy, self).__init__()

        self.options = {
            'policyname': '',
            'action': '',
            'cmdspec': '',
        }

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options:
                    self.options[key] = json_data[key]

        self.resourcetype = NSSystemCMDPolicy.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        return "systemcmdpolicy"

    def set_policyname(self, policyname):
        self.options['policyname'] = policyname

    def get_policyname(self):
        return self.options['policyname']

    def set_action(self, action):
        self.options['action'] = action

    def get_action(self):
        return self.options['action']

    def set_cmdspec(self, cmdspec):
        self.options['cmdspec'] = cmdspec

    def get_cmdspec(self):
        return self.options['cmdspec']

    @staticmethod
    def add(nitro, systemcmdpolicy):
        __systemcmdpolicy = NSSystemCMDPolicy()
        __systemcmdpolicy.set_policyname(systemcmdpolicy.get_policyname())
        __systemcmdpolicy.set_action(systemcmdpolicy.get_action())
        __systemcmdpolicy.set_cmdspec(systemcmdpolicy.get_cmdspec())
        return __systemcmdpolicy.add_resource(nitro)

    @staticmethod
    def update(nitro, systemcmdpolicy):
        __systemcmdpolicy = NSSystemCMDPolicy()
        __systemcmdpolicy.set_policyname(systemcmdpolicy.get_policyname())
        __systemcmdpolicy.set_action(systemcmdpolicy.get_action())
        __systemcmdpolicy.set_cmdspec(systemcmdpolicy.get_cmdspec())
        return __systemcmdpolicy.update_resource(nitro)

    @staticmethod
    def delete(nitro, systemcmdpolicy):
        __systemcmdpolicy = NSSystemCMDPolicy()
        __systemcmdpolicy.set_policyname(systemcmdpolicy.get_policyname())
        nsresponse = __systemcmdpolicy.delete_resource(nitro, object_name=__systemcmdpolicy.get_policyname())
        return nsresponse

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all cmdpolicy resources that are configured on netscaler.
        """
        __url = nitro.get_url() + NSSystemCMDPolicy.get_resourcetype()
        __json_systemcmdpolicies = nitro.get(__url).get_response_field(NSSystemCMDPolicy.get_resourcetype())
        __systemcmdpolicies = []
        for json_systemcmdpolicy in __json_systemcmdpolicies:
            __systemcmdpolicies.append(NSSystemCMDPolicy(json_systemcmdpolicy))
        return __systemcmdpolicies
