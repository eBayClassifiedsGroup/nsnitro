from nsbaseresource import NSBaseResource

__author__ = 'vlazarenko'


class NSRewriteAction(NSBaseResource):

    # Configuration for content-switching rewrite action resource.

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSRewriteAction, self).__init__()

        self.options = {
            'name': '',
            'type': '',
            'target': '',
            'stringbuilderexpr': '',
            'pattern': '',
            'search': '',
            'allow_unsafe_pi': '',
            'refinesearch': '',
            'comment': '',
            'allow_unsafe_pi1': '',
            'newname': '',
            'hits': '',
            'undefhits': '',
            'referencecount': '',
            'description': '',
        }

        self.resourcetype = NSRewriteAction.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "rewriteaction"

    def set_name(self, name):
        self.options['name'] = name

    def get_name(self):
        return self.options['name']

    def set_type(self, type):
        self.options['type'] = type

    def get_type(self):
        return self.options['type']

    def set_target(self, target):
        self.options['target'] = target

    def get_target(self):
        return self.options['target']

    def set_stringbuilderexpr(self, stringbuilderexpr):
        self.options['stringbuilderexpr'] = stringbuilderexpr

    def get_stringbuilderexpr(self):
        return self.options['stringbuilderexpr']

    def set_pattern(self, pattern):
        self.options['pattern'] = pattern

    def get_pattern(self):
        return self.options['pattern']

    def set_search(self, search):
        self.options['search'] = search

    def get_search(self):
        return self.options['search']

    def set_allow_unsafe_pi(self, allow_unsafe_pi):
        self.options['allow_unsafe_pi'] = allow_unsafe_pi

    def get_allow_unsafe_pi(self):
        return self.options['allow_unsafe_pi']

    def set_refinesearch(self, refinesearch):
        self.options['refinesearch'] = refinesearch

    def get_refinesearch(self):
        return self.options['refinesearch']

    def set_comment(self, comment):
        self.options['comment'] = comment

    def get_comment(self):
        return self.options['comment']

    def set_allow_unsafe_pi1(self, allow_unsafe_pi1):
        self.options['allow_unsafe_pi1'] = allow_unsafe_pi1

    def get_allow_unsafe_pi1(self):
        return self.options['allow_unsafe_pi1']

    def set_newname(self, newname):
        self.options['newname'] = newname

    def get_newname(self):
        return self.options['newname']

    def get_hits(self):
        return self.options['hits']

    def get_undefhits(self):
        return self.options['undefhits']

    def get_referencecount(self):
        return self.options['referencecount']

    def get_description(self):
        return self.options['description']

    # Operations methods
    @staticmethod
    def get(nitro, rewriteaction):
        """
        Use this API to fetch rewriteaction resource of given name.
        """
        __rewriteaction = NSRewriteAction()
        __rewriteaction.set_name(rewriteaction.get_name())
        __rewriteaction.get_resource(nitro)
        return __rewriteaction

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured rewriteaction resources.
        """
        __url = nitro.get_url() + NSRewriteAction.get_resourcetype()
        __json_cspolicies = nitro.get(__url).get_response_field(NSRewriteAction.get_resourcetype())
        __rewritepolicies = []
        for json_rewriteaction in __json_cspolicies:
            __rewritepolicies.append(NSRewriteAction(json_rewriteaction))
        return __rewritepolicies

    @staticmethod
    def add(nitro, rewriteaction):
        """
        Use this API to add rewriteaction.
        """
        __rewriteaction = NSRewriteAction()
        __rewriteaction.set_name(rewriteaction.get_name())
        __rewriteaction.set_type(rewriteaction.get_type())
        __rewriteaction.set_target(rewriteaction.get_target())
        __rewriteaction.set_stringbuilderexpr(rewriteaction.get_stringbuilderexpr())
        __rewriteaction.set_pattern(rewriteaction.get_pattern())
        __rewriteaction.set_search(rewriteaction.get_search())
        __rewriteaction.set_allow_unsafe_pi(rewriteaction.get_allow_unsafe_pi())
        __rewriteaction.set_refinesearch(rewriteaction.get_refinesearch())
        __rewriteaction.set_comment(rewriteaction.get_comment())

        return __rewriteaction.add_resource(nitro)

    @staticmethod
    def delete(nitro, rewriteaction):
        """
        Use this API to delete rewriteaction of a given name.
        """
        __rewriteaction = NSRewriteAction()
        __rewriteaction.set_name(rewriteaction.get_name())
        nsresponse = __rewriteaction.delete_resource(nitro)
        return nsresponse

    @staticmethod
    def update(nitro, rewriteaction):
        """
        Use this API to update a rewriteaction of a given name.
        """
        __rewriteaction = NSRewriteAction()
        __rewriteaction.set_name(rewriteaction.get_name())
        __rewriteaction.set_target(rewriteaction.get_target())
        __rewriteaction.set_stringbuilderexpr(rewriteaction.get_stringbuilderexpr())
        __rewriteaction.set_pattern(rewriteaction.get_pattern())
        __rewriteaction.set_search(rewriteaction.get_search())
        __rewriteaction.set_allow_unsafe_pi(rewriteaction.get_allow_unsafe_pi())
        __rewriteaction.set_allow_unsafe_pi1(rewriteaction.get_allow_unsafe_pi1())
        __rewriteaction.set_refinesearch(rewriteaction.get_refinesearch())
        __rewriteaction.set_comment(rewriteaction.get_comment())
        return __rewriteaction.update_resource(nitro)

    # No unset functionality for now.
    @staticmethod
    def rename(nitro, rewriteaction):
        """
        Use this API to rename rewriteaction.
        """
        __rewriteaction = NSRewriteAction()
        __rewriteaction.set_name(rewriteaction.get_name())
        __rewriteaction.set_newname(rewriteaction.get_newname())
        return __rewriteaction.perform_operation(nitro, "rename")
