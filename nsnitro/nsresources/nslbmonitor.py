from nsbaseresource import NSBaseResource
__author__ = 'robison'


class NSLBMonitor(NSBaseResource):

    # Managing monitors for lb vservers
    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSLBMonitor, self).__init__()
        self.options = {'monitorname': '',
                        'alertretries': '',
                        'destip': '',
                        'destport': '',
                        'deviation': '',
                        'dispatcherip': '',
                        'dispatcherport': '',
                        'downtime': '',
                        'dup_state': '',
                        'dynamicinterval': '',
                        'dynamicresponsetimeout': '',
                        'failureretries': '',
                        'firmwarerevision': '',
                        'httprequest': '',
                        'inbandsecurityid': '',
                        'interval': '',
                        'iptunnel': '',
                        'lrtm': '',
                        'lrtmconf': '',
                        'maxforwards': '',
                        'multimetrictable': '',
                        'query': '',
                        'querytype': '',
                        'radaccounttype': '',
                        'radframedip': '',
                        'radnasip': '',
                        'recv': '',
                        'respcode': '',
                        'resptimeout': '',
                        'resptimeoutthresh': '',
                        'retries': '',
                        'reverse': '',
                        'rtsprequest': '',
                        'secure': '',
                        'send': '',
                        'sipmethod': '',
                        'snmpversion': '',
                        'state': '',
                        'storedb': '',
                        'storefrontacctservice': '',
                        'successretries': '',
                        'tos': '',
                        'transparent': '',
                        'type': '',
                        'units1': '',
                        'units2': '',
                        'units3': '',
                        'units4': '',
                        'validatecred': '',
                        'vendorid': '',
                        }

        self.resourcetype = NSLBMonitor.get_resourcetype()

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

    @staticmethod
    def get_resourcetype():
        return "lbmonitor"

    def set_monitorname(self, monitorname):
        self.options['monitorname'] = monitorname

    def get_monitorname(self):
        return self.options['monitorname']

    def set_alertretries(self, alertretries):
        self.options['alertretries'] = alertretries

    def get_alertretries(self):
        return self.options['alertretries']

    def set_destport(self, destport):
        self.options['destport'] = destport

    def get_destport(self):
        return self.options['destport']

    def set_destip(self, destip):
        self.options['destip'] = destip

    def get_destip(self):
        return self.options['destip']

    def set_deviation(self, deviation):
        self.options['deviation'] = deviation

    def get_deviation(self):
        return self.options['deviation']

    def set_dispatcherip(self, dispatcherip):
        self.options['dispatcherip'] = dispatcherip

    def get_dispatcherip(self):
        return self.options['dispatcherip']

    def set_dispatcherport(self, dispatcherport):
        self.options['dispatcherport'] = dispatcherport

    def get_dispatcherport(self):
        return self.options['dispatcherport']

    def set_downtime(self, downtime):
        self.options['downtime'] = downtime

    def get_downtime(self):
        return self.options['downtime']

    def set_dup_state(self, dup_state):
        self.options['dup_state'] = dup_state

    def get_dup_state(self):
        return self.options['dup_state']

    def set_dynamicinterval(self, dynamicinterval):
        self.options['dynamicinterval'] = dynamicinterval

    def get_dynamicinterval(self):
        return self.options['dynamicinterval']

    def set_dynamicresponsetimeout(self, dynamicresponsetimeout):
        self.options['dynamicresponsetimeout'] = dynamicresponsetimeout

    def get_dynamicresponsetimeout(self):
        return self.options['dynamicresponsetimeout']

    def set_failureretries(self, failureretries):
        self.options['failureretries'] = failureretries

    def get_failureretries(self):
        return self.options['failureretries']

    def set_firmwarerevision(self, firmwarerevision):
        self.options['firmwarerevision'] = firmwarerevision

    def get_firmwarerevision(self):
        return self.options['firmwarerevision']

    def set_httprequest(self, httprequest):
        self.options['httprequest'] = httprequest

    def get_httprequest(self):
        return self.options['httprequest']

    def set_inbandsecurityid(self, inbandsecurityid):
        self.options['inbandsecurityid'] = inbandsecurityid

    def get_inbandsecurityid(self):
        return self.options['inbandsecurityid']

    def set_interval(self, interval):
        self.options['interval'] = interval

    def get_interval(self):
        return self.options['interval']

    def set_iptunnel(self, iptunnel):
        self.options['iptunnel'] = iptunnel

    def get_iptunnel(self):
        return self.options['iptunnel']

    def set_lrtm(self, lrtm):
        self.options['lrtm'] = lrtm

    def get_lrtm(self):
        return self.options['lrtm']

    def set_lrtmconf(self, lrtmconf):
        self.options['lrtmconf'] = lrtmconf

    def get_lrtmconf(self):
        return self.options['lrtmconf']

    def set_maxforwards(self, maxforwards):
        self.options['maxforwards'] = maxforwards

    def get_maxforwards(self):
        return self.options['maxforwards']

    def set_query(self, query):
        self.options['query'] = query

    def get_query(self):
        return self.options['query']

    def set_querytype(self, querytype):
        self.options['querytype'] = querytype

    def get_querytype(self):
        return self.options['querytype']

    def set_radaccounttype(self, radaccounttype):
        self.options['radaccounttype'] = radaccounttype

    def get_radaccounttype(self):
        return self.options['radaccounttype']

    def set_radframedip(self, radframedip):
        self.options['radframedip'] = radframedip

    def get_radframedip(self):
        return self.options['radframedip']

    def set_radnasip(self, radnasip):
        self.options['radnasip'] = radnasip

    def get_radnasip(self):
        return self.options['radnasip']

    def set_recv(self, recv):
        self.options['recv'] = recv

    def get_recv(self):
        return self.options['recv']

    def set_respcode(self, respcode):
        self.options['respcode'] = respcode

    def get_respcode(self):
        return self.options['respcode']

    def set_resptimeout(self, resptimeout):
        self.options['resptimeout'] = resptimeout

    def get_resptimeout(self):
        return self.options['resptimeout']

    def set_resptimeoutthresh(self, resptimeoutthresh):
        self.options['resptimeoutthresh'] = resptimeoutthresh

    def get_resptimeoutthresh(self):
        return self.options['resptimeoutthresh']

    def set_retries(self, retries):
        self.options['retries'] = retries

    def get_retries(self):
        return self.options['retries']

    def set_reverse(self, reverse):
        self.options['reverse'] = reverse

    def get_reverse(self):
        return self.options['reverse']

    def set_rtsprequest(self, rtsprequest):
        self.options['rtsprequest'] = rtsprequest

    def get_rtsprequest(self):
        return self.options['rtsprequest']

    def set_secure(self, secure):
        self.options['secure'] = secure

    def get_secure(self):
        return self.options['secure']

    def set_send(self, send):
        self.options['send'] = send

    def get_send(self):
        return self.options['send']

    def set_sipmethod(self, sipmethod):
        self.options['sipmethod'] = sipmethod

    def get_sipmethod(self):
        return self.options['sipmethod']

    def set_snmpversion(self, snmpversion):
        self.options['snmpversion'] = snmpversion

    def get_snmpversion(self):
        return self.options['snmpversion']

    def set_state(self, state):
        self.options['state'] = state

    def get_state(self):
        return self.options['state']

    def set_storedb(self, storedb):
        self.options['storedb'] = storedb

    def get_storedb(self):
        return self.options['storedb']

    def set_storefrontacctservice(self, storefrontacctservice):
        self.options['storefrontacctservice'] = storefrontacctservice

    def get_storefrontacctservice(self):
        return self.options['storefrontacctservice']

    def set_successretries(self, successretries):
        self.options['successretries'] = successretries

    def get_successretries(self):
        return self.options['successretries']

    def set_tos(self, tos):
        self.options['tos'] = tos

    def get_tos(self):
        return self.options['tos']

    def set_transparent(self, transparent):
        self.options['transparent'] = transparent

    def get_transparent(self):
        return self.options['transparent']

    def set_type(self, lbmontype):
        self.options['type'] = lbmontype

    def get_type(self):
        return self.options['type']

    def set_units1(self, units1):
        self.options['units1'] = units1

    def get_units1(self):
        return self.options['units1']

    def set_units2(self, units2):
        self.options['units2'] = units2

    def get_units2(self):
        return self.options['units2']

    def set_units3(self, units3):
        self.options['units3'] = units3

    def get_units3(self):
        return self.options['units3']

    def set_units4(self, units4):
        self.options['units4'] = units4

    def get_units4(self):
        return self.options['units4']

    def set_validatecred(self, validatecred):
        self.options['validatecred'] = validatecred

    def get_validatecred(self):
        return self.options['validatecred']

    def set_vendorid(self, vendorid):
        self.options['vendorid'] = vendorid

    def get_vendorid(self):
        return self.options['vendorid']

    @staticmethod
    def get(nitro, monitor):
        """
        Use this API to fetch LB Monitor of given name.
        """
        __monitor = NSLBMonitor()
        __monitor.set_monitorname(monitor.get_monitorname())
        __monitor.get_resource(nitro, object_name=__monitor.get_monitorname())
        return __monitor

    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured monitor resources.
        """

        __url = nitro.get_url() + NSLBMonitor.get_resourcetype()
        __json_monitors = nitro.get(__url).get_response_field(
            NSLBMonitor.get_resourcetype())
        __monitors = []
        for json_monitor in __json_monitors:
            __monitors.append(NSLBMonitor(json_monitor))
        return __monitors

    @staticmethod
    def add(nitro, resource):
        """
        Use this API to add a new LB monitor.
        """
        __resource = NSLBMonitor()
        __resource.set_monitorname(resource.get_monitorname())
        __resource.set_alertretries(resource.get_alertretries())
        __resource.set_destip(resource.get_destip())
        __resource.set_destport(resource.get_destport())
        __resource.set_deviation(resource.get_deviation())
        __resource.set_dispatcherip(resource.get_dispatcherip())
        __resource.set_dispatcherport(resource.get_dispatcherport())
        __resource.set_downtime(resource.get_downtime())
        __resource.set_dup_state(resource.get_dup_state())
        __resource.set_dynamicinterval(resource.get_dynamicinterval())
        __resource.set_dynamicresponsetimeout(
            resource.get_dynamicresponsetimeout())
        __resource.set_failureretries(resource.get_failureretries())
        __resource.set_firmwarerevision(
            resource.get_firmwarerevision())
        __resource.set_httprequest(resource.get_httprequest())
        __resource.set_inbandsecurityid(
            resource.get_inbandsecurityid())
        __resource.set_interval(resource.get_interval())
        __resource.set_iptunnel(resource.get_iptunnel())
        __resource.set_lrtm(resource.get_lrtm())
        __resource.set_lrtmconf(resource.get_lrtmconf())
        __resource.set_maxforwards(resource.get_maxforwards())
        __resource.set_query(resource.get_query())
        __resource.set_querytype(resource.get_querytype())
        __resource.set_radaccounttype(resource.get_radaccounttype())
        __resource.set_radframedip(resource.get_radframedip())
        __resource.set_radnasip(resource.get_radnasip())
        __resource.set_recv(resource.get_recv())
        __resource.set_respcode(resource.get_respcode())
        __resource.set_resptimeout(resource.get_resptimeout())
        __resource.set_resptimeoutthresh(
            resource.get_resptimeoutthresh())
        __resource.set_retries(resource.get_retries())
        __resource.set_reverse(resource.get_reverse())
        __resource.set_secure(resource.get_secure())
        __resource.set_send(resource.get_send())
        __resource.set_sipmethod(resource.get_sipmethod())
        __resource.set_snmpversion(resource.get_snmpversion())
        __resource.set_state(resource.get_state())
        __resource.set_storedb(resource.get_storedb())
        __resource.set_storefrontacctservice(
            resource.get_storefrontacctservice())
        __resource.set_successretries(resource.get_successretries())
        __resource.set_tos(resource.get_tos())
        __resource.set_transparent(resource.get_transparent())
        __resource.set_type(resource.get_type())
        __resource.set_units1(resource.get_units1())
        __resource.set_units2(resource.get_units2())
        __resource.set_units3(resource.get_units3())
        __resource.set_units4(resource.get_units4())
        __resource.set_validatecred(resource.get_validatecred())
        __resource.set_vendorid(resource.get_vendorid())
        return __resource.add_resource(nitro)

    @staticmethod
    def update(nitro, resource):
        """
        Use this API to update an existing LB monitor.
        """
        __resource = NSLBMonitor()
        __resource.set_monitorname(resource.get_monitorname())
        __resource.set_alertretries(resource.get_alertretries())
        __resource.set_destip(resource.get_destip())
        __resource.set_destport(resource.get_destport())
        __resource.set_deviation(resource.get_deviation())
        __resource.set_dispatcherip(resource.get_dispatcherip())
        __resource.set_dispatcherport(resource.get_dispatcherport())
        __resource.set_downtime(resource.get_downtime())
        __resource.set_dup_state(resource.get_dup_state())
        __resource.set_dynamicinterval(resource.get_dynamicinterval())
        __resource.set_dynamicresponsetimeout(
            resource.get_dynamicresponsetimeout())
        __resource.set_failureretries(resource.get_failureretries())
        __resource.set_firmwarerevision(
            resource.get_firmwarerevision())
        __resource.set_httprequest(resource.get_httprequest())
        __resource.set_inbandsecurityid(
            resource.get_inbandsecurityid())
        __resource.set_interval(resource.get_interval())
        __resource.set_iptunnel(resource.get_iptunnel())
        __resource.set_lrtm(resource.get_lrtm())
        __resource.set_lrtmconf(resource.get_lrtmconf())
        __resource.set_maxforwards(resource.get_maxforwards())
        __resource.set_query(resource.get_query())
        __resource.set_querytype(resource.get_querytype())
        __resource.set_radaccounttype(resource.get_radaccounttype())
        __resource.set_radframedip(resource.get_radframedip())
        __resource.set_radnasip(resource.get_radnasip())
        __resource.set_recv(resource.get_recv())
        __resource.set_respcode(resource.get_respcode())
        __resource.set_resptimeout(resource.get_resptimeout())
        __resource.set_resptimeoutthresh(
            resource.get_resptimeoutthresh())
        __resource.set_retries(resource.get_retries())
        __resource.set_reverse(resource.get_reverse())
        __resource.set_secure(resource.get_secure())
        __resource.set_send(resource.get_send())
        __resource.set_sipmethod(resource.get_sipmethod())
        __resource.set_snmpversion(resource.get_snmpversion())
        __resource.set_state(resource.get_state())
        __resource.set_storedb(resource.get_storedb())
        __resource.set_storefrontacctservice(
            resource.get_storefrontacctservice())
        __resource.set_successretries(resource.get_successretries())
        __resource.set_tos(resource.get_tos())
        __resource.set_transparent(resource.get_transparent())
        __resource.set_type(resource.get_type())
        __resource.set_units1(resource.get_units1())
        __resource.set_units2(resource.get_units2())
        __resource.set_units3(resource.get_units3())
        __resource.set_units4(resource.get_units4())
        __resource.set_validatecred(resource.get_validatecred())
        __resource.set_vendorid(resource.get_vendorid())
        return __resource.update_resource(nitro)

    @staticmethod
    def delete(nitro, resource):
        """
        Use this API to delete given lbmonitor.
        """
        __resource = NSLBMonitor()
        __resource.set_monitorname(resource.get_monitorname())
        __resource.set_type(resource.get_type())
        nsresponse = __resource.delete_resource(
            nitro, object_name=__resource.get_monitorname())
        return nsresponse
