""" Citrix Netscaler Nitro API accessor """

import urllib
import urllib2
from nsutil import *
from nsexceptions import *

__version__ = "0.0.2"


class NSNitro:

    """ Main class """

    __ip = "1.2.3.4"
    __user = "api_user"
    __password = "api_user"
    __baseurl = "http://1.2.3.4/nitro/v1/config/"
    __sessionid = ""
    __loggedin = False
    __initialized = False
    __contenttype = "application/x-www-form-urlencoded"
    __postheaders = {
        'Cookie': 'sessionid=' + __sessionid,
        'Content-type': __contenttype}

    def __init__(self, ip, user, password, useSSL=False):
        """ Constructor: ip - LB ip, user - LB username, pass - LB password """
        self.__ip = ip
        self.__user = user
        self.__password = password
        self.__baseurl = "%s://%s/nitro/v1/config/" % (
            'https' if useSSL else 'http', ip)
        self.__initialized = True

    def get_url(self):
        """ Returns base url for nitro API. Mostly useful for debugging """
        if not self.__initialized:
            raise NSNitroError("Not initialized.")
        return self.__baseurl

    def get_sessionid(self):
        """ Returns sessionID that LB gave us after logging in """
        if not self.__initialized or not self.__loggedin:
            raise NSNitroError("Not initialized or not logged in.")

        return self.__sessionid

    def login(self):
        """ Logins to the LB using the credentials give to constructor """
        if not self.__initialized:
            raise NSNitroError("Not initialized.")

        payload = {"object": json.dumps(
            {"login": {"username": self.__user, "password": self.__password}})}
        try:
            nsresponse = self.post(payload)
            self.__sessionid = nsresponse.get_response_field('sessionid')
            self.__postheaders = {
                'Cookie': 'sessionid=' + self.__sessionid,
                'Content-type': self.__contenttype,
                'Set-Cookie': 'NITRO_AUTH_TOKEN={0}'.format(self.__sessionid)}
            self.__loggedin = True
            return nsresponse.get_json_response()
        except SyntaxError:
            raise NSNitroError("Could not parse LB response.")
        except urllib2.URLError, ue:
            raise NSNitroError("Error logging in!" + str(ue))

    def post(self, payload):
        try:
            payload_encoded = urllib.urlencode(payload)
            req = urllib2.Request(
                self.__baseurl, payload_encoded, self.__postheaders)
            response = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            try:
                NSNitroResponse(e.read())
            except AttributeError:
                raise NSNitroError(
                    "Could not send post request: %s, %s" % (e.code, e.reason))
        return NSNitroResponse(response.read())

    def put(self, payload):
        try:
            opener = urllib2.build_opener(urllib2.HTTPHandler)
            request = urllib2.Request(self.__baseurl, json.dumps(payload))
            request.add_header('Cookie', 'sessionid=' + self.__sessionid)
            request.get_method = lambda: 'PUT'
            response = opener.open(request)
        except urllib2.HTTPError, e:
            try:
                NSNitroResponse(e.read())
            except AttributeError:
                raise NSNitroError(
                    "Could not send put request: %s, %s" % (e.code, e.reason))
        return NSNitroResponse(response.read())

    def get(self, url):
        try:
            opener = urllib2.build_opener()
            opener.addheaders.append(
                ('Cookie', 'sessionid=' + self.__sessionid))
            response = opener.open(url)
        except urllib2.HTTPError, e:
            try:
                NSNitroResponse(e.read())
            except AttributeError:
                raise NSNitroError(
                    "Could not get resource: %s, %s" % (e.code, e.reason))
        return NSNitroResponse(response.read())

    def delete(self, url):
        try:
            req = urllib2.Request(url)
            req.add_header('Cookie', 'sessionid=' + self.__sessionid)
            req.get_method = lambda: 'DELETE'
            response = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            try:
                NSNitroResponse(e.read())
            except AttributeError:
                raise NSNitroError(
                    "Could not send delete request: %s, %s" % (e.code, e.reason))

        return NSNitroResponse(response.read())

    def logout(self):
        payload = {
            "object": json.dumps(
                {"logout": {}, }
            )
        }
        try:
            nsresponse = self.post(payload)

            del self.__sessionid
            return nsresponse.get_json_response()

        except NSNitroError, nsresponse:
            raise NSNitroError(nsresponse.message)
