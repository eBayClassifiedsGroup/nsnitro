from nsbaseresource import NSBaseResource

__author__ = 'vlazarenko'

class NSCSVServer(NSBaseResource):
        def __init__(self, json_data = None):

                """
                Supplied with json_data the object can be pre-filled
                """
                super(NSCSVServer, self).__init__()

                options = {
                        'name' : '',
                        'servicetype' : '',
                        'ipv46' : '',
                        'ippattern' : '',
                        'ipmask' : '',
                        'range' : '',
                        'port' : '',
                        'state' : '',
                        'stateupdate' : '',
                        'cacheable' : '',
                        'redirecturl' : '',
                        'clttimeout' : '',
                        'precedence' : '',
                        'casesensitive' : '',
                        'somethod' : '',
                        'sopersistence' : '',
                        'sopersistencetimeout' : '',
                        'sothreshold' : '',
                        'redirectportrewrite' : '',
                        'downstateflush' : '',
                        'backupvserver' : '',
                        'disableprimaryondown' : '',
                        'insertvserveripport' : '',
                        'vipheader' : '',
                        'rtspnat' : '',
                        'authenticationhost' : '',
                        'authentication' : '',
                        'listenpolicy' : '',
                        'listenpriority' : '',
                        'authn401' : '',
                        'authnvsname' : '',
                        'push' : '',
                        'pushvserver' : '',
                        'pushlabel' : '',
                        'pushmulticlients' : '',
                        'tcpprofilename' : '',
                        'httpprofilename' : '',
                        'comment' : '',
                        'newname' : '',

                # --- Read-only options ---

                        'ip' : '',
                        'value' : '',
                        'type' : '',
                        'curstate' : '',
                        'status' : '',
                        'cachetype' : '',
                        'redirect' : '',
                        'homepage' : '',
                        'dnsvservername' : '',
                        'domain' : '',
                        'servicename' : '',
                        'weight' : '',
                        'cachevserver' : '',
                        'targetvserver' : '',
                        'url' : '',
                        'gotopriorityexpression' : '',
                        'bindpoint' : '',
                        'invoke' : '',
                        'labeltype' : '',
                        'labelname' : '',
                        'gt2gb' : '',
                        'statechangetimesec' : '',
                        'statechangetimemsec' : '',
                        'tickssincelaststatechange' : ''
                }

                self.resourcetype = NSCSVServer.get_resourcetype()

                if not (json_data is None):
                        for key in json_data.keys():
                                if self.options.has_key(key):
                                        self.options[key] = json_data[key]


        @staticmethod
        def get_resourcetype():
                return "csvserver"


        def set_name(self, name):
                self.options['name'] = name

        def get_name(self):
                return self.options['name']

        def set_servicetype(self, servicetype):
                self.options['servicetype'] = servicetype

        def get_servicetype(self):
                return self.options['servicetype']

        def set_ipv46(self, ipv46):
                self.options['ipv46'] = ipv46

        def get_ipv46(self):
                return self.options['ipv46']

        def set_ippattern(self, ippattern):
                self.options['ippattern'] = ippattern

        def get_ippattern(self):
                return self.options['ippattern']

        def set_ipmask(self, ipmask):
                self.options['ipmask'] = ipmask

        def get_ipmask(self):
                return self.options['ipmask']

        def set_range(self, range):
                self.options['range'] = range

        def get_range(self):
                return self.options['range']

        def set_port(self, port):
                self.options['port'] = port

        def get_port(self):
                return self.options['port']

        def set_state(self, state):
                self.options['state'] = state

        def get_state(self):
                return self.options['state']

        def set_stateupdate(self, stateupdate):
                self.options['stateupdate'] = stateupdate

        def get_stateupdate(self):
                return self.options['stateupdate']

        def set_cacheable(self, cacheable):
                self.options['cacheable'] = cacheable

        def get_cacheable(self):
                return self.options['cacheable']

        def set_redirecturl(self, redirecturl):
                self.options['redirecturl'] = redirecturl

        def get_redirecturl(self):
                return self.options['redirecturl']

        def set_clttimeout(self, clttimeout):
                self.options['clttimeout'] = clttimeout

        def get_clttimeout(self):
                return self.options['clttimeout']

        def set_precedence(self, precedence):
                self.options['precedence'] = precedence

        def get_precedence(self):
                return self.options['precedence']

        def set_casesensitive(self, casesensitive):
                self.options['casesensitive'] = casesensitive

        def get_casesensitive(self):
                return self.options['casesensitive']

        def set_somethod(self, somethod):
                self.options['somethod'] = somethod

        def get_somethod(self):
                return self.options['somethod']

        def set_sopersistence(self, sopersistence):
                self.options['sopersistence'] = sopersistence

        def get_sopersistence(self):
                return self.options['sopersistence']

        def set_sopersistencetimeout(self, sopersistencetimeout):
                self.options['sopersistencetimeout'] = sopersistencetimeout

        def get_sopersistencetimeout(self):
                return self.options['sopersistencetimeout']

        def set_sothreshold(self, sothreshold):
                self.options['sothreshold'] = sothreshold

        def get_sothreshold(self):
                return self.options['sothreshold']

        def set_redirectportrewrite(self, redirectportrewrite):
                self.options['redirectportrewrite'] = redirectportrewrite

        def get_redirectportrewrite(self):
                return self.options['redirectportrewrite']

        def set_downstateflush(self, downstateflush):
                self.options['downstateflush'] = downstateflush

        def get_downstateflush(self):
                return self.options['downstateflush']

        def set_backupvserver(self, backupvserver):
                self.options['backupvserver'] = backupvserver

        def get_backupvserver(self):
                return self.options['backupvserver']

        def set_disableprimaryondown(self, disableprimaryondown):
                self.options['disableprimaryondown'] = disableprimaryondown

        def get_disableprimaryondown(self):
                return self.options['disableprimaryondown']

        def set_insertvserveripport(self, insertvserveripport):
                self.options['insertvserveripport'] = insertvserveripport

        def get_insertvserveripport(self):
                return self.options['insertvserveripport']

        def set_vipheader(self, vipheader):
                self.options['vipheader'] = vipheader

        def get_vipheader(self):
                return self.options['vipheader']

        def set_rtspnat(self, rtspnat):
                self.options['rtspnat'] = rtspnat

        def get_rtspnat(self):
                return self.options['rtspnat']

        def set_authenticationhost(self, authenticationhost):
                self.options['authenticationhost'] = authenticationhost

        def get_authenticationhost(self):
                return self.options['authenticationhost']

        def set_authentication(self, authentication):
                self.options['authentication'] = authentication

        def get_authentication(self):
                return self.options['authentication']

        def set_listenpolicy(self, listenpolicy):
                self.options['listenpolicy'] = listenpolicy

        def get_listenpolicy(self):
                return self.options['listenpolicy']

        def set_listenpriority(self, listenpriority):
                self.options['listenpriority'] = listenpriority

        def get_listenpriority(self):
                return self.options['listenpriority']

        def set_authn401(self, authn401):
                self.options['authn401'] = authn401

        def get_authn401(self):
                return self.options['authn401']

        def set_authnvsname(self, authnvsname):
                self.options['authnvsname'] = authnvsname

        def get_authnvsname(self):
                return self.options['authnvsname']

        def set_push(self, push):
                self.options['push'] = push

        def get_push(self):
                return self.options['push']

        def set_pushvserver(self, pushvserver):
                self.options['pushvserver'] = pushvserver

        def get_pushvserver(self):
                return self.options['pushvserver']

        def set_pushlabel(self, pushlabel):
                self.options['pushlabel'] = pushlabel

        def get_pushlabel(self):
                return self.options['pushlabel']

        def set_pushmulticlients(self, pushmulticlients):
                self.options['pushmulticlients'] = pushmulticlients

        def get_pushmulticlients(self):
                return self.options['pushmulticlients']

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

        def set_newname(self, newname):
                self.options['newname'] = newname

        def get_newname(self):
                return self.options['newname']

        def get_ip(self):
                return self.options['ip']

        def get_value(self):
                return self.options['value']

        def get_type(self):
                return self.options['type']

        def get_curstate(self):
                return self.options['curstate']

        def get_status(self):
                return self.options['status']

        def get_cachetype(self):
                return self.options['cachetype']

        def get_redirect(self):
                return self.options['redirect']

        def get_homepage(self):
                return self.options['homepage']

        def get_dnsvservername(self):
                return self.options['dnsvservername']

        def get_domain(self):
                return self.options['domain']

        def get_servicename(self):
                return self.options['servicename']

        def get_weight(self):
                return self.options['weight']

        def get_cachevserver(self):
                return self.options['cachevserver']

        def get_targetvserver(self):
                return self.options['targetvserver']

        def get_url(self):
                return self.options['url']

        def get_gotopriorityexpression(self):
                return self.options['gotopriorityexpression']

        def get_bindpoint(self):
                return self.options['bindpoint']

        def get_invoke(self):
                return self.options['invoke']

        def get_labeltype(self):
                return self.options['labeltype']

        def get_labelname(self):
                return self.options['labelname']

        def get_gt2gb(self):
                return self.options['gt2gb']

        def get_statechangetimesec(self):
                return self.options['statechangetimesec']

        def get_statechangetimemsec(self):
                return self.options['statechangetimemsec']

        def get_tickssincelaststatechange(self):
                return self.options['tickssincelaststatechange']

        # Operations methods
        @staticmethod
        def disable(nitro, csvserver):
                """
                Use this API to disable csvserver.
                """
                __csvserver = NSCSVServer()
                __csvserver.set_name(csvserver.get_name())
                return __csvserver.perform_operation(nitro, "disable")

        @staticmethod
        def enable(nitro, csvserver):
                """
                Use this API to enable csvserver.
                """
                __csvserver = NSCSVServer()
                __csvserver.set_name(csvserver.get_name())
                return __csvserver.perform_operation(nitro, "enable")

        @staticmethod
        def rename(nitro, csvserver):
                """
                Use this API to rename csvserver.
                """
                __csvserver = NSCSVServer()
                __csvserver.set_name(csvserver.get_name())
                __csvserver.set_newname(csvserver.get_newname())
                return __csvserver.perform_operation(nitro, "rename")

        @staticmethod
        def get(nitro, csvserver):
                """
                Use this API to fetch csvserver resource of given name.
                """
                __csvserver = NSCSVServer()
                __csvserver.set_name(csvserver.get_name())
                __csvserver.get_resource(nitro)
                return __csvserver

        @staticmethod
        def get_all(nitro):
                """
                Use this API to fetch all configured csvserver resources.
                """
                __url = nitro.get_url() + NSCSVServer.get_resourcetype()
                __json_csvservers = nitro.get(__url).get_response_field(NSCSVServer.get_resourcetype())
                __csvservers = []
                for json_csvserver in __json_csvservers:
                        __csvservers.append(NSCSVServer(json_csvserver))
                return __csvservers

        @staticmethod
        def add(nitro, csvserver):
                """
                Use this API to add csvserver.
                """
                __csvserver = NSCSVServer()
                __csvserver.set_name(csvserver.get_name())
                __csvserver.set_servicetype(csvserver.get_servicetype())
                __csvserver.set_ipv46(csvserver.get_ipv46())
                __csvserver.set_ippattern(csvserver.get_ippattern())
                __csvserver.set_ipmask(csvserver.get_ipmask())
                __csvserver.set_range(csvserver.get_range())
                __csvserver.set_port(csvserver.get_port())
                __csvserver.set_state(csvserver.get_state())
                __csvserver.set_stateupdate(csvserver.get_stateupdate())
                __csvserver.set_cacheable(csvserver.get_cacheable())
                __csvserver.set_redirecturl(csvserver.get_redirecturl())
                __csvserver.set_clttimeout(csvserver.get_clttimeout())
                __csvserver.set_precedence(csvserver.get_precedence())
                __csvserver.set_casesensitive(csvserver.get_casesensitive())
                __csvserver.set_somethod(csvserver.get_somethod())
                __csvserver.set_sopersistence(csvserver.get_sopersistence())
                __csvserver.set_sopersistencetimeout(csvserver.get_sopersistencetimeout())
                __csvserver.set_sothreshold(csvserver.get_sothreshold())
                __csvserver.set_redirectportrewrite(csvserver.get_redirectportrewrite())
                __csvserver.set_downstateflush(csvserver.get_downstateflush())
                __csvserver.set_backupvserver(csvserver.get_backupvserver())
                __csvserver.set_disableprimaryondown(csvserver.get_disableprimaryondown())
                __csvserver.set_insertvserveripport(csvserver.get_insertvserveripport())
                __csvserver.set_vipheader(csvserver.get_vipheader())
                __csvserver.set_rtspnat(csvserver.get_rtspnat())
                __csvserver.set_authenticationhost(csvserver.get_authenticationhost())
                __csvserver.set_authentication(csvserver.get_authentication())
                __csvserver.set_listenpolicy(csvserver.get_listenpolicy())
                __csvserver.set_listenpriority(csvserver.get_listenpriority())
                __csvserver.set_authn401(csvserver.get_authn401())
                __csvserver.set_authnvsname(csvserver.get_authnvsname())
                __csvserver.set_push(csvserver.get_push())
                __csvserver.set_pushvserver(csvserver.get_pushvserver())
                __csvserver.set_pushlabel(csvserver.get_pushlabel())
                __csvserver.set_pushmulticlients(csvserver.get_pushmulticlients())
                __csvserver.set_tcpprofilename(csvserver.get_tcpprofilename())
                __csvserver.set_httpprofilename(csvserver.get_httpprofilename())
                __csvserver.set_comment(csvserver.get_comment())
                return __csvserver.add_resource(nitro)

        @staticmethod
        def delete(nitro, csvserver):
                """
                Use this API to delete csvserver of a given name.
                """
                __csvserver = NSCSVServer()
                __csvserver.set_name(csvserver.get_name())
                nsresponse = __csvserver.delete_resource(nitro)
                return nsresponse

        @staticmethod
        def update(nitro, csvserver):
                """
                Use this API to update csvserver of a given name.
                """
                __csvserver = NSCSVServer()
                __csvserver.set_name(csvserver.get_name())
                __csvserver.set_ipv46(csvserver.get_ipv46())
                __csvserver.set_ippattern(csvserver.get_ippattern())
                __csvserver.set_ipmask(csvserver.get_ipmask())
                __csvserver.set_stateupdate(csvserver.get_stateupdate())
                __csvserver.set_precedence(csvserver.get_precedence())
                __csvserver.set_casesensitive(csvserver.get_casesensitive())
                __csvserver.set_backupvserver(csvserver.get_backupvserver())
                __csvserver.set_redirecturl(csvserver.get_redirecturl())
                __csvserver.set_cacheable(csvserver.get_cacheable())
                __csvserver.set_clttimeout(csvserver.get_clttimeout())
                __csvserver.set_somethod(csvserver.get_somethod())
                __csvserver.set_sopersistence(csvserver.get_sopersistence())
                __csvserver.set_sopersistencetimeout(csvserver.get_sopersistencetimeout())
                __csvserver.set_sothreshold(csvserver.get_sothreshold())
                __csvserver.set_redirectportrewrite(csvserver.get_redirectportrewrite())
                __csvserver.set_downstateflush(csvserver.get_downstateflush())
                __csvserver.set_disableprimaryondown(csvserver.get_disableprimaryondown())
                __csvserver.set_insertvserveripport(csvserver.get_insertvserveripport())
                __csvserver.set_vipheader(csvserver.get_vipheader())
                __csvserver.set_rtspnat(csvserver.get_rtspnat())
                __csvserver.set_authenticationhost(csvserver.get_authenticationhost())
                __csvserver.set_authentication(csvserver.get_authentication())
                __csvserver.set_listenpolicy(csvserver.get_listenpolicy())
                __csvserver.set_listenpriority(csvserver.get_listenpriority())
                __csvserver.set_authn401(csvserver.get_authn401())
                __csvserver.set_authnvsname(csvserver.get_authnvsname())
                __csvserver.set_push(csvserver.get_push())
                __csvserver.set_pushvserver(csvserver.get_pushvserver())
                __csvserver.set_pushlabel(csvserver.get_pushlabel())
                __csvserver.set_pushmulticlients(csvserver.get_pushmulticlients())
                __csvserver.set_tcpprofilename(csvserver.get_tcpprofilename())
                __csvserver.set_httpprofilename(csvserver.get_httpprofilename())
                __csvserver.set_comment(csvserver.get_comment())
                return __csvserver.update_resource(nitro)
        

