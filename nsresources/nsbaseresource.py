class NSPayloadFormatter:

        __resourcetype = False
        __action = False
        __options = False

        def __init__(self, resourcetype, action, options):
                self.__resourcetype = resourcetype
                self.__action = action
                self.__options = options

        def get_payload(self):
                payload = { "object" : { "params" : { "action" : self.__action }, self.__resourcetype : self.__options } }
                return payload
