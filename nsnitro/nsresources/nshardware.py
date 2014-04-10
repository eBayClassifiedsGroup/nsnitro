from nsbaseresource import NSBaseResource

__author__ = 'Aleksandar Topuzovic'

class NSHardware(NSBaseResource):

        def __init__(self, json_data=None):
                """
                Supplied with json_data the object can be pre-filled
                """

                super(NSHardware, self).__init__()

                self.options = {
                        'hwdescription': '',
                        'sysid': '',
                        'manufactureday': '',
                        'manufacturemonth': '',
                        'manufactureyear': '',
                        'cpufrequncy': '',
                        'hostid': '',
                        'host': '',
                        'serialno': '',
                        'encodedserialno': ''
                }

                if not (json_data is None):
                        for key in json_data.keys():
                                if key in self.options.keys():
                                        self.options[key] = json_data[key]

                self.resourcetype = NSHardware.get_resourcetype()

        def get_hwdescription(self):
            return self.options['hwdescription']

        def get_sysid(self):
            return self.options['sysid']

        def get_manufactureday(self):
            return self.options['manufactureday']

        def get_manufacturemonth(self):
            return self.options['manufacturemonth']

        def get_manufactureyear(self):
            return self.options['manufactureyear']

        def get_cpufrequncy(self):
            return self.options['cpufrequncy']

        def get_hostid(self):
            return self.options['hostid']

        def get_host(self):
            return self.options['host']

        def get_serialno(self):
            return self.options['serialno']

        def get_encodedserialno(self):
            return self.options['encodedserialno']

        @staticmethod
        def get_resourcetype():
                return "nshardware"

        @staticmethod
        def get(nitro):
            __url = nitro.get_url() + NSHardware.get_resourcetype()
            __json_nshardware = nitro.get(__url).get_response_field(NSHardware.get_resourcetype())
            return NSHardware(__json_nshardware)
