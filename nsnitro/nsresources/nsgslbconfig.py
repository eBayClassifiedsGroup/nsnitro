# encoding: utf-8
from nsbaseresource import NSBaseResource


class NSGSLBConfig(NSBaseResource):

    # Configuration for GSLB ,Sync configuration to other devices.

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSGSLBConfig, self).__init__()
        self.options = {
            'preview': '',
            'debug': '',
            'forcesync': '',
            'nowarn': '',
            'saveconfig': '',
            'command': '',
        }

        self.resourcetype = NSGSLBConfig.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "gslbconfig"

    @staticmethod
    def sync(nitro):
        """
        Use this API to sync all gslb config.
        """
        pay_load = {'nowarn': True, 'saveconfig': True}
        __gslbconfi = NSGSLBConfig(pay_load)
        __gslbconfi.set_action('sync')
        response = __gslbconfi.add_resource(nitro)
        return response
