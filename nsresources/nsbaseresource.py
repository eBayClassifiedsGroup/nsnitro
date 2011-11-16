import json

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
                payload = { "object" : { "params" : { "action" : self.__baseaction }, self.resourcetype : options } }
                print payload
                return payload

        def perform_operation(self, nitro, action):
                self.set_action(action)
                response = nitro.post(self.get_payload())
                return response

        def get_resource(self, nitro):
                pass

        def get_resource(self, nitro, service_name):
                url = nitro.get_url() + self.resourcetype + "/" + service_name
                response = nitro.get(url)
                return response
