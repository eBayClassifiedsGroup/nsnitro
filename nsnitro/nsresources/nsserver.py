from nsbaseresource import NSBaseResource

__author__ = 'vlazarenko'


class NSServer(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSServer, self).__init__()

        self.options = {
            # Read-write values
            'name': '',
            'ipaddress': '',
            'domain': '',
            'translationip': '',
            'translationmask': '',
            'domainresolveretry': '',
            'state': '',
            'ipv6address': '',
            'comment': '',
            'domainresolvenow': '',
            'delay': '',
            'graceful': '',
            'newname': ''
        }

        self.resourcetype = NSServer.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options:
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "server"

    def set_name(self, name):
        """
        The server's name.
        Default value: 0
        Minimum length =  1.
        """
        self.options['name'] = name

    def get_name(self):
        """
        The server's name.
        Default value: 0
        Minimum length =  1.
        """
        return self.options['name']

    def set_ipaddress(self, ipaddress):
        """
        The IP address of the server.
        Default value: 0
        """
        self.options['ipaddress'] = ipaddress

    def get_ipaddress(self):
        """
        The IP address of the server.
        Default value: 0
        """
        return self.options['ipaddress']

    def set_domain(self, domain):
        """
        The domain name of the server for which a service needs to be added. If an IP Address has been
        specified, the domain name does not need to be specified.

        Default value: 0
        Minimum length =  1.
        """
        self.options['domain'] = domain

    def get_domain(self):
        """
        The domain name of the server for which a service needs to be added. If an IP Address has been
        specified, the domain name does not need to be specified.

        Default value: 0
        Minimum length =  1.
        """
        return self.options['domain']

    def set_translationip(self, translationip):
        """
        The IP address used for translating dns obtained ip.
        Default value: 0
        """
        self.options['translationip'] = translationip

    def get_translationip(self):
        """
        The IP address used for translating dns obtained ip.
        Default value: 0
        """
        return self.options['translationip']

    def set_translationmask(self, translationmask):
        """
        The netmask of the translation ip.
        Default value: 0
        """
        self.options['translationmask'] = translationmask

    def get_translationmask(self):
        """
        The netmask of the translation ip.
        Default value: 0
        """
        return self.options['translationmask']

    def set_domainresolveretry(self, domainresolveretry):
        """
        The duration in seconds for which NetScaler system waits to send the next dns query to resolve the
        domain name, in case the last query failed. If last query succeeds, the netscaler system waits for TTL
        time in the response.
        Default value: 5
        Minimum value =  5
        Maximum value =  20940
        """
        self.options['domainresolveretry'] = domainresolveretry

    def get_domainresolveretry(self):
        """
        The duration in seconds for which NetScaler system waits to send the next dns query to resolve the
        domain name, in case the last query failed. If last query succeeds, the netscaler system waits for TTL
        time in the response.
        Default value: 5
        Minimum value =  5
        Maximum value =  20940
        """
        return self.options['domainresolveretry']

    def set_state(self, state):
        """
        The initial state of the server.
        Default value: ENABLED
        """
        self.options['state'] = state

    def get_state(self):
        """
        The initial state of the server.
        Default value: ENABLED
        """
        return self.options['state']

    def set_ipv6address(self, ipv6address):
        """
        Defines whether server is of type ipv6 or not for DBS services.
        Default value: NO
        """
        self.options['ipv6address'] = ipv6address

    def get_ipv6address(self):
        """
        Defines whether server is of type ipv6 or not for DBS services.
        Default value: NO
        """
        return self.options['ipv6address']

    def set_comment(self, comment):
        """
        Comments associated with this server.
        Default value: 0
        """
        self.options['comment'] = comment

    def get_comment(self):
        """
        Comments associated with this server.
        Default value: 0
        """
        return self.options['comment']

    def set_domainresolvenow(self, domainresolvenow):
        """
        Restart the probe for this domain based server, immediately.
        Default value: 0
        """
        self.options['domainresolvenow'] = domainresolvenow

    def get_domainresolvenow(self):
        """
        Restart the probe for this domain based server, immediately.
        Default value: 0
        """
        return self.options['domainresolvenow']

    def set_delay(self, delay):
        """
        The time in seconds after which all services in this server are brought down.
        Default value: 0
        """
        self.options['delay'] = delay

    def get_delay(self):
        """
        The time in seconds after which all services in this server are brought down.
        Default value: 0
        """
        return self.options['delay']

    def set_graceful(self, graceful):
        """
        Indicates graceful shutdown of the service. System will wait for all outstanding
        connections to this service to be closed before disabling the service.
        Default value: NO
        """
        self.options['graceful'] = graceful

    def get_graceful(self):
        """
        Indicates graceful shutdown of the service. System will wait for all outstanding
        connections to this service to be closed before disabling the service.
        Default value: NO
        """
        return self.options['graceful']

    def set_newname(self, newname):
        """
        The new name of the server.
        Default value: 0
        Minimum length =  1.
        """
        self.options['newname'] = newname

    def get_newname(self):
        """
        The new name of the server.
        Default value: 0
        Minimum length =  1.
        """
        return self.options['newname']

    # Operations methods
    @staticmethod
    def disable(nitro, server):
        """
        Use this API to disable server.
        """
        __server = NSServer()
        __server.set_name(server.get_name())
        __server.set_delay(server.get_delay())
        __server.set_graceful(server.get_graceful())
        return __server.perform_operation(nitro, "disable")

    @staticmethod
    def enable(nitro, server):
        """
        Use this API to enable server.
        """
        __server = NSServer()
        __server.set_name(server.get_name())
        return __server.perform_operation(nitro, "enable")

    @staticmethod
    def rename(nitro, server):
        """
        Use this API to rename server.
        """
        __server = NSServer()
        __server.set_name(server.get_name())
        __server.set_newname(server.get_newname())
        return __server.perform_operation(nitro, "rename")

    @staticmethod
    def get(nitro, server):
        """
        Use this API to fetch server resource of given name.
        """
        __server = NSServer()
        __server.set_name(server.get_name())
        __server.get_resource(nitro)
        return __server

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured server resources.
        """
        __url = nitro.get_url() + NSServer.get_resourcetype()
        __json_servers = nitro.get(__url).get_response_field(NSServer.get_resourcetype())
        __servers = []
        for json_server in __json_servers:
            __servers.append(NSServer(json_server))
        return __servers

    @staticmethod
    def add(nitro, server):
        """
        Use this API to add server.
        """
        __server = NSServer()
        __server.set_name(server.get_name())
        __server.set_ipaddress(server.get_ipaddress())
        __server.set_domain(server.get_domain())
        __server.set_translationip(server.get_translationip())
        __server.set_translationmask(server.get_translationmask())
        __server.set_domainresolveretry(server.get_domainresolveretry())
        __server.set_state(server.get_state())
        __server.set_ipv6address(server.get_ipv6address())
        __server.set_comment(server.get_comment())
        return __server.add_resource(nitro)

    @staticmethod
    def delete(nitro, server):
        """
        Use this API to delete server of a given name.
        """
        __server = NSServer()
        __server.set_name(server.get_name())
        nsresponse = __server.delete_resource(nitro)
        return nsresponse

    @staticmethod
    def update(nitro, server):
        """
        Use this API to update a server of a given name.
        """
        __server = NSServer()
        __server.set_name(server.get_name())
        __server.set_ipaddress(server.get_ipaddress())
        __server.set_domainresolveretry(server.get_domainresolveretry())
        __server.set_translationip(server.get_translationip())
        __server.set_translationmask(server.get_translationmask())
        __server.set_domainresolvenow(server.get_domainresolvenow())
        __server.set_comment(server.get_comment())
        return __server.update_resource(nitro)
