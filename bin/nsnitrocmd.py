#!/usr/bin/env python
#
# Netscaler NITRO controller
#
#import the necessary libraries
import argparse
import sys
import nsnitro
from nsnitro.nsnitro import *
from nsnitro.nsresources.nsconfig import NSConfig
from nsnitro.nsutil import *
from nsnitro.nsresources.nslbvserver import NSLBVServer
from nsnitro.nsresources.nsservice import NSService
from nsnitro.nsresources.nsserver import NSServer
from nsnitro.nsresources.nscsvserver import NSCSVServer
from nsnitro.nsresources.nsacl import NSAcl
from nsnitro.nsresources.nsacls import NSAcls

if __name__ == "__main__":
        parser = argparse.ArgumentParser(description='Netscaler NITRO controller')
        parser.add_argument('--lbip', metavar='IP', required=True, help='lb ip address')
        parser.add_argument('--user', metavar='USERNAME', default='api_user', help='lb username')
        parser.add_argument('--password', metavar='PASSWORD', default='api_user', help='lb password')

        parser.add_argument('--addlbvserver', metavar='LBVSERVERNAME', help='enable lb vserver')
        parser.add_argument('--enablelbvserver', metavar='LBVSERVERNAME', help='enable lb vserver')
        parser.add_argument('--disablelbvserver', metavar='LBVSERVERNAME', help='disable lb vserver')
        parser.add_argument('--renamelbvserver', metavar=('LBVSERVERNAME', 'NEWNAME'), nargs=2, help='rename lb vserver from NAME to NEWNAME')

        parser.add_argument('--getlbvserver', metavar='LBVSERVERNAME', help='show lb vserver')
        parser.add_argument('--getlbvserverslist', action='store_true', help='show lb vservers list')
        parser.add_argument('--getlbvserverstatus', metavar='LBVSERVERNAME', help='show lb vserver status')
        parser.add_argument('--getlbvserverstatusfull', metavar='LBVSERVERNAME', help='show lb vserver status with bound services')
        parser.add_argument('--getlbvserversstatus', action='store_true', help='show lb vservers status')

        parser.add_argument('--enablecsvserver', metavar='CSVSERVERNAME', help='enable cs vserver')
        parser.add_argument('--disablecsvserver', metavar='CSVSERVERNAME', help='disable cs vserver')
        parser.add_argument('--renamecsvserver', metavar=('CSVSERVERNAME', 'NEWNAME'), nargs=2, help='rename cs vserver from NAME to NEWNAME')
        parser.add_argument('--getcsvserver', metavar='CSVSERVERNAME', help='show cs vserver')
        parser.add_argument('--getcsvserverslist', action='store_true', help='show cs vservers list')
        parser.add_argument('--getcsvserverstatus', metavar='CSVSERVERNAME', help='show cs vserver status')
        parser.add_argument('--getcsvserversstatus', action='store_true', help='show cs vservers status')

        parser.add_argument('--addservice', metavar=('SERVICENAME', 'LBVSERVERNAME'), nargs=2, help='add service SERVICENAME to lb vserver LBVSERVERNAME (ip and port also requires)')
        parser.add_argument('--enableservice', metavar='SERVICENAME', help='enable service')
        parser.add_argument('--disableservice', metavar='SERVICENAME', help='disable service')
        parser.add_argument('--renameservice', metavar=('NAME', 'NEWNAME'), nargs=2, help='rename service from NAME to NEWNAME')

        parser.add_argument('--getservice', metavar='SERVICENAME', help='show service')
        parser.add_argument('--getservicestatus', metavar='SERVICENAME', help='show service status')
        parser.add_argument('--getserviceslist', action='store_true', help='show services list')
        parser.add_argument('--getservicesstatus', action='store_true', help='show services status')
        parser.add_argument('--bindservice', metavar=('SERVICENAME', 'LBVSERVERNAME'), nargs=2, help='bind service SERVICENAME to lb vserver LBVSERVERNAME ')

        parser.add_argument('--getserver', metavar='SERVERNAME', help='show server')
        parser.add_argument('--getserverslist', action='store_true', help='show servers list')
        parser.add_argument('--getserversstatus', action='store_true', help='show servers status')
        parser.add_argument('--enableserver', metavar='SERVERNAME', help='enable server')
        parser.add_argument('--disableserver', metavar='SERVERNAME', help='disable server')
        parser.add_argument('--renameserver', metavar=('NAME', 'NEWNAME'), nargs=2, help='rename server from NAME to NEWNAME')

        parser.add_argument('--saveconfig', action='store_true', help='save loadbalancer config')

        parser.add_argument('--dargs', action='store_true', help='show service')
        # additional arguments
        parser.add_argument('--port', metavar='PORT', help='port number')
        parser.add_argument('--ip', metavar='IP', help='IP address')
        parser.add_argument('--servicetype', metavar='SERVICETYPE', choices=['TCP','HTTP'], default='TCP', help='Service type')
        parser.add_argument('--clttimeout', metavar='CLTTIMEOUT', default=9000, help='Clt timeout')
        parser.add_argument('--svrtimeout', metavar='SRVTIMEOUT', default=9000, help='service timeout')
        parser.add_argument('--persistencetype', metavar='PERSISTENCETYPE', default='NONE', help='persistence type')
        parser.add_argument('--bindingweight', metavar='BINDINGWIIGHT', default=40, help='weight parameter for binding service')

        # ACL related arguments
        parser.add_argument('--getacl', metavar='ACLNAME', help='show acl')
        parser.add_argument('--getaclslist', action='store_true', help='show acl list')
        parser.add_argument('--addacl', metavar='ACLNAME', help='add acl')
        parser.add_argument('--delacl', metavar='ACLNAME', help='del acl')
        parser.add_argument('--applyacls', action='store_true', help='apply acls to kernel')
        parser.add_argument('--clearacls', action='store_true', help='clear acls')
        parser.add_argument('--renumberacls', action='store_true', help='renumber acls')

        args = parser.parse_args()

        if args.dargs:
                print(args)
                sys.exit(0)

        nitro = NSNitro(args.lbip, args.user, args.password)

        try:
                nitro.login()

                if args.addlbvserver:
                        if not args.port or not args.ip:
                          print "--ip and --port are required for adding LB Vserver"
                          nitro.logout()
                          sys.exit(0)
                        lbvserver = NSLBVServer()
                        lbvserver.set_name(args.addlbvserver)
                        lbvserver.set_ipv46(args.ip)
                        lbvserver.set_port(args.port)
                        lbvserver.set_clttimeout(args.clttimeout)
                        lbvserver.set_persistencetype(args.persistencetype)
                        lbvserver.set_servicetype(args.servicetype)
                        NSLBVServer.add(nitro, lbvserver)
                        print "lb vserver %s (%s:%d/%s) was added" % (args.addlbvserver, args.ip, args.port, args.servicetype)
                        nitro.logout()
                        sys.exit(0)

                if args.enablelbvserver:
                        lbvserver = NSLBVServer()
                        lbvserver.set_name(args.enablelbvserver)
                        NSLBVServer.enable(nitro, lbvserver)
                        print "Enabled lb vserver: %s" % args.enablelbvserver
                        nitro.logout()
                        sys.exit(0)

                if args.saveconfig:
                        NSConfig.save(nitro)
                        print "Saved Netscaler configuration"
                        nitro.logout()
                        sys.exit(0)

                if args.disablelbvserver:
                        lbvserver = NSLBVServer()
                        lbvserver.set_name(args.disablelbvserver)
                        NSLBVServer.disable(nitro, lbvserver)
                        print "Disabled lb vserver: %s" % args.disablelbvserver
                        nitro.logout()
                        sys.exit(0)

                if args.getlbvserver:
                        lbvserver = NSLBVServer()
                        lbvserver.set_name(args.getlbvserver)
                        lbvserver = NSLBVServer.get(nitro, lbvserver)
                        print "--- LB vserver: " + lbvserver.get_name() + " ---"
                        for k in sorted(lbvserver.options.iterkeys(), key=lambda k: k):
                                print "\t%s: %s" % (k, lbvserver.options[k])

                        nitro.logout()
                        sys.exit(0)

                if args.enablecsvserver:
                        csvserver = NSCSVServer()
                        csvserver.set_name(args.enablecsvserver)
                        NSCSVServer.enable(nitro, csvserver)
                        print "Enabled cs vserver: %s" % args.enablecsvserver
                        nitro.logout()
                        sys.exit(0)

                if args.disablecsvserver:
                        csvserver = NSCSVServer()
                        csvserver.set_name(args.disablecsvserver)
                        NSCSVServer.disable(nitro, csvserver)
                        print "Disabled cs vserver: %s" % args.disablecsvserver
                        nitro.logout()
                        sys.exit(0)

                if args.getcsvserver:
                        csvserver = NSCSVServer()
                        csvserver.set_name(args.getcsvserver)
                        csvserver = NSCSVServer.get(nitro, csvserver)
                        print "--- CS vserver: " + csvserver.get_name() + " ---"
                        for k in sorted(csvserver.options.iterkeys(), key=lambda k: k):
                                print "\t%s: %s" % (k, csvserver.options[k])

                        nitro.logout()
                        sys.exit(0)

                if args.addservice:
                        if not args.port:
                          print "--port is required for adding service"
                          nitro.logout()
                          sys.exit(0)
                        service = NSService()
                        service.set_port(args.port)
                        service.set_servicetype(args.servicetype)
                        service.set_clttimeout(args.clttimeout)
                        service.set_svrtimeout(args.svrtimeout)
                        service.set_name(args.addservice[0])
                        service.set_servername(args.addservice[1])
                        NSService.add(nitro, addservice)
                        print "Service '%s:%d/%s' was added to '%s'." % (args.addservice[0], args.port, args.servicetype, args.addservice[1])
                        nitro.logout()
                        sys.exit(0)

                if args.bindservice:
                        binding = NSLBVServerServiceBinding()
                        binding.set_weight(args.bindingweight)
                        binding.set_servicename(args.bindservice[0])
                        binding.set_name(args.bindservice[1])
                        NSLBVServerServiceBinding.add(nitro, binding)
                        print "Service '%s' was binded to LB vserver '%s' with weight %d." % (args.bindservice[0], args.bindservice[1], args.bindingweight)
                        nitro.logout()
                        sys.exit(0)

                if args.enableservice:
                        service = NSService()
                        service.set_name(args.enableservice)
                        NSService.enable(nitro, service)
                        print "Enabled service: %s" % args.enableservice
                        nitro.logout()
                        sys.exit(0)

                if args.disableservice:
                        service = NSService()
                        service.set_name(args.disableservice)
                        NSService.disable(nitro, service)
                        print "Disabled service: %s" % args.disableservice
                        nitro.logout()
                        sys.exit(0)

                if args.getservice:
                        service = NSService()
                        service.set_name(args.getservice)
                        service = NSService.get(nitro, service)

                        print "--- Service: " + service.get_name() + " ---"
                        for k in sorted(service.options.iterkeys(), key=lambda k: k):
                                print "\t%s: %s" % (k, service.options[k])

                        nitro.logout()
                        sys.exit(0)

                if args.getserviceslist:
                        services = NSService().get_all(nitro)
                        print "-- Configured services ---"
                        for service in sorted(services, key=lambda k: k.get_name()):
                                print "\t" + service.get_name()
                        nitro.logout()
                        sys.exit(0)

                if args.getlbvserverslist:
                        vservers = NSLBVServer().get_all(nitro)
                        print "-- Configured LB vservers ---"
                        for vserver in sorted(vservers, key=lambda k: k.get_name()):
                                print "\t" + vserver.get_name()
                        nitro.logout()
                        sys.exit(0)

                if args.getcsvserverslist:
                        vservers = NSCSVServer().get_all(nitro)
                        print "-- Configured CS vservers ---"
                        for vserver in sorted(vservers, key=lambda k: k.get_name()):
                                print "\t" + vserver.get_name()
                        nitro.logout()
                        sys.exit(0)

                if args.getservicesstatus:
                        services = NSService().get_all(nitro)
                        print "-- Configured services (with status) ---"
                        for service in sorted(services, key=lambda k: k.get_name()):
                                print "\t" + service.get_name() + ": " + service.get_svrstate()
                        nitro.logout()
                        sys.exit(0)

                if args.getlbvserversstatus:
                        vservers = NSLBVServer().get_all(nitro)
                        print "-- Configured LB vservers (with status) ---"
                        for vserver in sorted(vservers, key=lambda k: k.get_name()):
                                print vserver.get_name() + ": " + vserver.get_effectivestate()
                        nitro.logout()
                        sys.exit(0)

                if args.getcsvserversstatus:
                        vservers = NSCSVServer().get_all(nitro)
                        print "-- Configured CS vservers (with status) ---"
                        for vserver in sorted(vservers, key=lambda k: k.get_name()):
                                print vserver.get_name() + ": " + vserver.get_curstate()
                        nitro.logout()
                        sys.exit(0)

                if args.getlbvserverstatus:
                        vserver = NSLBVServer()
                        vserver.set_name(args.getlbvserverstatus)
                        vserver = NSLBVServer().get(nitro, vserver)
                        print vserver.get_name() + ": " + vserver.get_effectivestate()
                        nitro.logout()
                        sys.exit(0)

                if args.getlbvserverstatusfull:
                        binding = NSLBVServerServiceBinding()
                        binding.set_name(args.getlbvserverstatusfull)
                        binded_services = NSLBVServerServiceBinding().get(nitro, binding)
                        print "-- | VServerName | Servicename | State | Type | IP | Port | Weight | ---"
                        for s in binded_services:
                            print ' | ', s.get_name(),        ' | ', s.get_servicename(), ' | ', s.get_curstate(),
                            print ' | ', s.get_servicetype(), ' | ', s.get_ipv46(),       ' | ', s.get_port(),
                            print ' | ', s.get_weight()
                        nitro.logout()
                        sys.exit(0)

                if args.getcsvserverstatus:
                        vserver = NSCSVServer()
                        vserver.set_name(args.getcsvserverstatus)
                        vserver = NSCSVServer().get(nitro, vserver)
                        print vserver.get_name() + ": " + vserver.get_curstate()
                        nitro.logout()
                        sys.exit(0)

                if args.getservicestatus:
                        service = NSService()
                        service.set_name(args.getservicestatus)
                        service = NSService.get(nitro, service)
                        print service.get_name() + ": " + service.get_svrstate()
                        nitro.logout()
                        sys.exit(0)


                if args.enableserver:
                        server = NSServer()
                        server.set_name(args.enableserver)
                        NSServer.enable(nitro, server)
                        print "Enabled server: %s" % args.enableserver
                        nitro.logout()
                        sys.exit(0)

                if args.disableserver:
                        server = NSServer()
                        server.set_name(args.disableserver)
                        NSServer.disable(nitro, server)
                        print "Disabled server: %s" % args.disableserver
                        nitro.logout()
                        sys.exit(0)

                if args.getserver:
                        server = NSServer()
                        server.set_name(args.getserver)
                        server = NSServer.get(nitro, server)
                        print "--- Server: " + server.get_name() + " ---"
                        for k in sorted(server.options.iterkeys(), key=lambda k: k):
                                print "\t%s: %s" % (k, server.options[k])
                        nitro.logout()
                        sys.exit(0)


                if args.getserverslist:
                        servers = NSServer().get_all(nitro)
                        print "-- Configured servers ---"
                        for server in sorted(servers, key=lambda k: k.get_name()):
                                print "\t" + server.get_name()
                        nitro.logout()
                        sys.exit(0)

                if args.getserversstatus:
                        servers = NSServer().get_all(nitro)
                        print "-- Configured servers (with status) ---"
                        for server in sorted(servers, key=lambda k: k.get_name()):
                                print "\t" + server.get_name() + ": " + server.get_state()
                        nitro.logout()
                        sys.exit(0)

                if args.renameservice:
                        service = NSService()
                        service.set_name(args.renameservice[0])
                        service.set_newname(args.renameservice[1])
                        NSService.rename(nitro, service)
                        print "Renamed service from '%s' to '%s'." % (args.renameservice[0], args.renameservice[1])
                        nitro.logout()
                        sys.exit(0)

                if args.renamelbvserver:
                        lbvserver = NSLBVServer()
                        lbvserver.set_name(args.renamelbvserver[0])
                        lbvserver.set_newname(args.renamelbvserver[1])
                        NSLBVServer.rename(nitro, lbvserver)
                        print "Renamed LB vserver from '%s' to '%s'." % (args.renamelbvserver[0], args.renamelbvserver[1])
                        nitro.logout()
                        sys.exit(0)

                if args.renamecsvserver:
                        csvserver = NSCSVServer()
                        csvserver.set_name(args.renamecsvserver[0])
                        csvserver.set_newname(args.renamecsvserver[1])
                        NSCSVServer.rename(nitro, csvserver)
                        print "Renamed CS vserver from '%s' to '%s'." % (args.renamecsvserver[0], args.renamecsvserver[1])
                        nitro.logout()
                        sys.exit(0)

                if args.renameserver:
                        server = NSServer()
                        server.set_name(args.renameserver[0])
                        server.set_newname(args.renameserver[1])
                        NSServer.rename(nitro, server)
                        print "Renamed server from '%s' to '%s'." % (args.renameserver[0], args.renameserver[1])
                        nitro.logout()
                        sys.exit(0)

                if args.getacl:
                        acl = NSAcl()
                        acl.set_aclname(args.getacl)
                        acl = NSAcl.get(nitro, acl)

                        print "--- ACL: " + acl.get_aclname() + " ---"
                        for k in sorted(acl.options.iterkeys(), key=lambda k: k):
                                print "\t%s: %s" % (k, acl.options[k])

                        nitro.logout()
                        sys.exit(0)

                if args.getaclslist:
                        acls = NSAcl().get_all(nitro)
                        print "-- Configured ACLs ---"
                        for acl in sorted(acls, key=lambda k: k.get_aclname()):
                                print "\t" + acl.get_aclname()
                        nitro.logout()
                        sys.exit(0)

                if args.applyacls:
                        NSAcls.apply(nitro)
                        print "Applied all ACLs to netscaler kernel."
                        nitro.logout()
                        sys.exit(0)

                if args.clearacls:
                        NSAcls.clear(nitro)
                        print "Cleared ACLs on the netscaler."
                        nitro.logout()
                        sys.exit(0)

                if args.renumberacls:
                        NSAcls.renumber(nitro)
                        print "Renumbered ACLs on the netscaler."
                        nitro.logout()
                        sys.exit(0)

                if args.delacl:
                        acl = NSAcl()
                        acl.set_aclname(args.delacl)
                        acl = NSAcl.delete(nitro, acl)
                        print "ACL '%s' was deleted. Do not forget to run --applyacls to activate it." % (args.delacl)
                        nitro.logout()
                        sys.exit(0)

                print "No action specified. Exiting."
                sys.exit(0)
        except NSNitroError, e:
                print "Error: %s" % e.message
