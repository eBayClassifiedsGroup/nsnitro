import json
import urllib
from nsutil import *
from nsbaseresource import NSPayloadFormatter

class NSService:

        # Public variables
        __options = {
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
                'cmp' : ''
        }
        # Readonly values
        __options_readonly = {
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
                'tcpb' : '',
        }

        def __init__(self):
                pass

        def get(self, nitro, service_name):
                url = nitro.get_url() + self.__get_resource_type() + "/" + service_name

                nsresponse = nitro.get(url)
                if nsresponse.failed:
                        raise NSNitroError(nsresponse.message)

                for key in self.__options.iterkeys():
                        self.__options[key] = nsresponse.get_response_field("service")[0][key]

                for key in self.__options_readonly.iterkeys():
                        self.__options_readonly[key] = nsresponse.get_response_field("service")[0][key]

        def __get_resource_type(self):
                return "service"

        def get_name(self):
                return self.__options['name']

        def get_svrstate(self):
                return self.__options_readonly['svrstate']

        def disable(self, nitro, service_name):
                self.__options['name'] = service_name
                payload = NSPayloadFormatter(self.__get_resource_type(), "disable", self.__options).get_payload()
                print payload
                nsresponse = nitro.post(payload)
                print nsresponse.message

#                nsresponse = nitro.post(url)

        def json(self):
                return json.JSONEncoder().encode(self.__options)



