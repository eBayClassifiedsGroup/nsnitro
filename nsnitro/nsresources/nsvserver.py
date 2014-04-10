from nsbaseresource import NSBaseResource

__author__ = 'Aleksandar Topuzovic'


class NSVServer(NSBaseResource):

    # Configuration for Load Balancing Virtual Server resource.

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSVServer, self).__init__()
        self.options = {
            "name": "",
            "insertvserveripport": "",
            "vipheader": "",
            "ip": "",
            "ipv46": "",
            "port": "",
            "range": "",
            "ipv6address": "",
            "ippattern": "",
            "ipmask": "",
            "servicetype": "",
            "value": "",
            "type": "",
            "state": "",
            "effectivestate": "",
            "status": "",
            "cachetype": "",
            "redirect": "",
            "precedence": "",
            "redirecturl": "",
            "authentication": "",
            "homepage": "",
            "dnsvservername": "",
            "domain": "",
            "rule": "",
            "policyname": "",
            "hits": "",
            "servicename": "",
            "weight": "",
            "cachevserver": "",
            "backupvserver": "",
            "priority": "",
            "clttimeout": "",
            "somethod": "",
            "sopersistence": "",
            "sopersistencetimeout": "",
            "sothreshold": "",
            "lbmethod": "",
            "hashlength": "",
            "dataoffset": "",
            "datalength": "",
            "netmask": "",
            "groupname": "",
            "m": "",
            "tosid": "",
            "persistencetype": "",
            "cookiedomain": "",
            "persistmask": "",
            "persistencebackup": "",
            "timeout": "",
            "cacheable": "",
            "pq": "",
            "sc": "",
            "sessionless": "",
            "url": "",
            "reuse": "",
            "destinationvserver": "",
            "via": "",
            "flags": "",
            "connfailover": "",
            "casesensitive": "",
            "redirectportrewrite": "",
            "downstateflush": "",
            "cookieipport": "",
            "vserverid": "",
            "version": "",
            "totalservices": "",
            "activeservices": "",
            "pushvserver": "",
        }

        self.resourcetype = NSVServer.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "vserver"

    # Read/write properties
    def set_name(self, name):
        """
        The name of the virtual server to be removed.
        Minimum length = 1
        """
        self.options['name'] = name

    def get_name(self):
        """
        The name of the virtual server to be removed.
        Minimum length = 1
        """
        return self.options['name']

    def set_backupvserver(self, backupvserver):
        """
        The name of the backup virtual server for this virtual server.
        Minimum length = 1
        """
        self.options['backupvserver'] = backupvserver

    def get_backupvserver(self):
        """
        The name of the backup virtual server for this virtual server.
        Minimum length = 1
        """
        return self.options['backupvserver']

    def set_redirecturl(self, redirecturl):
        """
        The URL where traffic is redirected if the virtual server in the system becomes unavailable.
        Minimum length = 1
        """
        self.options['redirecturl'] = redirecturl

    def get_redirecturl(self):
        """
        The URL where traffic is redirected if the virtual server in the system becomes unavailable.
        Minimum length = 1
        """
        return self.options['redirecturl']

    def set_cacheable(self, cacheable):
        """
        Use this option to specify whether a virtual server (used for load balancing or content
        switching) routes requests to the cache redirection virtual server before sending it to
        the configured servers.
        """
        self.options['cacheable'] = cacheable

    def get_cacheable(self):
        """
        Use this option to specify whether a virtual server (used for load balancing or content
        switching) routes requests to the cache redirection virtual server before sending it to
        the configured servers.
        """
        return self.options['cacheable']

    def set_clttimeout(self, clttimeout):
        """
        The timeout value in seconds for idle client connection.
        Minimum value = 0
        Maximum value = 31536000
        """
        self.options['clttimeout'] = clttimeout

    def get_clttimeout(self):
        """
        The timeout value in seconds for idle client connection.
        Minimum value = 0
        Maximum value = 31536000
        """
        return self.options['clttimeout']

    def set_somethod(self, somethod):
        """
        The spillover factor. The system will use this value to determine if it should send
        traffic to the backupvserver when the main virtual server reaches the spillover threshold.
        """
        self.options['somethod'] = somethod

    def get_somethod(self):
        """
        The spillover factor. The system will use this value to determine if it should send
        traffic to the backupvserver when the main virtual server reaches the spillover threshold.
        """
        return self.options['somethod']

    def set_sopersistence(self, sopersistence):
        """
        The state of the spillover persistence.
        Default value: DISABLED
        """
        self.options['sopersistence'] = sopersistence

    def get_sopersistence(self):
        """
        The state of the spillover persistence.
        Default value: DISABLED
        """
        return self.options['sopersistence']

    def set_sopersistencetimeout(self, sopersistencetimeout):
        """
        The spillover persistence entry timeout.
        Default value: 2
        Minimum value = 2
        Maximum value = 1440
        """
        self.options['sopersistencetimeout'] = sopersistencetimeout

    def get_sopersistencetimeout(self):
        """
        The spillover persistence entry timeout.
        Default value: 2
        Minimum value = 2
        Maximum value = 1440
        """
        return self.options['sopersistencetimeout']

    def set_sothreshold(self, sothreshold):
        """
        The spillver threshold value.
        Minimum value = 1
        Maximum value = 4294967294
        """
        self.options['sothreshold'] = sothreshold

    def get_sothreshold(self):
        """
        The spillver threshold value.
        Minimum value = 1
        Maximum value = 4294967294
        """
        return self.options['sothreshold']

    def set_pushvserver(self, pushvserver):
        """
        The lb vserver of type PUSH/SSL_PUSH to which server pushes the updates
        received on the client facing non-push lb vserver.
        Minimum length = 1
        """
        self.options['pushvserver'] = pushvserver

    def get_pushvserver(self):
        """
        The lb vserver of type PUSH/SSL_PUSH to which server pushes the updates
        received on the client facing non-push lb vserver.
        Minimum length = 1
        """
        return self.options['pushvserver']

    # Read only properties
    def get_insertvserveripport(self):
        """
        The virtual IP and port header insertion option for the vserver.
        """
        return self.options['insertvserveripport']

    def get_vipheader(self):
        """
        The name of the virtual IP and port header.
        """
        return self.options['vipheader']

    def get_ip(self):
        return self.options['ip']

    def get_ipv46(self):
        """
        The IP address of the virtual server.
        """
        return self.options['ipv46']

    def get_port(self):
        return self.options['port']

    def get_range(self):
        return self.options['range']

    def get_ipv6address(self):
        return self.options['ipv6address']

    def get_ippattern(self):
        """
        The IP pattern of the virtual server.
        """
        return self.options['ippattern']

    def get_ipmask(self):
        """
        The IP address mask of the virtual server.
        """
        return self.options['ipmask']

    def get_servicetype(self):
        return self.options['servicetype']

    def get_value(self):
        return self.options['value']

    def get_type(self):
        return self.options['type']

    def get_state(self):
        return self.options['state']

    def get_effectivestate(self):
        return self.options['effectivestate']

    def get_status(self):
        return self.options['status']

    def get_cachetype(self):
        return self.options['cachetype']

    def get_redirect(self):
        return self.options['redirect']

    def get_precedence(self):
        return self.options['precedence']

    def get_authentication(self):
        return self.options['authentication']

    def get_homepage(self):
        return self.options['homepage']

    def get_dnsvservername(self):
        return self.options['dnsvservername']

    def get_domain(self):
        return self.options['domain']

    def get_rule(self):
        return self.options['rule']

    def get_policyname(self):
        return self.options['policyname']

    def get_hits(self):
        return self.options['hits']

    def get_servicename(self):
        return self.options['servicename']

    def get_weight(self):
        return self.options['weight']

    def get_cachevserver(self):
        return self.options['cachevserver']

    def get_priority(self):
        return self.options['priority']

    def get_lbmethod(self):
        """
        lb method
        """
        return self.options['lbmethod']

    def get_hashlength(self):
        """
        max hash length
        """
        return self.options['hashlength']

    def get_dataoffset(self):
        """
        data offset
        """
        return self.options['dataoffset']

    def get_datalength(self):
        """
        data length
        """
        return self.options['datalength']

    def get_netmask(self):
        """
        hash netmask
        """
        return self.options['netmask']

    def get_groupname(self):
        """
        group name
        """
        return self.options['groupname']

    def get_m(self):
        """
        lb mode
        """
        return self.options['m']

    def get_tosid(self):
        """
        TOS ID
        """
        return self.options['tosid']

    def get_persistencetype(self):
        return self.options['persistencetype']

    def get_cookiedomain(self):
        """
        domain name
        """
        return self.options['cookiedomain']

    def get_persistmask(self):
        """
        persistence mask
        """
        return self.options['persistmask']

    def get_persistencebackup(self):
        """
        backup persistence type
        """
        return self.options['persistencebackup']

    def get_timeout(self):
        """
        timeout
        """
        return self.options['timeout']

    def get_pq(self):
        """
        number
        """
        return self.options['pq']

    def get_sc(self):
        """
        The state of SureConnect on this vserver.
        """
        return self.options['sc']

    def get_sessionless(self):
        """
        sessionless lb
        """
        return self.options['sessionless']

    def get_url(self):
        """
        URL for probe
        """
        return self.options['url']

    def get_reuse(self):
        """
        wtm
        """
        return self.options['reuse']

    def get_destinationvserver(self):
        """
        destination vserver
        """
        return self.options['destinationvserver']

    def get_via(self):
        """
        via
        """
        return self.options['via']

    def get_flags(self):
        """
        vserver flags
        """
        return self.options['flags']

    def get_connfailover(self):
        """
        connection failover
        """
        return self.options['connfailover']

    def get_casesensitive(self):
        """
        persistence type
        """
        return self.options['casesensitive']

    def get_redirectportrewrite(self):
        """
        port rewrite for ssl
        """
        return self.options['redirectportrewrite']

    def get_downstateflush(self):
        """
        Perform delayed clean up of connections on this vserver.
        """
        return self.options['downstateflush']

    def get_cookieipport(self):
        """
        Encryped Ip address and port of the service that is inserted into the
        set-cookie http header
        """
        return self.options['cookieipport']

    def get_vserverid(self):
        """
        Vserver Id
        """
        return self.options['vserverid']

    def get_version(self):
        """
        Cookie version
        """
        return self.options['version']

    def get_totalservices(self):
        """
        Total number of services bound to the vserver.
        """
        return self.options['totalservices']

    def get_activeservices(self):
        """
        Total number of active services bound to the vserver.
        """
        return self.options['activeservices']

    # Operations methods
    @staticmethod
    def disable(nitro, vserver):
        """
        Use this API to disable vserver.
        """
        __vserver = NSVServer()
        __vserver.set_name(vserver.get_name())
        return __vserver.perform_operation(nitro, "disable")

    @staticmethod
    def enable(nitro, vserver):
        """
        Use this API to enable vserver.
        """
        __vserver = NSVServer()
        __vserver.set_name(vserver.get_name())
        return __vserver.perform_operation(nitro, "enable")

    @staticmethod
    def get(nitro, vserver):
        """
        Use this API to fetch vserver resource of given name.
        """
        __vserver = NSVServer()
        __vserver.set_name(vserver.get_name())
        __vserver.get_resource(nitro)
        return __vserver

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured vserver resources.
        """
        __url = nitro.get_url() + NSVServer.get_resourcetype()
        __json_vservers = nitro.get(__url).get_response_field(NSVServer.get_resourcetype())
        __vservers = []
        for json_vserver in __json_vservers:
            __vservers.append(NSVServer(json_vserver))
        return __vservers

    @staticmethod
    def delete(nitro, vserver):
        """
        Use this API to delete vserver of a given name.
        """
        __vserver = NSVServer()
        __vserver.set_name(vserver.get_name())
        nsresponse = __vserver.delete_resource(nitro)
        return nsresponse

    @staticmethod
    def update(nitro, vserver):
        """
        Use this API to update vserver of a given name.
        """
        __vserver = NSVServer()
        __vserver.set_name(vserver.get_name())
        __vserver.set_backupvserver(vserver.get_backupvserver())
        __vserver.set_redirecturl(vserver.get_redirecturl())
        __vserver.set_cacheable(vserver.get_cacheable())
        __vserver.set_clttimeout(vserver.get_clttimeout())
        __vserver.set_somethod(vserver.get_somethod())
        __vserver.set_sopersistence(vserver.get_sopersistence())
        __vserver.set_sopersistencetimeout(vserver.get_sopersistencetimeout())
        __vserver.set_sothreshold(vserver.get_sothreshold())
        __vserver.set_pushvserver(vserver.get_pushvserver())
        return __vserver.update_resource(nitro)
