#!/usr/bin/env python
#import the necessary libraries
import argparse
import sys
import nsnitro
from nsutil import *
from nsresources.nslbvserver import NSLBVServer
from nsresources.nsservice import NSService
from nsresources.nsserver import NSServer

if __name__ == "__main__":
        parser = argparse.ArgumentParser(description='Netscaler NITRO controller')
        parser.add_argument('--lbip', metavar='IP', required=True, help='lb ip address')
        parser.add_argument('--user', metavar='USERNAME', default='api_user', help='lb username')
        parser.add_argument('--password', metavar='PASSWORD', default='api_user', help='lb password')

        parser.add_argument('--enablelbvserver', metavar='VSERVERNAME', help='enable lb vserver')
        parser.add_argument('--disablelbvserver', metavar='VSERVERNAME', help='disable lb vserver')
        parser.add_argument('--renamelbvserver', metavar=('NAME', 'NEWNAME'), nargs=2, help='rename lb vserver from NAME to NEWNAME')
        parser.add_argument('--getlbvserver', metavar='NAME', help='show lb vserver')
        parser.add_argument('--getlbvserverslist', action='store_true', help='show lb vservers list')
        parser.add_argument('--getlbvserverstatus', metavar='NAME', help='show lb vserver status')
        parser.add_argument('--getlbvserversstatus', action='store_true', help='show lb vservers status')

        parser.add_argument('--enableservice', metavar='SERVICENAME', help='enable service')
        parser.add_argument('--disableservice', metavar='SERVICENAME', help='disable service')
        parser.add_argument('--renameservice', metavar=('NAME', 'NEWNAME'), nargs=2, help='rename service from NAME to NEWNAME')

        parser.add_argument('--getservice', metavar='SERVICENAME', help='show service')
        parser.add_argument('--getservicestatus', metavar='SERVICENAME', help='show service status')
        parser.add_argument('--getserviceslist', action='store_true', help='show services list')
        parser.add_argument('--getservicesstatus', action='store_true', help='show services status')

        parser.add_argument('--getserver', metavar='SERVERNAME', help='show server')
        parser.add_argument('--getserverslist', action='store_true', help='show servers list')
        parser.add_argument('--getserversstatus', action='store_true', help='show servers status')
        parser.add_argument('--enableserver', metavar='SERVERNAME', help='enable server')
        parser.add_argument('--disableserver', metavar='SERVERNAME', help='disable server')
        parser.add_argument('--renameserver', metavar=('NAME', 'NEWNAME'), nargs=2, help='rename server from NAME to NEWNAME')

        parser.add_argument('--dargs', action='store_true', help='show service')
        args = parser.parse_args()

        if args.dargs:
                print(args)
                sys.exit(0)

        nitro = nsnitro.NSNitro(args.lbip, args.user, args.password)

        try:
                nitro.login()

                if args.enablelbvserver:
                        lbvserver = NSLBVServer()
                        lbvserver.set_name(args.enablelbvserver)
                        NSLBVServer.enable(nitro, lbvserver)
                        print "Enabled vserver: %s" % args.enablelbvserver
                        sys.exit(0)

                if args.disablelbvserver:
                        lbvserver = NSLBVServer()
                        lbvserver.set_name(args.disablelbvserver)
                        NSLBVServer.disable(nitro, lbvserver)
                        print "Disabled vserver: %s" % args.disablelbvserver
                        sys.exit(0)

                if args.getlbvserver:
                        lbvserver = NSLBVServer()
                        lbvserver.set_name(args.getlbvserver)
                        lbvserver = NSLBVServer.get(nitro, lbvserver)
                        print "--- LB vserver: " + lbvserver.get_name() + " ---"
                        for k in sorted(lbvserver.options.iterkeys(), key=lambda k: k):
                                print "\t%s: %s" % (k, lbvserver.options[k])

                        sys.exit(0)

                if args.enableservice:
                        service = NSService()
                        service.set_name(args.enableservice)
                        NSService.enable(nitro, service)
                        print "Enabled service: %s" % args.enableservice
                        sys.exit(0)

                if args.disableservice:
                        service = NSService()
                        service.set_name(args.disableservice)
                        NSService.disable(nitro, service)
                        print "Disabled service: %s" % args.disableservice
                        sys.exit(0)

                if args.getservice:
                        service = NSService()
                        service.set_name(args.getservice)
                        service = NSService.get(nitro, service)

                        print "--- Service: " + service.get_name() + " ---"
                        for k in sorted(service.options.iterkeys(), key=lambda k: k):
                                print "\t%s: %s" % (k, service.options[k])

                        sys.exit(0)

                if args.getserviceslist:
                        services = NSService().get_all(nitro)
                        print "-- Configured services ---"
                        for service in sorted(services, key=lambda k: k.get_name()):
                                print "\t" + service.get_name()
                        sys.exit(0)

                if args.getlbvserverslist:
                        vservers = NSLBVServer().get_all(nitro)
                        print "-- Configured LB vservers ---"
                        for vserver in sorted(vservers, key=lambda k: k.get_name()):
                                print "\t" + vserver.get_name()
                        sys.exit(0)

                if args.getservicesstatus:
                        services = NSService().get_all(nitro)
                        print "-- Configured services (with status) ---"
                        for service in sorted(services, key=lambda k: k.get_name()):
                                print "\t" + service.get_name() + ": " + service.get_svrstate()
                        sys.exit(0)

                if args.getlbvserversstatus:
                        vservers = NSLBVServer().get_all(nitro)
                        print "-- Configured LB vservers (with status) ---"
                        for vserver in sorted(vservers, key=lambda k: k.get_name()):
                                print vserver.get_name() + ": " + vserver.get_effectivestate()
                        sys.exit(0)

                if args.getlbvserverstatus:
                        vserver = NSLBVServer()
                        vserver.set_name(args.getlbvserverstatus)
                        vserver = NSLBVServer().get(nitro, vserver)
                        print vserver.get_name() + ": " + vserver.get_effectivestate()
                        sys.exit(0)

                if args.getservicestatus:
                        service = NSService()
                        service.set_name(args.getservicestatus)
                        service = NSService.get(nitro, service)
                        print service.get_name() + ": " + service.get_svrstate()
                        sys.exit(0)


                if args.enableserver:
                        server = NSServer()
                        server.set_name(args.enableserver)
                        NSServer.enable(nitro, server)
                        print "Enabled server: %s" % args.enableserver
                        sys.exit(0)

                if args.disableserver:
                        server = NSServer()
                        server.set_name(args.disableserver)
                        NSServer.disable(nitro, server)
                        print "Disabled server: %s" % args.disableserver
                        sys.exit(0)

                if args.getserver:
                        server = NSServer()
                        server.set_name(args.getserver)
                        server = NSServer.get(nitro, server)
                        print "--- Server: " + server.get_name() + " ---"
                        for k in sorted(server.options.iterkeys(), key=lambda k: k):
                                print "\t%s: %s" % (k, server.options[k])
                        sys.exit(0)


                if args.getserverslist:
                        servers = NSServer().get_all(nitro)
                        print "-- Configured servers ---"
                        for server in sorted(servers, key=lambda k: k.get_name()):
                                print "\t" + server.get_name()
                        sys.exit(0)

                if args.getserversstatus:
                        servers = NSServer().get_all(nitro)
                        print "-- Configured servers (with status) ---"
                        for server in sorted(servers, key=lambda k: k.get_name()):
                                print "\t" + server.get_name() + ": " + server.get_state()
                        sys.exit(0)

                if args.renameservice:
                        service = NSService()
                        service.set_name(args.renameservice[0])
                        service.set_newname(args.renameservice[1])
                        NSService.rename(nitro, service)
                        print "Renamed service from '%s' to '%s'." % (args.renameservice[0], args.renameservice[1])
                        sys.exit(0)

                if args.renamelbvserver:
                        lbvserver = NSLBVServer()
                        lbvserver.set_name(args.renamelbvserver[0])
                        lbvserver.set_newname(args.renamelbvserver[1])
                        NSLBVServer.rename(nitro, lbvserver)
                        print "Renamed LB vserver from '%s' to '%s'." % (args.renamelbvserver[0], args.renamelbvserver[1])
                        sys.exit(0)

                if args.renameserver:
                        server = NSServer()
                        server.set_name(args.renameserver[0])
                        server.set_newname(args.renameserver[1])
                        NSServer.rename(nitro, server)
                        print "Renamed server from '%s' to '%s'." % (args.renameserver[0], args.renameserver[1])
                        sys.exit(0)

                print "No action specified. Exiting."
                sys.exit(0)
        except NSNitroError, e:
                print "Error: %s" % e.message
