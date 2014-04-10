__author__ = 'vllazarenko'

from nsbaseresource import NSBaseResource


class NSFeature(NSBaseResource):

    # Configuration for NS Features.

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSFeature, self).__init__()
        self.options = {'feature': '',
                        'reqfeature': '',
                        'wl': '',
                        'sp': '',
                        'lb': '',
                        'cs': '',
                        'cr': '',
                        'sc': '',
                        'cmp': '',
                        'pq': '',
                        'ssl': '',
                        'gslb': '',
                        'hdosp': '',
                        'cf': '',
                        'ic': '',
                        'sslvpn': '',
                        'aaa': '',
                        'ospf': '',
                        'rip': '',
                        'bgp': '',
                        'rewrite': '',
                        'ipv6pt': '',
                        'appfw': '',
                        'responder': '',
                        'htmlinjection': '',
                        'push': ''}

        self.resourcetype = NSFeature.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "nsfeature"

    def set_feature(self, feature):
        self.options['feature'] = feature

    def get_feature(self):
        return self.options['feature']

    def get_reqfeature(self):
        return self.options['reqfeature']

    def get_wl(self):
        return self.options['wl']

    def get_sp(self):
        return self.options['sp']

    def get_lb(self):
        return self.options['lb']

    def get_cs(self):
        return self.options['cs']

    def get_cr(self):
        return self.options['cr']

    def get_sc(self):
        return self.options['sc']

    def get_cmp(self):
        return self.options['cmp']

    def get_pq(self):
        return self.options['pq']

    def get_ssl(self):
        return self.options['ssl']

    def get_gslb(self):
        return self.options['gslb']

    def get_hdosp(self):
        return self.options['hdosp']

    def get_cf(self):
        return self.options['cf']

    def get_ic(self):
        return self.options['ic']

    def get_sslvpn(self):
        return self.options['sslvpn']

    def get_aaa(self):
        return self.options['aaa']

    def get_ospf(self):
        return self.options['ospf']

    def get_rip(self):
        return self.options['rip']

    def get_bgp(self):
        return self.options['bgp']

    def get_rewrite(self):
        return self.options['rewrite']

    def get_ipv6pt(self):
        return self.options['ipv6pt']

    def get_appfw(self):
        return self.options['appfw']

    def get_responder(self):
        return self.options['responder']

    def get_htmlinjection(self):
        return self.options['htmlinjection']

    def get_push(self):
        return self.options['push']

    # Operations methods
    @staticmethod
    def disable(nitro, resource):
        """
        Use this API to disable server.
        """
        __resource = NSFeature()
        __resource.set_feature(resource.get_feature())
        return __resource.perform_operation(nitro, "disable")

    @staticmethod
    def enable(nitro, resource):
        """
        Use this API to enable server.
        """
        __resource = NSFeature()
        __resource.set_feature(resource.get_feature())
        return __resource.perform_operation(nitro, "enable")
