from nsbaseresource import NSBaseResource
__author__ = 'Aleksandar Topuzovic'


class NSServiceLBMonitorBinding(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSServiceLBMonitorBinding, self).__init__()
        self.options = {'policyname': '',
                        'name': '',
                        'monitor_name': '',
                        'monstatparam2': '',
                        'monstatcode': '',
                        'failedprobes': '',
                        'monstatparam3': '',
                        'totalprobes': '',
                        'responsetime': '',
                        'monstatparam1': '',
                        'monitor_state': '',
                        'monstate': '',
                        'totalfailedprobes': '',
                        'dup_weight': ''}

        self.resourcetype = NSServiceLBMonitorBinding.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        """
        Binding object showing the lbmonitor that can be bound to service.
        """
        return "service_lbmonitor_binding"

    # Read/write properties
    def set_policyname(self, policyname):
        """
        The DoS protection policy name must be bound to the service. Also, for DoS protection to work on a service, an appropriate policy must be bound to the service.
        Minimum length = 1
        """
        self.options['policyname'] = policyname

    def get_policyname(self):
        """
        The DoS protection policy name must be bound to the service. Also, for DoS protection to work on a service, an appropriate policy must be bound to the service.
        Minimum length = 1
        """
        return self.options['policyname']

    def set_name(self, name):
        """
        The name of the service to which the policy will be bound.
        Minimum length = 1
        """
        self.options['name'] = name

    def get_name(self):
        """
        The name of the service to which the policy will be bound.
        Minimum length = 1
        """
        return self.options['name']

    def set_monitor_name(self, monitorname):
        """
        The monitor Names.
        """
        self.options['monitor_name'] = monitorname

    def get_monitor_name(self):
        """
        The monitor Names.
        """
        return self.options['monitor_name']

    # Read only properties
    def get_monstatparam2(self):
        """
        Second parameter for use with message code.
        """
        return self.options['monstatparam2']

    def get_monstatcode(self):
        """
        The code indicating the monitor response.
        """
        return self.options['monstatcode']

    def get_failedprobes(self):
        """
        Number of the current failed monitoring probes.
        """
        return self.options['failedprobes']

    def get_monitorname(self):
        """
        Third parameter for use with message code.
        """
        return self.options['monstatparam3']

    def get_totalprobes(self):
        """
        The total number of probs sent.
        """
        return self.options['totalprobes']

    def get_responsetime(self):
        """
        Response time of this monitor.
        """
        return self.options['responsetime']

    def get_monstatparam1(self):
        """
        First parameter for use with message code.
        """
        return self.options['monstatparam1']

    def get_monitor_state(self):
        """
        The running state of the monitor on this service.
        """
        return self.options['monitor_state']

    def get_monstate(self):
        """
        The configured state (enable/disable) of the monitor on this server.
        """
        return self.options['monstate']

    def get_totalfailedprobes(self):
        """
        The total number of failed probs.
        """
        return self.options['totalfailedprobes']

    def get_dup_weight(self):
        """
        The weight of the monitor.
        """
        return self.options['dup_weight']

    @staticmethod
    def get(nitro, servicelbmonitorbinding):
        """
        Use this API to fetch service monitor binding resource of given name.
        """
        __url = nitro.get_url() + NSServiceLBMonitorBinding.get_resourcetype() + "/" + servicelbmonitorbinding.get_name()
        __json_servicelbmonitorbindings = nitro.get(__url).get_response_field(NSServiceLBMonitorBinding.get_resourcetype())
        __servicelbmonitorbindings = []
        for json_servicelbmonitorbinding in __json_servicelbmonitorbindings:
            __servicelbmonitorbindings.append(NSServiceLBMonitorBinding(json_servicelbmonitorbinding))
        return __servicelbmonitorbindings
