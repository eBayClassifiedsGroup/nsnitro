import json
from nsexceptions import *


class NSNitroResponse:

    """
    Generic class for accessing LB response dictionary.
    Can provide string response back and a parsed dictionary
    """
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
        self.message = self.__jresponse['message']
        if self.errorcode != 0:
            self._raise_exception()
            self.failed = True

    def get_response_field(self, field_name):
        """ Returns field_name of parsed JSON dictionary """
        if field_name in self.__jresponse:
            return self.__jresponse[field_name]
        else:
            return []

    def _raise_exception(self):
        """
            Lookup specific exception based on errorcode in response,
            if that fails raises NSNitroError.
        """
        exception_class = NSNitroExceptionClassMap[self.errorcode]
        raise exception_class(self.message, self.errorcode)
