# encoding: utf-8
from nsbaseresource import NSBaseResource


class NSCSVServerStat(NSBaseResource):
    
    def __init__(self, json_data=None):
        super(NSCSVServerStat, self).__init__()
        self.options = {
            'name': '',                 # Name of the content switching virtual server for which to display statistics. \
                                        # To display statistics for all configured Content Switching virtual servers, \
                                        # do not specify a value for this parameter.
            'clearstats': '',
            # ----- read-only options ------
            'establishedconn': '',      # Number of client connections in ESTABLISHED state.
            'primaryipaddress': '',     # The IP address on which the service is running.
            'primaryport': '',          # The port on which the service is running.
            'type': '',                 # Protocol associated with the vserver
            'state': '',                # Current state of the server. Possible values are UP, DOWN, UNKNOWN, \
                                        # OFS(Out of Service), TROFS(Transition Out of Service), \
                                        # TROFS_DOWN(Down When going Out of Service)
            'tothits': '',              # Total vserver hits
            'hitsrate': '',             # Rate (/s) counter for tothits
            'totalrequests': '',        # Total number of requests received on this service or virtual server. \
                                        # (This applies to HTTP/SSL services and servers.)
            'requestsrate': '',         # Rate (/s) counter for totalrequests
            'totalresponses': '',       # Number of responses received on this service or virtual server. \
                                        # (This applies to HTTP/SSL services and servers.)
            'responsesrate': '',        # Rate (/s) counter for totalresponses
            'totalrequestbytes': '',    # Total number of request bytes received on this service or virtual server.
            'requestbytesrate': '',     # Rate (/s) counter for totalrequestbytes
            'totalresponsebytes': '',   # Number of response bytes received by this service or virtual server.
            'responsebytesrate': '',    # Rate (/s) counter for totalresponsebytes
            'totalpktsrecvd': '',       # Total number of packets received by this service or virtual server.
            'pktsrecvdrate': '',        # Rate (/s) counter for totalpktsrecvd
            'totalpktssent': '',        # Total number of packets sent.
            'pktssentrate': '',         # Rate (/s) counter for totalpktssent
            'curclntconnections': '',   # Number of current client connections.
            'cursrvrconnections': '',   # Number of current connections to the actual servers behind the virtual server.
            'sothreshold': '',          # Spill Over Threshold set on the VServer.
            'totspillovers': '',        # Number of times vserver experienced spill over.
            'labelledconn': '',         # Number of Labeled connection on this vserver
            'pushlabel': '',            # Number of labels for this push vserver.
            'deferredreq': '',          # Number of deferred request on this vserver
            'deferredreqrate': '',      # Rate (/s) counter for deferredreq
            'invalidrequestresponse': '',  #Number invalid requests/responses on this vserver
            'invalidrequestresponsedropped': '',  # Number invalid requests/responses dropped on this vserver
        } 

        self.resourcetype = NSCSVServerStat.get_resourcetype()
        if not (json_data is None):
            for key in json_data.keys():
		if self.options.has_key(key):
		    self.options[key] = json_data[key]


    @staticmethod
    def get_resourcetype():
	return 'csvserver'

    def set_name(self, name):
        self.options['name'] = name

    def get_name(self):
        return self.options['name']

    def get_state(self):
        return self.options['state']

    def get_primaryipaddress(self):
        return self.options['primaryipaddress']

    @staticmethod
    def get(nitro, csvserver):
        __csvs = NSCSVServerStat()
        __csvs.set_name(csvserver.get_name())
        __csvs.get_resource(nitro, urltype='stat') 
        
        return __csvs

    @staticmethod
    def get_all(nitro):
        __url = nitro.get_url('stat') + NSCSVServerStat.get_resourcetype()
        __json_csvs = nitro.get(__url).get_response_field(NSCSVServerStat.get_resourcetype())
        __csvs = []
        for __json_vs in __json_csvs:
            __csvs.append(NSCSVServerStat(__json_vs))

        return __csvs
