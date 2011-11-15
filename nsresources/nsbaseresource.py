class NSBaseResource(object):

        __resourcetype = False
        __action = False
        __options = False

        def set_resource_type(self, resourcetype):
                self.__resourcetype = resourcetype

        def set_action(self, action):
                self.__action = action

        def set_options(self, options):
                self.__options = options

        def get_payload(self):
                payload = { "object" : { "params" : { "action" : self.__action }, self.__resourcetype : self.__options } }
                return payload
