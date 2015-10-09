from nsbaseresource import NSBaseResource

class NSServiceGroupLBMonitorBinding(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSServiceGroupLBMonitorBinding, self).__init__()
        self.options = {'servicegroupname': '',
                        'port': '',
                        'state': '',
                        'hashid': '',
                        'serverid': '',
                        'customserverid': '',
                        'weight': '',
                        'monitor_name': '',
                        'passive': '',
                        'monstate': '',
                        # read only options
                        'monweight': '',
                        '__count': ''}

        self.resourcetype = NSServiceGroupLBMonitorBinding.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        """
        Binding object showing the lbmonitor that can be bound to service.
        """
        return "servicegroup_lbmonitor_binding"

    # Read/write properties
    def set_servicegroupname(self, policyname):
        self.options['servicegroupname'] = policyname

    def get_servicegroupname(self):
        return self.options['servicegroupname']

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

    def set_monitor_state(self, state):
        self.options['monstate'] = state

    def get_monitor_state(self):
        return self.options['monstate']


    @staticmethod
    def add(nitro, sglbmonitorbinding):
        __servicegroup_lbmonitor_binding = NSServiceGroupLBMonitorBinding()
        __servicegroup_lbmonitor_binding.set_servicegroupname(sglbmonitorbinding.get_servicegroupname())
        __servicegroup_lbmonitor_binding.set_monitor_name(sglbmonitorbinding.get_monitor_name())
        __servicegroup_lbmonitor_binding.set_monitor_state(sglbmonitorbinding.get_monitor_state())
        return __servicegroup_lbmonitor_binding.add_resource(nitro)

    
    @staticmethod
    def delete(nitro, sgmonitorbinding):
        __sgmonitorbinding = NSServiceGroupLBMonitorBinding()
        __sgmonitorbinding.set_servicegroupname(sgmonitorbinding.get_servicegroupname())
        nsresponse = __sgmonitorbinding.delete_resource(nitro, sgmonitorbinding.get_servicegroupname())
        return nsresponse


    @staticmethod
    def get(nitro, servicelbmonitorbinding):
        __url = nitro.get_url() + NSServiceGroupLBMonitorBinding.get_resourcetype() + "/" + servicelbmonitorbinding.get_servicegroupname()
        __json_servicelbmonitorbindings = nitro.get(__url).get_response_field(NSServiceGroupLBMonitorBinding.get_resourcetype())
        __servicelbmonitorbindings = []
        for json_servicelbmonitorbinding in __json_servicelbmonitorbindings:
            __servicelbmonitorbindings.append(NSServiceGroupLBMonitorBinding(json_servicelbmonitorbinding))
        return __servicelbmonitorbindings

