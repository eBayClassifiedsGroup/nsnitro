from nsbaseresource import NSBaseResource

__author__ = 'vlazarenko'


class NSSSLCertKey(NSBaseResource):

    # General Netscaler configuration object

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """

        super(NSSSLCertKey, self).__init__()

        self.options = {'certkey': '',
                        'cert': '',
                        'key': '',
                        'password': '',
                        'fipskey': '',
                        'inform': '',
                        'passplain': '',
                        'expirymonitor': '',
                        'notificationperiod': '',
                        'linkcertkeyname': '',
                        'nodomaincheck': '',
                        'signaturealg': '',
                        'serial': '',
                        'issuer': '',
                        'clientcertnotbefore': '',
                        'clientcertnotafter': '',
                        'daystoexpiration': '',
                        'subject': '',
                        'publickey': '',
                        'publickeysize': '',
                        'version': '',
                        'priority': '',
                        'status': '',
                        'passcrypt': '',
                        'data': '',
                        'servicename': ''}

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options:
                    self.options[key] = json_data[key]

        self.resourcetype = NSSSLCertKey.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        return "sslcertkey"

    def set_certkey(self, certkey):
        self.options['certkey'] = certkey

    def get_certkey(self):
        return self.options['certkey']

    def set_cert(self, cert):
        self.options['cert'] = cert

    def get_cert(self):
        return self.options['cert']

    def set_key(self, key):
        self.options['key'] = key

    def get_key(self):
        return self.options['key']

    def set_password(self, password):
        self.options['password'] = password

    def get_password(self):
        return self.options['password']

    def set_fipskey(self, fipskey):
        self.options['fipskey'] = fipskey

    def get_fipskey(self):
        return self.options['fipskey']

    def set_inform(self, inform):
        self.options['inform'] = inform

    def get_inform(self):
        return self.options['inform']

    def set_passplain(self, passplain):
        self.options['passplain'] = passplain

    def get_passplain(self):
        return self.options['passplain']

    def set_expirymonitor(self, expirymonitor):
        self.options['expirymonitor'] = expirymonitor

    def get_expirymonitor(self):
        return self.options['expirymonitor']

    def set_notificationperiod(self, notificationperiod):
        self.options['notificationperiod'] = notificationperiod

    def get_notificationperiod(self):
        return self.options['notificationperiod']

    def set_linkcertkeyname(self, linkcertkeyname):
        self.options['linkcertkeyname'] = linkcertkeyname

    def get_linkcertkeyname(self):
        return self.options['linkcertkeyname']

    def set_nodomaincheck(self, nodomaincheck):
        self.options['nodomaincheck'] = nodomaincheck

    def get_nodomaincheck(self):
        return self.options['nodomaincheck']

    def set_passcrypt(self, passcrypt):
        self.options['passcrypt'] = passcrypt

    def get_passcrypt(self):
        return self.options['passcrypt']

    def get_signaturealg(self):
        return self.options['signaturealg']

    def get_serial(self):
        return self.options['serial']

    def get_issuer(self):
        return self.options['issuer']

    def get_clientcertnotbefore(self):
        return self.options['clientcertnotbefore']

    def get_clientcertnotafter(self):
        return self.options['clientcertnotafter']

    def get_daystoexpiration(self):
        return self.options['daystoexpiration']

    def get_subject(self):
        return self.options['subject']

    def get_publickey(self):
        return self.options['publickey']

    def get_publickeysize(self):
        return self.options['publickeysize']

    def get_version(self):
        return self.options['version']

    def get_priority(self):
        return self.options['priority']

    def get_status(self):
        return self.options['status']

    def get_data(self):
        return self.options['data']

    def get_servicename(self):
        return self.options['servicename']

    @staticmethod
    def get(nitro, resource):
        """
        Use this API to fetch SSL certkey resource of given name.
        """
        __resource = NSSSLCertKey()
        __resource.get_resource(nitro, resource.get_certkey())
        return __resource

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured SSL certkey resources.
        """
        __url = nitro.get_url() + NSSSLCertKey.get_resourcetype()
        __json_resources = nitro.get(__url).get_response_field(NSSSLCertKey.get_resourcetype())
        __resources = []
        for json_resource in __json_resources:
            __resources.append(NSSSLCertKey(json_resource))
        return __resources

    @staticmethod
    def add(nitro, resource):
        """
        Use this API to add resource.
        """
        __resource = NSSSLCertKey()
        __resource.set_certkey(resource.get_certkey())
        __resource.set_cert(resource.get_cert())
        __resource.set_key(resource.get_key())
        __resource.set_password(resource.get_password())
        __resource.set_fipskey(resource.get_fipskey())
        __resource.set_inform(resource.get_inform())
        __resource.set_passplain(resource.get_passplain())
        __resource.set_passcrypt(resource.get_passcrypt())
        __resource.set_expirymonitor(resource.get_expirymonitor())
        __resource.set_notificationperiod(resource.get_notificationperiod())
        return __resource.add_resource(nitro)

    @staticmethod
    def delete(nitro, resource):
        """
        Use this API to delete server of a given name.
        """
        __resource = NSSSLCertKey()
        __resource.set_certkey(resource.get_certkey())
        nsresponse = __resource.delete_resource(nitro)
        return nsresponse

    @staticmethod
    def update(nitro, resource):
        """
        Use this API to update a server of a given name.
        """
        __resource = NSSSLCertKey()
        __resource.set_certkey(resource.get_certkey())
        __resource.set_expirymonitor(resource.get_expirymonitor())
        __resource.set_notificationperiod(resource.get_notificationperiod())
        return __resource.update_resource(nitro)

    @staticmethod
    def link(nitro, resource):
        """
        Use this API to link resource of a given name
        """
        __resource = NSSSLCertKey()
        __resource.set_certkey(resource.get_certkey())
        __resource.set_linkcertkeyname(resource.get_linkcertkeyname())
        nsresponse = __resource.perform_operation(nitro, "link")
        return nsresponse

    @staticmethod
    def unlink(nitro, resource):
        """
        Use this API to link resource of a given name
        """
        __resource = NSSSLCertKey()
        __resource.set_certkey(resource.get_certkey())
        nsresponse = __resource.perform_operation(nitro, "unlink")
        return nsresponse
