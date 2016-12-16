# encoding: utf-8
from nsbaseresource import NSBaseResource


class NSServiceStat(NSBaseResource):
        def __init__(self, json_data=None):
                super(NSServiceStat, self).__init__()
                self.options = {
                        'name': '',             # Name of the service.
                        'requestbytesrate': '',
                        'requestsrate': '',
                        'surgecount': '',
                        'cursrvrconnections': '',
                        'servicetype': '',
                        'curtflags': '',
                        'primaryport': '',
                        'totalrequests': '',
                        'svrestablishedconn': '',
                        'vsvrservicehitsrate': '',
                        'state': '',
                        'maxclients': '',
                        'throughputrate': '',
                        'responsesrate': '',
                        'totalrequestbytes': '',
                        'primaryipaddress': '',
                        'curload': '',
                        'vsvrservicehits': '',
                        'activetransactions': '',
                        'curclntconnections': '',
                        'totalresponses': '',
                        'curreusepool': '',
                        'throughput': '',
                        'totalresponsebytes': '',
                        'responsebytesrate': '',
                        'avgsvrttfb': '',       # Average TTFB between the NetScaler appliance and the server.TTFB is the time interval
                }
                self.resourcetype = NSServiceStat.get_resourcetype()

                if not (json_data is None):
                        for key in json_data.keys():
                                if key in self.options.keys():
                                        self.options[key] = json_data[key]

        @staticmethod
        def get_resourcetype():
                return 'service'

        def set_name(self, name):
                self.options['name'] = name

        def get_name(self):
                return self.options['name']

        def get_state(self):
                return self.options['state']

        def get_servicetype(self):
                return self.options['servicetype']


        @staticmethod
        def get(nitro, servicestat):
                __servicestat = NSServiceStat()
                __servicestat.set_servicename(
                        servicestat.get_servicename())
                __servicestat.get_resource(
                        nitro, 'stat', __servicestat.get_servicegroupname())
                return __servicestat

        @staticmethod
        def get_all(nitro):
                __url = nitro.get_url('stat') + NSServiceStat.get_resourcetype()
                __json_sstat = nitro.get(__url).get_response_field(
                        NSServiceStat.get_resourcetype())
                __sstats = []
                for json_sstat in __json_sstat:
                        __sstats.append(NSServiceStat(json_sstat))
                return __sstats