import json

class NSBaseResource(object):

        def __init__(self):
                self.__baseresourcetype = False
                self.__baseaction = False
                self.__baseoptions = False

        def set_resource_type(self, resourcetype):
                self.__baseresourcetype = resourcetype

        def get_resource_type(self):
                return self.__baseresourcetype

        def set_action(self, action):
                self.__baseaction = action

        def set_options(self, options):
                self.__baseoptions = options

                # Filter out empty options
                self.__baseoptions = dict([(k,v) for k,v in self.__baseoptions.items() if (v)])

        def get_payload(self):
                options = dict([(k,v) for k,v in self.__baseoptions.items() if (v)])
                payload = { "object" : { "params" : { "action" : self.__baseaction }, self.__baseresourcetype : options } }
                return payload

        def perform_operation(self, nitro, action):
                self.set_action(action)
                response = nitro.post(self.get_payload())
                return response

        def get_resource(self, nitro):
                pass

        def get_resource(self, nitro, service_name):
                url = nitro.get_url() + self.get_resource_type() + "/" + service_name
                response = nitro.get(url)
                return response
