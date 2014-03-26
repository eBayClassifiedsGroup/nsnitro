from nsbaseresource import NSBaseResource


class NSAcls(NSBaseResource):

    def __init__(self):

        super(NSAcls, self).__init__()

        self.options = {}
        self.resourcetype = NSAcls.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        return "nsacls"

    @staticmethod
    def renumber(nitro):
        """
        Use this API to renumber nsacls.
        """
        __nsacls = NSAcls()
        return __nsacls.perform_operation(nitro, "renumber")

    @staticmethod
    def clear(nitro):
        """
        Use this API to clear nsacls.
        """
        __nsacls = NSAcls()
        return __nsacls.perform_operation(nitro, "clear")

    @staticmethod
    def apply(nitro):
        """
        Use this API to apply nsacls.
        """
        __nsacls = NSAcls()
        return __nsacls.perform_operation(nitro, "apply")
