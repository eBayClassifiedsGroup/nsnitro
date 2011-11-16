import json
import urllib
from nsutil import *
from nsbaseresource import NSBaseResource

class NSService(NSBaseResource):

        def __init__(self):
                super(NSService, self).__init__()
                
                self.options = {
                # Read-write values
                        'cachetype' : '',
                        'servername' : '',
                        'downstateflush' : '',
                        'maxreq' : '',
                        'maxbandwidth' : '',
                        'svrtimeout' : '',
                        'port' : '',
                        'clttimeout' : '',
                        'servicetype' : '',
                        'cacheable' : '',
                        'maxclient' : '',
                        'ipaddress' : '',
                        'delay' : '',
                        'usip' : '',
                        'rtspsessionidremap' : '',
                        'cleartextport' : '',
                        'monthreshold' : '',
                        'accessdown' : '',
                        'serverid' : '',
                        'cka' : '',
                        'name' : '',
                        'newname' : '',
                        'sp' : '',
                        'dup_weight' : '',
                        'cip' : '',
                        'cipheader' : '',
                        'useproxyport' : '',
                        'sc' : '',
                        'cmp' : '',
                        'tcpb' : '',
                        'state' : '',
                        'httpprofilename' : '',
                        'tcpprofilename' : '',
                        'comment' : '',

                # Readonly values
                        'policyname' : '',
                        'monstatparam2' : '',
                        'monstatparam3' : '',
                        'stateupdatereason' : '',
                        'serviceconftype' : '',
                        'gslb' : '',
                        'svrstate' : '',
                        'monstatcode' : '',
                        'timesincelaststatechange' : '',
                        'tickssincelaststatechange' : '',
                        'responsetime' : '',
                        'statechangetimesec' : '',
                        'statechangetimemsec' : '',
                        'failedprobes' : '',
                        'totalfailedprobes' : '',
                        'totalprobes' : '',
                }

                self.resourcetype = "service"



        # Getters and setters for configurable options

        def get_name(self):
                return self.options['name']

        def set_name(self, name):
                self.options['name'] = name

        def get_newname(self):
                return self.options['newname']

        def set_newname(self, name):
                self.options['newname'] = name

        def get_cachetype(self):
                return self.options['cachetype']

        def set_cachetype(self, cachetype):
                self.options['cachetype'] = cachetype

        def get_servername(self):
                return self.options['servername']

        def set_servername(self, servername):
                self.options['servername'] = servername

        def get_downstateflush(self):
                return self.options['downstateflush']

        def set_downstateflush(self, downstateflush):
                self.options['downstateflush'] = downstateflush

        def get_maxreq(self):
                return self.options['maxreq']

        def set_maxreq(self, maxreq):
                self.options['maxreq'] = maxreq

        def get_maxbandwidth(self):
                return self.options['maxbandwidth']

        def set_maxbandwidth(self, maxbandwidth):
                self.options['maxbandwidth'] = maxbandwidth

        def get_svrtimeout(self):
                return self.options['svrtimeout']

        def set_svrtimeout(self, svrtimeout):
                self.options['svrtimeout'] = svrtimeout

        def get_port(self):
                return self.options['port']

        def set_port(self, port):
                self.options['port'] = port

        def get_clttimeout(self):
                return self.options['clttimeout']

        def set_clttimeout(self, clttimeout):
                self.options['clttimeout'] = clttimeout

        def get_servicetype(self):
                return self.options['servicetype']

        def set_servicetype(self, servicetype):
                self.options['servicetype'] = servicetype

        def get_cacheable(self):
                return self.options['cacheable']

        def set_cacheable(self, cacheable):
                self.options['cacheable'] = cacheable

        def get_maxclient(self):
                return self.options['maxclient']

        def set_maxclient(self, maxclient):
                self.options['maxclient'] = maxclient

        def get_ipaddress(self):
                return self.options['ipaddress']

        def set_ipaddress(self, ipaddress):
                self.options['ipaddress'] = ipaddress

        def get_delay(self):
                return self.options['delay']

        def set_delay(self, delay):
                self.options['delay'] = delay

        def get_usip(self):
                return self.options['usip']

        def set_usip(self, usip):
                self.options['usip'] = usip

        def get_rtspsessionidremap(self):
                return self.options['rtspsessionidremap']

        def set_rtspsessionidremap(self, rtspsessionidremap):
                self.options['rtspsessionidremap'] = rtspsessionidremap

        def get_cleartextport(self):
                return self.options['cleartextport']

        def set_cleartextport(self, cleartextport):
                self.options['cleartextport'] = cleartextport

        def get_monthreshold(self):
                return self.options['monthreshold']

        def set_monthreshold(self, monthreshold):
                self.options['monthreshold'] = monthreshold

        def get_accessdown(self):
                return self.options['accessdown']

        def set_accessdown(self, accessdown):
                self.options['accessdown'] = accessdown

        def get_serverid(self):
                return self.options['serverid']

        def set_serverid(self, serverid):
                self.options['serverid'] = serverid

        def get_state(self):
                return self.options['state']

        def set_state(self, state):
                self.options['state'] = state

        def get_cka(self):
                return self.options['cka']

        def set_cka(self, cka):
                self.options['cka'] = cka

        def get_sp(self):
                return self.options['sp']

        def set_sp(self, sp):
                self.options['sp'] = sp

        def get_dup_weight(self):
                return self.options['dup_weight']

        def set_dup_weight(self, dup_weight):
                self.options['dup_weight'] = dup_weight

        def get_cip(self):
                return self.options['cip']

        def set_cip(self, cip):
                self.options['cip'] = cip

        def get_cipheader(self):
                return self.options['cip']

        def set_cipheader(self, cipheader):
                self.options['cipheader'] = cipheader


        def get_useproxyport(self):
                return self.options['useproxyport']

        def set_useproxyport(self, useproxyport):
                self.options['useproxyport'] = useproxyport

        def get_sc(self):
                return self.options['sc']

        def set_sc(self, sc):
                self.options['sc'] = sc

        def get_cmp(self):
                return self.options['cmp']

        def set_cmp(self, cmp):
                self.options['cmp'] = cmp

        def get_tcpb(self):
                return self.options['tcpb']

        def set_tcpb(self, tcpb):
                self.options['tcpb'] = tcpb

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


        # Read-only option getters
        def get_svrstate(self):
                return self.options['svrstate']

        def get_totalfailedprobes(self):
                return self.options['totalfailedprobes']

        def get_policyname(self):
                return self.options['policyname']

        def get_monstatparam2(self):
                return self.options['monstatparam2']

        def get_monstatparam3(self):
                return self.options['monstatparam3']

        def get_stateupdatereason(self):
                return self.options['stateupdatereason']

        def get_serviceconftype(self):
                return self.options['serviceconftype']

        def get_gslb(self):
                return self.options['gslb']

        def get_monstatcode(self):
                return self.options['monstatcode']

        def get_timesincelaststatechange(self):
                return self.options['timesincelaststatechange']

        def get_tickssincelaststatechange(self):
                return self.options['tickssincelaststatechange']

        def get_responsetime(self):
                return self.options['responsetime']

        def get_statechangetimesec(self):
                return self.options['statechangetimesec']

        def get_statechangetimemsec(self):
                return self.options['statechangetimemsec']

        def get_failedprobes(self):
                return self.options['failedprobes']

        def get_totalprobes(self):
                return self.options['totalprobes']


        # Operations methods
        @staticmethod
        def disable(nitro, service):
                __service = NSService()
                __service.set_name(service.get_name())
                return __service.perform_operation(nitro, "disable")

        @staticmethod
        def enable(nitro, service):
                __service = NSService()
                __service.set_name(service.get_name())
                return __service.perform_operation(nitro, "enable")

        @staticmethod
        def rename(nitro, service):
                __service = NSService()
                __service.set_name(service.get_name())
                __service.set_newname(service.get_newname())
                return __service.perform_operation(nitro, "rename")

        @staticmethod
        def get(nitro, service_name):
                __service = NSService()
                __service.get_resource(nitro, service_name)
                return __service

        @staticmethod
        def add(nitro, service):
                __service = NSService()
                __service.set_name(service.get_name())
                __service.set_ipaddress(service.get_ipaddress())
                __service.set_servername(service.get_servername())
                __service.set_servicetype(service.get_servicetype())
                __service.set_port(service.get_port())
                __service.set_cleartextport(service.get_cleartextport())
                __service.set_cachetype(service.get_cachetype())
                __service.set_maxclient(service.get_maxclient())
                __service.set_maxreq(service.get_maxreq())
                __service.set_cacheable(service.get_cacheable())
                __service.set_cip(service.get_cip())
                __service.set_cipheader(service.get_cipheader())
                __service.set_usip(service.get_usip())
                __service.set_useproxyport(service.get_useproxyport())
                __service.set_sc(service.get_sc())
                __service.set_sp(service.get_sp())
                __service.set_rtspsessionidremap(service.get_rtspsessionidremap())
                __service.set_clttimeout(service.get_clttimeout())
                __service.set_svrtimeout(service.get_svrtimeout())
                __service.set_serverid(service.get_serverid())
                __service.set_cka(service.get_cka())
                __service.set_tcpb(service.get_tcpb())
                __service.set_maxbandwidth(service.get_maxbandwidth())
                __service.set_accessdown(service.get_accessdown())
                __service.set_monthreshold(service.get_monthreshold())
                __service.set_state(service.get_state())
                __service.set_downstateflush(service.get_downstateflush())
                __service.set_tcpprofilename(service.get_tcpprofilename())
                __service.set_httpprofilename(service.get_httpprofilename())
                __service.set_comment(service.get_comment())
                return __service.add_resource(nitro)

        @staticmethod
        def delete(nitro, service_name):
                __service = NSService()
                nsresponse = __service.delete_resource(nitro, service_name)
                return nsresponse