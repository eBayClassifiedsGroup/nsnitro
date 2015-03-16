#!/usr/bin/env python
#
# Netscaler NITRO controller
#
# import the necessary libraries
import argparse
import getpass
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
from nsnitro.nsresources.nshanode import NSHANode
from nsnitro.nsresources.nsservicegroupserverbinding import NSServiceGroupServerBinding
from nsnitro.nsresources.nslbvserverservicebinding import NSLBVServerServiceBinding


def action_getprimarylb(args):
        ha_node = NSHANode()
        for node in ha_node.get_all(nitro):
                state = node.get_state().lower()
                if state == 'primary':
                        print(node.get_ipaddress())
                        break

def action_get(args, nitro):
        if args.object == "csvserver":
                csvserver = NSCSVServer()
                csvserver.set_name(args.object_name)
                csvserver = NSCSVServer.get(nitro, csvserver)
                print "--- CS vserver: " + csvserver.get_name() + " ---"
                for k in sorted(csvserver.options.iterkeys(), key=lambda k: k):
                        print "\t%s: %s" % (k, csvserver.options[k])

        if args.object == "lbvserver":
                lbvserver = NSLBVServer()
                lbvserver.set_name(args.object_name)
                lbvserver = NSLBVServer.get(nitro, lbvserver)
                print "--- LB vserver: " + lbvserver.get_name() + " ---"
                for k in sorted(lbvserver.options.iterkeys(), key=lambda k: k):
                        print "\t%s: %s" % (k, lbvserver.options[k])

        if args.object == "server":
                server = NSServer()
                server.set_name(args.object_name)
                server = NSServer.get(nitro, server)
                print "--- Server: " + server.get_name() + " ---"
                for k in sorted(server.options.iterkeys(), key=lambda k: k):
                        print "\t%s: %s" % (k, server.options[k])

        if args.object == "service":
                service = NSService()
                service.set_name(args.object_name)
                service = NSService.get(nitro, service)

                print "--- Service: " + service.get_name() + " ---"
                for k in sorted(service.options.iterkeys(), key=lambda k: k):
                        print "\t%s: %s" % (k, service.options[k])


def action_addservice(args, nitro):
        service = NSService()
        service.set_port(args.port)
        service.set_servicetype(args.servicetype)
        service.set_clttimeout(args.clttimeout)
        service.set_svrtimeout(args.svrtimeout)
        service.set_name(args.service)
        service.set_servername(args.target)
        NSService.add(nitro, service)
        print "Service '%s:%d/%s' was added to '%s'." % (args.service, args.port, args.servicetype, args.target)


def action_addlbvserver(args, nitro):
        lbvserver = NSLBVServer()
        lbvserver.set_name(args.lbvserver)
        lbvserver.set_ipv46(args.ip)
        lbvserver.set_port(args.port)
        lbvserver.set_clttimeout(args.clttimeout)
        lbvserver.set_persistencetype(args.persistencetype)
        lbvserver.set_servicetype(args.servicetype)
        NSLBVServer.add(nitro, lbvserver)
        print "lb vserver %s (%s:%d/%s) was added" % (args.lbvserver, args.ip, args.port, args.servicetype)


def action_enable(args, nitro):
        if args.object == "csvserver":
                csvserver = NSCSVServer()
                csvserver.set_name(args.object_name)
                NSCSVServer.enable(nitro, csvserver)
                print "Enabled cs vserver: %s" % args.object_name

        if args.object == "lbvserver":
                lbvserver = NSLBVServer()
                lbvserver.set_name(args.object_name)
                NSLBVServer.enable(nitro, lbvserver)
                print "Enabled lb vserver: %s" % args.object_name

        if args.object == "server":
                server = NSServer()
                server.set_name(args.object_name)
                NSServer.enable(nitro, server)
                print "Enabled server: %s" % args.object_name

        if args.object == "service":
                service = NSService()
                service.set_name(args.object_name)
                NSService.enable(nitro, service)
                print "Enabled service: %s" % args.object_name


def action_disable(args, nitro):
        if args.object == "csvserver":
                csvserver = NSCSVServer()
                csvserver.set_name(args.object_name)
                NSCSVServer.disable(nitro, csvserver)
                print "Disabled cs vserver: %s" % args.object_name

        if args.object == "lbvserver":
                lbvserver = NSLBVServer()
                lbvserver.set_name(args.object_name)
                NSLBVServer.disable(nitro, lbvserver)
                print "Disabled lb vserver: %s" % args.object_name

        if args.object == "server":
                server = NSServer()
                server.set_name(args.object_name)
                server.set_delay(args.delay)
                server.set_graceful(args.graceful)
                NSServer.disable(nitro, server)
                print "Disabled server: %s" % args.object_name

        if args.object == "service":
                service = NSService()
                service.set_name(args.object_name)
                service.set_delay(args.delay)
                service.set_graceful(args.graceful)
                NSService.disable(nitro, service)
                print "Disabled service: %s" % args.object_name


def action_rename(args, nitro):
        if args.object == "csvserver":
                csvserver = NSCSVServer()
                csvserver.set_name(args.object_name)
                csvserver.set_newname(args.newname)
                NSCSVServer.rename(nitro, csvserver)
                print "Renamed CS vserver from '%s' to '%s'." % (args.object_name, args.newname)

        if args.object == "lbvserver":
                lbvserver = NSLBVServer()
                lbvserver.set_name(args.object_name)
                lbvserver.set_newname(args.newname)
                NSLBVServer.rename(nitro, lbvserver)
                print "Renamed LB vserver from '%s' to '%s'." % (args.object_name, args.newname)

        if args.object == "server":
                server = NSServer()
                server.set_name(args.object_name)
                server.set_newname(args.newname)
                NSServer.rename(nitro, server)
                print "Renamed server from '%s' to '%s'." % (args.object_name, args.newname)

        if args.object == "service":
                service = NSService()
                service.set_name(args.object_name)
                service.set_newname(args.newname)
                NSService.rename(nitro, service)
                print "Renamed service from '%s' to '%s'." % (args.object_name, args.newname)


def action_list(args, nitro):
        if args.object == "csvserver":
                vservers = NSCSVServer().get_all(nitro)
                print "-- Configured CS vservers ---"
                for vserver in sorted(vservers, key=lambda k: k.get_name()):
                        print "\t" + vserver.get_name()

        if args.object == "lbvserver":
                vservers = NSLBVServer().get_all(nitro)
                print "-- Configured LB vservers ---"
                for vserver in sorted(vservers, key=lambda k: k.get_name()):
                        print "\t" + vserver.get_name()

        if args.object == "server":
                servers = NSServer().get_all(nitro)
                print "-- Configured servers ---"
                for server in sorted(servers, key=lambda k: k.get_name()):
                        print "\t" + server.get_name()

        if args.object == "service":
                services = NSService().get_all(nitro)
                print "-- Configured services ---"
                for service in sorted(services, key=lambda k: k.get_name()):
                        print "\t" + service.get_name()


def action_status(args, nitro):
        if args.object == "csvserver":
                vservers = NSCSVServer().get_all(nitro)
                print "-- Configured CS vservers (with status) ---"
                for vserver in sorted(vservers, key=lambda k: k.get_name()):
                        print vserver.get_name() + ": " + vserver.get_curstate()

        if args.object == "lbvserver":
                vservers = NSLBVServer().get_all(nitro)
                print "-- Configured LB vservers (with status) ---"
                for vserver in sorted(vservers, key=lambda k: k.get_name()):
                        print vserver.get_name() + ": " + vserver.get_effectivestate()

        if args.object == "server":
                servers = NSServer().get_all(nitro)
                print "-- Configured servers (with status) ---"
                for server in sorted(servers, key=lambda k: k.get_name()):
                        print "\t" + server.get_name() + ": " + server.get_state()

        if args.object == "service":
                services = NSService().get_all(nitro)
                print "-- Configured services (with status) ---"
                for service in sorted(services, key=lambda k: k.get_name()):
                        print "\t" + service.get_name() + ": " + service.get_svrstate()


def action_statusfull(args, nitro):
        binding = NSLBVServerServiceBinding()
        binding.set_name(args.object_name)
        binded_services = NSLBVServerServiceBinding().get(nitro, binding)
        print "-- | VServerName | Servicename | State | Type | IP | Port | Weight | ---"
        for s in binded_services:
                print ' | ', s.get_name(), ' | ', s.get_servicename(), ' | ', s.get_curstate(),
                print ' | ', s.get_servicetype(), ' | ', s.get_ipv46(), ' | ', s.get_port(),
                print ' | ', s.get_weight()


def action_saveconfig(args, nitro):
        NSConfig.save(nitro)
        print "Saved Netscaler configuration"


def action_bindserver(args, nitro):
        svcgrpbinding = NSServiceGroupServerBinding()
        svcgrpbinding.set_servername(args.server)
        svcgrpbinding.set_servicegroupname(args.servicegroup)
        svcgrpbinding.set_port(args.serviceport)
        try:
                NSServiceGroupServerBinding.add(nitro, svcgrpbinding)
                print "bound server %s to service group %s on port %s" % (
                        args.servername, args.servicegroupname, args.serviceport)
        except nsnitro.nsexceptions.nsexceptions.NSNitroNserrExist as e:
                print "Error: ", e.message


def action_unbindserver(args, nitro):
        svcgrpbinding = NSServiceGroupServerBinding()
        svcgrpbinding.set_servername(args.server)
        svcgrpbinding.set_servicegroupname(args.servicegroup)
        svcgrpbinding.set_port(args.serviceport)
        try:
                NSServiceGroupServerBinding.delete(nitro, svcgrpbinding)
                print "unbound server %s from service group %s on port %s" % (
                        args.servername, args.servicegroupname, args.serviceport)
        except nsnitro.nsexceptions.nsexceptions.NSNitroNserrNoent as e:
                print "Error: ", e.message


def action_bindservice(args, nitro):
        binding = NSLBVServerServiceBinding()
        binding.set_weight(args.bindingweight)
        binding.set_servicename(args.service)
        binding.set_name(args.lbvserver)
        NSLBVServerServiceBinding.add(nitro, binding)
        print "Service '%s' was binded to LB vserver '%s' with weight %d." % (
                args.service, args.lbvserver, args.bindingweight)


def action_unbindservice(args, nitro):
        raise NotImplementedError


def action_acl(args, nitro):
        if args.action == "get":
                acl = NSAcl()
                acl.set_aclname(args.name)
                acl = NSAcl.get(nitro, acl)

                print "--- ACL: " + acl.get_aclname() + " ---"
                for k in sorted(acl.options.iterkeys(), key=lambda k: k):
                        print "\t%s: %s" % (k, acl.options[k])


        if args.action == "list":
                acls = NSAcl().get_all(nitro)
                print "-- Configured ACLs ---"
                for acl in sorted(acls, key=lambda k: k.get_aclname()):
                        print "\t" + acl.get_aclname()

        if args.action == "apply":
                NSAcls.apply(nitro)
                print "Applied all ACLs to netscaler kernel."

        if args.action == "clear":
                NSAcls.clear(nitro)
                print "Cleared ACLs on the netscaler."

        if args.action == "renumber":
                NSAcls.renumber(nitro)
                print "Renumbered ACLs on the netscaler."

        if args.action == "delete":
                if not args.name:
                        print("--name required for deletion")
                else:
                        acl = NSAcl()
                        acl.set_aclname(args.delacl)
                        acl = NSAcl.delete(nitro, acl)
                        print "ACL '%s' was deleted. Do not forget to run --applyacls to activate it." % (args.name)


if __name__ == "__main__":
        OBJECTS = ("csvserver", "lbvserver", "server", "service")

        parser = argparse.ArgumentParser(description='Netscaler NITRO controller')
        # Top-level optional arguments
        parser.add_argument('lbip', metavar='IP', help='lb ip address')
        parser.add_argument('--user', metavar='USERNAME', help='lb username')
        parser.add_argument('--password', metavar='PASSWORD', help='lb password')
        parser.add_argument('--ssl', action="store_true", help='turns SSL on')

        # Parent Parsers
        pp_objects = argparse.ArgumentParser(add_help=False)
        pp_objects.add_argument('object', choices=OBJECTS, help="Object type to operate on")
        pp_objects.add_argument('object_name', metavar="OBJECTNAME", help="Name of object")

        pp_list = argparse.ArgumentParser(add_help=False)
        pp_list.add_argument('object', choices=OBJECTS, help="Object type to list")

        pp_addservice = argparse.ArgumentParser(description="Add a service to a lbvserver", add_help=False)
        pp_addservice.add_argument('service', metavar='NAME', help='name of service to add')
        pp_addservice.add_argument('target', metavar='LBVSERVER', help='target lbvserver to add it to')
        pp_addservice.add_argument('--persistence', metavar='TYPE', default='NONE',
                                   help='persistence type (none by default)')
        pp_addservice.add_argument('ip', metavar='IP', help='IP address')
        pp_addservice.add_argument('port', metavar='PORT', help='port number')
        pp_addservice.add_argument('--clttimeout', metavar='CLTTIMEOUT', default=9000,
                                   help='Clt timeout (9000 by default')
        pp_addservice.add_argument('--svrtimeout', metavar='SRVTIMEOUT', default=9000,
                                   help='service timeout (9000 by default')
        pp_addservice.add_argument('--servicetype', metavar='TYPE', choices=['TCP', 'HTTP'], default='TCP',
                                   help='Service type, TCP by default')

        pp_addlbvserver = argparse.ArgumentParser(description="Add a service to a lbvserver", add_help=False)
        pp_addlbvserver.add_argument('lbvserver', metavar='NAME', help='name of lbvserver to add')
        pp_addlbvserver.add_argument('ip', metavar='IP', help='IP address')
        pp_addlbvserver.add_argument('port', metavar='PORT', help='port number')
        pp_addlbvserver.add_argument('--persistencetype', metavar='PERSISTENCETYPE', default='NONE',
                                     help='persistence type')
        pp_addlbvserver.add_argument('--clttimeout', metavar='CLTTIMEOUT', default=9000, help='Clt timeout')
        pp_addlbvserver.add_argument('--servicetype', metavar='SERVICETYPE', choices=['TCP', 'HTTP'], default='TCP',
                                     help='Service type')

        pp_bindservice = argparse.ArgumentParser(description="Bind a service to a lbvserver", add_help=False)
        pp_bindservice.add_argument('service', metavar='SERVICENAME', help='service to bind')
        pp_bindservice.add_argument('lbvserver', metavar='LBVSERVERNAME', help='lbvserver to bind to')
        pp_bindservice.add_argument('--bindingweight', metavar='BINDINGWIIGHT', default=40,
                                    help='weight parameter for binding service')

        pp_bindserver = argparse.ArgumentParser(description="Bind a server to a service group", add_help=False)
        pp_bindserver.add_argument('server', metavar='SERVERNAME', help='server to bind')
        pp_bindserver.add_argument('servicegroup', metavar='SERVICEGROUPNAME',
                                   help='service group object to bind to')
        pp_bindserver.add_argument('--serviceport', required=True, help='service port')

        pp_disable = argparse.ArgumentParser(description="Disable parameters", add_help=False)
        pp_disable.add_argument('--delay', metavar='DELAY', help='Delay in seconds', default=None)
        pp_disable.add_argument('--graceful', metavar='GRACEFUL', choices=['YES', 'NO'], default='NO',
                                help='Graceful YES | NO')

        pp_rename = argparse.ArgumentParser(description="Rename an object", add_help=False)
        pp_rename.add_argument('newname', metavar='NEWNAME', help="New name for object")

        pp_acl = argparse.ArgumentParser(description="ACL operations", add_help=False)
        pp_acl.add_argument('action', choices=['get', 'list', 'apply', 'clear', 'renumber', 'delete'],
                            help="Action to perform")
        pp_acl.add_argument('--name', metavar="ACLNAME", help="Name of acl when getting/deleting", default=None)

        pp_statusfull = argparse.ArgumentParser(description="Print more detailed lbvserver status", add_help=False)
        pp_statusfull.add_argument('object_name', metavar="LBVSERVERNAME", help="Name of lbvserver")


        # Subparsers
        subparsers = parser.add_subparsers(dest="context")
        sp_get = subparsers.add_parser('get', parents=[pp_objects], help="Get information about an object")
        sp_addlbvserver = subparsers.add_parser('addlbvserver', parents=[pp_addlbvserver], help="Add an lbvserver")
        sp_addservice = subparsers.add_parser('addservice', parents=[pp_addservice], help="Add a service")
        sp_enable = subparsers.add_parser('enable', parents=[pp_objects], help="Enable an object")
        sp_disable = subparsers.add_parser('disable', parents=[pp_objects, pp_disable], help="Disable an object")
        sp_rename = subparsers.add_parser('rename', parents=[pp_objects, pp_rename], help="Rename an object")
        sp_list = subparsers.add_parser('list', parents=[pp_list], help="Get a list of objects")
        sp_status = subparsers.add_parser('status', parents=[pp_list], help="Get status of an object")
        sp_saveconfig = subparsers.add_parser('saveconfig', help="save load balancer config")
        sp_getprimarylb = subparsers.add_parser('getprimarylb', parents=[])
        sp_bindservice = subparsers.add_parser('bindservice', parents=[pp_bindservice],
                                               help="Bind a service to a lbvserver")
        sp_unbindservice = subparsers.add_parser('unbindservice', parents=[pp_bindservice],
                                                 help="Unbind a service from a lbvserver")
        sp_bindserver = subparsers.add_parser('bindserver', parents=[pp_bindserver],
                                              help="Bind a server to a servicegroup")
        sp_unbindserver = subparsers.add_parser('unbindserver', parents=[pp_bindserver],
                                                help="Unbind a server from a servicegroup")
        sp_statusfull = subparsers.add_parser('statusfull', parents=[pp_statusfull], help="Get full status")
        sp_acl = subparsers.add_parser('acl', parents=[pp_acl], help="ACL operations")


        # Set functions
        sp_get.set_defaults(func=action_get)
        sp_addlbvserver.set_defaults(func=action_addlbvserver)
        sp_addservice.set_defaults(func=action_addservice)
        sp_enable.set_defaults(func=action_enable)
        sp_disable.set_defaults(func=action_disable)
        sp_rename.set_defaults(func=action_rename)
        sp_list.set_defaults(func=action_list)
        sp_status.set_defaults(func=action_status)
        sp_saveconfig.set_defaults(func=action_saveconfig)
        sp_getprimarylb.set_defaults(func=action_getprimarylb)
        sp_bindservice.set_defaults(func=action_bindservice)
        sp_unbindservice.set_defaults(func=action_unbindservice)
        sp_bindserver.set_defaults(func=action_bindserver)
        sp_unbindserver.set_defaults(func=action_unbindserver)
        sp_statusfull.set_defaults(func=action_statusfull)
        sp_acl.set_defaults(func=action_acl)
        args = parser.parse_args()

        if not args.user:
                user = getpass.getuser()
        else:
                user = args.user

        if not args.password:
                password = getpass.getpass("{0}@{1}'s password: ".format(user, args.lbip))
        else:
                password = args.password

        nitro = NSNitro(args.lbip, user, password, args.ssl)

        try:
                nitro.login()
        except NSNitroError, e:
                print("Error: %s" % e.message)
                sys.exit(1)

        try:
                args.func(args, nitro)
        finally:
                nitro.logout()
                sys.exit(0)
