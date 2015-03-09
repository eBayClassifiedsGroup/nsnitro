from nsbaseresource import NSBaseResource

__author__ = 'Aleksandar Topuzovic'


class NSSavedConfig(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """

        super(NSSavedConfig, self).__init__()

        self.options = {'textblob': ''}

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

        self.resourcetype = NSSavedConfig.get_resourcetype()

    def get_textblob(self):
        return self.options['textblob']

    @staticmethod
    def get_resourcetype():
        return "nssavedconfig"

    @staticmethod
    def get(nitro):
        __url = nitro.get_url() + NSSavedConfig.get_resourcetype()
        __json_nsversion = nitro.get(__url).get_response_field(NSSavedConfig.get_resourcetype())
        return NSSavedConfig(__json_nsversion)
