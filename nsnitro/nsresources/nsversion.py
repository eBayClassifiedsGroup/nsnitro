from nsbaseresource import NSBaseResource

__author__ = 'ivanxx@gmail.com'


class NSVersion(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """

        super(NSVersion, self).__init__()

        self.options = {'version': '',
                        'mode': ''}

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

        self.resourcetype = NSVersion.get_resourcetype()

    def get_version(self):
        return self.options['version']

    def get_mode(self):
        return self.options['mode']

    @staticmethod
    def get_resourcetype():
        return "nsversion"

    @staticmethod
    def get(nitro):
        __url = nitro.get_url() + NSVersion.get_resourcetype()
        __json_nsversion = nitro.get(__url).get_response_field(NSVersion.get_resourcetype())
        return NSVersion(__json_nsversion)
