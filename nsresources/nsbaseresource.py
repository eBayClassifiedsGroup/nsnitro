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
                payload = { "object" : { "params" : { "action" : self.__baseaction }, self.__baseresourcetype : self.__baseoptions } }
                return payload
