import time
from nsnitro import *

class test_nitro:
        def __init__(self,args):
                self.nitro = NSNitro(args.get('ip'),args.get('user'),args.get('password'))
                self.nitro.login()

        def add_server(self):

                # add server test
                addserver = NSServer()
                addserver.set_name("nitro_example_server")
                addserver.set_ipaddress("10.32.110.99")
                NSServer.add(self.nitro, addserver)

                server = NSServer()
                server.set_name("nitro_example_server")
                server = server.get(self.nitro, server)
                print server.get_name() + ": " + server.get_state()


        def add_servicegroup(self):
                # add servicegroup test
                servicegroup = NSServiceGroup()
                servicegroup.set_servicegroupname('nitro_example_servicegroup')
                NSServiceGroup.add(self.nitro, servicegroup)

        def delete_servicegroup(self):
                # add servicegroup test
                servicegroup = NSServiceGroup()
                servicegroup.set_servicegroupname('nitro_example_servicegroup')
                NSServiceGroup.delete(self.nitro, servicegroup)

        def disable_server(self):

                # disable server test
                server = NSServer()
                server.set_name("nitro_example_server")
                NSServer.disable(self.nitro, server)

                time.sleep(2)
                server = NSServer()
                server.set_name("nitro_example_server")
                server = server.get(self.nitro, server)
                print server.get_name() + ": " + server.get_state()


        def enable_server(self):
                # enable server test
                server = NSServer()
                server.set_name("nitro_example_server")
                NSServer.enable(self.nitro, server)

                time.sleep(2)

                server = NSServer()
                server.set_name("nitro_example_server")
                server = server.get(self.nitro, server)
                print server.get_name() + ": " + server.get_state()

        def add_service(self):
                # add service test

                addservice = NSService()
                addservice.set_name("service_nitro_test")
                addservice.set_servername("nitro_example_server")
                addservice.set_servicetype("HTTP")
                addservice.set_port(11111)
                NSService.add(self.nitro, addservice)

        def add_lbvserver(self):
                # add lbvserver test
                lbvserver = NSLBVServer()
                lbvserver.set_name("nitro_lbvserver_test")
                lbvserver.set_ipv46("10.32.110.55")
                lbvserver.set_port(11111)
                lbvserver.set_clttimeout(180)
                lbvserver.set_persistencetype("NONE")
                lbvserver.set_servicetype("HTTP")
                NSLBVServer.add(self.nitro, lbvserver)
                #
                print "LB vserver added"

        def bind_lbvserver(self):
                # bind service to lbvserver test


                lbbinding = NSLBVServerServiceBinding()
                #{'serviceGroupName':'Test-SG-192.168.8.139','policyName':'http','name':'Test-SG-192.168.8.139' })
                #lbbinding.set_name('Test-SG-192.168.8.139')
                lbbinding.set_name('nitro_lbvserver_test')
                lbbinding.set_servicename("service_nitro_test")
                lbbinding.set_weight(40)
                NSLBVServerServiceBinding.add(self.nitro, lbbinding)

                print "Binding added"

        def print_lbvserver_binding(self):
                print "printing lbvserver binding"
                lbbinding = NSLBVServerServiceBinding()
                lbbinding.set_name("nitro_lbvserver_test")
                lbbindings = NSLBVServerServiceBinding.get(self.nitro, lbbinding)

                for lbb in lbbindings:
                        print "sgn: " + lbb.get_servicegroupname()


        def delete_binding(self):

                # delete binding test
                lbbinding = NSLBVServerServiceBinding()
                lbbinding.set_name("nitro_lbvserver_test")
                lbbinding.set_servicename("service_nitro_test")
                NSLBVServerServiceBinding.delete(self.nitro, lbbinding)

                print "Binding removed"

        def delete_lbvserver(self):
                # delete lbvserver test
                lbvserver = NSLBVServer()
                lbvserver.set_name("nitro_lbvserver_test")
                NSLBVServer.delete(self.nitro, lbvserver)
                print "LB vserver deleted"

                # get service test
        def get_service(self):
                service = NSService()
                service.set_name("service_nitro_test")
                service = service.get(self.nitro, service)
                print service.get_name() + ": " + service.get_svrstate()
                print service.get_name() + ": %s %s" % (service.get_port(), service.get_useproxyport())


        def update_service(self):
                #update service test
                updateservice = NSService()
                updateservice.set_name("service_nitro_test")
                updateservice.set_comment("test comment")
                updateservice.set_useproxyport("NO")
                NSService.update(self.nitro, updateservice)

                # get service test

                service = NSService()
                service.set_name("service_nitro_test")
                service = service.get(self.nitro, service)
                print service.get_name() + ": " + service.get_svrstate()
                print service.get_name() + ": %s %s %s" % (service.get_port(), service.get_comment(), service.get_useproxyport())


        def disable_service(self):
                # disable service test

                disservice = NSService()
                disservice.set_name("service_nitro_test")
                NSService.disable(self.nitro, disservice)

                service = NSService()
                service.set_name("service_nitro_test")
                service = service.get(self.nitro, service)
                print service.get_name() + ": " + service.get_svrstate()

                # enable service test

        def enable_service(self):

                enservice = NSService()
                enservice.set_name("service_nitro_test")
                NSService.enable(self.nitro, enservice)

                service = NSService()
                service.set_name("service_nitro_test")
                service = service.get(self.nitro, service)
                print service.get_name() + ": " + service.get_svrstate()

        def rename_service(self):

                # rename service test

                renservice = NSService()
                renservice.set_name("service_nitro_test")
                renservice.set_newname("service_nitro_test_rename")
                NSService.rename(self.nitro, renservice)

                # rename service back test

                renservice = NSService()
                renservice.set_name("service_nitro_test_rename")
                renservice.set_newname("service_nitro_test")
                NSService.rename(self.nitro, renservice)

        def delete_service(self):
                # delete service test

                delservice = NSService()
                delservice.set_name("service_nitro_test")
                NSService.delete(self.nitro, delservice)

                try:
                        service = NSService()
                        service.set_name("service_nitro_test")
                        service = service.get(self.nitro, service)
                        print service.get_name() + ": " + service.get_svrstate()
                except NSNitroError, e:
                        print e.message

        def delete_server(self):
                # delete server test
                delserver = NSServer()
                delserver.set_name("nitro_example_server")
                NSServer.delete(self.nitro, delserver)

                try:
                        server = NSServer()
                        server.set_name("nitro_example_server")
                        server = server.get(self.nitro, server)
                        print server.get_name() + ": " + server.get_state()
                except NSNitroError, e:
                        print e.message


        def list_hanodes(self):
                #list hanodes
                hanodes = NSHANode.get_all(self.nitro)
                for node in hanodes:
                        print node.get_id() + " " + node.get_state() + " " + node.get_hastatus() + " " + node.get_failsafe() + " " + node.get_haprop() + " " + str(node.get_masterstatetime())

        def list_vlans(self):
                vlans = NSVLAN.get_all(self.nitro)
                for vlan in vlans:
                        print vlan.get_id()

        def add_vlan(self):
                vlan = NSVLAN()
                vlan.set_id(125)
                NSVLAN.add(self.nitro, vlan)

        def delete_vlan(self):
                vlan = NSVLAN()
                vlan.set_id(125)
                NSVLAN.delete(self.nitro, vlan)

        def list_ips(self):
                ips = NSIP.get_all(self.nitro)
                for ip in ips:
                        print ip.get_ipaddress()

        def list_vlan_if_bindings(self):
                b = NSVLANInterfaceBinding()
                b.set_id(125)
                vib = NSVLANInterfaceBinding.get(self.nitro, b)
                print vib.get_id(), vib.get_ifnum(), vib.get_tagged()

        def list_vlan_ip_bindings(self):
                b = NSVLANNSIPBinding()
                b.set_id(125)
                vib = NSVLANNSIPBinding.get(self.nitro, b)

                print vib.get_id(), vib.get_ipaddress(), vib.get_netmask()


        def add_ip(self):
                ip = NSIP()
                ip.set_ipaddress('10.40.12.181')
                ip.set_netmask('255.255.255.224')
                ip.set_vserver('disabled')
                NSIP.add(self.nitro, ip)

        def delete_ip(self):
                ip = NSIP()
                ip.set_ipaddress('10.40.12.181')
                NSIP.delete(self.nitro, ip)

        def delete_vipb(self):
                ip = NSVLANNSIPBinding()
                ip.set_id(125)
                ip.set_ipaddress('10.40.12.181')
                ip.set_netmask('255.255.255.224')
                NSVLANNSIPBinding.delete(self.nitro, ip)

        def delete_vifb(self):
                ip = NSVLANInterfaceBinding()
                ip.set_id(125)
                ip.set_ifnum("1/1")
                #ip.set_tagged(True)
                NSVLANInterfaceBinding.delete(self.nitro, ip)


        def bind_vlan_to_if(self):
                b = NSVLANInterfaceBinding()
                b.set_id(125)
                b.set_ifnum("1/1")
                b.set_tagged(True)
                NSVLANInterfaceBinding.add(self.nitro, b)

        def bind_vlan_to_ip(self):
                b = NSVLANNSIPBinding()
                b.set_id(125)
                b.set_ipaddress('10.40.12.181')
                b.set_netmask('255.255.255.224')
                NSVLANNSIPBinding.add(self.nitro, b)

        def disable_feature(self):
                b = NSFeature()
                b.set_feature(['CS', 'LB'])
                NSFeature.disable(self.nitro, b)

        def enable_feature(self):
                b = NSFeature()
                b.set_feature(['CS', 'LB'])
                NSFeature.enable(self.nitro, b)

        def add_cspolicy(self):
                asdf = NSCSPolicy()
                asdf.set_rule("asdf")
                asdf.set_policyname("foobar")
                NSCSPolicy.add(self.nitro, asdf)

        def add_rewriteaction(self):
                asdf = NSRewriteAction()
                asdf.set_name("insert-X-eBay-Client-IP")
                asdf.set_type("insert_http_header")
                asdf.set_target("X-eBay-Client-IP")
                asdf.set_stringbuilderexpr("CLIENT.IP.SRC")
                NSRewriteAction.add(self.nitro, asdf)

        def add_lbmonitor(self):
                asdf = NSLBMonitorServiceBinding()
                asdf.set_servicename("supermario_rbs-frontend_fe001")
                asdf.set_monitorname("http-web1")
                NSLBMonitorServiceBinding.add(self.nitro, asdf)

        def delete_lbmonitor(self):
                asdf = NSLBMonitorServiceBinding()
                asdf.set_servicename("supermario_rbs-frontend_fe001")
                asdf.set_monitorname("http-web1")
                NSLBMonitorServiceBinding.delete(self.nitro, asdf)



def main():
        a = test_nitro({'ip':'10.40.11.162','user':'nsroot','password':'nsroot'})

#    a.add_server()

#    a.disable_server()
#    a.enable_server()

#    a.add_service()
        a.add_lbvserver()

#    a.bind_lbvserver()
#    a.print_lbvserver_binding()

#    a.add_servicegroup()
#    a.delete_servicegroup()

#    a.delete_binding()
        a.delete_lbvserver()
#    a.update_service()
#    a.disable_service()
#    a.enable_service()
#    a.rename_service()
#    a.delete_service()
#    a.delete_server()
#    a.list_hanodes()
        #a.add_vlan()
        #a.bind_vlan_to_if()
        #a.add_ip()
        #a.bind_vlan_to_ip()
        #a.list_vlan_ip_bindings()
        #a.list_vlan_if_bindings()
        #a.delete_vifb()
        #a.delete_vipb()
        #a.delete_vlan()
        #a.enable_feature()
        #a.add_cspolicy()
        #a.add_rewriteaction()
        #a.add_lbmonitor()
        #a.delete_lbmonitor()
        #a.disable_feature()
#    a.list_vlans()
#    a.delete_vlan()
#    a.list_vlans()

#        a.delete_ip()
#        a.list_ips()

if __name__ == '__main__':
        main()
