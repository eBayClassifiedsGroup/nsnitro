from nsbaseresource import NSBaseResource
__author__ = 'ndenev'


class NSPbrs(NSBaseResource):

    def __init__(self):

        super(NSPbrs, self).__init__()

        self.options = {}
        self.resourcetype = NSPbrs.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        return "nspbrs"

    @staticmethod
    def renumber(nitro):
        """
        Use this API to renumber nspbrs.
        """
        __nsprbs = NSPbrs()
        return __nsprbs.perform_operation(nitro, "renumber")

    @staticmethod
    def clear(nitro):
        """
        Use this API to clear nspbrs.
        """
        __nspbrs = NSPbrs()
        return __nspbrs.perform_operation(nitro, "clear")

    @staticmethod
    def apply(nitro):
        """
        Use this API to apply nspbrs.
        """
        __nspbrs = NSPbrs()
        return __nspbrs.perform_operation(nitro, "apply")
