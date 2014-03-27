from nsbaseresource import NSBaseResource

__author__ = 'timl'


class NSResponderPolicyLabel(NSBaseResource):

    # Configuration for responder policy labels

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSResponderPolicyLabel, self).__init__()
        self.options = {
            'labelname': '',
            'policylabeltype': '',
            'numpol': '',
            'hits': '',
            'priority': '',
        }

        self.resourcetype = NSResponderPolicyLabel.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "responderpolicylabel"

    def set_labelname(self, labelname):
        """
        Name of the responder policy label.

        Default value: 0
        """
        self.options['labelname'] = labelname

    def get_labelname(self):
        """
        Name of the responder policy label.

        Default value: 0
        """
        return self.options['labelname']

    def set_policylabeltype(self, policylabeltype):
        """
        Policy label type  = "HTTP | OTHERTCP"

        Default value: 0
        """
        valid_types = ('HTTP', 'OTHERTCP')
        if policylabeltype and policylabeltype not in valid_types:
            raise ValueError("policylabeltype must be one of %s" %
                             ",".join(valid_types))
        self.options['policylabeltype'] = policylabeltype

    def get_policylabeltype(self):
        """
        Get the policylabeltype

        Default value: HTTP
        """
        return self.options['policylabeltype']

    def get_numpol(self):
        """
        Number of bound policies

        Default value: 0
        """
        return self.options['numpol']

    def get_hits(self):
        """
        Number of hits.

        Default value: 0
        """
        return self.options['hits']

    def set_priority(self, priority):
        """
        Set the priority for the responder policy label.

        Default value: 0
        """
        self.options['priority'] = priority

    def get_priority(self):
        """
        Priority of the responder policy label.

        Default value: 0
        """
        return self.options['priority']

    # Operations methods
    @staticmethod
    def get(nitro, responderpolicylabel):
        """
        Use this API to fetch responderpolicylabel resource of given name.
        """
        __responderpolicylabel = NSResponderPolicyLabel()
        __responderpolicylabel.set_labelname(responderpolicylabel.get_labelname())
        __responderpolicylabel.get_resource(nitro)
        return __responderpolicylabel

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured responderpolicylabel resources.
        """
        __url = nitro.get_url() + NSResponderPolicyLabel.get_resourcetype()
        __json_cspolicies = nitro.get(__url).get_response_field(NSResponderPolicyLabel.get_resourcetype())
        __responderpolicies = []
        for json_responderpolicylabel in __json_cspolicies:
            __responderpolicies.append(NSResponderPolicyLabel(json_responderpolicylabel))
        return __responderpolicies

    @staticmethod
    def add(nitro, responderpolicylabel):
        """
        Use this API to add responderpolicylabel.
        """
        __responderpolicylabel = NSResponderPolicyLabel()
        __responderpolicylabel.set_labelname(responderpolicylabel.get_labelname())
        __responderpolicylabel.set_policylabeltype(responderpolicylabel.get_policylabeltype())
        __responderpolicylabel.set_priority(responderpolicylabel.get_priority())
        return __responderpolicylabel.add_resource(nitro)

    @staticmethod
    def delete(nitro, responderpolicylabel):
        """
        Use this API to delete responderpolicylabel of a given name.
        """
        __responderpolicylabel = NSResponderPolicyLabel()
        __name = responderpolicylabel.get_labelname()
        __responderpolicylabel.set_labelname(__name)
        nsresponse = __responderpolicylabel.delete_resource(nitro, __name)
        return nsresponse

    @staticmethod
    def update(nitro, responderpolicylabel):
        """
        Use this API to update a responderpolicylabel of a given name.
        """
        __responderpolicylabel = NSResponderPolicyLabel()
        __responderpolicylabel.set_labelname(responderpolicylabel.get_labelname())
        __responderpolicylabel.set_policylabeltype(responderpolicylabel.get_policylabeltype())
        __responderpolicylabel.set_priority(responderpolicylabel.get_priority())
        return __responderpolicylabel.update_resource(nitro)


    # No unset functionality for now.

    # No rename functionality for now.
