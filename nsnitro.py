""" Citrix Netscaler Nitro API accessor """

import urllib, urllib2
import json
from nsutil import *
from nsresources.nsservice import NSService

__version__ = "0.0.2"

class NSNitro:
        """ Main class """

        __ip      = "1.2.3.4"
        __user  = "api_user"
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
                if not self.__ready:
                        raise NSNitroError("Not initialized or not logged in.")

                return self.__sessionid

        def login(self):
                """ Logins to the LB using the credentials give to constructor """
                if not self.__initialized:
                        raise NSNitroError("Not initialized.")

                payload = {"object":{"login":{"username":self.__user,"password":self.__password}}}
                try:
                        nsresponse = self.__post(payload)
                        if nsresponse.failed:
                                raise NSNitroError(nsresponse.message)

                        self.__sessionid = nsresponse.get_response_field('sessionid')
                        self.__postheaders = {'Cookie' : 'sessionid='+self.__sessionid, 'Content-type' : self.__contenttype}
                        self.__loggedin = True
                        return True

                except SyntaxError:
                        raise NSNitroError("Could not parse LB response.")
                except urllib2.URLError, ue:
                        raise NSNitroError("Error logging in!" + ue.message)


        def rename_lbvserver(self, vserver_name, vserver_new_name):
                """ Renames vserver vserver_name to vserver_new_name"""
                if not self.__ready:
                        raise NSNitroError("Not initialized or not logged in.")

                try:
                        self.get_lbvserver(vserver_name)
                except NSNitroError, e:
                        raise e

                payload = { "object" : { "params" : { "action" : "rename" }, "lbvserver" : { "name" : vserver_name, "newname" : vserver_new_name } } }

                nsresponse = self.__post(payload)
                return nsresponse

        def enable_lbvserver(self, vserver_name):
                """ Enables vserver vserver_name """
                if not self.__ready:
                        raise NSNitroError("Not initialized or not logged in.")

                try:
                        self.get_lbvserver(vserver_name)
                except NSNitroError, e:
                        raise e

                payload = { "object" : { "params" : { "action" : "enable" }, "lbvserver" : { "name" : vserver_name } } }
                nsresponse = self.__post(payload)
                return nsresponse

        def disable_lbvserver(self, vserver_name):
                """ Disables vserver vserver_name """
                if not self.__ready:
                        raise NSNitroError("Not initialized or not logged in.")

                try:
                        self.get_lbvserver(vserver_name)
                except NSNitroError, e:
                        raise e

                payload = { "object" : { "params" : { "action" : "disable" }, "lbvserver" : { "name" : vserver_name } } }
                nsresponse = self.__post(payload)
                return nsresponse

        def bind_service_to_lbvserver(self, vserver_name, service_name, weight):
                """ Bind service service_name to lb vserver vserver_name """
                if not self.__ready:
                        raise NSNitroError("Not initialized or not logged in.")

                try:
                        self.get_lbvserver(vserver_name)
                        self.get_service(service_name)
                except NSNitroError, e:
                        raise e

                payload = { "object" : { "lbvserver_service_binding" : { "servicename" : service_name, "weight" : weight, "name" : vserver_name } } }
                nsresponse = self.__put(self, payload)
                return nsresponse

        def get_lbvserver(self, vserver_name):
                """ Gets vserver details matching vserver_name """
                if not self.__ready:
                        raise NSNitroError("Not initialized or not logged in.")

                url = self.__baseurl + "lbvserver/" + vserver_name

                nsresponse = self.get(url)
                return nsresponse


        def get_service(self, service_name):
                """ Gets service details matching service_name """
                if not self.__ready:
                        raise NSNitroError("Not initialized or not logged in.")

                url = self.__baseurl + "service/" + service_name

                nsresponse = self.get(url)
                return nsresponse

        def get_server(self, server_name):
                """ Gets server details matching server_name """
                if not self.__ready:
                        raise NSNitroError("Not initialized or not logged in.")

                url = self.__baseurl + "server/" + server_name

                nsresponse = self.get(url)
                return nsresponse

        def disable_server(self, server_name):
                """ Disables server server_name """
                if not self.__ready:
                        raise NSNitroError("Not initialized or not logged in.")

                try:
                        self.get_server(server_name)
                except NSNitroError, e:
                        raise e

                payload = { "object" : { "params" : { "action" : "disable" }, "server" : { "name" : server_name } } }
                nsresponse = self.__post(payload)
                return nsresponse

        def enable_server(self, server_name):
                """ Enables server server_name """
                if not self.__ready:
                        raise NSNitroError("Not initialized or not logged in.")

                try:
                        self.get_server(server_name)
                except NSNitroError, e:
                        raise e

                payload = { "object" : { "params" : { "action" : "enable" }, "server" : { "name" : server_name } } }

                nsresponse = self.__post(payload)
                return nsresponse


        def disable_service(self, service_name):
                """ Disables service service_name """
                if not self.__ready:
                        raise NSNitroError("Not initialized or not logged in.")

                try:
                        self.get_service(service_name)
                except NSNitroError, e:
                        raise e

                payload = { "object" : { "params" : { "action" : "disable" }, "service" : { "name" : service_name } } }
                nsresponse = self.__post(payload)
                return nsresponse

        def enable_service(self, service_name):
                """ Enables service service_name """
                if not self.__ready:
                        raise NSNitroError("Not initialized or not logged in.")

                try:
                        self.get_service(service_name)
                except NSNitroError, e:
                        raise e

                payload = { "object" : { "params" : { "action" : "enable" }, "service" : { "name" : service_name } } }

                nsresponse = self.__post(payload)
                return nsresponse

        def rename_service(self, service_name, service_new_name):
                """ Renames service service_name to service_new_name """
                if not self.__ready:
                        raise NSNitroError("Not initialized or not logged in.")

                try:
                        self.get_service(service_name)
                except NSNitroError, e:
                        raise e

                payload = { "object" : { "params" : { "action" : "rename" }, "service" : { "name" : service_name, "newname" : service_new_name } } }

                nsresponse = self.__post(payload)
                return nsresponse

        def __post(self, payload):
                try:
                        payload_encoded = urllib.urlencode(payload)
                        req = urllib2.Request(self.__baseurl, payload_encoded, self.__postheaders)
                        response = urllib2.urlopen(req)

                except urllib2.HTTPError, e:
                        raise NSNitroError("Could not send post request: %s, %s" % (e.code, e.message))

                nsresponse = NSNitroResponse(response.read())
                if nsresponse.failed:
                        raise NSNitroError(nsresponse.message)
                return nsresponse

        def post(self, payload):
                try:
                        payload_encoded = urllib.urlencode(payload)
                        req = urllib2.Request(self.__baseurl, payload_encoded, self.__postheaders)
                        response = urllib2.urlopen(req)

                except urllib2.HTTPError, e:
                        raise NSNitroError("Could not send post request: %s, %s" % (e.code, e.message))

                nsresponse = NSNitroResponse(response.read())
                if nsresponse.failed:
                        raise NSNitroError(nsresponse.message)
                return nsresponse

        def __put(self, payload):
                try:
                        payload_encoded = urllib.urlencode(payload)
                        req = urllib2.Request(self.__baseurl, payload_encoded, self.__postheaders)
                        req.get_method = lambda: 'PUT'
                        response = urllib2.urlopen(req)

                except urllib2.HTTPError, e:
                        raise NSNitroError("Could not send post request: %s, %s" % (e.code, e.message))

                nsresponse = NSNitroResponse(response.read())
                if nsresponse.failed:
                        raise NSNitroError(nsresponse.message)
                return nsresponse

        def get(self, url):
                try:
                        opener = urllib2.build_opener()
                        opener.addheaders.append(('Cookie', 'sessionid='+self.__sessionid))
                        response = opener.open(url)

                except urllib2.HTTPError, e:
                        print "Got reponse code: %s from the server" % e.code
                        raise NSNitroError("Could not get resource: %s, %s" % (e.code, e.message))

                nsresponse = NSNitroResponse(response.read())
                if nsresponse.failed:
                        raise NSNitroError(nsresponse.message)

                return nsresponse

        def delete(self, url):
                try:
                        opener = urllib2.build_opener()
                        req = urllib2.Request(url)
                        req.add_header('Cookie', 'sessionid='+self.__sessionid)
                        req.get_method = lambda: 'DELETE'
                        response = urllib2.urlopen(req)

                except urllib2.HTTPError, e:
                        raise NSNitroError("Could not send delete request: %s, %s" % (e.code, e.message))

                nsresponse = NSNitroResponse(response.read())
                if nsresponse.failed:
                        raise NSNitroError(nsresponse.message)
                return nsresponse



        def __ready(self):
                if not self.__initialized or not self.__loggedin:
                        return False
                else:
                        return True

