""" Citrix Netscaler Nitro API accessor """

import urllib, urllib2
import json

__version__ = "0.0.1"
__all__ = [ 'NSNitro', 'NSNitroError', 'NSNitroResponse' ]

class NSNitro:
	""" Main class """

        __ip          = "1.2.3.4"
        __user        = "api_user"
        __password    = "api_user"
        __baseurl     = "http://1.2.3.4/nitro/v1/config/"
	__sessionid   = ""
	__loggedin    = False
        __initialized = False
	__contenttype = "application/x-www-form-urlencoded"
	__postheaders = {'Cookie' : 'sessionid='+__sessionid, 'Content-type' : __contenttype}

        def __init__(self, ip, user, password):
		""" Contructor: ip - LB ip, user - LB username, pass - LB password """
                self.__ip = ip
                self.__user = user
                self.__password = password
                self.__baseurl = "http://%s/nitro/v1/config/" % ip
                self.__initialized = True

        def get_url(self):
		""" Returns base url for nitro API. Mostly useful for debugging """
                if not self.__initialized:
                        raise NSNitroError("Not initialized.")
                return self.__baseurl        

	def get_sessionid(self):
		""" Returns sessionID that LB gave us after logging in """
		if not self.__initialized:
			raise NSNitroError("Not initialized.")
		if not self.__loggedin:
			raise NSNitroError("Not logged in. Call NSNitro.login()")

		return self.__sessionid

        def login(self):
		""" Logins to the LB using the credentials give to constructor """
		if not self.__initialized:
			raise NSNitroError("Not initialized.")

                payload = {"object":{"login":{"username":"api_user","password":"api_user"}}}
                payload_encoded = urllib.urlencode(payload)

        	try:
                	req = urllib2.Request(self.__baseurl, payload_encoded, { 'Content-Type': self.__contenttype } )
                	response = urllib2.urlopen(req)
                	de_content = eval(response.read())

                	self.__sessionid = de_content['sessionid']
			self.__postheaders = {'Cookie' : 'sessionid='+self.__sessionid, 'Content-type' : self.__contenttype}
                	self.__loggedin = True
			return True

        	except urllib2.HTTPError, e:
                	print "Got reponse code: %s from the server" % e.code
                	raise NSNitroError("Could not login: %s, %s" % (e.code, e.message))


	def rename_lbvserver(self, vserver_name, vserver_new_name):
		""" Renames vserver vserver_name to vserver_new_name"""
		if not self.__initialized:
			raise NSNitroError("Not initialized.")
		if not self.__loggedin:
			raise NSNitroError("Not logged in. Call NSNitro.login()")

		try:
			self.get_lbvserver(vserver_name)
		except NSNitroError, e:
			raise e

        	payload = { "object" : { "params" : { "action" : "rename" }, "lbvserver" : { "name" : vserver_name, "newname" : vserver_new_name } } }
		payload_encoded = urllib.urlencode(payload)

		try:
			req = urllib2.Request(self.__baseurl, payload_encoded, self.__postheaders)
        		response = urllib2.urlopen(req)

        	except urllib2.HTTPError, e:
                	print "Got reponse code: %s from the server" % e.code
                	raise NSNitroError("Could not enable vserver: %s, %s" % (e.code, e.message))

		nsresponse = NSNitroResponse(response.read())
		if nsresponse.failed:
			raise NSNitroError(nsresponse.message)
        	return nsresponse	

	def enable_lbvserver(self, vserver_name):
		""" Enables vserver vserver_name """
		if not self.__initialized:
			raise NSNitroError("Not initialized.")
		if not self.__loggedin:
			raise NSNitroError("Not logged in. Call NSNitro.login()")

		try:
			self.get_lbvserver(vserver_name)
		except NSNitroError, e:
			raise e

        	payload = { "object" : { "params" : { "action" : "enable" }, "lbvserver" : { "name" : vserver_name } } }
		payload_encoded = urllib.urlencode(payload)

		try:
			req = urllib2.Request(self.__baseurl, payload_encoded, self.__postheaders)
        		response = urllib2.urlopen(req)

        	except urllib2.HTTPError, e:
                	print "Got reponse code: %s from the server" % e.code
                	raise NSNitroError("Could not enable vserver: %s, %s" % (e.code, e.message))

		nsresponse = NSNitroResponse(response.read())
		if nsresponse.failed:
			raise NSNitroError(nsresponse.message)
        	return nsresponse	

	def disable_lbvserver(self, vserver_name):
		""" Disables vserver vserver_name """
		if not self.__initialized:
			raise NSNitroError("Not initialized.")
		if not self.__loggedin:
			raise NSNitroError("Not logged in. Call NSNitro.login()")

		try:
			self.get_lbvserver(vserver_name)
		except NSNitroError, e:
			raise e

        	payload = { "object" : { "params" : { "action" : "disable" }, "lbvserver" : { "name" : vserver_name } } }
		payload_encoded = urllib.urlencode(payload)

		try:
			req = urllib2.Request(self.__baseurl, payload_encoded, self.__postheaders)
        		response = urllib2.urlopen(req)

        	except urllib2.HTTPError, e:
                	print "Got reponse code: %s from the server" % e.code
                	raise NSNitroError("Could not disable vserver: %s, %s" % (e.code, e.message))

		nsresponse = NSNitroResponse(response.read())
		if nsresponse.failed:
			raise NSNitroError(nsresponse.message)
        	return nsresponse	

	def bind_service_to_lbvserver(self, vserver_name, service_name, weight):
		""" Bind service service_name to lb vserver vserver_name """
		if not self.__initialized:
			raise NSNitroError("Not initialized.")
		if not self.__loggedin:
			raise NSNitroError("Not logged in. Call NSNitro.login()")

		try:
			self.get_lbvserver(vserver_name)
			self.get_service(service_name)
		except NSNitroError, e:
			raise e

        	payload = { "object" : { "lbvserver_service_binding" : { "servicename" : service_name, "weight" : weight, "name" : vserver_name } } }
		payload_encoded = urllib.urlencode(payload)

		try:
			req = urllib2.Request(self.__baseurl, payload_encoded, self.__postheaders)
        		response = urllib2.urlopen(req)

        	except urllib2.HTTPError, e:
                	print "Got reponse code: %s from the server" % e.code
                	raise NSNitroError("Could not enable vserver: %s, %s" % (e.code, e.message))

		nsresponse = NSNitroResponse(response.read())
		if nsresponse.failed:
			raise NSNitroError(nsresponse.message)
        	return nsresponse	

	def get_lbvserver(self, vserver_name):
		""" Gets vserver details matching vserver_name """
		if not self.__initialized:
			raise NSNitroError("Not initialized.")
		if not self.__loggedin:
			raise NSNitroError("Not logged in. Call NSNitro.login()")

		url = self.__baseurl + "lbvserver/" + vserver_name

		try:
			opener = urllib2.build_opener()
			opener.addheaders.append(('Cookie', 'sessionid='+self.__sessionid))
			response = opener.open(url)

        	except urllib2.HTTPError, e:
                	print "Got reponse code: %s from the server" % e.code
                	raise NSNitroError("Could not get vserver: %s, %s" % (e.code, e.message))

		nsresponse = NSNitroResponse(response.read())
		if nsresponse.failed:
			raise NSNitroError(nsresponse.message)
        	return nsresponse	


	def get_service(self, service_name):
		""" Gets service details matching service_name """
		if not self.__initialized:
			raise NSNitroError("Not initialized.")
		if not self.__loggedin:
			raise NSNitroError("Not logged in. Call NSNitro.login()")

		url = self.__baseurl + "service/" + service_name

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

	def disable_service(self, service_name):
		""" Disables service service_name """
		if not self.__initialized:
			raise NSNitroError("Not initialized.")
		if not self.__loggedin:
			raise NSNitroError("Not logged in. Call NSNitro.login()")

		try:
			self.get_service(service_name)
		except NSNitroError, e:
			raise e

        	payload = { "object" : { "params" : { "action" : "disable" }, "service" : { "name" : service_name } } }
		payload_encoded = urllib.urlencode(payload)

		try:
			req = urllib2.Request(self.__baseurl, payload_encoded, self.__postheaders)
        		response = urllib2.urlopen(req)

        	except urllib2.HTTPError, e:
                	print "Got reponse code: %s from the server" % e.code
                	raise NSNitroError("Could not disable service: %s, %s" % (e.code, e.message))

		nsresponse = NSNitroResponse(response.read())
		if nsresponse.failed:
			raise NSNitroError(nsresponse.message)
        	return nsresponse	

	def enable_service(self, service_name):
		""" Enables service service_name """
		if not self.__initialized:
			raise NSNitroError("Not initialized.")
		if not self.__loggedin:
			raise NSNitroError("Not logged in. Call NSNitro.login()")

		try:
			self.get_service(service_name)
		except NSNitroError, e:
			raise e

        	payload = { "object" : { "params" : { "action" : "enable" }, "service" : { "name" : service_name } } }
		payload_encoded = urllib.urlencode(payload)

		try:
			req = urllib2.Request(self.__baseurl, payload_encoded, self.__postheaders)
        		response = urllib2.urlopen(req)

        	except urllib2.HTTPError, e:
                	print "Got reponse code: %s from the server" % e.code
                	raise NSNitroError("Could not enable service: %s, %s" % (e.code, e.message))

		nsresponse = NSNitroResponse(response.read())
		if nsresponse.failed:
			raise NSNitroError(nsresponse.message)
        	return nsresponse	

	def rename_service(self, service_name, service_new_name):
		""" Renames service service_name to service_new_name """
		if not self.__initialized:
			raise NSNitroError("Not initialized.")
		if not self.__loggedin:
			raise NSNitroError("Not logged in. Call NSNitro.login()")

		try:
			self.get_service(service_name)
		except NSNitroError, e:
			raise e

        	payload = { "object" : { "params" : { "action" : "rename" }, "service" : { "name" : service_name, "newname" : service_new_name } } }
		payload_encoded = urllib.urlencode(payload)

		try:
			req = urllib2.Request(self.__baseurl, payload_encoded, self.__postheaders)
        		response = urllib2.urlopen(req)

        	except urllib2.HTTPError, e:
                	print "Got reponse code: %s from the server" % e.code
                	raise NSNitroError("Could not enable vserver: %s, %s" % (e.code, e.message))

		nsresponse = NSNitroResponse(response.read())
		if nsresponse.failed:
			raise NSNitroError(nsresponse.message)
        	return nsresponse	

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
		return self.jresponse[field_name]
			
class NSNitroError(Exception):
	""" Custom exception class """
	def __init__(self, value):
		self.message = value
	def __str__(self):
		return repr(self.message)
