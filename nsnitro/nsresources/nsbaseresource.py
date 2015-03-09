from nsnitro.nsutil import NSNitroError
import urllib
import json


class NSBaseResource(object):

    options = {}
    resourcetype = False

    def __init__(self):
        self.options = {}
        self.resourcetype = False
        self.__baseaction = False

    def __str__(self):
        ret = ""
        for key, value in self.options.items():
            ret += "\t%s: \t\t%s\n" % (key, value)

        return ret

    def set_action(self, action):
        self.__baseaction = action

    def set_options(self, options):
        self.options = options

        # Filter out empty options
        self.options = dict([(k, v) for k, v in self.options.items() if v != ''])

    def get_payload(self):
        options = dict([(k, v) for k, v in self.options.items() if v != ''])
        if self.__baseaction:
            payload = {"object": json.dumps({"params": {"action": self.__baseaction}, self.resourcetype: options})}
        else:
            payload = {"object": json.dumps({self.resourcetype: options})}
        # print payload
        return payload

    def get_put_payload(self, sessionid):
        options = dict([(k, v) for k, v in self.options.items() if v != ''])
        if self.__baseaction:
            payload = {"params": {"action": self.__baseaction}, self.resourcetype: options}
        else:
            payload = {"sessionid": sessionid, self.resourcetype: options}
        # print payload
        return payload

    def get_delete_args(self):
        options = dict([(k, v) for k, v in self.options.items() if v != ''])

        args = "?args="

        for key, value in options.iteritems():
            args = "%s%s:%s%s" % (args, key, urllib.quote_plus(value) if type(value) is str else value, ",")

        args = args[:-1]  # remove last comma

        return args

    def perform_operation(self, nitro, action):
        self.set_action(action)
        response = nitro.post(self.get_payload())
        return response

    def get_resource(self, nitro, object_name=None):
        url = "%s%s/%s" % (nitro.get_url(),
                           self.resourcetype,
                           object_name if object_name else self.options['name'])
        response = nitro.get(url)

        if response.failed:
            raise NSNitroError(response.message)

        for resource in response.get_response_field(self.resourcetype):
            for k in resource.iterkeys():
                self.options[k] = resource[k]

    def add_resource(self, nitro):
        response = nitro.post(self.get_payload())
        return response

    def update_resource(self, nitro):
        response = nitro.put(self.get_put_payload(nitro.get_sessionid()))
        if response.failed:
            raise NSNitroError(response.message)
        return response

    def delete_resource(self, nitro, object_name=None):
        url = "%s%s" % (nitro.get_url(), self.resourcetype)

        if object_name is not None:
            url += "/%s" % object_name
        elif 'name' in self.options and self.options['name'] is not None:
            url += "/%s" % self.options['name']

        urlargs = self.get_delete_args()
        url += urlargs

        response = nitro.delete(url)

        if response.failed:
            raise NSNitroError(response.message)

        return response
