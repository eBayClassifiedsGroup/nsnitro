from nsbaseresource import NSBaseResource
__author__ = 'Aleksandar Topuzovic'


class NSSSLCertKeySSLVServerBinding(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSSSLCertKeySSLVServerBinding, self).__init__()
        self.options = {'vserver': '',
                        'crlcheck': '',
                        'ca': '',
                        'vservername': '',
                        'servername': '',
                        'certkey': '',
                        'version': '',
                        'data': ''}

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options:
                    self.options[key] = json_data[key]

        self.resourcetype = NSSSLCertKeySSLVServerBinding.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        return "sslcertkey_sslvserver_binding"

    # Read/write properties
    def set_vserver(self, vserver):
        """
        Specify this option to bind the certificate to an SSL virtual
        server. Note: The default option is -vServer.
        """
        self.options['vserver'] = vserver

    def get_vserver(self):
        """
        Specify this option to bind the certificate to an SSL virtual
        server. Note: The default option is -vServer.
        """
        return self.options['vserver']

    def set_crlcheck(self, crlcheck):
        """
        The rule for use of CRL corresponding to this CA certificate
        during client authentication. If crlCheck is set to Mandatory,
        the system will deny all SSL clients if the CRL is missing,
        expired - NextUpdate date is in the past, or is incomplete with
        remote CRL refresh enabled. If crlCheck is set to optional, the
        system will allow SSL clients in the above error cases.However,
        in any case if the client certificate is revoked in the CRL,
        the SSL client will be denied access.
        Default value: CRLCHECK_OPTIONAL
        """
        self.options['crlcheck'] = crlcheck

    def get_crlcheck(self):
        """
        The rule for use of CRL corresponding to this CA certificate
        during client authentication. If crlCheck is set to Mandatory,
        the system will deny all SSL clients if the CRL is missing,
        expired - NextUpdate date is in the past, or is incomplete with
        remote CRL refresh enabled. If crlCheck is set to optional, the
        system will allow SSL clients in the above error cases.However,
        in any case if the client certificate is revoked in the CRL,
        the SSL client will be denied access.
        Default value: CRLCHECK_OPTIONAL
        """
        return self.options['crlcheck']

    def set_ca(self, ca):
        """
        If this option is specified, it indicates that the
        certificate-key pair being bound to the SSL virtual server is a
        CA certificate. If this option is not specified, the
        certificate-key pair is bound as a normal server certificate.
        Note: In case of a normal server certificate, the
        certificate-key pair should consist of both the certificate and
        the private-key.
        """
        self.options['ca'] = ca

    def get_ca(self):
        """
        If this option is specified, it indicates that the
        certificate-key pair being bound to the SSL virtual server is a
        CA certificate. If this option is not specified, the
        certificate-key pair is bound as a normal server certificate.
        Note: In case of a normal server certificate, the
        certificate-key pair should consist of both the certificate and
        the private-key.
        """
        return self.options['ca']

    def set_vservername(self, vservername):
        """
        The name of the SSL virtual server name to which the
        certificate-key pair needs to be bound.
        Minimum length = 1
        """
        self.options['vservername'] = vservername

    def get_vservername(self):
        """
        The name of the SSL virtual server name to which the
        certificate-key pair needs to be bound.
        Minimum length = 1
        """
        return self.options['vservername']

    def set_servername(self, servername):
        """
        Vserver name to which the certificate key pair is bound.
        """
        self.options['servername'] = servername

    def get_servername(self):
        """
        Vserver name to which the certificate key pair is bound.
        """
        return self.options['servername']

    def set_certkey(self, certkey):
        """
        The object name for the certificate-key pair.
        Minimum length = 1
        """
        self.options['certkey'] = certkey

    def get_certkey(self):
        """
        The object name for the certificate-key pair.
        Minimum length = 1
        """
        return self.options['certkey']

    # Read only properties
    def get_version(self):
        """
        Version.
        """
        return self.options['version']

    def get_data(self):
        """
        Vserver Id.
        """
        return self.options['data']

    @staticmethod
    def get(nitro, sslcertkey):
        """
        Use this API to fetch configured sslcertkey_sslvserver_binding resources of a given name.
        """
        __url = nitro.get_url() + NSSSLCertKeySSLVServerBinding.get_resourcetype() + "/" + sslcertkey.get_certkey()
        __json_bindings = nitro.get(__url).get_response_field(NSSSLCertKeySSLVServerBinding.get_resourcetype())
        __bindings = []
        for json_binding in __json_bindings:
            __bindings.append(NSSSLCertKeySSLVServerBinding(json_binding))
        return __bindings
