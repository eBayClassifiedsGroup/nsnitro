import json
from nsutil import NSNitroError

class NSBaseResource(object):

        options = {}
        resourcetype = False

        def __init__(self):
                self.options = {}
                self.resourcetype = False
                self.__baseaction = False

        def set_action(self, action):
                self.__baseaction = action

        def set_options(self, options):
                self.options = options

                # Filter out empty options
                self.options = dict([(k,v) for k,v in self.options.items() if (v)])

        def get_payload(self):
                options = dict([(k,v) for k,v in self.options.items() if (v)])
                if self.__baseaction:
                        payload = { "object" : { "params" : { "action" : self.__baseaction }, self.resourcetype : options } }
                else:
                        payload = { "object" : { self.resourcetype : options } }
                #print payload
                return payload

        def get_put_payload(self, sessionid):
                options = dict([(k,v) for k,v in self.options.items() if (v)])
                if self.__baseaction:
                        payload = { "params" : { "action" : self.__baseaction }, self.resourcetype : options }
                else:
                        payload = { "sessionid" : sessionid, self.resourcetype : options }
                #print payload
                return payload

        def perform_operation(self, nitro, action):
                self.set_action(action)
                response = nitro.post(self.get_payload())
                return response

        def get_resource(self, nitro):
                url = nitro.get_url() + self.resourcetype + "/" + self.options['name']
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
                return response        

        def delete_resource(self, nitro):
                url = nitro.get_url() + self.resourcetype + "/" + self.options['name']
                response = nitro.delete(url)

                if response.failed:
                        raise NSNitroError(response.message)

                return response
