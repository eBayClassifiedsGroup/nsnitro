from nsbaseresource import NSBaseResource
__author__ = 'Aleksandar Topuzovic'


class NSSSLAction(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSSSLAction, self).__init__()
        self.options = {'name': '',
                        'clientauth': '',
                        'clientcert': '',
                        'certheader': '',
                        'clientcertserialnumber': '',
                        'certserialheader': '',
                        'clientcertsubject': '',
                        'certsubjectheader': '',
                        'clientcerthash': '',
                        'certhashheader': '',
                        'clientcertissuer': '',
                        'certissuerheader': '',
                        'sessionid': '',
                        'sessionidheader': '',
                        'cipher': '',
                        'cipherheader': '',
                        'clientcertnotbefore': '',
                        'certnotbeforeheader': '',
                        'clientcertnotafter': '',
                        'certnotafterheader': '',
                        'owasupport': ''}

        self.resourcetype = NSSSLAction.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        """
        Binding object showing the lbmonitor that can be bound to service.
        """
        return "sslaction"

    # Read/write properties
    def set_name(self, name):
        """
        The name for the new SSL action. Maximum Length: 32.
        Minimum length = 1
        """
        self.options['name'] = name

    def get_name(self):
        """
        The name for the new SSL action. Maximum Length: 32.
        Minimum length = 1
        """
        return self.options['name']

    def set_clientauth(self, clientauth):
        """
        Set action to do client certificate authentication or no
        authentication. DOCLIENTAUTH: Perform client certificate
        authentication. NOCLIENTAUTH: No client certificate authentication.
        """
        self.options['clientauth'] = clientauth

    def get_clientauth(self):
        """
        Set action to do client certificate authentication or no
        authentication. DOCLIENTAUTH: Perform client certificate
        authentication. NOCLIENTAUTH: No client certificate authentication.
        """
        return self.options['clientauth']

    def set_clientcert(self, clientcert):
        """
        The state of insertion of the client certificate in the HTTP header
        when the request is sent to the web-server.
        """
        self.options['clientcert'] = clientcert

    def get_clientcert(self):
        """
        The state of insertion of the client certificate in the HTTP header
        when the request is sent to the web-server.
        """
        return self.options['clientcert']

    def set_certheader(self, certheader):
        """
        The tag name to be used while inserting the client certificate in the
        HTTP header.
        """
        self.options['certheader'] = certheader

    def get_certheader(self):
        """
        The tag name to be used while inserting the client certificate in the
        HTTP header.
        """
        return self.options['certheader']

    def set_clientcertserialnumber(self, clientcertserialnumber):
        """
        The state of insertion of the client certificate's Serial Number in the
        HTTP header when the request is sent to the web-server.
        """
        self.options['clientcertserialnumber'] = clientcertserialnumber

    def get_clientcertserialnumber(self):
        """
        The state of insertion of the client certificate's Serial Number in the
        HTTP header when the request is sent to the web-server.
        """
        return self.options['clientcertserialnumber']

    def set_certserialheader(self, certserialheader):
        """
        The tag name to be used while inserting the client certificate's Serial
        Number in the HTTP header.
        """
        self.options['certserialheader'] = certserialheader

    def get_certserialheader(self):
        """
        The tag name to be used while inserting the client certificate's Serial
        Number in the HTTP header.
        """
        return self.options['certserialheader']

    def set_clientcertsubject(self, clientcertsubject):
        """
        The state of insertion of the client certificate's Subject Name in the
        HTTP header when the request is sent to the web-server.
        """
        self.options['clientcertsubject'] = clientcertsubject

    def get_clientcertsubject(self):
        """
        The state of insertion of the client certificate's Subject Name in the
        HTTP header when the request is sent to the web-server.
        """
        return self.options['clientcertsubject']

    def set_certsubjectheader(self, certsubjectheader):
        """
        The tag name to be used while inserting the client certificate's
        Subject Name in the HTTP header.
        """
        self.options['certsubjectheader'] = certsubjectheader

    def get_certsubjectheader(self):
        """
        The tag name to be used while inserting the client certificate's
        Subject Name in the HTTP header.
        """
        return self.options['certsubjectheader']

    def set_clientcerthash(self, clientcerthash):
        """
        The state of insertion of the client certificate's hash (signature) in
        the HTTP header when the request is sent to the web-server.
        """
        self.options['clientcerthash'] = clientcerthash

    def get_clientcerthash(self):
        """
        The state of insertion of the client certificate's hash (signature) in
        the HTTP header when the request is sent to the web-server.
        """
        return self.options['clientcerthash']

    def set_certhashheader(self, certhashheader):
        """
        The tag name to be used while inserting the client certificate's hash
        (signature) in the HTTP header.
        """
        self.options['certhashheader'] = certhashheader

    def get_certhashheader(self):
        """
        The tag name to be used while inserting the client certificate's hash
        (signature) in the HTTP header.
        """
        return self.options['certhashheader']

    def set_clientcertissuer(self, clientcertissuer):
        """
        The state of insertion of the client certificate's Issuer Name in the
        HTTP header when the request is sent to the web-server.
        """
        self.options['clientcertissuer'] = clientcertissuer

    def get_clientcertissuer(self):
        """
        The state of insertion of the client certificate's Issuer Name in the
        HTTP header when the request is sent to the web-server.
        """
        return self.options['clientcertissuer']

    def set_certissuerheader(self, certissuerheader):
        """
        The tag name to be used while inserting the certificate's Issuer Name
        in the HTTP header.
        """
        self.options['certissuerheader'] = certissuerheader

    def get_certissuerheader(self):
        """
        The tag name to be used while inserting the certificate's Issuer Name
        in the HTTP header.
        """
        return self.options['certissuerheader']

    def set_sessionid(self, sessionid):
        """
        The state of insertion of the Session-ID in the HTTP header when the
        request is sent to the web-server.
        """
        self.options['sessionid'] = sessionid

    def get_sessionid(self):
        """
        The state of insertion of the Session-ID in the HTTP header when the
        request is sent to the web-server.
        """
        return self.options['sessionid']

    def set_sessionidheader(self, sessionidheader):
        """
        The tag name to be used while inserting the Session-ID in the HTTP
        header.
        """
        self.options['sessionidheader'] = sessionidheader

    def get_sessionidheader(self):
        """
        The tag name to be used while inserting the Session-ID in the HTTP
        header.
        """
        return self.options['sessionidheader']

    def set_cipher(self, cipher):
        """
        The state of insertion of the cipher details in the HTTP header when
        the request is sent to the web-server.
        """
        self.options['cipher'] = cipher

    def get_cipher(self):
        """
        The state of insertion of the cipher details in the HTTP header when
        the request is sent to the web-server.
        """
        return self.options['cipher']

    def set_cipherheader(self, cipherheader):
        """
        The tag name to be used while inserting the cipher details in the HTTP
        header.
        """
        self.options['cipherheader'] = cipherheader

    def get_cipherheader(self):
        """
        The tag name to be used while inserting the cipher details in the HTTP
        header.
        """
        return self.options['cipherheader']

    def set_clientcertnotbefore(self, clientcertnotbefore):
        """
        The state of insertion of the client certificate's Not-Before date in
        the HTTP header when the request is sent to the web-server.
        """
        self.options['clientcertnotbefore'] = clientcertnotbefore

    def get_clientcertnotbefore(self):
        """
        The state of insertion of the client certificate's Not-Before date in
        the HTTP header when the request is sent to the web-server.
        """
        return self.options['clientcertnotbefore']

    def set_certnotbeforeheader(self, certnotbeforeheader):
        """
        The tag name to be used while inserting the client certificate's
        Not-Before date in the HTTP header.
        """
        self.options['certnotbeforeheader'] = certnotbeforeheader

    def get_certnotbeforeheader(self):
        """
        The tag name to be used while inserting the client certificate's
        Not-Before date in the HTTP header.
        """
        return self.options['certnotbeforeheader']

    def set_clientcertnotafter(self, clientcertnotafter):
        """
        The state of insertion of the client certificate's Not-After in the
        HTTP header when the request is sent to the web-server.
        """
        self.options['clientcertnotafter'] = clientcertnotafter

    def get_clientcertnotafter(self):
        """
        The state of insertion of the client certificate's Not-After in the
        HTTP header when the request is sent to the web-server.
        """
        return self.options['clientcertnotafter']

    def set_certnotafterheader(self, certnotafterheader):
        """
        The tag name to be used while inserting the client certificate's
        Not-After date in the HTTP header.
        """
        self.options['certnotafterheader'] = certnotafterheader

    def get_certnotafterheader(self):
        """
        The tag name to be used while inserting the client certificate's
        Not-After date in the HTTP header.
        """
        return self.options['certnotafterheader']

    def set_owasupport(self, owasupport):
        """
        The state of Outlook Web-Access support. If the system is in front of
        an Outlook Web Access (OWA) server, a special header field,
        'FRONT-END-HTTPS: ON', needs to be inserted in the HTTP requests going
        to the OWA server. Note: This parameter is required as the SSL requests
        (HTTPS) arrives at the back-end Exchange-2000 server on the configured
        HTTP port (80) instead of arriving at the front-end Exchange 2000
        server.
        """
        self.options['owasupport'] = owasupport

    def get_owasupport(self):
        """
        The state of Outlook Web-Access support. If the system is in front of
        an Outlook Web Access (OWA) server, a special header field,
        'FRONT-END-HTTPS: ON', needs to be inserted in the HTTP requests going
        to the OWA server. Note: This parameter is required as the SSL requests
        (HTTPS) arrives at the back-end Exchange-2000 server on the configured
        HTTP port (80) instead of arriving at the front-end Exchange 2000
        server.
        """
        return self.options['owasupport']

    # Read only properties

    @staticmethod
    def get(nitro, sslaction):
        """
        Use this API to fetch sslaction resource of given name.
        """
        __sslaction = NSSSLAction()
        __sslaction.get_resource(nitro, sslaction.get_name())
        return __sslaction

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured sslpolicy resources.
        """
        __url = nitro.get_url() + NSSSLAction.get_resourcetype()
        __json_sslactions = nitro.get(__url).get_response_field(NSSSLAction.get_resourcetype())
        __sslactions = []
        for json_sslaction in __json_sslactions:
            __sslactions.append(NSSSLAction(json_sslaction))
        return __sslactions

    @staticmethod
    def add(nitro, resource):
        """
        Use this API to add resource.
        """
        __resource = NSSSLAction()
        __resource.set_name(resource.get_name())
        __resource.set_clientauth(resource.get_clientauth())
        __resource.set_clientcert(resource.get_clientcert())
        __resource.set_certheader(resource.get_certheader())
        __resource.set_clientcertserialnumber(resource.get_clientcertserialnumber())
        __resource.set_certserialheader(resource.get_certserialheader())
        __resource.set_clientcertsubject(resource.get_clientcertsubject())
        __resource.set_certsubjectheader(resource.get_certsubjectheader())
        __resource.set_clientcerthash(resource.get_clientcerthash())
        __resource.set_certhashheader(resource.get_certhashheader())
        __resource.set_clientcertissuer(resource.get_clientcertissuer())
        __resource.set_certissuerheader(resource.get_certissuerheader())
        __resource.set_sessionid(resource.get_sessionid())
        __resource.set_sessionidheader(resource.get_sessionidheader())
        __resource.set_cipher(resource.get_cipher())
        __resource.set_cipherheader(resource.get_cipherheader())
        __resource.set_clientcertnotbefore(resource.get_clientcertnotbefore())
        __resource.set_certnotbeforeheader(resource.get_certnotbeforeheader())
        __resource.set_clientcertnotafter(resource.get_clientcertnotafter())
        __resource.set_certnotafterheader(resource.get_certnotafterheader())
        __resource.set_owasupport(resource.get_owasupport())
        return __resource.add_resource(nitro)

    @staticmethod
    def delete(nitro, resource):
        """
        Use this API to delete server of a given name.
        """
        __resource = NSSSLAction()
        __resource.set_name(resource.get_name())
        return __resource.delete_resource(nitro)