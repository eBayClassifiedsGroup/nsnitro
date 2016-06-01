from nsbaseresource import NSBaseResource


class NSGSLBSite(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSGSLBSite, self).__init__()

        self.options = {
            # Read-write values
            'sitename': '',
            'sitetype': '',
            'siteipaddress': '',
            'publicip': '',
            'metricexchange': '',
            'nwmetricexchange': '',
            'sessionexchange': '',
            'triggermonitor': '',
            'parentsite': '',
            'clip': '',
            'publicclip': '',

            # Readonly values
            'status': '',
            'persistencemepstatus': '',
            'version': '',
        }

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options:
                    self.options[key] = json_data[key]

        self.resourcetype = NSGSLBSite.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        return "gslbsite"

    # Getters and setters for configurable options
    def get_sitename(self):
        """
        """
        return self.options['sitename']

    def set_sitename(self, sitename):
        """
        """
        self.options['sitename'] = sitename

    def get_sitetype(self):
        """
        """
        return self.options['sitetype']

    def set_sitetype(self, sitetype):
        """
        """
        self.options['sitetype'] = sitetype

    def get_siteipaddress(self):
        """
        """
        return self.options['siteipaddress']

    def set_siteipaddress(self, siteipaddress):
        """
        """
        self.options['siteipaddress'] = siteipaddress

    def get_publicip(self):
        """
        """
        return self.options['publicip']

    def set_publicip(self, publicip):
        """
        """
        self.options['publicip'] = publicip

    def get_metricexchange(self):
        """
        """
        return self.options['metricexchange']

    def set_metricexchange(self, metricexchange):
        """
        """
        self.options['metricexchange'] = metricexchange

    def get_nwmetricexchange(self):
        """
        """
        return self.options['nwmetricexchange']

    def set_nwmetricexchange(self, nwmetricexchange):
        """
        """
        self.options['nwmetricexchange'] = nwmetricexchange

    def get_sessionexchange(self):
        """
        """
        return self.options['sessionexchange']

    def set_sessionexchange(self, sessionexchange):
        """
        """
        self.options['sessionexchange'] = sessionexchange

    def get_triggermonitor(self):
        """
        """
        return self.options['triggermonitor']

    def set_triggermonitor(self, triggermonitor):
        """
        """
        self.options['triggermonitor'] = triggermonitor

    def get_parentsite(self):
        """
        """
        return self.options['parentsite']

    def set_parentsite(self, parentsite):
        """
        """
        self.options['parentsite'] = parentsite

    def get_clip(self):
        """
        """
        return self.options['clip']

    def set_clip(self, clip):
        """
        """
        self.options['clip'] = clip

    def get_publicclip(self):
        """
        """
        return self.options['publicclip']

    def set_publicclip(self, publicclip):
        """
        """
        self.options['publicclip'] = publicclip

    def get_status(self):
        """
        """
        return self.options['status']

    def get_persistencemepstatus(self):
        """
        """
        return self.options['persistencemepstatus']

    def get_version(self):
        """
        """
        return self.options['version']

    # Operations methods
    @staticmethod
    def get(nitro, site):
        """
        Use this API to fetch site resource of given name.
        """
        __site = NSGSLBSite()
        __site.set_sitename(site.get_sitename())
        __site.get_resource(nitro, site.get_sitename())
        return __site

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured site resources.
        """
        __url = nitro.get_url() + NSGSLBSite.get_resourcetype()
        __json_sites = nitro.get(__url).get_response_field(
            NSGSLBSite.get_resourcetype())
        __sites = []
        for json_site in __json_sites:
            __sites.append(NSGSLBSite(json_site))
        return __sites

    @staticmethod
    def add(nitro, site):
        """
        Use this API to add site.
        """
        __site = NSGSLBSite()
        __site.set_sitename(site.get_sitename())
        __site.set_sitetype(site.get_sitetype())
        __site.set_siteipaddress(site.get_siteipaddress())
        __site.set_publicip(site.get_publicip())
        __site.set_metricexchange(site.get_metricexchange())
        __site.set_nwmetricexchange(site.get_nwmetricexchange())
        __site.set_sessionexchange(site.get_sessionexchange())
        __site.set_triggermonitor(site.get_triggermonitor())
        __site.set_parentsite(site.get_parentsite())
        __site.set_clip(site.get_clip())
        __site.set_publicclip(site.get_publicclip())
        return __site.add_resource(nitro)

    @staticmethod
    def update(nitro, site):
        """
        Use this API to add site.
        """
        __site = NSGSLBSite()
        __site.set_sitename(site.get_sitename())
        __site.set_metricexchange(site.get_metricexchange())
        __site.set_nwmetricexchange(site.get_nwmetricexchange())
        __site.set_sessionexchange(site.get_sessionexchange())
        __site.set_triggermonitor(site.get_triggermonitor())
        return __site.update_resource(nitro)

    @staticmethod
    def delete(nitro, site):
        """
        Use this API to delete site of a given name.
        """
        __site = NSGSLBSite()
        __site.set_sitename(site.get_sitename())
        nsresponse = __site.delete_resource(nitro)
        return nsresponse
