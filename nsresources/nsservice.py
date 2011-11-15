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

        def get(self, nitro, service_name):
                url = nitro.get_url() + self.get_resource_type() + "/" + service_name

                nsresponse = nitro.get(url)
                if nsresponse.failed:
                        raise NSNitroError(nsresponse.message)

                for key in self.__options.iterkeys():
                        self.__options[key] = nsresponse.get_response_field("service")[0][key]

                for key in self.__options_readonly.iterkeys():
                        self.__options_readonly[key] = nsresponse.get_response_field("service")[0][key]

        def get_name(self):
                return self.__options['name']

        def get_svrstate(self):
                return self.__options_readonly['svrstate']

        def disable(self, nitro, service_name):
                self.__options['name'] = service_name
                self.set_options(self.__options)
                self.set_action("disable")
                payload = self.get_payload()
                nsresponse = nitro.post(payload)
                return nsresponse

        def enable(self, nitro, service_name):
                self.__options['name'] = service_name
                self.set_options(self.__options)
                self.set_action("enable")
                payload = self.get_payload()
                print payload
                nsresponse = nitro.post(payload)
                return nsresponse

        def rename(self, nitro, service_name, new_name):
                self.__options['name'] = service_name
                self.__options['newname'] = new_name
                self.set_options(self.__options)
                self.set_action("rename")
                payload = self.get_payload()
                print payload
                nsresponse = nitro.post(payload)
                return nsresponse


        def reset(self):
                self.__init__()
