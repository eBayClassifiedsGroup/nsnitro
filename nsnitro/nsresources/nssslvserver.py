from nsbaseresource import NSBaseResource
__author__ = 'Aleksandar Topuzovic'


class NSSSLVServer(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSSSLVServer, self).__init__()
        self.options = {'vservername': '',
                        'cipherdetails': '',
                        'cleartextport': '',
                        'dh': '',
                        'dhfile': '',
                        'dhcount': '',
                        'ersa': '',
                        'ersacount': '',
                        'sessreuse': '',
                        'sesstimeout': '',
                        'cipherredirect': '',
                        'crlcheck': '',
                        'cipherurl': '',
                        'sslv2redirect': '',
                        'sslv2url': '',
                        'clientauth': '',
                        'clientcert': '',
                        'sslredirect': '',
                        'redirectportrewrite': '',
                        'nonfipsciphers': '',
                        'ssl2': '',
                        'ssl3': '',
                        'tls1': '',
                        'snienable': '',
                        'service': '',
                        'certkeyname': '',
                        'servicename': '',
                        'ocspcheck': '',
                        'pushenctrigger': ''}

        self.resourcetype = NSSSLVServer.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        """
        Binding object showing the lbmonitor that can be bound to service.
        """
        return "sslvserver"

    # Read/write properties
    def set_vservername(self, vservername):
        """
        The name of the SSL virtual server.
        Minimum length = 1
        """
        self.options['vservername'] = vservername

    def get_vservername(self):
        """
        The name of the SSL virtual server.
        Minimum length = 1
        """
        return self.options['vservername']

    def set_cleartextport(self, cleartextport):
        """
        The port on the back-end web-servers where the clear-text data
        is sent by system. Use this setting for the wildcard IP based
        SSL Acceleration configuration (*:443).
        Minimum value = 1
        """
        self.options['cleartextport'] = cleartextport

    def get_cleartextport(self):
        """
        The port on the back-end web-servers where the clear-text data
        is sent by system. Use this setting for the wildcard IP based
        SSL Acceleration configuration (*:443).
        Minimum value = 1
        """
        return self.options['cleartextport']

    def set_dh(self, dh):
        """
        The state of DH key exchange support for the specified SSL virtual server.
        Default value: DISABLED
        """
        self.options['dh'] = dh

    def get_dh(self):
        """
        The state of DH key exchange support for the specified SSL virtual server.
        Default value: DISABLED
        """
        return self.options['dh']

    def set_dhfile(self, dhfile):
        """
        The file name and path for the DH parameter. The file format is
        PEM. Note: The '-dh' argument must be enabled if this argument
        is specified.
        Minimum length = 1
        """
        self.options['dhfile'] = dhfile

    def get_dhfile(self):
        """
        The file name and path for the DH parameter. The file format is
        PEM. Note: The '-dh' argument must be enabled if this argument
        is specified.
        Minimum length = 1
        """
        return self.options['dhfile']

    def set_dhcount(self, ersa):
        """
        The refresh count for the re-generation of DH public-key and
        private-key from the DH parameter. Zero means infinite usage
        (no refresh). Note: The '-dh' argument must be enabled if this
        argument is specified.
        Default value: 0
        Minimum value = 0
        Maximum value = 65534
        """
        self.options['dhcount'] = ersa

    def get_dhcount(self):
        """
        The refresh count for the re-generation of DH public-key and
        private-key from the DH parameter. Zero means infinite usage
        (no refresh). Note: The '-dh' argument must be enabled if this
        argument is specified.
        Default value: 0
        Minimum value = 0
        Maximum value = 65534
        """
        return self.options['dhcount']

    def set_ersa(self, ersa):
        """
        The state of Ephemeral RSA key exchange support for the SSL
        virtual server.
        Default value: ENABLED
        """
        self.options['ersa'] = ersa

    def get_ersa(self):
        """
        The state of Ephemeral RSA key exchange support for the SSL
        virtual server.
        Default value: ENABLED
        """
        return self.options['ersa']

    def set_ersacount(self, ersacount):
        """
        The refresh count for the re-generation of RSA public-key and
        private-key pair. Zero means infinite usage (no refresh) Note:
        The '-eRSA' argument must be enabled if this argument is
        specified.
        Default value: 0
        Minimum value = 0
        Maximum value = 65534
        """
        self.options['ersacount'] = ersacount

    def get_ersacount(self):
        """
        The refresh count for the re-generation of RSA public-key and
        private-key pair. Zero means infinite usage (no refresh) Note:
        The '-eRSA' argument must be enabled if this argument is
        specified.
        Default value: 0
        Minimum value = 0
        Maximum value = 65534
        """
        return self.options['ersacount']

    def set_sessreuse(self, sessreuse):
        """
        The state of session re-use support for the SSL virtual server.
        Default value: ENABLED
        """
        self.options['sessreuse'] = sessreuse

    def get_sessreuse(self):
        """
        The state of session re-use support for the SSL virtual server.
        Default value: ENABLED
        """
        return self.options['sessreuse']

    def set_sesstimeout(self, sesstimeout):
        """
        The Session timeout value in seconds. The value has to be a
        positive integer. The '-sessReuse' argument must be enabled if
        this argument is specified.
        Default value: 120
        Minimum value = 0
        Maximum value = 0xFFFFFFFE
        """
        self.options['sesstimeout'] = sesstimeout

    def get_sesstimeout(self):
        """
        The Session timeout value in seconds. The value has to be a
        positive integer. The '-sessReuse' argument must be enabled if
        this argument is specified.
        Default value: 120
        Minimum value = 0
        Maximum value = 0xFFFFFFFE
        """
        return self.options['sesstimeout']

    def set_cipherredirect(self, cipherredirect):
        """
        The state of Cipher Redirect feature.
        Default value: DISABLED
        """
        self.options['cipherredirect'] = cipherredirect

    def get_cipherredirect(self):
        """
        The state of Cipher Redirect feature.
        Default value: DISABLED
        """
        return self.options['cipherredirect']

    def set_cipherurl(self, cipherurl):
        """
        The redirect URL to be used with the Cipher Redirect feature.
        """
        self.options['cipherurl'] = cipherurl

    def get_cipherurl(self):
        """
        The redirect URL to be used with the Cipher Redirect feature.
        """
        return self.options['cipherurl']

    def set_sslv2redirect(self, sslv2redirect):
        """
        The state of SSLv2 Redirect feature.
        Default value: DISABLED
        """
        self.options['sslv2redirect'] = sslv2redirect

    def get_sslv2redirect(self):
        """
        The state of SSLv2 Redirect feature.
        Default value: DISABLED
        """
        return self.options['sslv2redirect']

    def set_sslv2url(self, sslv2url):
        """
        The redirect URL to be used with SSLv2 Redirect feature.
        """
        self.options['sslv2url'] = sslv2url

    def get_sslv2url(self):
        """
        The redirect URL to be used with SSLv2 Redirect feature.
        """
        return self.options['sslv2url']

    def set_clientauth(self, clientauth):
        """
        The state of Client-Authentication support for the SSL virtual server.
        Default value: DISABLED
        """
        self.options['clientauth'] = clientauth

    def get_clientauth(self):
        """
        The state of Client-Authentication support for the SSL virtual server.
        Default value: DISABLED
        """
        return self.options['clientauth']

    def set_clientcert(self, clientcert):
        """
        The rule for client authentication. If the clientCert if set to
        Mandatory, the system will terminate the SSL handshake if the
        SSL client does not provide a valid certificate. If the setting
        is Optional, then System will allow SSL clients with no
        certificate or invalid certificates to access the secure
        resource. Note: Make sure proper access control policies are
        defined before changing the above setting to Optional.
        """
        self.options['clientcert'] = clientcert

    def get_clientcert(self):
        """
        The rule for client authentication. If the clientCert if set to
        Mandatory, the system will terminate the SSL handshake if the
        SSL client does not provide a valid certificate. If the setting
        is Optional, then System will allow SSL clients with no
        certificate or invalid certificates to access the secure
        resource. Note: Make sure proper access control policies are
        defined before changing the above setting to Optional.
        """
        return self.options['clientcert']

    def set_sslredirect(self, sslredirect):
        """
        The state of HTTPS redirects for the SSL virtual server. This
        is required for proper working of the redirect messages from
        the web server. The redirect message from the server gives the
        new location for the moved object. This is contained in the
        HTTP header field: Location (for example, Location:
        http://www.moved.org/here.html). For an SSL session, if the
        client browser receives this message, the browser will try to
        connect to the new location. This will break the secure SSL
        session, as the object has moved from a secure site (https://)
        to an unsecured one (http://). Browsers usually flash a warning
        message on the screen and prompt the user to either continue or
        disconnect. When the above feature is enabled, all such http://
        redirect messages are automatically converted to https://. This
        does not break the client SSL session.
        Default value: DISABLED
        """
        self.options['sslredirect'] = sslredirect

    def get_sslredirect(self):
        """
        The state of HTTPS redirects for the SSL virtual server. This
        is required for proper working of the redirect messages from
        the web server. The redirect message from the server gives the
        new location for the moved object. This is contained in the
        HTTP header field: Location (for example, Location:
        http://www.moved.org/here.html). For an SSL session, if the
        client browser receives this message, the browser will try to
        connect to the new location. This will break the secure SSL
        session, as the object has moved from a secure site (https://)
        to an unsecured one (http://). Browsers usually flash a warning
        message on the screen and prompt the user to either continue or
        disconnect. When the above feature is enabled, all such http://
        redirect messages are automatically converted to https://. This
        does not break the client SSL session.
        Default value: DISABLED
        """
        return self.options['sslredirect']

    def set_redirectportrewrite(self, redirectportrewrite):
        """
        The state of port in rewrite while performing HTTPS redirect.
        Default value: DISABLED
        """
        self.options['redirectportrewrite'] = redirectportrewrite

    def get_redirectportrewrite(self):
        """
        The state of port in rewrite while performing HTTPS redirect.
        Default value: DISABLED
        """
        return self.options['redirectportrewrite']

    def set_nonfipsciphers(self, nonfipsciphers):
        """
        The state of usage of non FIPS approved ciphers. Valid only for
        an SSL vserver bound with a FIPS key and certificate.
        Default value: DISABLED
        """
        self.options['nonfipsciphers'] = nonfipsciphers

    def get_nonfipsciphers(self):
        """
        The state of usage of non FIPS approved ciphers. Valid only for
        an SSL vserver bound with a FIPS key and certificate.
        Default value: DISABLED
        """
        return self.options['nonfipsciphers']

    def set_ssl2(self, ssl2):
        """
        The state of SSLv2 protocol support for the SSL virtual server.
        Default value: DISABLED
        """
        self.options['ssl2'] = ssl2

    def get_ssl2(self):
        """
        The state of SSLv2 protocol support for the SSL virtual server.
        Default value: DISABLED
        """
        return self.options['ssl2']

    def set_ssl3(self, ssl3):
        """
        The state of SSLv3 protocol support for the SSL virtual server.
        Default value: ENABLED
        """
        self.options['ssl3'] = ssl3

    def get_ssl3(self):
        """
        The state of SSLv3 protocol support for the SSL virtual server.
        Default value: ENABLED
        """
        return self.options['ssl3']

    def set_tls1(self, tls1):
        """
        The state of TLSv1 protocol support for the SSL virtual server.
        Default value: ENABLED
        """
        self.options['tls1'] = tls1

    def get_tls1(self):
        """
        The state of TLSv1 protocol support for the SSL virtual server.
        Default value: ENABLED
        """
        return self.options['tls1']

    def set_snienable(self, snienable):
        """
        state of SNI feature on virtual server.
        Default value: DISABLED
        """
        self.options['snienable'] = snienable

    def get_snienable(self):
        """
        state of SNI feature on virtual server.
        Default value: DISABLED
        """
        return self.options['snienable']

    def set_pushenctrigger(self, pushenctrigger):
        """
        PUSH packet triggering encryption Always - Any PUSH packet
        triggers encryption Ignore - Ignore PUSH packet for triggering
        encryption Merge - For consecutive sequence of PUSH packets,
        last PUSH packet triggers encryption Timer - PUSH packet
        triggering encryption delayed by timer period defined in 'set
        ssl parameter' .
        """
        self.options['pushenctrigger'] = pushenctrigger

    def get_pushenctrigger(self):
        """
        PUSH packet triggering encryption Always - Any PUSH packet
        triggers encryption Ignore - Ignore PUSH packet for triggering
        encryption Merge - For consecutive sequence of PUSH packets,
        last PUSH packet triggers encryption Timer - PUSH packet
        triggering encryption delayed by timer period defined in 'set
        ssl parameter' .
        """
        return self.options['pushenctrigger']

    def set_cipherdetails(self, cipherdetails):
        """
        Details of the individual ciphers bound to the SSL vserver.
        Select this flag value to display the details of the individual
        ciphers bound to the SSL vserver.
        """
        self.options['cipherdetails'] = cipherdetails

    def get_cipherdetails(self):
        """
        Details of the individual ciphers bound to the SSL vserver.
        Select this flag value to display the details of the individual
        ciphers bound to the SSL vserver.
        """
        return self.options['cipherdetails']

    # Read only properties
    def get_crlcheck(self):
        """
        The state of the CRL check parameter. (Mandatory/Optional)
        """
        return self.options['crlcheck']

    def get_service(self):
        """
        Service
        """
        return self.options['service']

    def get_certkeyname(self):
        """
        The name of the certificate key pair binding.
        """
        return self.options['certkeyname']

    def get_servicename(self):
        """
        Service name.
        """
        return self.options['servicename']

    def get_ocspcheck(self):
        """
        The state of the OCSP check parameter. (Mandatory/Optional)
        """
        return self.options['ocspcheck']

    @staticmethod
    def get(nitro, sslvserver):
        """
        Use this API to fetch sslvserver resource of given name.
        """
        __sslvserver = NSSSLVServer()
        __sslvserver.get_resource(nitro, sslvserver.get_vservername())
        return __sslvserver

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured sslvserver resources.
        """
        __url = nitro.get_url() + NSSSLVServer.get_resourcetype()
        __json_sslvservers = nitro.get(__url).get_response_field(NSSSLVServer.get_resourcetype())
        __sslvservers = []
        for json_sslvserver in __json_sslvservers:
            __sslvservers.append(NSSSLVServer(json_sslvserver))
        return __sslvservers

    @staticmethod
    def update(nitro, sslvserver):
        """
        Use this API to update sslvserver of a given name.
        """
        __sslvserver = NSSSLVServer()
        __sslvserver.set_vservername(sslvserver.get_vservername())
        __sslvserver.set_cleartextport(sslvserver.get_cleartextport())
        __sslvserver.set_dh(sslvserver.get_dh())
        __sslvserver.set_dhfile(sslvserver.get_dhfile())
        __sslvserver.set_dhcount(sslvserver.get_dhcount())
        __sslvserver.set_ersa(sslvserver.get_ersa())
        __sslvserver.set_ersacount(sslvserver.get_ersacount())
        __sslvserver.set_sessreuse(sslvserver.get_sessreuse())
        __sslvserver.set_sesstimeout(sslvserver.get_sesstimeout())
        __sslvserver.set_cipherredirect(sslvserver.get_cipherredirect())
        __sslvserver.set_cipherurl(sslvserver.get_cipherurl())
        __sslvserver.set_sslv2redirect(sslvserver.get_sslv2redirect())
        __sslvserver.set_sslv2url(sslvserver.get_sslv2redirect())
        __sslvserver.set_clientauth(sslvserver.get_clientauth())
        __sslvserver.set_clientcert(sslvserver.get_clientcert())
        __sslvserver.set_sslredirect(sslvserver.get_sslredirect())
        __sslvserver.set_redirectportrewrite(sslvserver.get_redirectportrewrite())
        __sslvserver.set_nonfipsciphers(sslvserver.get_nonfipsciphers())
        __sslvserver.set_ssl2(sslvserver.get_ssl2())
        __sslvserver.set_ssl3(sslvserver.get_ssl3())
        __sslvserver.set_tls1(sslvserver.get_tls1())
        __sslvserver.set_snienable(sslvserver.get_snienable())
        __sslvserver.set_pushenctrigger(sslvserver.get_pushenctrigger())
        return __sslvserver.update_resource(nitro)

    # No unset functionality for now.
