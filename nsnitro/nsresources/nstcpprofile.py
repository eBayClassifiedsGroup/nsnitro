from nsbaseresource import NSBaseResource

__author__ = 'Aleksandar Topuzovic'


class NSTCPProfile(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSTCPProfile, self).__init__()

        self.options = {
            # Read-write values
            'name': '',
            'ws': '',
            'sack': '',
            'wsval': '',
            'nagle': '',
            'ackonpush': '',
            'mss': '',
            'maxburst': '',
            'initialcwnd': '',
            'delayedack': '',
            'oooqsize': '',
            'maxpktpermss': '',
            'pktperretx': '',
            'minrto': '',
            'slowstartincr': '',
            'buffersize': '',

            # Readonly values
            'refcnt': '',
        }

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options:
                    self.options[key] = json_data[key]

        self.resourcetype = NSTCPProfile.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        return "nstcpprofile"

    # Read-write
    def get_name(self):
        """
        Name of the TCP profile.
        Minimum length = 1
        Maximum length = 127
        """
        return self.options['name']

    def set_name(self, name):
        """
        Name of the TCP profile.
        Minimum length = 1
        Maximum length = 127
        """
        self.options['name'] = name

    def get_ws(self):
        """
        The state of WS.
        Default value: DISABLED
        """
        return self.options['ws']

    def set_ws(self, ws):
        """
        The state of WS.
        Default value: DISABLED
        """
        self.options['ws'] = ws

    def get_sack(self):
        """
        The state of SACK.
        Default value: DISABLED
        """
        return self.options['sack']

    def set_sack(self, sack):
        """
        The state of SACK.
        Default value: DISABLED
        """
        self.options['sack'] = sack

    def get_wsval(self):
        """
        Window Scaling Factor used.
        Default value: 4
        Minimum value = 0
        Maximum value = 8
        """
        return self.options['wsval']

    def set_wsval(self, wsval):
        """
        Window Scaling Factor used.
        Default value: 4
        Minimum value = 0
        Maximum value = 8
        """
        self.options['wsval'] = wsval

    def get_nagle(self):
        """
        Whether to enable Nagle's algorithm on connections.
        Default value: DISABLED
        """
        return self.options['nagle']

    def set_nagle(self, nagle):
        """
        Whether to enable Nagle's algorithm on connections.
        Default value: DISABLED
        """
        self.options['nagle'] = nagle

    def get_ackonpush(self):
        """
        Enable/disable immediate ACK on PUSH packet.
        Default value: ENABLED
        """
        return self.options['ackonpush']

    def set_ackonpush(self, ackonpush):
        """
        Enable/disable immediate ACK on PUSH packet.
        Default value: ENABLED
        """
        self.options['ackonpush'] = ackonpush

    def get_mss(self):
        """
        Set Maximum Segment Size(MSS) to use for TCP Connection (0 forces use of global setting).
        Default value: 0
        Minimum value = 0
        Maximum value = 1460
        """
        return self.options['mss']

    def set_mss(self, mss):
        """
        Set Maximum Segment Size(MSS) to use for TCP Connection (0 forces use of global setting).
        Default value: 0
        Minimum value = 0
        Maximum value = 1460
        """
        self.options['mss'] = mss

    def get_maxburst(self):
        """
        Max-Burst Factor used.
        Default value: 6
        Minimum value = 1
        Maximum value = 255
        """
        return self.options['maxburst']

    def set_maxburst(self, maxburst):
        """
        Max-Burst Factor used.
        Default value: 6
        Minimum value = 1
        Maximum value = 255
        """
        self.options['maxburst'] = maxburst

    def get_initialcwnd(self):
        """
        Intial value of TCP cwnd used.
        Default value: 4
        Minimum value = 1
        Maximum value = 44
        """
        return self.options['initialcwnd']

    def set_initialcwnd(self, initialcwnd):
        """
        Intial value of TCP cwnd used.
        Default value: 4
        Minimum value = 1
        Maximum value = 44
        """
        self.options['initialcwnd'] = initialcwnd

    def get_delayedack(self):
        """
        Delayed acknowledgement timeout (in millisec).
        Default value: 200
        Minimum value = 10
        Maximum value = 300
        """
        return self.options['delayedack']

    def set_delayedack(self, delayedack):
        """
        Delayed acknowledgement timeout (in millisec).
        Default value: 200
        Minimum value = 10
        Maximum value = 300
        """
        self.options['delayedack'] = delayedack

    def get_oooqsize(self):
        """
        Maximum size of out-of-order packet queue (0 means infinite).
        Default value: 64
        Minimum value = 0
        Maximum value = 65535
        """
        return self.options['oooqsize']

    def set_oooqsize(self, oooqsize):
        """
        Maximum size of out-of-order packet queue (0 means infinite).
        Default value: 64
        Minimum value = 0
        Maximum value = 65535
        """
        self.options['oooqsize'] = oooqsize

    def get_maxpktpermss(self):
        """
        Enable packet count based congestion control by setting to non zero value.
        Default value: 0
        Minimum value = 0
        Maximum value = 512
        """
        return self.options['maxpktpermss']

    def set_maxpktpermss(self, maxpktpermss):
        """
        Enable packet count based congestion control by setting to non zero value.
        Default value: 0
        Minimum value = 0
        Maximum value = 512
        """
        self.options['maxpktpermss'] = maxpktpermss

    def get_pktperretx(self):
        """
        Set value for maximum number packets per retransmission.
        Default value: 1
        Minimum value = 1
        Maximum value = 512
        """
        return self.options['pktperretx']

    def set_pktperretx(self, pktperretx):
        """
        Set value for maximum number packets per retransmission.
        Default value: 1
        Minimum value = 1
        Maximum value = 512
        """
        self.options['pktperretx'] = pktperretx

    def get_minrto(self):
        """
        Set minimum limit on TCP RTO (in millisec).
        Default value: 1000
        Minimum value = 10
        Maximum value = 64000
        """
        return self.options['minrto']

    def set_minrto(self, minrto):
        """
        Set minimum limit on TCP RTO (in millisec).
        Default value: 1000
        Minimum value = 10
        Maximum value = 64000
        """
        self.options['minrto'] = minrto

    def get_slowstartincr(self):
        """
        Set TCP slowstart increment factor.
        Default value: 2
        Minimum value = 1
        Maximum value = 100
        """
        return self.options['slowstartincr']

    def set_slowstartincr(self, slowstartincr):
        """
        Set TCP slowstart increment factor.
        Default value: 2
        Minimum value = 1
        Maximum value = 100
        """
        self.options['slowstartincr'] = slowstartincr

    def get_buffersize(self):
        """
        Set TCP buffer size.
        Default value: 8190
        Minimum value = 8190
        Maximum value = 4194304
        """
        return self.options['buffersize']

    def set_buffersize(self, buffersize):
        """
        Set TCP buffer size.
        Default value: 8190
        Minimum value = 8190
        Maximum value = 4194304
        """
        self.options['buffersize'] = buffersize

    # Read-only
    def get_refcnt(self):
        """
        Number of entities using this profile
        """
        return self.options['refcnt']

    # Operations methods

    @staticmethod
    def get(nitro, tcpprofile):
        """
        Use this API to fetch service resource of given name.
        """
        __tcpprofile = NSTCPProfile()
        __tcpprofile.set_name(tcpprofile.get_name())
        __tcpprofile.get_resource(nitro)
        return __tcpprofile

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured service resources.
        """
        __url = nitro.get_url() + NSTCPProfile.get_resourcetype()
        __json_tcpprofiles = nitro.get(__url).get_response_field(NSTCPProfile.get_resourcetype())
        __tcpprofiles = []
        for json_service in __json_tcpprofiles:
            __tcpprofiles.append(NSTCPProfile(json_service))
        return __tcpprofiles

    @staticmethod
    def add(nitro, tcpprofile):
        """
        Use this API to add a tcp profile.
        """
        __tcpprofile = NSTCPProfile()
        __tcpprofile.set_name(tcpprofile.get_name())
        __tcpprofile.set_ws(tcpprofile.get_ws())
        __tcpprofile.set_sack(tcpprofile.get_sack())
        __tcpprofile.set_wsval(tcpprofile.get_wsval())
        __tcpprofile.set_nagle(tcpprofile.get_nagle())
        __tcpprofile.set_ackonpush(tcpprofile.get_ackonpush())
        __tcpprofile.set_mss(tcpprofile.get_mss())
        __tcpprofile.set_maxburst(tcpprofile.get_maxburst())
        __tcpprofile.set_initialcwnd(tcpprofile.get_initialcwnd())
        __tcpprofile.set_delayedack(tcpprofile.get_delayedack())
        __tcpprofile.set_oooqsize(tcpprofile.get_oooqsize())
        __tcpprofile.set_maxpktpermss(tcpprofile.get_maxpktpermss())
        __tcpprofile.set_pktperretx(tcpprofile.get_pktperretx())
        __tcpprofile.set_minrto(tcpprofile.get_minrto())
        __tcpprofile.set_slowstartincr(tcpprofile.get_slowstartincr())
        __tcpprofile.set_buffersize(tcpprofile.get_buffersize())
        return __tcpprofile.add_resource(nitro)

    @staticmethod
    def update(nitro, tcpprofile):
        """
        Use this API to update a tcp profile.
        """
        __tcpprofile = NSTCPProfile()
        __tcpprofile.set_name(tcpprofile.get_name())
        __tcpprofile.set_ws(tcpprofile.get_ws())
        __tcpprofile.set_sack(tcpprofile.get_sack())
        __tcpprofile.set_wsval(tcpprofile.get_wsval())
        __tcpprofile.set_nagle(tcpprofile.get_nagle())
        __tcpprofile.set_ackonpush(tcpprofile.get_ackonpush())
        __tcpprofile.set_mss(tcpprofile.get_mss())
        __tcpprofile.set_maxburst(tcpprofile.get_maxburst())
        __tcpprofile.set_initialcwnd(tcpprofile.get_initialcwnd())
        __tcpprofile.set_delayedack(tcpprofile.get_delayedack())
        __tcpprofile.set_oooqsize(tcpprofile.get_oooqsize())
        __tcpprofile.set_maxpktpermss(tcpprofile.get_maxpktpermss())
        __tcpprofile.set_pktperretx(tcpprofile.get_pktperretx())
        __tcpprofile.set_minrto(tcpprofile.get_minrto())
        __tcpprofile.set_slowstartincr(tcpprofile.get_slowstartincr())
        __tcpprofile.set_buffersize(tcpprofile.get_buffersize())
        return __tcpprofile.update_resource(nitro)

    @staticmethod
    def delete(nitro, tcpprofile):
        """
        Use this API to delete a tcpprofile of a given name.
        """
        __tcpprofile = NSTCPProfile()
        __tcpprofile.set_name(tcpprofile.get_name())
        nsresponse = __tcpprofile.delete_resource(nitro)
        return nsresponse
