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

                # get service test

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
                vlan.set_id(115)
                NSVLAN.add(self.nitro, vlan)

        def delete_vlan(self):
                vlan = NSVLAN()
                vlan.set_id(115)
                NSVLAN.delete(self.nitro, vlan)

        def list_ips(self):
                ips = NSIP.get_all(self.nitro)
                for ip in ips:
                        print ip.get_ipaddress()

        def add_ip(self):
                ip = NSIP()
                ip.set_ipaddress('10.40.11.174')
                ip.set_netmask('255.255.255.224')
                ip.set_type('MIP')
                ip.set_mgmtaccess('enabled')
                ip.set_vserver('disabled')
                NSIP.add(self.nitro, ip)

        def delete_ip(self):
                ip = NSIP()
                ip.set_ipaddress('10.40.11.174')
                NSIP.delete(self.nitro, ip)


def main():
        a = test_nitro({'ip':'10.40.11.173','user':'nsroot','password':'nsroot'})

#    a.add_server()

#    a.disable_server()
#    a.enable_server()

#    a.add_service()
#    a.add_lbvserver()

#    a.bind_lbvserver()
#    a.print_lbvserver_binding()

#    a.add_servicegroup()
#    a.delete_servicegroup()

#    a.delete_binding()
#    a.delete_lbvserver()
#    a.update_service()
#    a.disable_service()
#    a.enable_service()
#    a.rename_service()
#    a.delete_service()
#    a.delete_server()
#    a.list_hanodes()
#    a.add_vlan()
#    a.list_vlans()
#    a.delete_vlan()
#    a.list_vlans()

        a.delete_ip()
        a.list_ips()

if __name__ == '__main__':
        main()
