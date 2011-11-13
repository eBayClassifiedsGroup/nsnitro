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
	policyname = False
	cachetype = False
	servername = False
	downstateflush = False
	maxreq = False
	statechangetimesec = False
	maxbandwidth = False
	svrtimeout = False
	gslb = False
	port = False
	clttimeout = False
	servicetype = False
	cacheable = False
	maxclient = False
	ipaddress = False
	delay = False
	usip = False
	failedprobes = False
	responsetime = False
	rtspsessionidremap = False
	totalprobes = False
	monstate = False
	cleartextport = False
	svrstate = False
	tickssincelaststatechange = False
	monthreshold = False
	monstatcode = False
	serviceconftype = False
	accessdown = False
	serverid = False
	tcpb = False
	monstatparam1 = False
	cka = False
	name = False
	monstatparam2 = False
	monstatparam3 = False
	statupdatereason = False
	sp = False
	dup_weight = False
	totalfailedprobes = False
	statechangetimemsec = False
	timesincelaststatechange = False
	cip = False
	userproxyport = False
	sc = False
	cmp = False
	
	def __init__(self, nitro):
		self.__nitro = nitro


	def load(self, service_name):
		url = self.__nitro.__baseurl + "service/" + service_name

                try:
                        opener = urllib2.build_opener()
                        opener.addheaders.append(('Cookie', 'sessionid='+self.__sessionid))
                        response = opener.open(url)

                except urllib2.HTTPError, e:
                        print "Got reponse code: %s from the server" % e.code
                        raise NSNitroError("Could not get service: %s, %s" % (e.code, e.message))

                nsresponse = NSNitroResponse(response.read())
                if nsresponse.failed:
                        raise NSNitroError(nsresponse.message)
                return nsresponse		
