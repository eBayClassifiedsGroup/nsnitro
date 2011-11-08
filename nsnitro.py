import urllib, urllib2
import json

__version__ = "0.0.1"
__all__ = [ 'NSNitro', 'NSNitroError', 'NSNitroResponse' ]

class NSNitro:

        ip          = "1.2.3.4"
        user        = "api_user"
        password    = "api_user"
        baseurl     = "http://1.2.3.4/nitro/v1/config/"
	sessionid   = ""
	loggedin    = False
        initialized = False
	contenttype = "application/x-www-form-urlencoded"
	postheaders = {'Cookie' : 'sessionid='+sessionid, 'Content-type' : contenttype}

        def __init__(self):
                pass

        def initialize(self, ip, user, password):
                self.ip = ip
                self.user = user
                self.password = password
                self.baseurl = "http://%s/nitro/v1/config/" % ip
                self.initialized = True

        def get_url(self):
                if not self.initialized:
                        raise NSNitroError("Not initialized. Call NSNitro.initialize() with ip, user, pass")
                return self.baseurl        

	def get_sessionid(self):
		if not self.initialized:
			raise NSNitroError("Not initialized. Call NSNitro.initialize() with ip, user, pass")
		if not self.loggedin:
			raise NSNitroError("Not logged in. Call NSNitro.login()")

		return self.sessionid

        def login(self):
		if not self.initialized:
			raise NSNitroError("Not initialized. Call NSNitro.initialize() with ip, user, pass")

                payload = {"object":{"login":{"username":"api_user","password":"api_user"}}}
                payload_encoded = urllib.urlencode(payload)

        	try:
                	req = urllib2.Request(self.baseurl, payload_encoded, { 'Content-Type': self.contenttype } )
                	response = urllib2.urlopen(req)
                	de_content = eval(response.read())

                	self.sessionid = de_content['sessionid']
			self.postheaders = {'Cookie' : 'sessionid='+self.sessionid, 'Content-type' : self.contenttype}
                	self.loggedin = True
			return True

        	except urllib2.HTTPError, e:
                	print "Got reponse code: %s from the server" % e.code
                	raise NSNitroError("Could not login: %s, %s" % (e.code, e.message))


	def enable_lbvserver(self, vserver_name):
		if not self.initialized:
			raise NSNitroError("Not initialized. Call NSNitro.initialize() with ip, user, pass")
		if not self.loggedin:
			raise NSNitroError("Not logged in. Call NSNitro.login()")

		try:
			self.get_lbvserver(vserver_name)
		except NSNitroError, e:
			raise e

        	payload = { "object" : { "params" : { "action" : "enable" }, "lbvserver" : { "name" : vserver_name } } }
		payload_encoded = urllib.urlencode(payload)

		try:
			req = urllib2.Request(self.baseurl, payload_encoded, self.postheaders)
        		response = urllib2.urlopen(req)

        	except urllib2.HTTPError, e:
                	print "Got reponse code: %s from the server" % e.code
                	raise NSNitroError("Could not enable vserver: %s, %s" % (e.code, e.message))

		nsresponse = NSNitroResponse(response.read())
		if nsresponse.failed:
			raise NSNitroError(nsresponse.message)
        	return nsresponse	

	def disable_lbvserver(self, vserver_name):
		if not self.initialized:
			raise NSNitroError("Not initialized. Call NSNitro.initialize() with ip, user, pass")
		if not self.loggedin:
			raise NSNitroError("Not logged in. Call NSNitro.login()")

		try:
			self.get_lbvserver(vserver_name)
		except NSNitroError, e:
			raise e

        	payload = { "object" : { "params" : { "action" : "disable" }, "lbvserver" : { "name" : vserver_name } } }
		payload_encoded = urllib.urlencode(payload)

		try:
			req = urllib2.Request(self.baseurl, payload_encoded, self.postheaders)
        		response = urllib2.urlopen(req)

        	except urllib2.HTTPError, e:
                	print "Got reponse code: %s from the server" % e.code
                	raise NSNitroError("Could not disable vserver: %s, %s" % (e.code, e.message))

		nsresponse = NSNitroResponse(response.read())
		if nsresponse.failed:
			raise NSNitroError(nsresponse.message)
        	return nsresponse	

	def get_lbvserver(self, vserver_name):
		if not self.initialized:
			raise NSNitroError("Not initialized. Call NSNitro.initialize() with ip, user, pass")
		if not self.loggedin:
			raise NSNitroError("Not logged in. Call NSNitro.login()")

		url = self.baseurl + "lbvserver/" + vserver_name

		try:
			opener = urllib2.build_opener()
			opener.addheaders.append(('Cookie', 'sessionid='+self.sessionid))
			response = opener.open(url)

        	except urllib2.HTTPError, e:
                	print "Got reponse code: %s from the server" % e.code
                	raise NSNitroError("Could not get vserver: %s, %s" % (e.code, e.message))

		nsresponse = NSNitroResponse(response.read())
		if nsresponse.failed:
			raise NSNitroError(nsresponse.message)
        	return nsresponse	


	def get_service(self, service_name):
		if not self.initialized:
			raise NSNitroError("Not initialized. Call NSNitro.initialize() with ip, user, pass")
		if not self.loggedin:
			raise NSNitroError("Not logged in. Call NSNitro.login()")

		url = self.baseurl + "service/" + service_name

		try:
			opener = urllib2.build_opener()
			opener.addheaders.append(('Cookie', 'sessionid='+self.sessionid))
			response = opener.open(url)

        	except urllib2.HTTPError, e:
                	print "Got reponse code: %s from the server" % e.code
                	raise NSNitroError("Could not get service: %s, %s" % (e.code, e.message))

		nsresponse = NSNitroResponse(response.read())
		if nsresponse.failed:
			raise NSNitroError(nsresponse.message)
        	return nsresponse	

	def disable_service(self, service_name):
		if not self.initialized:
			raise NSNitroError("Not initialized. Call NSNitro.initialize() with ip, user, pass")
		if not self.loggedin:
			raise NSNitroError("Not logged in. Call NSNitro.login()")

		try:
			self.get_service(service_name)
		except NSNitroError, e:
			raise e

        	payload = { "object" : { "params" : { "action" : "disable" }, "service" : { "name" : service_name } } }
		payload_encoded = urllib.urlencode(payload)

		url = self.baseurl + "service/" + service_name

		try:
			req = urllib2.Request(self.baseurl, payload_encoded, self.postheaders)
        		response = urllib2.urlopen(req)

        	except urllib2.HTTPError, e:
                	print "Got reponse code: %s from the server" % e.code
                	raise NSNitroError("Could not disable service: %s, %s" % (e.code, e.message))

		nsresponse = NSNitroResponse(response.read())
		if nsresponse.failed:
			raise NSNitroError(nsresponse.message)
        	return nsresponse	

	def enable_service(self, service_name):
		if not self.initialized:
			raise NSNitroError("Not initialized. Call NSNitro.initialize() with ip, user, pass")
		if not self.loggedin:
			raise NSNitroError("Not logged in. Call NSNitro.login()")

		try:
			self.get_service(service_name)
		except NSNitroError, e:
			raise e

        	payload = { "object" : { "params" : { "action" : "enable" }, "service" : { "name" : service_name } } }
		payload_encoded = urllib.urlencode(payload)

		url = self.baseurl + "service/" + service_name

		try:
			req = urllib2.Request(self.baseurl, payload_encoded, self.postheaders)
        		response = urllib2.urlopen(req)

        	except urllib2.HTTPError, e:
                	print "Got reponse code: %s from the server" % e.code
                	raise NSNitroError("Could not enable service: %s, %s" % (e.code, e.message))

		nsresponse = NSNitroResponse(response.read())
		if nsresponse.failed:
			raise NSNitroError(nsresponse.message)
        	return nsresponse	

class NSNitroResponse:

	jresponse = False
	sresponse = False
	errorcode = -1
	messages = False
	failed = False

	def __init__(self, response):
		self.sresponse = response
		self.jresponse = json.loads(response)
		self.parse_response()


	def get_json_response(self):
		return self.jresponse

	def get_string_response(self):
		return self.sresponse


	def parse_response(self):
		self.errorcode = self.jresponse['errorcode']
		self.message   = self.jresponse['message']
		if self.errorcode != 0:
			self.failed = True
	
	def get_response_field(self, field_name):
		return self.jresponse[field_name]
			
class NSNitroError(Exception):
	def __init__(self, value):
		self.message = value
	def __str__(self):
		return repr(self.message)
