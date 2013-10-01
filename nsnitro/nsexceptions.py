from collections import defaultdict

class NSNitroError(Exception):
    """ Custom exception class """
    def __init__(self, value, code=0):
        self.message = value
        self.code = code

    def __str__(self):
        return repr(self.message)

class NSNitroRetryableException(Exception):
    """ Operations that can be retried """
    pass

class NSNitroNoSuchResource(NSNitroError):
    """ No such resource """
    pass

class NSNitroResourceAlreadyExists(NSNitroError):
    """ Resource already exists """
    pass

class NSNitroOperationInProgress(NSNitroError, NSNitroRetryableException):
    """ Operation in progress """
    pass

class NSNitroInvalidUsernameOrPassword(NSNitroError):
    """ Invalid username or password """
    pass

class NSNitroRequiredArgumentMissing(NSNitroError):
    """ Required argument missing """
    pass

class NSNitroVServerMismatch(NSNitroError):
    """ Vserver type mismatch. """
    pass

NSNitroExceptionsMap = defaultdict(lambda: NSNitroError)
NSNitroKnownExceptions = {
    258:  NSNitroNoSuchResource,             # NSERR_NOENT
    273:  NSNitroResourceAlreadyExists,      # NSERR_EXIST
    292:  NSNitroOperationInProgress,        # NSERR_INPROGRESS
    293:  NSNitroOperationInProgress,        # NSERR_ALREADY
    344:  NSNitroNoSuchResource,             # NSERR_NOSERVICE
    351:  NSNitroNoSuchResource,             # NSERR_NOSERVER
    354:  NSNitroInvalidUsernameOrPassword,  # NSERR_NOUSER
    355:  NSNitroInvalidUsernameOrPassword,  # NSERR_INVALPASSWD
    471:  NSNitroVServerMismatch,            # NSERR_VSERVER_TYPE_MISMATCH
    1095: NSNitroRequiredArgumentMissing,    # NSERR_ARGMISSING
}

NSNitroExceptionsMap.update(NSNitroKnownExceptions)
