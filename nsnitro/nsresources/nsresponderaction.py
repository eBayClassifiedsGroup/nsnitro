from nsbaseresource import NSBaseResource

__author__ = 'timl'


class NSResponderAction(NSBaseResource):

    # Configuration for responder actions.

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSResponderAction, self).__init__()
        self.options = {
            'name': '',
            'newname': '',
            'type': '',
            'target': '',
            'bypasssafetycheck': '',
            'hits': '',
            'referencecount': '',
            'undefhits': '',
        }

        self.resourcetype = NSResponderAction.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "responderaction"

    def set_name(self, name):
        """
        Name of the responder action.

        Default value: 0
        """
        self.options['name'] = name

    def get_name(self):
        """
        Name of the responder action.

        Default value: 0
        """
        return self.options['name']

    def set_type(self, action_type):
        """
        Type (respondwith, redirect) of responder action.

        Default value: 0
        """
        self.options['type'] = action_type

    def get_type(self):
        """
        Type (respondwith, redirect) of responder action.

        Default value: 0
        """
        return self.options['type']

    def set_target(self, target):
        """
        Target of responder action.

        Default value: 0
        """
        self.options['target'] = target

    def get_target(self):
        """
        Target of responder action.

        Default value: 0
        """
        return self.options['target']

    def set_newname(self, newname):
        """
        The new name of the responder action.

        Default value: 0
        Minimum length =  1.
        """
        self.options['newname'] = newname

    def get_newname(self):
        """
        The new name of the responder action.

        Default value: 0
        Minimum length =  1.
        """
        return self.options['newname']

    def get_hits(self):
        """
        Number of hits.

        Default value: 0
        """
        return self.options['hits']

    def get_undefhits(self):
        """
        Number of undef hits.

        Default value: 0
        """
        return self.options['undefhits']

    def get_referencecount(self):
        """
        Number of references to this action.

        Default value: 0
        """
        return self.options['referencecount']

    def set_bypasssafetycheck(self, bypasssafetycheck):
        """
        Bypass the safety check

        Default value: NO
        """
        valid = ('YES', 'NO')
        if bypasssafetycheck and bypasssafetycheck not in valid:
            raise ValueError("bypasssafetycheck must be one of %s" %
                             ",".join(valid))
        self.options['bypasssafetycheck'] = bypasssafetycheck

    def get_bypasssafetycheck(self):
        """
        Bypass the safety check

        Default value: NO
        """
        return self.options['bypasssafetycheck']

    # Operations methods
    @staticmethod
    def get(nitro, responderaction):
        """
        Use this API to fetch responderaction resource of given name.
        """
        __responderaction = NSResponderAction()
        __responderaction.set_name(responderaction.get_name())
        __responderaction.get_resource(nitro)
        return __responderaction

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured responderaction resources.
        """
        __url = nitro.get_url() + NSResponderAction.get_resourcetype()
        __json_cspolicies = nitro.get(__url).get_response_field(NSResponderAction.get_resourcetype())
        __responderpolicies = []
        for json_responderaction in __json_cspolicies:
            __responderpolicies.append(NSResponderAction(json_responderaction))
        return __responderpolicies

    @staticmethod
    def add(nitro, responderaction):
        """
        Use this API to add responderaction.
        """
        __responderaction = NSResponderAction()
        __responderaction.set_name(responderaction.get_name())
        __responderaction.set_type(responderaction.get_type())
        __responderaction.set_target(responderaction.get_target())
        __responderaction.set_bypasssafetycheck(responderaction.get_bypasssafetycheck())
        return __responderaction.add_resource(nitro)

    @staticmethod
    def delete(nitro, responderaction):
        """
        Use this API to delete responderaction of a given name.
        """
        __responderaction = NSResponderAction()
        __responderaction.set_name(responderaction.get_name())
        nsresponse = __responderaction.delete_resource(nitro)
        return nsresponse

    @staticmethod
    def update(nitro, responderaction):
        """
        Use this API to update a responderaction of a given name.
        """
        __responderaction = NSResponderAction()
        __responderaction.set_name(responderaction.get_name())
        __responderaction.set_target(responderaction.get_target())
        __responderaction.set_bypasssafetycheck(responderaction.get_bypasssafetycheck())
        return __responderaction.update_resource(nitro)

    # No unset functionality for now.
    @staticmethod
    def rename(nitro, responderaction):
        """
        Use this API to rename responderaction.
        """
        __responderaction = NSResponderAction()
        __responderaction.set_name(responderaction.get_name())
        __responderaction.set_newname(responderaction.get_newname())
        return __responderaction.perform_operation(nitro, "rename")
