# encoding: utf-8
from nsbaseresource import NSBaseResource


class NSLBVServerStat(NSBaseResource):

    def __init__(self, json_data=None):
        super(NSLBVServerStat, self).__init__()
        self.options = {
            'name': '',             # Name of the virtual server. If no name is provided, statistical 
                                    # data of all configured virtual servers is displayed.
            'clearstats': '',       # Clear the statsistics / counters,Possible values = basic, full
            'sortby': '',           # use this argument to sort by specific key.
            'sortorder': '',        # use this argument to specify sort order.Default value:
                                    # SORT_DESCENDING,Possible values = ascending, descending
            
            # -----read only options -----
            'vsvrsurgecount': '',   # Number of requests waiting on this vserver.
            'establishedconn': '',  # Number of client connections in ESTABLISHED state.
            'inactsvcs': '',        # number of INACTIVE services bound to a vserver.
            'vslbhealth': '',       # Health of the vserver. This gives percentage of UP services
                                    # bound to this vserver.
            'primaryipaddress': '', # IP address of the vserver
            'primaryport': '',      # The port on which the service is running.
            'type': '',             # Protocol associated with the vserver
            'state': '',            # Current state of the server. Possible values are UP, DOWN, UNKNOWN, 
                                    # OFS(Out of Service), TROFS(Transition Out of Service), TROFS_DOWN(Down 
                                    # When going Out of Service)
            'actsvcs': '',          # number of ACTIVE services bound to a vserver
            'tothits': '',          # Total vserver hits
            'hitsrate': '',         # Rate (/s) counter for tothits
            'totalrequests': '',    # Total number of requests received on this service or virtual
                                    # server. (This applies to HTTP/SSL services and servers.)
            'requestsrate': '',     # Rate (/s) counter for totalrequests
            'totalresponses': '',   # Number of responses received on this service or virtual
                                    # server. (This applies to HTTP/SSL services and servers.)
            'responsesrate': '',    # Rate (/s) counter for totalresponses
            'totalrequestbytes': '',# Total number of request bytes received on this service or
                                    # virtual server.
            'requestbytesrate': '', # Rate (/s) counter for totalrequestbytes
            'totalresponsebytes':'',# Number of response bytes received by this service or virtual server.
            'responsebytesrate': '',# Rate (/s) counter for totalresponsebytes
            'totalpktsrecvd': '',   # Total number of packets received by this service or virtual server.
            'pktsrecvdrate': '',    # Rate (/s) counter for totalpktsrecvd
            'totalpktssent': '',    # Total number of packets sent.
            'pktssentrate': '',     # Rate (/s) counter for totalpktssent
            'curclntconnections':'',# Number of current client connections.
            'cursrvrconnections':'',# Number of current connections to the actual servers behind
                                    # the virtual server.
            'surgecount': '',       # Number of requests in the surge queue.
            'svcsurgecount': '',    # Total number of requests in the surge queues of all the
                                    # services bound to this LB-vserver.
            'sothreshold': '',      # Spill Over Threshold set on the VServer.
            'totspillovers': '',    # Number of times vserver experienced spill over.
            'labelledconn': '',     # Number of Labeled connection on this vserver
            'pushlabel': '',        # Number of labels for this push vserver.
            'deferredreq': '',      # Number of deferred request on this vserver.
            'deferredreqrate': '',  # Rate (/s) counter for deferredreq.
            'invalidrequestresponse': '',        # Number invalid requests/responses on this vserver
            'invalidrequestresponsedropped': '', # Number invalid requests/responses dropped on this vserver  
        }
        self.resourcetype = NSLBVServerStat.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return 'lbvserver'

    def set_name(self, name):
        self.options['name'] = name

    def get_name(self):
        return self.options['name']

    def set_clearstats(self, method):
        self.options['clearstats'] = method

    def get_clearstats(self):
        return self.options['clearstats']

    def set_sortby(self, sortby):
        self.options['sortby'] = sortby

    def get_sortby(self):
        return self.options['sortby']

    # ---- read-only options -------
    def get_primaryipaddress(self):
        return self.options['primaryipaddress']

    def get_primaryport(self):
        return self.options['primaryport']

    def get_type(self):
        return self.options['type']

    def get_state(self):
        return self.options['state']

    def get_primaryipaddress(self):
        return self.options['primaryipaddress']

    @staticmethod
    def get(nitro, lbvserver):
        """
        Use this api to fetch lbvserver's stat info of given name.
        """
        __lbvserver = NSLBVServerStat()
        __lbvserver.set_name(lbvserver.get_name())
        __lbvserver.get_resource(nitro, 'stat')
        return __lbvserver

    @staticmethod
    def get_all(nitro):
        """
        Use this api to fetch all lbvserver' stat info
        """
        __url = nitro.get_url('stat') + NSLBVServerStat.get_resourcetype()
        __json_lbvservers = nitro.get(__url).get_response_field(
            NSLBVServerStat.get_resourcetype())
        __lbvservers = []
        for json_lbvserver in __json_lbvservers:
            __lbvservers.append(NSLBVServerStat(json_lbvserver))
        return __lbvservers
