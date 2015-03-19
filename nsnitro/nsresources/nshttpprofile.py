from nsbaseresource import NSBaseResource

__author__ = 'Aleksandar Topuzovic'


class NSHTTPProfile(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSHTTPProfile, self).__init__()

        self.options = {
            # Read-write values
            'name': '',
            'dropinvalreqs': '',
            'markhttp09inval': '',
            'markconnreqinval': '',
            'cmponpush': '',
            'conmultiplex': '',
            'maxreusepool': '',
            'dropextracrlf': '',
            'incomphdrdelay': '',
            'reqtimeout': '',
            'dropextradata': '',
            'maxreq': '',
            'reusepooltimeout': '',

            # Readonly values
            'refcnt': '',
        }

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options:
                    self.options[key] = json_data[key]

        self.resourcetype = NSHTTPProfile.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        return "nshttpprofile"

    # Read-write
    def get_name(self):
        """
        Name of the HTTP profile.
        Minimum length = 1
        Maximum length = 127
        """
        return self.options['name']

    def set_name(self, name):
        """
        Name of the HTTP profile.
        Minimum length = 1
        Maximum length = 127
        """
        self.options['name'] = name

    def get_dropinvalreqs(self):
        """
        Enable/disable dropping of invalid HTTP requests/responses.
        Default value: DISABLED
        """
        return self.options['dropinvalreqs']

    def set_dropinvalreqs(self, dropinvalreqs):
        """
        Enable/disable dropping of invalid HTTP requests/responses.
        Default value: DISABLED
        """
        self.options['dropinvalreqs'] = dropinvalreqs

    def get_markhttp09inval(self):
        """
        Enable/disable invalidating HTTP 0.9 requests.
        Default value: DISABLED
        """
        return self.options['markhttp09inval']

    def set_markhttp09inval(self, markhttp09inval):
        """
        Enable/disable invalidating HTTP 0.9 requests.
        Default value: DISABLED
        """
        self.options['markhttp09inval'] = markhttp09inval

    def get_markconnreqinval(self):
        """
        Enable/disable invalidating CONNECT HTTP requests.
        Default value: DISABLED
        """
        return self.options['markconnreqinval']

    def set_markconnreqinval(self, markconnreqinval):
        """
        Enable/disable invalidating CONNECT HTTP requests.
        Default value: DISABLED
        """
        self.options['markconnreqinval'] = markconnreqinval

    def get_cmponpush(self):
        """
        Enable/disable compression on PUSH packet.
        Default value: DISABLED
        """
        return self.options['cmponpush']

    def set_cmponpush(self, cmponpush):
        """
        Enable/disable compression on PUSH packet.
        Default value: DISABLED
        """
        self.options['cmponpush'] = cmponpush

    def get_conmultiplex(self):
        """
        Connection multiplexing.
        Default value: ENABLED
        """
        return self.options['conmultiplex']

    def set_conmultiplex(self, conmultiplex):
        """
        Connection multiplexing.
        Default value: ENABLED
        """
        self.options['conmultiplex'] = conmultiplex

    def get_maxreusepool(self):
        """
        Maximum connections in reusepool. If set to zero, limit will not be applied.
        Default value: 0
        """
        return self.options['maxreusepool']

    def set_maxreusepool(self, maxreusepool):
        """
        Maximum connections in reusepool. If set to zero, limit will not be applied.
        Default value: 0
        """
        self.options['maxreusepool'] = maxreusepool

    def get_dropextracrlf(self):
        """
        Drop extra CRLF after header is complete.
        Default value: ENABLED
        """
        return self.options['dropextracrlf']

    def set_dropextracrlf(self, dropextracrlf):
        """
        Drop extra CRLF after header is complete.
        Default value: ENABLED
        """
        self.options['dropextracrlf'] = dropextracrlf

    def get_incomphdrdelay(self):
        """
        Maximum time to wait between incomplete header packets (ms ticks).
        Default value: 7000
        """
        return self.options['incomphdrdelay']

    def set_incomphdrdelay(self, incomphdrdelay):
        """
        Maximum time to wait between incomplete header packets (ms ticks).
        Default value: 7000
        """
        self.options['incomphdrdelay'] = incomphdrdelay

    def get_reqtimeout(self):
        """
        The time (in seconds) within which the HTTP request must complete.
        Default value: 0
        """
        return self.options['reqtimeout']

    def set_reqtimeout(self, reqtimeout):
        """
        The time (in seconds) within which the HTTP request must complete.
        Default value: 0
        """
        self.options['reqtimeout'] = reqtimeout

    def get_dropextradata(self):
        """
        Drop extra data coming from Server.
        Default value: DISABLED
        """
        return self.options['dropextradata']

    def set_dropextradata(self, dropextradata):
        """
        Drop extra data coming from Server.
        Default value: DISABLED
        """
        self.options['dropextradata'] = dropextradata

    def get_maxreq(self):
        """
        Maximum requests allowed on a single connection.
        Default value: 0
        """
        return self.options['maxreq']

    def set_maxreq(self, maxreq):
        """
        Maximum requests allowed on a single connection.
        Default value: 0
        """
        self.options['maxreq'] = maxreq

    def get_reusepooltimeout(self):
        """
        Idle timeout (in seconds) for server connections in re-use pool.
        Connections in the re-use pool are flushed, if they remain idle for the
        configured timeout.
        Default value: 0
        """
        return self.options['reusepooltimeout']

    def set_reusepooltimeout(self, reusepooltimeout):
        """
        Idle timeout (in seconds) for server connections in re-use pool.
        Connections in the re-use pool are flushed, if they remain idle for the
        configured timeout.
        Default value: 0
        """
        self.options['reusepooltimeout'] = reusepooltimeout

    # Read-only
    def get_refcnt(self):
        """
        Number of entities using this profile
        """
        return self.options['refcnt']

    # Operations methods

    @staticmethod
    def get(nitro, httpprofile):
        """
        Use this API to fetch service resource of given name.
        """
        __httpprofile = NSHTTPProfile()
        __httpprofile.set_name(httpprofile.get_name())
        __httpprofile.get_resource(nitro)
        return __httpprofile

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured service resources.
        """
        __url = nitro.get_url() + NSHTTPProfile.get_resourcetype()
        __json_httpprofiles = nitro.get(__url).get_response_field(NSHTTPProfile.get_resourcetype())
        __httpprofiles = []
        for json_service in __json_httpprofiles:
            __httpprofiles.append(NSHTTPProfile(json_service))
        return __httpprofiles

    @staticmethod
    def add(nitro, httpprofile):
        """
        Use this API to add a http profile.
        """
        __httpprofile = NSHTTPProfile()
        __httpprofile.set_name(httpprofile.get_name())
        __httpprofile.set_dropinvalreqs(httpprofile.get_dropinvalreqs())
        __httpprofile.set_markhttp09inval(httpprofile.get_markhttp09inval())
        __httpprofile.set_markconnreqinval(httpprofile.get_markconnreqinval())
        __httpprofile.set_cmponpush(httpprofile.get_cmponpush())
        __httpprofile.set_conmultiplex(httpprofile.get_conmultiplex())
        __httpprofile.set_maxreusepool(httpprofile.get_maxreusepool())
        __httpprofile.set_dropextracrlf(httpprofile.get_dropextracrlf())
        __httpprofile.set_incomphdrdelay(httpprofile.get_incomphdrdelay())
        __httpprofile.set_reqtimeout(httpprofile.get_reqtimeout())
        __httpprofile.set_dropextradata(httpprofile.get_dropextradata())
        __httpprofile.set_maxreq(httpprofile.get_maxreq())
        __httpprofile.set_reusepooltimeout(httpprofile.get_reusepooltimeout())
        return __httpprofile.add_resource(nitro)

    @staticmethod
    def update(nitro, httpprofile):
        """
        Use this API to update a http profile.
        """
        __httpprofile = NSHTTPProfile()
        __httpprofile.set_name(httpprofile.get_name())
        __httpprofile.set_dropinvalreqs(httpprofile.get_dropinvalreqs())
        __httpprofile.set_markhttp09inval(httpprofile.get_markhttp09inval())
        __httpprofile.set_markconnreqinval(httpprofile.get_markconnreqinval())
        __httpprofile.set_cmponpush(httpprofile.get_cmponpush())
        __httpprofile.set_conmultiplex(httpprofile.get_conmultiplex())
        __httpprofile.set_maxreusepool(httpprofile.get_maxreusepool())
        __httpprofile.set_dropextracrlf(httpprofile.get_dropextracrlf())
        __httpprofile.set_incomphdrdelay(httpprofile.get_incomphdrdelay())
        __httpprofile.set_reqtimeout(httpprofile.get_reqtimeout())
        __httpprofile.set_dropextradata(httpprofile.get_dropextradata())
        __httpprofile.set_maxreq(httpprofile.get_maxreq())
        __httpprofile.set_reusepooltimeout(httpprofile.get_reusepooltimeout())
        return __httpprofile.update_resource(nitro)

    @staticmethod
    def delete(nitro, httpprofile):
        """
        Use this API to delete a httpprofile of a given name.
        """
        __httpprofile = NSHTTPProfile()
        __httpprofile.set_name(httpprofile.get_name())
        nsresponse = __httpprofile.delete_resource(nitro)
        return nsresponse
