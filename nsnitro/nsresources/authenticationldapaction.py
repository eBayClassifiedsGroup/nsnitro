from nsbaseresource import NSBaseResource

__author__ = 'md2k@md2k.net'


class AuthLdapAction(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(AuthLdapAction, self).__init__()

        self.options = {'name': '',
                        'serverip': '',
                        'servername': '',
                        'serverport': '',
                        'authtimeout': '',
                        'ldapbase': '',
                        'ldapbinddn': '',
                        'ldapbinddnpassword': '',
                        'ldaploginname': '',
                        'searchfilter': '',
                        'groupattrname': '',
                        'subattributename': '',
                        'sectype': '',
                        'svrtype': '',
                        'ssonameattribute': '',
                        'authentication': '',
                        'requireuser': '',
                        'passwdchange': '',
                        'nestedgroupextraction': '',
                        'maxnestinglevel': '',
                        'followreferrals': '',
                        'maxldapreferrals': '',
                        'validateservercert': '',
                        'ldaphostname': '',
                        'groupnameidentifier': '',
                        'groupsearchattribute': '',
                        'groupsearchsubattribute': '',
                        'groupsearchfilter': '',
                        'defaultauthenticationgroup': '',
                        'attribute1': '',
                        'attribute2': '',
                        'attribute3': '',
                        'attribute4': '',
                        'attribute5': '',
                        'attribute6': '',
                        'attribute7': '',
                        'attribute8': '',
                        'attribute9': '',
                        'attribute10': '',
                        'attribute11': '',
                        'attribute12': '',
                        'attribute13': '',
                        'attribute14': '',
                        'attribute15': '',
                        'attribute16': '',
                        'success': '',
                        'failure': ''}

        self.resourcetype = AuthLdapAction.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "authenticationldapaction"

    def set_name(self, name):
        """Name for the new LDAP action.
        Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the LDAP action is added.
        The following requirement applies only to the NetScaler CLI:
        If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication action" or 'my authentication action').<br/>Minimum length =  1.
        """
        self.options["name"] = name

    def get_name(self):
        """Name for the new LDAP action.
        Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the LDAP action is added.
        The following requirement applies only to the NetScaler CLI:
        If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication action" or 'my authentication action').<br/>Minimum length =  1.
        """
        return self.options["name"]

    def set_serverip(self, serverip):
        """IP address assigned to the LDAP server.<br/>Minimum length =  1.
        """
        self.options["serverip"] = serverip

    def get_serverip(self):
        """IP address assigned to the LDAP server.<br/>Minimum length =  1.
        """
        return self.options["serverip"]

    def set_servername(self, servername):
        """LDAP server name as a FQDN.  Mutually exclusive with LDAP IP address.<br/>Minimum length =  1.
        """
        self.options["servername"] = servername

    def get_servername(self):
        """LDAP server name as a FQDN.  Mutually exclusive with LDAP IP address.<br/>Minimum length =  1.
        """
        return self.options["servername"]

    def set_serverport(self, serverport):
        """Port on which the LDAP server accepts connections.<br/>Default value: 389<br/>Minimum length =  1.
        """
        self.options["serverport"] = serverport

    def get_serverport(self):
        """Port on which the LDAP server accepts connections.<br/>Default value: 389<br/>Minimum length =  1.
        """
        return self.options["serverport"]

    def set_authtimeout(self, authtimeout):
        """Number of seconds the NetScaler appliance waits for a response from the RADIUS server.<br/>Default value: 3<br/>Minimum length =  1.
        """
        self.options["authtimeout"] = authtimeout

    def get_authtimeout(self):
        """Number of seconds the NetScaler appliance waits for a response from the RADIUS server.<br/>Default value: 3<br/>Minimum length =  1.
        """
        return self.options["authtimeout"]

    def set_ldapbase(self, ldapbase):
        """Base (node) from which to start LDAP searches.
        If the LDAP server is running locally, the default value of base is dc=netscaler, dc=com.
        """
        self.options["ldapbase"] = ldapbase

    def get_ldapbase(self):
        """Base (node) from which to start LDAP searches.
        If the LDAP server is running locally, the default value of base is dc=netscaler, dc=com.
        """
        return self.options["ldapbase"]

    def set_ldapbinddn(self, ldapbinddn):
        """Full distinguished name (DN) that is used to bind to the LDAP server.
        Default: cn=Manager,dc=netscaler,dc=com.
        """
        self.options["ldapbinddn"] = ldapbinddn

    def get_ldapbinddn(self):
        """Full distinguished name (DN) that is used to bind to the LDAP server.
        Default: cn=Manager,dc=netscaler,dc=com.
        """
        return self.options["ldapbinddn"]

    def set_ldapbinddnpassword(self, ldapbinddnpassword):
        """Password used to bind to the LDAP server.<br/>Minimum length =  1.
        """
        self.options["ldapbinddnpassword"] = ldapbinddnpassword

    def get_ldapbinddnpassword(self):
        """Password used to bind to the LDAP server.<br/>Minimum length =  1.
        """
        return self.options["ldapbinddnpassword"]

    def set_ldaploginname(self, ldaploginname):
        """LDAP login name attribute.
        The NetScaler appliance uses the LDAP login name to query external LDAP servers or Active Directories.
        """
        self.options["ldaploginname"] = ldaploginname

    def get_ldaploginname(self):
        """LDAP login name attribute.
        The NetScaler appliance uses the LDAP login name to query external LDAP servers or Active Directories.
        """
        return self.options["ldaploginname"]

    def set_searchfilter(self, searchfilter):
        """String to be combined with the default LDAP user search string to form the search value.
        For example, if the search filter ""vpnallowed=true"" is combined with the LDAP login name ""samaccount"" and the user-supplied username is ""bob"",
        the result is the LDAP search string ""(&(vpnallowed=true)(samaccount=bob)"" (Be sure to enclose the search string in two sets of double quotation marks;
        both sets are needed.).<br/>Minimum length =  1.
        """
        self.options["searchfilter"] = searchfilter

    def get_searchfilter(self):
        """String to be combined with the default LDAP user search string to form the search value.
        For example, if the search filter ""vpnallowed=true"" is combined with the LDAP login name ""samaccount"" and the user-supplied username is ""bob"",
        the result is the LDAP search string ""(&(vpnallowed=true)(samaccount=bob)"" (Be sure to enclose the search string in two sets of double quotation marks;
        both sets are needed.).<br/>Minimum length =  1.
        """
        return self.options["searchfilter"]

    def set_groupattrname(self, groupattrname):
        """LDAP group attribute name.
        Used for group extraction on the LDAP server.
        """
        self.options["groupattrname"] = groupattrname

    def get_groupattrname(self):
        """LDAP group attribute name.
        Used for group extraction on the LDAP server.
        """
        return self.options["groupattrname"]

    def set_subattributename(self, subattributename):
        """LDAP group sub-attribute name.
        Used for group extraction from the LDAP server.
        """
        self.options["subattributename"] = subattributename

    def get_subattributename(self):
        """LDAP group sub-attribute name.
        Used for group extraction from the LDAP server.
        """
        return self.options["subattributename"]

    def set_sectype(self, sectype):
        """Type of security used for communications between the NetScaler appliance and the LDAP server. For the PLAINTEXT setting, no encryption is required.<br/>Default value: PLAINTEXT<br/>Possible values = PLAINTEXT, TLS, SSL.
        """
        self.options["sectype"] = sectype

    def get_sectype(self):
        """Type of security used for communications between the NetScaler appliance and the LDAP server. For the PLAINTEXT setting, no encryption is required.<br/>Default value: PLAINTEXT<br/>Possible values = PLAINTEXT, TLS, SSL.
        """
        return self.options["sectype"]

    def set_svrtype(self, svrtype):
        """The type of LDAP server.<br/>Default value: AAA_LDAP_SERVER_TYPE_DEFAULT<br/>Possible values = AD, NDS.
        """
        self.options["svrtype"] = svrtype

    def get_svrtype(self):
        """The type of LDAP server.<br/>Default value: AAA_LDAP_SERVER_TYPE_DEFAULT<br/>Possible values = AD, NDS.
        """
        return self.options["svrtype"]

    def set_ssonameattribute(self, ssonameattribute):
        """LDAP single signon (SSO) attribute.
        The NetScaler appliance uses the SSO name attribute to query external LDAP servers or Active Directories for an alternate username.
        """
        self.options["ssonameattribute"] = ssonameattribute

    def get_ssonameattribute(self):
        """LDAP single signon (SSO) attribute.
        The NetScaler appliance uses the SSO name attribute to query external LDAP servers or Active Directories for an alternate username.
        """
        return self.options["ssonameattribute"]

    def set_authentication(self, authentication):
        """Perform LDAP authentication.
        If authentication is disabled, any LDAP authentication attempt returns authentication success if the user is found.
        CAUTION! Authentication should be disabled only for authorization group extraction or where other (non-LDAP) authentication methods are in use and either bound to a primary list or flagged as secondary.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
        """
        self.options["authentication"] = authentication

    def get_authentication(self):
        """Perform LDAP authentication.
        If authentication is disabled, any LDAP authentication attempt returns authentication success if the user is found.
        CAUTION! Authentication should be disabled only for authorization group extraction or where other (non-LDAP) authentication methods are in use and either bound to a primary list or flagged as secondary.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
        """
        return self.options["authentication"]

    def set_requireuser(self, requireuser):
        """Require a successful user search for authentication.<br/>Default value: YES<br/>Possible values = YES, NO.
        """
        self.options["requireuser"] = requireuser

    def get_requireuser(self):
        """Require a successful user search for authentication.<br/>Default value: YES<br/>Possible values = YES, NO.
        """
        return self.options["requireuser"]

    def set_passwdchange(self, passwdchange):
        """Allow password change requests.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
        """
        self.options["passwdchange"] = passwdchange

    def get_passwdchange(self):
        """Allow password change requests.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
        """
        return self.options["passwdchange"]

    def set_nestedgroupextraction(self, nestedgroupextraction):
        """Allow nested group extraction, in which the NetScaler appliance queries external LDAP servers to determine whether a group is part of another group.<br/>Default value: OFF<br/>Possible values = ON, OFF.
        """
        self.options["nestedgroupextraction"] = nestedgroupextraction

    def get_nestedgroupextraction(self):
        """Allow nested group extraction, in which the NetScaler appliance queries external LDAP servers to determine whether a group is part of another group.<br/>Default value: OFF<br/>Possible values = ON, OFF.
        """
        return self.options["nestedgroupextraction"]

    def set_maxnestinglevel(self, maxnestinglevel):
        """If nested group extraction is ON, specifies the number of levels up to which group extraction is performed.<br/>Default value: 2<br/>Minimum length =  2.
        """
        self.options["maxnestinglevel"] = maxnestinglevel

    def get_maxnestinglevel(self):
        """If nested group extraction is ON, specifies the number of levels up to which group extraction is performed.<br/>Default value: 2<br/>Minimum length =  2.
        """
        return self.options["maxnestinglevel"]

    def set_followreferrals(self, followreferrals):
        """Setting this option to ON enables following LDAP referrals received from the LDAP server.<br/>Default value: OFF<br/>Possible values = ON, OFF.
        """
        self.options["followreferrals"] = followreferrals

    def get_followreferrals(self):
        """Setting this option to ON enables following LDAP referrals received from the LDAP server.<br/>Default value: OFF<br/>Possible values = ON, OFF.
        """
        return self.options["followreferrals"]

    def set_maxldapreferrals(self, maxldapreferrals):
        """Specifies the maximum number of nested referrals to follow.<br/>Default value: 1<br/>Minimum length =  1.
        """
        self.options["maxldapreferrals"] = maxldapreferrals

    def get_maxldapreferrals(self):
        """Specifies the maximum number of nested referrals to follow.<br/>Default value: 1<br/>Minimum length =  1.
        """
        return self.options["maxldapreferrals"]

    def set_validateservercert(self, validateservercert):
        """When to validate LDAP server certs.<br/>Default value: NO<br/>Possible values = YES, NO.
        """
        self.options["validateservercert"] = validateservercert

    def get_validateservercert(self):
        """When to validate LDAP server certs.<br/>Default value: NO<br/>Possible values = YES, NO.
        """
        return self.options["validateservercert"]

    def set_ldaphostname(self, ldaphostname):
        """Hostname for the LDAP server.  If -validateServerCert is ON then this must be the host name on the certificate from the LDAP server.
        A hostname mismatch will cause a connection failure.
        """
        self.options["ldaphostname"] = ldaphostname

    def get_ldaphostname(self):
        """Hostname for the LDAP server.  If -validateServerCert is ON then this must be the host name on the certificate from the LDAP server.
        A hostname mismatch will cause a connection failure.
        """
        return self.options["ldaphostname"]

    def set_groupnameidentifier(self, groupnameidentifier):
        """Name that uniquely identifies a group in LDAP or Active Directory.
        """
        self.options["groupnameidentifier"] = groupnameidentifier

    def get_groupnameidentifier(self):
        """Name that uniquely identifies a group in LDAP or Active Directory.
        """
        return self.options["groupnameidentifier"]

    def set_groupsearchattribute(self, groupsearchattribute):
        """LDAP group search attribute.
        Used to determine to which groups a group belongs.
        """
        self.options["groupsearchattribute"] = groupsearchattribute

    def get_groupsearchattribute(self):
        """LDAP group search attribute.
        Used to determine to which groups a group belongs.
        """
        return self.options["groupsearchattribute"]

    def set_groupsearchsubattribute(self, groupsearchsubattribute):
        """LDAP group search subattribute.
        Used to determine to which groups a group belongs.
        """
        self.options["groupsearchsubattribute"] = groupsearchsubattribute

    def get_groupsearchsubattribute(self):
        """LDAP group search subattribute.
        Used to determine to which groups a group belongs.
        """
        return self.options["groupsearchsubattribute"]

    def set_groupsearchfilter(self, groupsearchfilter):
        """String to be combined with the default LDAP group search string to form the search value.
        For example, the group search filter ""vpnallowed=true"" when combined with the group identifier ""samaccount"" and the group name ""g1"" yields
        the LDAP search string ""(&(vpnallowed=true)(samaccount=g1)"". (Be sure to enclose the search string in two sets of double quotation marks; both sets are needed.).
        """
        self.options["groupsearchfilter"] = groupsearchfilter

    def get_groupsearchfilter(self):
        """String to be combined with the default LDAP group search string to form the search value.
        For example, the group search filter ""vpnallowed=true"" when combined with the group identifier ""samaccount"" and the group name ""g1"" yields
        the LDAP search string ""(&(vpnallowed=true)(samaccount=g1)"". (Be sure to enclose the search string in two sets of double quotation marks; both sets are needed.).
        """
        return self.options["groupsearchfilter"]

    def set_defaultauthenticationgroup(self, defaultauthenticationgroup):
        """This is the default group that is chosen when the authentication succeeds in addition to extracted groups.<br/>Maximum length =  64.
        """
        self.options["defaultauthenticationgroup"] = defaultauthenticationgroup

    def get_defaultauthenticationgroup(self):
        """This is the default group that is chosen when the authentication succeeds in addition to extracted groups.<br/>Maximum length =  64.
        """
        return self.options["defaultauthenticationgroup"]

    def set_attribute1(self, attribute1):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        self.options["attribute1"] = attribute1

    def get_attribute1(self):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        return self.options["attribute1"]

    def set_attribute2(self, attribute2):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        self.options["attribute2"] = attribute2

    def get_attribute2(self):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        return self.options["attribute2"]

    def set_attribute3(self, attribute3):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        self.options["attribute3"] = attribute3

    def get_attribute3(self):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        return self.options["attribute3"]

    def set_attribute4(self, attribute4):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        self.options["attribute4"] = attribute4

    def get_attribute4(self):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        return self.options["attribute4"]

    def set_attribute5(self, attribute5):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        self.options["attribute5"] = attribute5

    def get_attribute5(self):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        return self.options["attribute5"]

    def set_attribute6(self, attribute6):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        self.options["attribute6"] = attribute6

    def get_attribute6(self):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        return self.options["attribute6"]

    def set_attribute7(self, attribute7):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        self.options["attribute7"] = attribute7

    def get_attribute7(self):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        return self.options["attribute7"]

    def set_attribute8(self, attribute8):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        self.options["attribute8"] = attribute8

    def get_attribute8(self):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        return self.options["attribute8"]

    def set_attribute9(self, attribute9):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        self.options["attribute9"] = attribute9

    def get_attribute9(self):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        return self.options["attribute9"]

    def set_attribute10(self, attribute10):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        self.options["attribute10"] = attribute10

    def get_attribute10(self):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        return self.options["attribute10"]

    def set_attribute11(self, attribute11):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        self.options["attribute11"] = attribute11

    def get_attribute11(self):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        return self.options["attribute11"]

    def set_attribute12(self, attribute12):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        self.options["attribute12"] = attribute12

    def get_attribute12(self):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        return self.options["attribute12"]

    def set_attribute13(self, attribute13):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        self.options["attribute13"] = attribute13

    def get_attribute13(self):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        return self.options["attribute13"]

    def set_attribute14(self, attribute14):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        self.options["attribute14"] = attribute14

    def get_attribute14(self):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        return self.options["attribute14"]

    def set_attribute15(self, attribute15):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        self.options["attribute15"] = attribute15

    def get_attribute15(self):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        return self.options["attribute15"]

    def set_attribute16(self, attribute16):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        self.options["attribute16"] = attribute16

    def get_attribute16(self):
        """Expression that would be evaluated to extract attribute1 from the ldap response.<br/>Maximum length =  64.
        """
        return self.options["attribute16"]

    @staticmethod
    def add(nitro, ldapaction):
        __ldapaction = AuthLdapAction()
        __ldapaction.set_name(ldapaction.get_name())
        __ldapaction.set_serverip(ldapaction.get_serverip())
        __ldapaction.set_servername(ldapaction.get_servername())
        __ldapaction.set_serverport(ldapaction.get_serverport())
        __ldapaction.set_authtimeout(ldapaction.get_authtimeout())
        __ldapaction.set_ldapbase(ldapaction.get_ldapbase())
        __ldapaction.set_ldapbinddn(ldapaction.get_ldapbinddn())
        __ldapaction.set_ldapbinddnpassword(ldapaction.get_ldapbinddnpassword())
        __ldapaction.set_ldaploginname(ldapaction.get_ldaploginname())
        __ldapaction.set_searchfilter(ldapaction.get_searchfilter())
        __ldapaction.set_groupattrname(ldapaction.get_groupattrname())
        __ldapaction.set_subattributename(ldapaction.get_subattributename())
        __ldapaction.set_sectype(ldapaction.get_sectype())
        __ldapaction.set_svrtype(ldapaction.get_svrtype())
        __ldapaction.set_ssonameattribute(ldapaction.get_ssonameattribute())
        __ldapaction.set_authentication(ldapaction.get_authentication())
        __ldapaction.set_requireuser(ldapaction.get_requireuser())
        __ldapaction.set_passwdchange(ldapaction.get_passwdchange())
        __ldapaction.set_nestedgroupextraction(ldapaction.get_nestedgroupextraction())
        __ldapaction.set_maxnestinglevel(ldapaction.get_maxnestinglevel())
        __ldapaction.set_followreferrals(ldapaction.get_followreferrals())
        __ldapaction.set_maxldapreferrals(ldapaction.get_maxldapreferrals())
        __ldapaction.set_validateservercert(ldapaction.get_validateservercert())
        __ldapaction.set_ldaphostname(ldapaction.get_ldaphostname())
        __ldapaction.set_groupnameidentifier(ldapaction.get_groupnameidentifier())
        __ldapaction.set_groupsearchattribute(ldapaction.get_groupsearchattribute())
        __ldapaction.set_groupsearchsubattribute(ldapaction.get_groupsearchsubattribute())
        __ldapaction.set_groupsearchfilter(ldapaction.get_groupsearchfilter())
        __ldapaction.set_defaultauthenticationgroup(ldapaction.get_defaultauthenticationgroup())
        __ldapaction.set_attribute1(ldapaction.get_attribute1())
        __ldapaction.set_attribute2(ldapaction.get_attribute2())
        __ldapaction.set_attribute3(ldapaction.get_attribute3())
        __ldapaction.set_attribute4(ldapaction.get_attribute4())
        __ldapaction.set_attribute5(ldapaction.get_attribute5())
        __ldapaction.set_attribute6(ldapaction.get_attribute6())
        __ldapaction.set_attribute7(ldapaction.get_attribute7())
        __ldapaction.set_attribute8(ldapaction.get_attribute8())
        __ldapaction.set_attribute9(ldapaction.get_attribute9())
        __ldapaction.set_attribute10(ldapaction.get_attribute10())
        __ldapaction.set_attribute11(ldapaction.get_attribute11())
        __ldapaction.set_attribute12(ldapaction.get_attribute12())
        __ldapaction.set_attribute13(ldapaction.get_attribute13())
        __ldapaction.set_attribute14(ldapaction.get_attribute14())
        __ldapaction.set_attribute15(ldapaction.get_attribute15())
        __ldapaction.set_attribute16(ldapaction.get_attribute16())
        return __ldapaction.add_resource(nitro)

    @staticmethod
    def update(nitro, ldapaction):
        __ldapaction = AuthLdapAction()
        __ldapaction.set_name(ldapaction.get_name())
        __ldapaction.set_serverip(ldapaction.get_serverip())
        __ldapaction.set_servername(ldapaction.get_servername())
        __ldapaction.set_serverport(ldapaction.get_serverport())
        __ldapaction.set_authtimeout(ldapaction.get_authtimeout())
        __ldapaction.set_ldapbase(ldapaction.get_ldapbase())
        __ldapaction.set_ldapbinddn(ldapaction.get_ldapbinddn())
        __ldapaction.set_ldapbinddnpassword(ldapaction.get_ldapbinddnpassword())
        __ldapaction.set_ldaploginname(ldapaction.get_ldaploginname())
        __ldapaction.set_searchfilter(ldapaction.get_searchfilter())
        __ldapaction.set_groupattrname(ldapaction.get_groupattrname())
        __ldapaction.set_subattributename(ldapaction.get_subattributename())
        __ldapaction.set_sectype(ldapaction.get_sectype())
        __ldapaction.set_svrtype(ldapaction.get_svrtype())
        __ldapaction.set_ssonameattribute(ldapaction.get_ssonameattribute())
        __ldapaction.set_authentication(ldapaction.get_authentication())
        __ldapaction.set_requireuser(ldapaction.get_requireuser())
        __ldapaction.set_passwdchange(ldapaction.get_passwdchange())
        __ldapaction.set_nestedgroupextraction(ldapaction.get_nestedgroupextraction())
        __ldapaction.set_maxnestinglevel(ldapaction.get_maxnestinglevel())
        __ldapaction.set_followreferrals(ldapaction.get_followreferrals())
        __ldapaction.set_maxldapreferrals(ldapaction.get_maxldapreferrals())
        __ldapaction.set_validateservercert(ldapaction.get_validateservercert())
        __ldapaction.set_ldaphostname(ldapaction.get_ldaphostname())
        __ldapaction.set_groupnameidentifier(ldapaction.get_groupnameidentifier())
        __ldapaction.set_groupsearchattribute(ldapaction.get_groupsearchattribute())
        __ldapaction.set_groupsearchsubattribute(ldapaction.get_groupsearchsubattribute())
        __ldapaction.set_groupsearchfilter(ldapaction.get_groupsearchfilter())
        __ldapaction.set_defaultauthenticationgroup(ldapaction.get_defaultauthenticationgroup())
        __ldapaction.set_attribute1(ldapaction.get_attribute1())
        __ldapaction.set_attribute2(ldapaction.get_attribute2())
        __ldapaction.set_attribute3(ldapaction.get_attribute3())
        __ldapaction.set_attribute4(ldapaction.get_attribute4())
        __ldapaction.set_attribute5(ldapaction.get_attribute5())
        __ldapaction.set_attribute6(ldapaction.get_attribute6())
        __ldapaction.set_attribute7(ldapaction.get_attribute7())
        __ldapaction.set_attribute8(ldapaction.get_attribute8())
        __ldapaction.set_attribute9(ldapaction.get_attribute9())
        __ldapaction.set_attribute10(ldapaction.get_attribute10())
        __ldapaction.set_attribute11(ldapaction.get_attribute11())
        __ldapaction.set_attribute12(ldapaction.get_attribute12())
        __ldapaction.set_attribute13(ldapaction.get_attribute13())
        __ldapaction.set_attribute14(ldapaction.get_attribute14())
        __ldapaction.set_attribute15(ldapaction.get_attribute15())
        __ldapaction.set_attribute16(ldapaction.get_attribute16())
        return __ldapaction.update_resource(nitro)

    @staticmethod
    def delete(nitro, ldapaction):
        __ldapaction = AuthLdapAction()
        __ldapaction.set_name(ldapaction.get_name())
        return __ldapaction.delete_resource(nitro)

    @staticmethod
    def get(nitro, ldapaction):
        __ldapaction = AuthLdapAction()
        __ldapaction.set_name(ldapaction.get_name())
        return __ldapaction.get_resource(nitro)

    @staticmethod
    def get_all(nitro):
        __url = nitro.get_url() + AuthLdapAction.get_resourcetype()
        __json_ldapaction = nitro.get(__url).get_response_field(AuthLdapAction.get_resourcetype())
        __ldapaction = []
        for json_ldapaction in __json_ldapaction:
            __ldapaction.append(AuthLdapAction(json_ldapaction))
        return __ldapaction
