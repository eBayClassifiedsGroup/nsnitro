from nsbaseresource import NSBaseResource

__author__ = 'Aleksandar Topuzovic'

class NSHostname(NSBaseResource):

        def __init__(self, json_data=None):
                """
                Supplied with json_data the object can be pre-filled
                """

                super(NSHostname, self).__init__()

                self.options = {
                        'hostname': '',
                }

                if not (json_data is None):
                        for key in json_data.keys():
                                if key in self.options.keys():
                                        self.options[key] = json_data[key]

                self.resourcetype = NSHostname.get_resourcetype()

        def get_hostname(self):
            return self.options['hostname']

        @staticmethod
        def get_resourcetype():
                return "nshostname"

        @staticmethod
        def get(nitro):
            __url = nitro.get_url() + NSHostname.get_resourcetype()
            __json_nshostname = nitro.get(__url).get_response_field(NSHostname.get_resourcetype())
            if isinstance(__json_nshostname, list):
                    return NSHostname(__json_nshostname[0])
            return NSHostname(__json_nshostname)
