from nsbaseresource import NSBaseResource
__author__ = 'Aleksandar Topuzovic'


class NSSSLService(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSSSLService, self).__init__()
        self.options = {'servicename': '',
                        'dh': '',
                        'dhfile': '',
                        'dhcount': '',
                        'ersa': '',
                        'ersacount': '',
                        'sessreuse': '',
                        'sesstimeout': '',
                        'cipherredirect': '',
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
                        'serverauth': '',
                        'pushenctrigger': '',
                        'cipherdetails': '',
                        'crlcheck': '',
                        'certkeyname': '',
                        'cleartextport': '',
                        'ocspcheck': ''}

        self.resourcetype = NSSSLService.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        """
        Binding object showing the lbmonitor that can be bound to service.
        """
        return "sslservice"

    # Read/write properties
    def set_servicename(self, servicename):
        """
        The SSL service name for which the advance configurations are to be
        set.
        Minimum length = 1
        """
        self.options['servicename'] = servicename

    def get_servicename(self):
        """
        The SSL service name for which the advance configurations are to be
        set.
        Minimum length = 1
        """
        return self.options['servicename']

    def set_dh(self, dh):
        """
        The state of Diffie-Hellman (DH) key exchange support for the SSL
        service.
        Default value: DISABLED
        """
        self.options['dh'] = dh

    def get_dh(self):
        """
        The state of Diffie-Hellman (DH) key exchange support for the SSL
        service.
        Default value: DISABLED
        """
        return self.options['dh']

    def set_dhfile(self, dhfile):
        """
        The file name and path for the DH parameter. You need to enable the -dh
        option. File format is PEM. The default input path for the DH file is
        /nsconfig/ssl/.
        Minimum length = 1
        """
        self.options['dhfile'] = dhfile

    def get_dhfile(self):
        """
        The file name and path for the DH parameter. You need to enable the -dh
        option. File format is PEM. The default input path for the DH file is
        /nsconfig/ssl/.
        Minimum length = 1
        """
        return self.options['dhfile']

    def set_dhcount(self, dhcount):
        """
        The refresh count for regeneration of DH public-key and private-key
        from the DH parameter. Zero means infinite usage (no refresh). Option
        '-dh' has to be enabled.
        Default value: 0
        Minimum value = 0
        Maximum value = 65534
        """
        self.options['dhcount'] = dhcount

    def get_dhcount(self):
        """
        The refresh count for regeneration of DH public-key and private-key
        from the DH parameter. Zero means infinite usage (no refresh). Option
        '-dh' has to be enabled.
        Default value: 0
        Minimum value = 0
        Maximum value = 65534
        """
        return self.options['dhcount']

    def set_ersa(self, ersa):
        """
        The state of Ephemeral RSA key exchange support for the SSL service.
        Default value: ENABLED
        """
        self.options['ersa'] = ersa

    def get_ersa(self, ersa):
        """
        The state of Ephemeral RSA key exchange support for the SSL service.
        Default value: ENABLED
        """
        return self.options['ersa']

    def set_ersacount(self, ersacount):
        """
        The refresh count for re-generation of RSA public-key and private-key
        pair. Zero means infinite usage (no refresh). Option '-eRSA' has to be
        enabled.
        Default value: 0
        Minimum value = 0
        Maximum value = 65534
        """
        self.options['ersacount'] = ersacount

    def get_ersacount(self):
        """
        The refresh count for re-generation of RSA public-key and private-key
        pair. Zero means infinite usage (no refresh). Option '-eRSA' has to be
        enabled.
        Default value: 0
        Minimum value = 0
        Maximum value = 65534
        """
        return self.options['ersacount']

    def set_sessreuse(self, sessreuse):
        """
        The state of session reuse support for the SSL service.
        Default value: ENABLED
        """
        self.options['sessreuse'] = sessreuse

    def get_sessreuse(self):
        """
        The state of session reuse support for the SSL service.
        Default value: ENABLED
        """
        return self.options['sessreuse']

    def set_sesstimeout(self, sesstimeout):
        """
        The session timeout value in seconds. The value has to be a positive
        integer. Option '-sessReuse' has to be enabled.
        Default value: 300
        Minimum value = 0
        Maximum value = 0xFFFFFFFE
        """
        self.options['sesstimeout'] = sesstimeout

    def get_sesstimeout(self):
        """
        The session timeout value in seconds. The value has to be a positive
        integer. Option '-sessReuse' has to be enabled.
        Default value: 300
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
        The redirect URL to be used with the SSLv2 Redirect feature.
        """
        self.options['sslv2url'] = sslv2url

    def get_sslv2url(self):
        """
        The redirect URL to be used with the SSLv2 Redirect feature.
        """
        return self.options['sslv2url']

    def set_clientauth(self, clientauth):
        """
        The state of Client-Authentication support for the SSL service.
        Default value: DISABLED
        """
        self.options['clientauth'] = clientauth

    def get_clientauth(self):
        """
        The state of Client-Authentication support for the SSL service.
        Default value: DISABLED
        """
        return self.options['clientauth']

    def set_clientcert(self, clientcert):
        """
        The rule for client authentication. If clientCert is set to Mandatory,
        System will terminate the SSL handshake if SSL client does not provide
        a valid certificate. If the setting is optional, then System will allow
        SSL clients with no certificate or invalid certificates to access the
        secure resource. Note: Make sure proper access control policies are
        defined before changing the above setting to Optional.
        """
        self.options['clientcert'] = clientcert

    def get_clientcert(self):
        """
        The rule for client authentication. If clientCert is set to Mandatory,
        System will terminate the SSL handshake if SSL client does not provide
        a valid certificate. If the setting is optional, then System will allow
        SSL clients with no certificate or invalid certificates to access the
        secure resource. Note: Make sure proper access control policies are
        defined before changing the above setting to Optional.
        """
        return self.options['clientcert']

    def set_sslredirect(self, sslredirect):
        """
        The state of HTTPS redirects for the SSL service. This is required for
        the proper functioning of the redirect messages from the server. The
        redirect message from the server provides the new location for the
        moved object. This is contained in the HTTP header field: Location,
        e.g. Location: http://www.moved.org/here.html For the SSL session, if
        the client browser receives this message, the browser will try to
        connect to the new location. This will break the secure SSL session, as
        the object has moved from a secure site (https://) to an un-secure one
        (http://). Generally browsers flash a warning message on the screen and
        prompt the user, either to continue or disconnect. The above feature,
        when enabled will automatically convert all such http:// redirect
        message to https://. This will not break the client SSL session. Note:
        The set ssl service command can be used for configuring a front-end SSL
        service for service based SSL Off-Loading, or a backend SSL service for
        backend-encryption setup. Some of the command options are not
        applicable while configuring a backend service. System will not report
        an error if these options are used for a backend SSL service. These
        are: [-dh (ENABLED|DISABLED) (-dhFile < file_name >)] [(-dhCount )]
        [-eRSA (ENABLED|DISABLED)] [(-eRSACount )] [-cipherRedirect (ENABLED |
        DISABLED) [-cipherURL ]] [-sslv2Redirect ( ENABLED | DISABLED )
        [-sslv2URL ]] [-clientAuth ( ENABLED | DISABLED ) [-clientCert (
        Mandatory | Optional )]] [-sslRedirect ( ENABLED | DISABLED )] [-ssl2
        (ENABLED|DISABLED)].
        Default value: DISABLED
        """
        self.options['sslredirect'] = sslredirect

    def get_sslredirect(self):
        """
        The state of HTTPS redirects for the SSL service. This is required for
        the proper functioning of the redirect messages from the server. The
        redirect message from the server provides the new location for the
        moved object. This is contained in the HTTP header field: Location,
        e.g. Location: http://www.moved.org/here.html For the SSL session, if
        the client browser receives this message, the browser will try to
        connect to the new location. This will break the secure SSL session, as
        the object has moved from a secure site (https://) to an un-secure one
        (http://). Generally browsers flash a warning message on the screen and
        prompt the user, either to continue or disconnect. The above feature,
        when enabled will automatically convert all such http:// redirect
        message to https://. This will not break the client SSL session. Note:
        The set ssl service command can be used for configuring a front-end SSL
        service for service based SSL Off-Loading, or a backend SSL service for
        backend-encryption setup. Some of the command options are not
        applicable while configuring a backend service. System will not report
        an error if these options are used for a backend SSL service. These
        are: [-dh (ENABLED|DISABLED) (-dhFile < file_name >)] [(-dhCount )]
        [-eRSA (ENABLED|DISABLED)] [(-eRSACount )] [-cipherRedirect (ENABLED |
        DISABLED) [-cipherURL ]] [-sslv2Redirect ( ENABLED | DISABLED )
        [-sslv2URL ]] [-clientAuth ( ENABLED | DISABLED ) [-clientCert (
        Mandatory | Optional )]] [-sslRedirect ( ENABLED | DISABLED )] [-ssl2
        (ENABLED|DISABLED)].
        Default value: DISABLED
        """
        return self.options['sslredirect']

    def set_redirectportrewrite(self, redirectportrewrite):
        """
        The state of the port in rewrite while performing HTTPS redirect.
        Default value: DISABLED
        """
        self.options['redirectportrewrite'] = redirectportrewrite

    def get_redirectportrewrite(self):
        """
        The state of the port in rewrite while performing HTTPS redirect.
        Default value: DISABLED
        """
        return self.options['redirectportrewrite']

    def set_nonfipsciphers(self, nonfipsciphers):
        """
        The state of usage of non FIPS approved ciphers. Valid only for an SSL
        service bound with a FIPS key and certificate.
        Default value: DISABLED
        """
        self.options['nonfipsciphers'] = nonfipsciphers

    def get_nonfipsciphers(self):
        """
        The state of usage of non FIPS approved ciphers. Valid only for an SSL
        service bound with a FIPS key and certificate.
        Default value: DISABLED
        """
        return self.options['nonfipsciphers']

    def set_ssl2(self, ssl2):
        """
        The state of SSLv2 protocol support for the SSL service.
        Default value: DISABLED
        """
        self.options['ssl2'] = ssl2

    def get_ssl2(self):
        """
        The state of SSLv2 protocol support for the SSL service.
        Default value: DISABLED
        """
        return self.options['ssl2']

    def set_ssl3(self, ssl3):
        """
        The state of SSLv3 protocol support for the SSL service.
        Default value: ENABLED
        """
        self.options['ssl3'] = ssl3

    def get_ssl3(self):
        """
        The state of SSLv3 protocol support for the SSL service.
        Default value: ENABLED
        """
        return self.options['ssl3']

    def set_tls1(self, tls1):
        """
        The state of TLSv1 protocol support for the SSL service.
        Default value: ENABLED
        """
        self.options['tls1'] = tls1

    def get_tls1(self):
        """
        The state of TLSv1 protocol support for the SSL service.
        Default value: ENABLED
        """
        return self.options['tls1']

    def set_snienable(self, snienable):
        """
        state of SNI feature on service.
        Default value: DISABLED
        """
        self.options['snienable'] = snienable

    def get_snienable(self):
        """
        state of SNI feature on service.
        Default value: DISABLED
        """
        return self.options['snienable']


    def set_serverauth(self, serverauth):
        """
        The state of Server-Authentication support for the SSL service.
        Default value: DISABLED
        """
        self.options['serverauth'] = serverauth

    def get_serverauth(self):
        """
        The state of Server-Authentication support for the SSL service.
        Default value: DISABLED
        """
        return self.options['serverauth']

    def set_pushenctrigger(self, pushenctrigger):
        """
        PUSH packet triggering encryption Always - Any PUSH packet triggers
        encryption Ignore - Ignore PUSH packet for triggering encryption Merge
        - For consecutive sequence of PUSH packets, last PUSH packet triggers
        encryption Timer - PUSH packet triggering encryption delayed by timer
        period defined in 'set ssl parameter' .
        """
        self.options['pushenctrigger'] = pushenctrigger

    def get_pushenctrigger(self):
        """
        PUSH packet triggering encryption Always - Any PUSH packet triggers
        encryption Ignore - Ignore PUSH packet for triggering encryption Merge
        - For consecutive sequence of PUSH packets, last PUSH packet triggers
        encryption Timer - PUSH packet triggering encryption delayed by timer
        period defined in 'set ssl parameter' .
        """
        return self.options['pushenctrigger']

    def set_cipherdetails(self, cipherdetails):
        """
        Details of the individual ciphers bound to the SSL service. Select this
        flag value to display the details of the individual ciphers bound to
        the SSL service.
        """
        self.options['cipherdetails'] = cipherdetails

    def get_cipherdetails(self):
        """
        Details of the individual ciphers bound to the SSL service. Select this
        flag value to display the details of the individual ciphers bound to
        the SSL service.
        """
        return self.options['cipherdetails']

    # Read only properties
    def get_crlcheck(self):
        """
        The state of the CRL check parameter. (Mandatory/Optional)
        """
        return self.options['crlcheck']

    def get_certkeyname(self):
        """
        The certificate key pair binding.
        """
        return self.options['certkeyname']

    def get_cleartextport(self):
        """
        The clearTextPort settings.
        """
        return self.options['cleartextport']

    def get_ocspcheck(self):
        """
        The state of the OCSP check parameter. (Mandatory/Optional)
        """
        return self.options['ocspcheck']

    @staticmethod
    def get(nitro, sslservice):
        """
        Use this API to fetch sslservice resource of given name.
        """
        __sslservice = NSSSLService()
        __sslservice.get_resource(nitro, sslservice.get_servicename())
        return __sslservice

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured sslservice resources.
        """
        __url = nitro.get_url() + NSSSLService.get_resourcetype()
        __json_sslservices = nitro.get(__url).get_response_field(NSSSLService.get_resourcetype())
        __sslservices = []
        for json_sslservice in __json_sslservices:
            __sslservices.append(NSSSLService(json_sslservice))
        return __sslservices

    @staticmethod
    def update(nitro, sslservice):
        """
        Use this API to update sslservice of a given name.
        """
        __sslservice = NSSSLService()
        __sslservice.set_servicename(sslservice.get_servicename())
        __sslservice.set_dh(sslservice.get_dh())
        __sslservice.set_dhfile(sslservice.get_dhfile())
        __sslservice.set_dhcount(sslservice.get_dhcount())
        __sslservice.set_ersa(sslservice.get_ersa())
        __sslservice.set_ersacount(sslservice.get_ersacount())
        __sslservice.set_sessreuse(sslservice.get_sessreuse())
        __sslservice.set_sesstimeout(sslservice.get_sesstimeout())
        __sslservice.set_cipherredirect(sslservice.get_cipherredirect())
        __sslservice.set_cipherurl(sslservice.get_cipherurl())
        __sslservice.set_sslv2redirect(sslservice.get_sslv2redirect())
        __sslservice.set_sslv2url(sslservice.get_sslv2redirect())
        __sslservice.set_clientauth(sslservice.get_clientauth())
        __sslservice.set_clientcert(sslservice.get_clientcert())
        __sslservice.set_sslredirect(sslservice.get_sslredirect())
        __sslservice.set_redirectportrewrite(sslservice.get_redirectportrewrite())
        __sslservice.set_nonfipsciphers(sslservice.get_nonfipsciphers())
        __sslservice.set_ssl2(sslservice.get_ssl2())
        __sslservice.set_ssl3(sslservice.get_ssl3())
        __sslservice.set_tls1(sslservice.get_tls1())
        __sslservice.set_snienable(sslservice.get_snienable())
        __sslservice.set_serverauth(sslservice.get_serverauth())
        __sslservice.set_pushenctrigger(sslservice.get_pushenctrigger())
        return __sslvservice.update_resource(nitro)