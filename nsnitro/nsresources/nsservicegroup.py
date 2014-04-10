from nsbaseresource import NSBaseResource

__author__ = 'vlazarenko'


class NSServiceGroup(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSServiceGroup, self).__init__()

        self.options = {
            'servicegroupname': '',
            'servicetype': '',
            'cachetype': '',
            'maxclient': '',
            'maxreq': '',
            'cacheable': '',
            'cip': '',
            'cipheader': '',
            'usip': '',
            'useproxyport': '',
            'sc': '',
            'sp': '',
            'rtspsessionidremap': '',
            'clttimeout': '',
            'svrtimeout': '',
            'cka': '',
            'tcpb': '',
            'cmp': '',
            'maxbandwidth': '',
            'monthreshold': '',
            'state': '',
            'downstateflush': '',
            'tcpprofilename': '',
            'httpprofilename': '',
            'comment': '',
            'servername': '',
            'port': '',
            'weight': '',
            'serverid': '',
            'monitor_name_svc': '',
            'dup_weight': '',
            'delay': '',
            'graceful': '',
            'includemembers': '',
            'newname': '',
            'serviceconftype': '',
            'value': '',
            'svrstate': '',
            'ip': '',
            'monitostate': '',
            'monstatcode': '',
            'monstatparam1': '',
            'monstatparam2': '',
            'monstatparam3': '',
            'statechangetimesec': '',
            'statechangetimemsec': '',
            'timesincelaststatechange': '',
            'tickssincelaststatechange': '',
            'stateupdatereason': '',
            'groupcount': '',
        }

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options:
                    self.options[key] = json_data[key]

        self.resourcetype = NSServiceGroup.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        return "servicegroup"

    def set_servicegroupname(self, servicegroupname):
        self.options['servicegroupname'] = servicegroupname

    def get_servicegroupname(self):
        return self.options['servicegroupname']

    def set_servicetype(self, servicetype):
        self.options['servicetype'] = servicetype

    def get_servicetype(self):
        return self.options['servicetype']

    def set_cachetype(self, cachetype):
        self.options['cachetype'] = cachetype

    def get_cachetype(self):
        return self.options['cachetype']

    def set_maxclient(self, maxclient):
        self.options['maxclient'] = maxclient

    def get_maxclient(self):
        return self.options['maxclient']

    def set_maxreq(self, maxreq):
        self.options['maxreq'] = maxreq

    def get_maxreq(self):
        return self.options['maxreq']

    def set_cacheable(self, cacheable):
        self.options['cacheable'] = cacheable

    def get_cacheable(self):
        return self.options['cacheable']

    def set_cip(self, cip):
        self.options['cip'] = cip

    def get_cip(self):
        return self.options['cip']

    def set_cipheader(self, cipheader):
        self.options['cipheader'] = cipheader

    def get_cipheader(self):
        return self.options['cipheader']

    def set_usip(self, usip):
        self.options['usip'] = usip

    def get_usip(self):
        return self.options['usip']

    def set_useproxyport(self, useproxyport):
        self.options['useproxyport'] = useproxyport

    def get_useproxyport(self):
        return self.options['useproxyport']

    def set_sc(self, sc):
        self.options['sc'] = sc

    def get_sc(self):
        return self.options['sc']

    def set_sp(self, sp):
        self.options['sp'] = sp

    def get_sp(self):
        return self.options['sp']

    def set_rtspsessionidremap(self, rtspsessionidremap):
        self.options['rtspsessionidremap'] = rtspsessionidremap

    def get_rtspsessionidremap(self):
        return self.options['rtspsessionidremap']

    def set_clttimeout(self, clttimeout):
        self.options['clttimeout'] = clttimeout

    def get_clttimeout(self):
        return self.options['clttimeout']

    def set_svrtimeout(self, svrtimeout):
        self.options['svrtimeout'] = svrtimeout

    def get_svrtimeout(self):
        return self.options['svrtimeout']

    def set_cka(self, cka):
        self.options['cka'] = cka

    def get_cka(self):
        return self.options['cka']

    def set_tcpb(self, tcpb):
        self.options['tcpb'] = tcpb

    def get_tcpb(self):
        return self.options['tcpb']

    def set_cmp(self, scmp):
        self.options['cmp'] = scmp

    def get_cmp(self):
        return self.options['cmp']

    def set_maxbandwidth(self, maxbandwidth):
        self.options['maxbandwidth'] = maxbandwidth

    def get_maxbandwidth(self):
        return self.options['maxbandwidth']

    def set_monthreshold(self, monthreshold):
        self.options['monthreshold'] = monthreshold

    def get_monthreshold(self):
        return self.options['monthreshold']

    def set_state(self, state):
        self.options['state'] = state

    def get_state(self):
        return self.options['state']

    def set_downstateflush(self, downstateflush):
        self.options['downstateflush'] = downstateflush

    def get_downstateflush(self):
        return self.options['downstateflush']

    def set_tcpprofilename(self, tcpprofilename):
        self.options['tcpprofilename'] = tcpprofilename

    def get_tcpprofilename(self):
        return self.options['tcpprofilename']

    def set_httpprofilename(self, httpprofilename):
        self.options['httpprofilename'] = httpprofilename

    def get_httpprofilename(self):
        return self.options['httpprofilename']

    def set_comment(self, comment):
        self.options['comment'] = comment

    def get_comment(self):
        return self.options['comment']

    def set_servername(self, servername):
        self.options['servername'] = servername

    def get_servername(self):
        return self.options['servername']

    def set_port(self, port):
        self.options['port'] = port

    def get_port(self):
        return self.options['port']

    def set_weight(self, weight):
        self.options['weight'] = weight

    def get_weight(self):
        return self.options['weight']

    def set_serverid(self, serverid):
        self.options['serverid'] = serverid

    def get_serverid(self):
        return self.options['serverid']

    def get_monitor_name_svc(self):
        return self.options['monitor_name_svc']

    def set_monitor_name_svc(self, monitor_name_svc):
        self.options['monitor_name_svc'] = monitor_name_svc

    def set_dup_weight(self, dup_weight):
        self.options['dup_weight'] = dup_weight

    def get_dup_weight(self):
        return self.options['dup_weight']

    def set_delay(self, delay):
        self.options['delay'] = delay

    def get_delay(self):
        return self.options['delay']

    def set_graceful(self, graceful):
        self.options['graceful'] = graceful

    def get_graceful(self):
        return self.options['graceful']

    def set_includemembers(self, includemembers):
        self.options['includemembers'] = includemembers

    def get_includemembers(self):
        return self.options['includemembers']

    def set_newname(self, newname):
        self.options['newname'] = newname

    def get_newname(self):
        return self.options['newname']

    def get_serviceconftype(self):
        return self.options['serviceconftype']

    def get_value(self):
        return self.options['value']

    def get_svrstate(self):
        return self.options['svrstate']

    def get_ip(self):
        return self.options['ip']

    def get_monitostate(self):
        return self.options['monitostate']

    def get_monstatcode(self):
        return self.options['monstatcode']

    def get_monstatparam1(self):
        return self.options['monstatparam1']

    def get_monstatparam2(self):
        return self.options['monstatparam2']

    def get_monstatparam3(self):
        return self.options['monstatparam3']

    def get_statechangetimesec(self):
        return self.options['statechangetimesec']

    def get_statechangetimemsec(self):
        return self.options['statechangetimemsec']

    def get_timesincelaststatechange(self):
        return self.options['timesincelaststatechange']

    def get_tickssincelaststatechange(self):
        return self.options['tickssincelaststatechange']

    def get_stateupdatereason(self):
        return self.options['stateupdatereason']

    def get_groupcount(self):
        return self.options['groupcount']

    # Operations methods
    @staticmethod
    def disable(nitro, servicegroup):
        """
        Use this API to disable servicegroup.
        """
        __servicegroup = NSServiceGroup()
        __servicegroup.set_servicegroupname(servicegroup.get_servicegroupname())
        __servicegroup.set_delay(servicegroup.get_delay())
        return __servicegroup.perform_operation(nitro, "disable")

    @staticmethod
    def enable(nitro, servicegroup):
        """
        Use this API to enable servicegroup.
        """
        __servicegroup = NSServiceGroup()
        __servicegroup.set_servicegroupname(servicegroup.get_servicegroupname())
        return __servicegroup.perform_operation(nitro, "enable")

    @staticmethod
    def disable_server(nitro, servicegroup):
        """
        Use this API to disable server within servicegroup (Not globally).
        """
        __servicegroup = NSServiceGroup()
        __servicegroup.set_servicegroupname(servicegroup.get_servicegroupname())
        __servicegroup.set_servername(servicegroup.get_servername())
        __servicegroup.set_port(servicegroup.get_port())
        __servicegroup.set_delay(servicegroup.get_delay())
        return __servicegroup.perform_operation(nitro, "disable")

    @staticmethod
    def enable_server(nitro, servicegroup):
        """
        Use this API to enable server within servicegroup (Not globally).
        """
        __servicegroup = NSServiceGroup()
        __servicegroup.set_servicegroupname(servicegroup.get_servicegroupname())
        __servicegroup.set_servername(servicegroup.get_servername())
        __servicegroup.set_port(servicegroup.get_port())
        return __servicegroup.perform_operation(nitro, "enable")

    @staticmethod
    def rename(nitro, servicegroup):
        """
        Use this API to rename servicegroup.
        """
        __servicegroup = NSServiceGroup()
        __servicegroup.set_servicegroupname(servicegroup.get_servicegroupname())
        __servicegroup.set_newname(servicegroup.get_newname())
        return __servicegroup.perform_operation(nitro, "rename")

    @staticmethod
    def get(nitro, servicegroup):
        """
        Use this API to fetch servicegroup resource of given name.
        """
        __servicegroup = NSServiceGroup()
        __servicegroup.set_servicegroupname(servicegroup.get_servicegroupname())
        __servicegroup.get_resource(nitro, servicegroup.get_servicegroupname())
        return __servicegroup

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured servicegroup resources.
        """
        __url = nitro.get_url() + NSServiceGroup.get_resourcetype()
        __json_services = nitro.get(__url).get_response_field(NSServiceGroup.get_resourcetype())
        __servicegroups = []
        for json_service in __json_services:
            __servicegroups.append(NSServiceGroup(json_service))
        return __servicegroups

    @staticmethod
    def get_servers(nitro, servicegroup):
        """
        Use this API to fetch all configured servicegroup members.
        """
        __url = nitro.get_url() + 'servicegroup_servicegroupmember_binding' + '/' + servicegroup.get_servicegroupname()
        __json_services = nitro.get(__url).get_response_field('servicegroup_servicegroupmember_binding')
        __servicegroupmembers = []
        for json_service in __json_services:
            __servicegroupmembers.append(NSServiceGroup(json_service))
        return __servicegroupmembers

    @staticmethod
    def add(nitro, servicegroup):
        """
        Use this API to add service.
        """
        __servicegroup = NSServiceGroup()
        __servicegroup.set_servicegroupname(servicegroup.get_servicegroupname())
        __servicegroup.set_servicetype(servicegroup.get_servicetype())
        __servicegroup.set_cachetype(servicegroup.get_cachetype())
        __servicegroup.set_maxclient(servicegroup.get_maxclient())
        __servicegroup.set_maxreq(servicegroup.get_maxreq())
        __servicegroup.set_cacheable(servicegroup.get_cacheable())
        __servicegroup.set_cip(servicegroup.get_cip())
        __servicegroup.set_cipheader(servicegroup.get_cipheader())
        __servicegroup.set_usip(servicegroup.get_usip())
        __servicegroup.set_useproxyport(servicegroup.get_useproxyport())
        __servicegroup.set_sc(servicegroup.get_sc())
        __servicegroup.set_sp(servicegroup.get_sp())
        __servicegroup.set_rtspsessionidremap(servicegroup.get_rtspsessionidremap())
        __servicegroup.set_clttimeout(servicegroup.get_clttimeout())
        __servicegroup.set_svrtimeout(servicegroup.get_svrtimeout())
        __servicegroup.set_cka(servicegroup.get_cka())
        __servicegroup.set_tcpb(servicegroup.get_tcpb())
        __servicegroup.set_cmp(servicegroup.get_cmp())
        __servicegroup.set_maxbandwidth(servicegroup.get_maxbandwidth())
        __servicegroup.set_monthreshold(servicegroup.get_monthreshold())
        __servicegroup.set_state(servicegroup.get_state())
        __servicegroup.set_downstateflush(servicegroup.get_downstateflush())
        __servicegroup.set_tcpprofilename(servicegroup.get_tcpprofilename())
        __servicegroup.set_httpprofilename(servicegroup.get_httpprofilename())
        __servicegroup.set_comment(servicegroup.get_comment())
        return __servicegroup.add_resource(nitro)

    @staticmethod
    def update(nitro, servicegroup):
        """
        Use this API to update servicegroup.
        """
        __servicegroup = NSServiceGroup()
        __servicegroup.set_servicegroupname(servicegroup.get_servicegroupname())
        __servicegroup.set_servername(servicegroup.get_servername())
        __servicegroup.set_port(servicegroup.get_port())
        __servicegroup.set_serverid(servicegroup.get_serverid())
        __servicegroup.set_monitor_name_svc(servicegroup.get_monitor_name_svc())
        __servicegroup.set_dup_weight(servicegroup.get_dup_weight())

        __servicegroup.set_maxclient(servicegroup.get_maxclient())
        __servicegroup.set_maxreq(servicegroup.get_maxreq())
        __servicegroup.set_cacheable(servicegroup.get_cacheable())
        __servicegroup.set_cip(servicegroup.get_cip())
        __servicegroup.set_cipheader(servicegroup.get_cipheader())
        __servicegroup.set_usip(servicegroup.get_usip())
        __servicegroup.set_useproxyport(servicegroup.get_useproxyport())
        __servicegroup.set_sc(servicegroup.get_sc())
        __servicegroup.set_sp(servicegroup.get_sp())
        __servicegroup.set_rtspsessionidremap(servicegroup.get_rtspsessionidremap())
        __servicegroup.set_clttimeout(servicegroup.get_clttimeout())
        __servicegroup.set_svrtimeout(servicegroup.get_svrtimeout())
        __servicegroup.set_cka(servicegroup.get_cka())
        __servicegroup.set_tcpb(servicegroup.get_tcpb())
        __servicegroup.set_cmp(servicegroup.get_cmp())
        __servicegroup.set_maxbandwidth(servicegroup.get_maxbandwidth())
        __servicegroup.set_monthreshold(servicegroup.get_monthreshold())
        __servicegroup.set_downstateflush(servicegroup.get_downstateflush())
        __servicegroup.set_tcpprofilename(servicegroup.get_tcpprofilename())
        __servicegroup.set_httpprofilename(servicegroup.get_httpprofilename())
        __servicegroup.set_comment(servicegroup.get_comment())
        return __servicegroup.update_resource(nitro)

    @staticmethod
    def delete(nitro, servicegroup):
        """
        Use this API to delete service of a given name.
        """
        __servicegroup = NSServiceGroup()
        __servicegroup.set_servicegroupname(servicegroup.get_servicegroupname())
        nsresponse = __servicegroup.delete_resource(nitro, servicegroup.get_servicegroupname())
        return nsresponse
