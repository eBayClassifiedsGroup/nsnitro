import json

class NSNitroError(Exception):
        """ Custom exception class """
        def __init__(self, value):
                self.message = value
        def __str__(self):
                return repr(self.message)

class NSNitroResponse:
        """ Generic class for accessing LB response dictionary. Can provide string response back and a parsed dictionary """
        __jresponse = False
        __sresponse = False
        errorcode = -1
        message = False
        failed = False

        def __init__(self, response):
                """ Constructor. reponse - string response """
                self.__sresponse = response
                self.__jresponse = json.loads(response)
                self.__parse_response()


        def get_json_response(self):
                """ Returns LB response as parsed dictionary """
                return self.__jresponse

        def get_string_response(self):
                """ Returns LB response as a string """
                return self.__sresponse


        def __parse_response(self):
                self.errorcode = self.__jresponse['errorcode']
                self.message   = self.__jresponse['message']
                if self.errorcode != 0:
                        self.failed = True

        def get_response_field(self, field_name):
                """ Returns field_name of parsed JSON dictionary """
                return self.__jresponse[field_name]
class NSService:

        __nitro = False

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
                'tcpb' : '',
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
                'totalprobes' : ''
        }

        def __init__(self, nitro):
                self.__nitro = nitro

        def __get_nitro(self):
                return self.__nitro


        def get(self, service_name):
                url = self.__nitro.get_url() + "service/" + service_name

                nitro = self.__nitro
                nsresponse = nitro.get(url)
                if nsresponse.failed:
                        raise NSNitroError(nsresponse.message)

                for key in self.__options.iterkeys():
                        self.__options[key] = nsresponse.get_response_field("service")[0][key]

                for key in self.__options_readonly.iterkeys():
                        self.__options_readonly[key] = nsresponse.get_response_field("service")[0][key]

        def get_resource_type(self):
                return "service"

        def get_name(self):
                return self.__options['name']

        def json(self):
                return json.JSONEncoder().encode(self.__options)

class NSPayloadFormatter:

        def __init__(self, sessionid, options):
                pass
