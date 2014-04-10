from nsbaseresource import NSBaseResource

__author__ = 'ndenev'


class NSRoute(NSBaseResource):

    # General Netscaler configuration object

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """

        super(NSRoute, self).__init__()

        self.options = {'network': '',
                        'netmask': '',
                        'gateway': '',
                        'cost': '',
                        'td': '',
                        'distance': '',
                        'cost1': '',
                        'weight': '',
                        'advertise': '',
                        'protocol': '',
                        'msr': '',
                        'monitor': '',
                        'routetype': '',
                        'detail': '',
                        'gatewayname': '',
                        'type': '',
                        'dynamic': '',
                        'Static': '',
                        'permanent': '',
                        'direct': '',
                        'nat': '',
                        'lbroute': '',
                        'adv': '',
                        'tunnel': '',
                        'data': '',
                        'data0': '',
                        'flags': '',
                        'routeowners': '',
                        'retain': '',
                        'ospf': '',
                        'isis': '',
                        'rip': '',
                        'bgp': '',
                        'dhcp': '',
                        'advospf': '',
                        'advisis': '',
                        'advrip': '',
                        'advbgp': '',
                        'state': '',
                        'totalprobes': '',
                        'totalfailedprobes': '',
                        'failedprobes': '',
                        'monstatcode': '',
                        'monstatparam1': '',
                        'monstatparam2': '',
                        'monstatparam3': '',
                        '__count': ''}

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

        self.resourcetype = NSRoute.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        return "route"

    def set_network(self, network):
        self.options['network'] = network

    def get_network(self):
        return self.options['network']

    def set_netmask(self, netmask):
        self.options['netmask'] = netmask

    def get_netmask(self):
        return self.options['netmask']

    def set_gateway(self, gateway):
        self.options['gateway'] = gateway

    def get_gateway(self):
        return self.options['gateway']

    def set_cost(self, cost):
        self.options['cost'] = cost

    def get_cost(self):
        return self.options['cost']

    def set_td(self, td):
        self.options['td'] = td

    def get_td(self):
        return self.options['td']

    def set_distance(self, distance):
        self.options['distance'] = distance

    def get_distance(self):
        return self.options['distance']

    def set_cost1(self, cost1):
        self.options['cost1'] = cost1

    def get_cost1(self):
        return self.options['cost1']

    def set_weight(self, weight):
        self.options['weight'] = weight

    def get_weight(self):
        return self.options['weight']

    def set_advertise(self, advertise):
        self.options['advertise'] = advertise

    def get_advertise(self):
        return self.options['advertise']

    def set_protocol(self, protocol):
        self.options['protocol'] = protocol

    def get_protocol(self):
        return self.options['protocol']

    def set_msr(self, msr):
        self.options['msr'] = msr

    def get_msr(self):
        return self.options['msr']

    def set_monitor(self, monitor):
        self.options['monitor'] = monitor

    def get_monitor(self):
        return self.options['monitor']

    def set_routetype(self, routetype):
        self.options['routetype'] = routetype

    def get_routetype(self):
        return self.options['routetype']

    def set_detail(self, detail):
        self.options['detail'] = detail

    def get_detail(self):
        return self.options['detail']

    def get_gatewayname(self):
        return self.options['gatewayname']

    def get_type(self):
        return self.options['type']

    def get_dynamic(self):
        return self.options['dynamic']

    def get_static(self):
        return self.options['Static']

    def get_permanent(self):
        return self.options['permanent']

    def get_direct(self):
        return self.options['direct']

    def get_nat(self):
        return self.options['nat']

    def get_lbroute(self):
        return self.options['lbroute']

    def get_adv(self):
        return self.options['adv']

    def get_tunnel(self):
        return self.options['tunnel']

    def get_data(self):
        return self.options['data']

    def get_data0(self):
        return self.options['data0']

    def get_flags(self):
        return self.options['flags']

    def get_routeowners(self):
        return self.options['routeowners']

    def get_retain(self):
        return self.options['retain']

    def get_ospf(self):
        return self.options['ospf']

    def get_isis(self):
        return self.options['isis']

    def get_rip(self):
        return self.options['rip']

    def get_bgp(self):
        return self.options['bgp']

    def get_dhcp(self):
        return self.options['dhcp']

    def get_advospf(self):
        return self.options['advospf']

    def get_advisis(self):
        return self.options['advisis']

    def get_advrip(self):
        return self.options['advrip']

    def get_advbgp(self):
        return self.options['advbgp']

    def get_state(self):
        return self.options['state']

    def get_totalprobes(self):
        return self.options['totalprobes']

    def get_totalfailedprobes(self):
        return self.options['totalfailedprobes']

    def get_failedprobes(self):
        return self.options['failedprobes']

    def get_monstatcode(self):
        return self.options['monstatcode']

    def get_monstatparam1(self):
        return self.options['monstatparam1']

    def get_monstatparam2(self):
        return self.options['monstatparam2']

    def get_monstatparam3(self):
        return self.options['monstatparam3']

    @staticmethod
    def add(nitro, route):
        __route = NSRoute()
        __route.set_network(route.get_network())
        __route.set_netmask(route.get_netmask())
        __route.set_gateway(route.get_gateway())
        __route.set_cost(route.get_cost())
        __route.set_td(route.get_td())
        __route.set_distance(route.get_distance())
        __route.set_cost1(route.get_cost1())
        __route.set_weight(route.get_weight())
        __route.set_advertise(route.get_advertise())
        __route.set_protocol(route.get_protocol())
        __route.set_msr(route.get_msr())
        __route.set_monitor(route.get_monitor())
        return __route.add_resource(nitro)

    @staticmethod
    def clear(nitro, route):
        __route = NSRoute()
        __route.set_routetype(route.get_routetype())
        return __route.perform_operation(nitro, "clear")

    @staticmethod
    def delete(nitro, route):
        __route = NSRoute()
        __route.set_netmask(route.get_netmask())
        __route.set_gateway(route.get_gateway())
        __route.set_td(route.get_td())
        nsresponse = __route.delete_resource(nitro, object_name=route.get_network())
        return nsresponse

    @staticmethod
    def update(nitro, route):
        __route = NSRoute()
        __route.set_network(route.get_network())
        __route.set_netmask(route.get_netmask())
        __route.set_gateway(route.get_gateway())
        __route.set_td(route.get_td())
        __route.set_distance(route.get_distance())
        __route.set_cost1(route.get_cost1())
        __route.set_weight(route.get_weight())
        __route.set_advertise(route.get_advertise())
        __route.set_protocol(route.get_protocol())
        __route.set_msr(route.get_msr())
        __route.set_monitor(route.get_monitor())
        return __route.update_resource(nitro)

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all nsroute resources that are configured on netscaler.
        """
        __url = nitro.get_url() + NSRoute.get_resourcetype()
        __json_routes = nitro.get(__url).get_response_field(NSRoute.get_resourcetype())
        __routes = []
        for json_route in __json_routes:
            __routes.append(NSRoute(json_route))
        return __routes

    # No route count functionality for now.
    # No unset functionality for now.
