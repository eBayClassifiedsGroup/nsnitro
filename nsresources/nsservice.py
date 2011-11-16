import json
import urllib
from nsutil import *
from nsbaseresource import NSBaseResource

class NSService(NSBaseResource):

        def __init__(self):
                super(NSService, self).__init__()
                
                self.options = {
                        'cachetype' : '',
                        'servername' : '',
                        'downstateflush' : '',
                        'maxreq' : '',
                        'maxbandwidth' : '',
                        'svrtimeout' : '',
                        'port' : '',
                        'clttimeout' : '',
                        'servicetype' : '',
                        'cacheable' : '',
                        'maxclient' : '',
                        'ipaddress' : '',
                        'delay' : '',
                        'usip' : '',
                        'rtspsessionidremap' : '',
                        'cleartextport' : '',
                        'monthreshold' : '',
                        'accessdown' : '',
                        'serverid' : '',
                        'cka' : '',
                        'name' : '',
                        'newname' : '',
                        'sp' : '',
                        'dup_weight' : '',
                        'totalfailedprobes' : '',
                        'cip' : '',
                        'useproxyport' : '',
                        'sc' : '',
                        'cmp' : '',
                        'tcpb' : '',
                }
                # Readonly values
                self.options_readonly = {
                        'policyname' : '',
                        'monstatparam2' : '',
                        'monstatparam3' : '',
                        'stateupdatereason' : '',
                        'serviceconftype' : '',
                        'gslb' : '',
                        'svrstate' : '',
                        'monstatcode' : '',
                        'timesincelaststatechange' : '',
                        'tickssincelaststatechange' : '',
                        'responsetime' : '',
                        'statechangetimesec' : '',
                        'statechangetimemsec' : '',
                        'failedprobes' : '',
                        'totalprobes' : '',
                }

                self.resourcetype = "service"



        # Getters and setters for configurable options
        def get_name(self):
                return self.options['name']

        def set_name(self, name):
                self.options['name'] = name

        def get_newname(self):
                return self.options['newname']

        def set_newname(self, name):
                self.options['newname'] = name

        def get_cachetype(self):
                return self.options['cachetype']

        def set_cachetype(self, cachetype):
                self.options['cachetype'] = cachetype

        def get_servername(self):
                return self.options['servername']

        def set_servername(self, servername):
                self.options['servername'] = servername

        def get_downstateflush(self):
                return self.options['downstateflush']

        def set_downstateflush(self, downstateflush):
                self.options['downstateflush'] = downstateflush

        def get_maxreq(self):
                return self.options['maxreq']

        def set_maxreq(self, maxreq):
                self.options['maxreq'] = maxreq


        # Read-only option getters
        def get_svrstate(self):
                return self.options_readonly['svrstate']


        # Operations methods
        @staticmethod
        def disable(nitro, service):
                __service = NSService()
                __service.set_name(service.get_name())
                return __service.perform_operation(nitro, "disable")

        @staticmethod
        def enable(nitro, service):
                __service = NSService()
                __service.set_name(service.get_name())
                return __service.perform_operation(nitro, "enable")

        @staticmethod
        def rename(nitro, service):
                __service = NSService()
                __service.set_name(service.get_name())
                __service.set_newname(service.get_newname())
                return __service.perform_operation(nitro, "rename")

        @staticmethod
        def get(nitro, service_name):
                __service = NSService()
                return __service.get_resource(nitro, service_name)
