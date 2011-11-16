import json
import urllib
from nsutil import *
from nsbaseresource import NSBaseResource

class NSService(NSBaseResource):

        def __init__(self):
                super(NSService, self).__init__()
                
                self.__options = {
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
                self.__options_readonly = {
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

                self.set_resource_type("service")



        # Getters and setters for configurable options
        def get_name(self):
                return self.__options['name']

        def set_name(self, name):
                self.__options['name'] = name
                self.set_options(self.__options)

        def get_newname(self):
                return self.__options['newname']

        def set_newname(self, name):
                self.__options['newname'] = name
                self.set_options(self.__options)

        def get_cachetype(self):
                return self.__options['cachetype']

        def set_cachetype(self, cachetype):
                self.__options['cachetype'] = cachetype
                self.set_options(self.__options)

        def get_servername(self):
                return self.__options['servername']

        def set_servername(self, servername):
                self.__options['servername'] = servername
                self.set_options(self.__options)

        def get_downstateflush(self):
                return self.__options['downstateflush']

        def set_downstateflush(self, downstateflush):
                self.__options['downstateflush'] = downstateflush
                self.set_options(self.__options)

        def get_maxreq(self):
                return self.__options['maxreq']

        def set_maxreq(self, maxreq):
                self.__options['maxreq'] = maxreq
                self.set_options(self.__options)


        # Read-only option getters
        def get_svrstate(self):
                return self.__options_readonly['svrstate']


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
