from nsbaseresource import NSBaseResource


class NSHANode(NSBaseResource):

    # Configuration for HA node resource.

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSHANode, self).__init__()
        self.options = {'id': '',
                        'ipaddress': '',
                        'inc': '',
                        'hastatus': '',
                        'hasync': '',
                        'haprop': '',
                        'hellointerval': '',
                        'deadinterval': '',
                        'failsafe': '',
                        'name': '',
                        'flags': '',
                        'state': '',
                        'enaifaces': '',
                        'disifaces': '',
                        'hamonifaces': '',
                        'pfifaces': '',
                        'ifaces': '',
                        'network': '',
                        'netmask': '',
                        'ssl2': '',
                        'masterstatetime': '',
                        'routemonitor': ''}

        self.resourcetype = NSHANode.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "hanode"

    def set_id(self, myid):
        self.options['id'] = myid

    def get_id(self):
        return self.options['id']

    def set_ipaddress(self, ipaddress):
        self.options['ipaddress'] = ipaddress

    def get_ipaddress(self):
        return self.options['ipaddress']

    def set_inc(self, inc):
        self.options['inc'] = inc

    def get_inc(self):
        return self.options['inc']

    def set_hastatus(self, hastatus):
        self.options['hastatus'] = hastatus

    def get_hastatus(self):
        return self.options['hastatus']

    def set_hasync(self, hasync):
        self.options['hasync'] = hasync

    def get_hasync(self):
        return self.options['hasync']

    def set_haprop(self, haprop):
        self.options['haprop'] = haprop

    def get_haprop(self):
        return self.options['haprop']

    def set_hellointerval(self, hellointerval):
        self.options['hellointerval'] = hellointerval

    def get_hellointerval(self):
        return self.options['hellointerval']

    def set_deadinterval(self, deadinterval):
        self.options['deadinterval'] = deadinterval

    def get_deadinterval(self):
        return self.options['deadinterval']

    def set_failsafe(self, failsafe):
        self.options['failsafe'] = failsafe

    def get_failsafe(self):
        return self.options['failsafe']

    def get_name(self):
        return self.options['name']

    def get_flags(self):
        return self.options['flags']

    def get_state(self):
        return self.options['state']

    def get_enaifaces(self):
        return self.options['enaifaces']

    def get_disifaces(self):
        return self.options['disifaces']

    def get_hamonifaces(self):
        return self.options['hamonifaces']

    def get_pfifaces(self):
        return self.options['pfifaces']

    def get_ifaces(self):
        return self.options['ifaces']

    def get_network(self):
        return self.options['network']

    def get_netmask(self):
        return self.options['netmask']

    def get_ssl2(self):
        return self.options['ssl2']

    def get_masterstatetime(self):
        return self.options['masterstatetime']

    def get_routemonitor(self):
        return self.options['routemonitor']

    # Operations methods
    @staticmethod
    def get(nitro, hanode):
        """
        Use this API to fetch hanode resource of given name.
        """
        __hanode = NSHANode()
        __hanode.get_resource(nitro, hanode.get_id())
        return __hanode

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured hanode resources.
        """
        __url = nitro.get_url() + NSHANode.get_resourcetype()
        __json_hanodes = nitro.get(__url).get_response_field(NSHANode.get_resourcetype())
        __hanodes = []
        for json_hanode in __json_hanodes:
            __hanodes.append(NSHANode(json_hanode))
        return __hanodes

    @staticmethod
    def add(nitro, hanode):
        """
        Use this API to add hanode.
        """
        __hanode = NSHANode()
        __hanode.set_id(hanode.get_id())
        __hanode.set_ipaddress(hanode.get_ipaddress())
        __hanode.set_inc(hanode.get_inc())
        return __hanode.add_resource(nitro)

    @staticmethod
    def delete(nitro, hanode):
        """
        Use this API to delete hanode of a given name.
        """
        __hanode = NSHANode()
        nsresponse = __hanode.delete_resource(nitro, hanode.get_id())
        return nsresponse

    @staticmethod
    def update(nitro, hanode):
        """
        Use this API to update a hanode of a given name.
        """
        __hanode = NSHANode()
        __hanode.set_id(hanode.get_id())
        __hanode.set_hastatus(hanode.get_hastatus())
        __hanode.set_hasync(hanode.get_hasync())
        __hanode.set_haprop(hanode.get_haprop())
        __hanode.set_hellointerval(hanode.get_hellointerval())
        __hanode.set_deadinterval(hanode.get_deadinterval())
        __hanode.set_failsafe(hanode.get_failsafe())
        return __hanode.update_resource(nitro)


    # No unset functionality for now.
