import sys
from nsnitro import *


class test_nitro:

<<<<<<< HEAD
    def __init__(self):
        self.nitro = NSNitro(
            '10.216.91.222',
            'nsroot',
            'nsroot',
            useSSL=False)

    def login(self):
        # Log in to Netscaler & create session
        try:
            return self.nitro.login()['message']
        except:
            return sys.exc_info()[1]

    def add_server(self):
        # Add server
        try:
            addserver = NSServer()
            addserver.set_name("nitro_example_server")
            addserver.set_ipaddress("10.32.110.99")
            NSServer.add(self.nitro, addserver)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def disable_server(self):
        # Disable server
        try:
            server = NSServer()
            server.set_name("nitro_example_server")
            NSServer.disable(self.nitro, server)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def enable_server(self):
        # Enable server
        try:
            server = NSServer()
            server.set_name("nitro_example_server")
            NSServer.enable(self.nitro, server)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def add_servicegroup(self):
        # Add servicegroup
        try:
            servicegroup = NSServiceGroup()
            servicegroup.set_servicegroupname("nitro_example_servicegroup")
            servicegroup.set_servicetype("http")
            NSServiceGroup.add(self.nitro, servicegroup)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def delete_servicegroup(self):
        # Delete servicegroup
        try:
            servicegroup = NSServiceGroup()
            servicegroup.set_servicegroupname('nitro_example_servicegroup')
            NSServiceGroup.delete(self.nitro, servicegroup)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def add_service(self):
        # Add service
        try:
            addservice = NSService()
            addservice.set_name("service_nitro_test")
            addservice.set_servername("nitro_example_server")
            addservice.set_servicetype("HTTP")
            addservice.set_port(11111)
            NSService.add(self.nitro, addservice)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def add_lbvserver(self):
        # Add load-balancing virtual server
        try:
            lbvserver = NSLBVServer()
            lbvserver.set_name("nitro_lbvserver_test")
            lbvserver.set_ipv46("10.32.110.55")
            lbvserver.set_port(11111)
            lbvserver.set_clttimeout(180)
            lbvserver.set_persistencetype("NONE")
            lbvserver.set_servicetype("HTTP")
            NSLBVServer.add(self.nitro, lbvserver)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def bind_lbvserver(self):
        # Bind service to load-balancing virtual server
        try:
            lbbinding = NSLBVServerServiceBinding()
            lbbinding.set_name('nitro_lbvserver_test')
            lbbinding.set_servicename("service_nitro_test")
            lbbinding.set_weight(40)
            NSLBVServerServiceBinding.add(self.nitro, lbbinding)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def list_lbvserver_binding(self):
        # List load-balanced service bindings
        try:
            lbbinding = NSLBVServerServiceBinding()
            lbbinding.set_name("nitro_lbvserver_test")
            lbbindings = NSLBVServerServiceBinding.get(self.nitro, lbbinding)
            lbb_list = []
            for lbb in lbbindings:
                lbb_list.append(lbb.get_servicename())
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def delete_binding(self):
        # Unbind service from load-balancing virtual server
        try:
            lbbinding = NSLBVServerServiceBinding()
            lbbinding.set_name("nitro_lbvserver_test")
            lbbinding.set_servicename("service_nitro_test")
            NSLBVServerServiceBinding.delete(self.nitro, lbbinding)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def delete_lbvserver(self):
        # Delete load-balancing virtual server
        try:
            lbvserver = NSLBVServer()
            lbvserver.set_name("nitro_lbvserver_test")
            NSLBVServer.delete(self.nitro, lbvserver)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def get_service(self):
        # Get info on a specific service
        try:
            service = NSService()
            service.set_name("service_nitro_test")
            NSService.get(self.nitro, service)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def update_service(self):
        # Update service
        try:
            service = NSService()
            service.set_name("service_nitro_test")
            service.set_comment("test comment")
            service.set_useproxyport("NO")
            NSService.update(self.nitro, service)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def disable_service(self):
        # Disable service
        try:
            service = NSService()
            service.set_name("service_nitro_test")
            NSService.disable(self.nitro, service)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def enable_service(self):
        # Enable service
        try:
            service = NSService()
            service.set_name("service_nitro_test")
            NSService.enable(self.nitro, service)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def rename_service(self):
        # Rename service
        try:
            service = NSService()
            service.set_name("service_nitro_test")
            service.set_newname("service_nitro_test_rename")
            NSService.rename(self.nitro, service)
            # Rename service back to original
            service = NSService()
            service.set_name("service_nitro_test_rename")
            service.set_newname("service_nitro_test")
            NSService.rename(self.nitro, service)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def delete_service(self):
        # Delete service
        try:
            service = NSService()
            service.set_name("service_nitro_test")
            NSService.delete(self.nitro, service)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def delete_server(self):
        # Delete server
        try:
            server = NSServer()
            server.set_name("nitro_example_server")
            NSServer.delete(self.nitro, server)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def list_hanodes(self):
        # List HA nodes
        try:
            hanodes = NSHANode.get_all(self.nitro)
            hanode_list = []
            for i in hanodes:
                hanode_list.append(i.get_id())
            if hanode_list is not None:
                return 'Passed'
            else:
                return 'Failed - empty list'
        except:
            return sys.exc_info()[1]

    def list_vlans(self):
        # List VLANs
        try:
            vlans = NSVLAN.get_all(self.nitro)
            vlan_list = []
            for vlan in vlans:
                vlan_list.append(vlan.get_id())
            if vlan_list is not None:
                return 'Passed'
            else:
                return 'Failed - empty list'
        except:
            return sys.exc_info()[1]

    def add_vlan(self):
        # Add VLAN
        try:
            vlan = NSVLAN()
            vlan.set_id(125)
            NSVLAN.add(self.nitro, vlan)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def delete_vlan(self):
        # Delete VLAN
        try:
            vlan = NSVLAN()
            vlan.set_id(125)
            NSVLAN.delete(self.nitro, vlan)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def list_ips(self):
        # List all IPs
        try:
            ips = NSIP.get_all(self.nitro)
            ip_list = []
            for ip in ips:
                ip_list.append(ip.get_ipaddress())
            if ip_list is not None:
                return 'Passed'
            else:
                return 'Failed - empty list'
        except:
            return sys.exc_info()[1]

    def list_vlan_if_bindings(self):
        # List VLAN/interface bindings
        try:
            vlans = NSVLAN.get_all(self.nitro)
            vifb_list = []
            for vlan in vlans:
                vifbs = NSVLANInterfaceBinding.get(self.nitro, vlan)
                vifb_list.append(vifbs)
            if vifb_list is not None:
                return 'Passed'
            else:
                return 'Failed - Empty list'
        except:
            return sys.exc_info()[1]

    def list_vlan_ip_bindings(self):
        # List VLAN/IP address bindings
        try:
            vlans = NSVLAN.get_all(self.nitro)
            vipb_list = []
            for vlan in vlans:
                vipbs = NSVLANNSIPBinding.get(self.nitro, vlan)
                vipb_list.append(vipbs)
            if vipb_list is not None:
                return 'Passed'
            else:
                return 'Failed - empty list'
        except:
            return sys.exc_info()[1]

    def add_ip(self):
        # Add IP address
        try:
            ip = NSIP()
            ip.set_ipaddress('10.40.12.181')
            ip.set_netmask('255.255.255.224')
            ip.set_vserver('disabled')
            NSIP.add(self.nitro, ip)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def delete_ip(self):
        # Delete IP address
        try:
            ip = NSIP()
            ip.set_ipaddress('10.40.12.181')
            NSIP.delete(self.nitro, ip)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def delete_vipb(self):
        # Unbind VLAN from IP address
        try:
            ip = NSVLANNSIPBinding()
            ip.set_id(125)
            ip.set_ipaddress('10.40.12.181')
            ip.set_netmask('255.255.255.224')
            NSVLANNSIPBinding.delete(self.nitro, ip)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def delete_vifb(self):
        # Unbind VLAN from interface
        try:
            ip = NSVLANInterfaceBinding()
            ip.set_id(125)
            ip.set_ifnum("1/1")
            NSVLANInterfaceBinding.delete(self.nitro, ip)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def bind_vlan_to_if(self):
        # Bind VLAN to interface
        try:
            vifb = NSVLANInterfaceBinding()
            vifb.set_id(125)
            vifb.set_ifnum("1/1")
            vifb.set_tagged(True)
            NSVLANInterfaceBinding.add(self.nitro, vifb)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def bind_vlan_to_ip(self):
        # Bind VLAN to IP address
        try:
            vipb = NSVLANNSIPBinding()
            vipb.set_id(125)
            vipb.set_ipaddress('10.40.12.181')
            vipb.set_netmask('255.255.255.224')
            NSVLANNSIPBinding.add(self.nitro, vipb)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def disable_feature(self):
        # Disable Netscaler feature
        try:
            feature = NSFeature()
            feature.set_feature(['CS', 'LB'])
            NSFeature.disable(self.nitro, feature)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def enable_feature(self):
        # Enable Netscaler feature
        try:
            feature = NSFeature()
            feature.set_feature(['CS', 'LB'])
            NSFeature.enable(self.nitro, feature)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def add_cspolicy(self):
        # Add content-switching policy
        try:
            cspol = NSCSPolicy()
            cspol.set_rule("CLIENT.IP.SRC.SUBNET(24).EQ(10.10.42.0)")
            cspol.set_policyname("test_policyname")
            NSCSPolicy.add(self.nitro, cspol)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def delete_cspolicy(self):
        # Delete content-switching policy
        try:
            cspol = NSCSPolicy()
            cspol.set_rule("CLIENT.IP.SRC.SUBNET(24).EQ(10.10.42.0)")
            cspol.set_policyname("test_policyname")
            NSCSPolicy.delete(self.nitro, cspol)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def add_rewriteaction(self):
        # Add rewrite action
        try:
            rewriteaction = NSRewriteAction()
            rewriteaction.set_name("test_rewrite_action")
            rewriteaction.set_type("insert_http_header")
            rewriteaction.set_target("ble")
            rewriteaction.set_stringbuilderexpr("CLIENT.IP.SRC")
            NSRewriteAction.add(self.nitro, rewriteaction)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def delete_rewriteaction(self):
        # Delete rewrite action
        try:
            rewriteaction = NSRewriteAction()
            rewriteaction.set_name("test_rewrite_action")
            NSRewriteAction.delete(self.nitro, rewriteaction)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def add_lbmonitor(self):
        # Add load-balancing monitor
        try:
            lbmon = NSLBMonitor()
            lbmon.set_monitorname("test_https")
            lbmon.set_type("HTTP")
            lbmon.set_httprequest("HEAD /")
            lbmon.set_rtsprequest("HEAD /")
            lbmon.set_respcode(["200"])
            lbmon.set_interval("5")
            lbmon.set_resptimeout("2")
            lbmon.set_resptimeoutthresh("0")
            NSLBMonitor.add(self.nitro, lbmon)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def update_lbmonitor(self):
        # Update load-balancing monitor
        try:
            lbmon = NSLBMonitor()
            lbmon.set_monitorname("test_https")
            lbmon.set_type("HTTP")
            lbmon.set_interval("60")
            lbmon.set_resptimeout("24")
            NSLBMonitor.update(self.nitro, lbmon)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def add_lbmonitorbinding(self):
        # Bind load-balancing monitor to a service
        try:
            lbmonbind = NSLBMonitorServiceBinding()
            lbmonbind.set_servicename("service_nitro_test")
            lbmonbind.set_monitorname("test_https")
            NSLBMonitorServiceBinding.add(self.nitro, lbmonbind)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def delete_lbmonitorbinding(self):
        # Unbind load-balancing monitor from a service
        try:
            lbmonbind = NSLBMonitorServiceBinding()
            lbmonbind.set_servicename("service_nitro_test")
            lbmonbind.set_monitorname("test_https")
            NSLBMonitorServiceBinding.delete(self.nitro, lbmonbind)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def delete_lbmonitor(self):
        # Delete load-balancing monitor
        try:
            lbmon = NSLBMonitor()
            lbmon.set_monitorname("test_https")
            lbmon.set_type("HTTP")
            NSLBMonitor.delete(self.nitro, lbmon)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def add_cmdpol(self):
        # Add command policy
        try:
            cmdpol = NSSystemCMDPolicy()
            cmdpol.set_action('ALLOW')
            cmdpol.set_policyname('nitro-cmdpol-test')
            cmdpol.set_cmdspec('show hardware')
            NSSystemCMDPolicy.add(self.nitro, cmdpol)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def update_cmdpol(self):
        # Update command policy
        try:
            cmdpol = NSSystemCMDPolicy()
            cmdpol.set_action('DENY')
            cmdpol.set_policyname('nitro-cmdpol-test')
            cmdpol.set_cmdspec('show lb vserver')
            NSSystemCMDPolicy.update(self.nitro, cmdpol)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def delete_cmdpol(self):
        # Delete command policy
        try:
            cmdpol = NSSystemCMDPolicy()
            cmdpol.set_policyname('nitro-cmdpol-test')
            NSSystemCMDPolicy.delete(self.nitro, cmdpol)
            return 'Passed'
        except:
            return sys.exc_info()[1]

    def logout(self):
        # Log out of Netscaler
        try:
            return self.nitro.logout()['message']
        except:
            return sys.exc_info()[1]
=======
        def __init__(self):
                self.nitro = NSNitro(
                    '10.216.91.222',
                    'nsroot',
                    'nsroot',
                    useSSL=False)

        def login(self):
                # Log in to Netscaler
                return self.nitro.login()

        def add_server(self):
                # Add server
                try:
                    addserver = NSServer()
                    addserver.set_name("nitro_example_server")
                    addserver.set_ipaddress("10.32.110.99")
                    return NSServer.add(self.nitro, addserver)
                except NSNitroError, nsresponse:
                    return NSNitroError(nsresponse.message)

        def disable_server(self):
                # Disable server
                try:
                    server = NSServer()
                    server.set_name("nitro_example_server")
                    return NSServer.disable(self.nitro, server)
                except NSNitroError, e:
                    raise e

        def enable_server(self):
                # Enable server
                server = NSServer()
                server.set_name("nitro_example_server")
                return NSServer.enable(self.nitro, server)

        def add_servicegroup(self):
                # Add servicegroup
                servicegroup = NSServiceGroup()
                servicegroup.set_servicegroupname("nitro_example_servicegroup")
                servicegroup.set_servicetype("http")
                return NSServiceGroup.add(self.nitro,
                                          servicegroup)

        def delete_servicegroup(self):
                # Delete servicegroup
                servicegroup = NSServiceGroup()
                servicegroup.set_servicegroupname('nitro_example_servicegroup')
                return NSServiceGroup.delete(self.nitro,
                                             servicegroup)

        def add_service(self):
                # Add service
                addservice = NSService()
                addservice.set_name("service_nitro_test")
                addservice.set_servername("nitro_example_server")
                addservice.set_servicetype("HTTP")
                addservice.set_port(11111)
                return NSService.add(self.nitro, addservice)

        def add_lbvserver(self):
                # Add load-balancing virtual server
                lbvserver = NSLBVServer()
                lbvserver.set_name("nitro_lbvserver_test")
                lbvserver.set_ipv46("10.32.110.55")
                lbvserver.set_port(11111)
                lbvserver.set_clttimeout(180)
                lbvserver.set_persistencetype("NONE")
                lbvserver.set_servicetype("HTTP")
                return NSLBVServer.add(self.nitro, lbvserver)

        def bind_lbvserver(self):
                # Bind service to load-balancing virtual server
                lbbinding = NSLBVServerServiceBinding()
                lbbinding.set_name('nitro_lbvserver_test')
                lbbinding.set_servicename("service_nitro_test")
                lbbinding.set_weight(40)
                return NSLBVServerServiceBinding.add(self.nitro, lbbinding)

        def list_lbvserver_binding(self):
                lbbinding = NSLBVServerServiceBinding()
                lbbinding.set_name("nitro_lbvserver_test")
                lbbindings = NSLBVServerServiceBinding.get(
                    self.nitro, lbbinding)
                lbb_list = []
                for lbb in lbbindings:
                        lbb_list.append(lbb.get_servicegroupname())
                return lbb_list

        def delete_binding(self):
                # Unbind service from load-balancing virtual server
                lbbinding = NSLBVServerServiceBinding()
                lbbinding.set_name("nitro_lbvserver_test")
                lbbinding.set_servicename("service_nitro_test")
                return NSLBVServerServiceBinding.delete(self.nitro, lbbinding)

        def delete_lbvserver(self):
                # Delete load-balancing virtual server
                lbvserver = NSLBVServer()
                lbvserver.set_name("nitro_lbvserver_test")
                return NSLBVServer.delete(self.nitro, lbvserver)

        def get_service(self):
                service = NSService()
                service.set_name("service_nitro_test")
                return NSService.get(self.nitro, service)

        def update_service(self):
                # Update service
                service = NSService()
                service.set_name("service_nitro_test")
                service.set_comment("test comment")
                service.set_useproxyport("NO")
                return NSService.update(self.nitro, service)

        def disable_service(self):
                # Disable service
                service = NSService()
                service.set_name("service_nitro_test")
                return NSService.disable(self.nitro, service)

        def enable_service(self):
                # Enable service
                service = NSService()
                service.set_name("service_nitro_test")
                return NSService.enable(self.nitro, service)

        def rename_service(self):
                # Rename service
                service = NSService()
                service.set_name("service_nitro_test")
                service.set_newname("service_nitro_test_rename")
                NSService.rename(self.nitro, service)
                # Rename service back to original
                service = NSService()
                service.set_name("service_nitro_test_rename")
                service.set_newname("service_nitro_test")
                return NSService.rename(self.nitro, service)

        def delete_service(self):
                # Delete service
                service = NSService()
                service.set_name("service_nitro_test")
                return NSService.delete(self.nitro, service)

        def delete_server(self):
                # Delete server
                server = NSServer()
                server.set_name("nitro_example_server")
                return NSServer.delete(self.nitro, server)

        def list_hanodes(self):
                # List HA nodes
                hanodes = NSHANode.get_all(self.nitro)
                hanode_list = []
                for i in hanodes:
                        hanode_list.append(i.get_id())
                return hanode_list

        def list_vlans(self):
                # List VLANs
                vlans = NSVLAN.get_all(self.nitro)
                vlan_list = []
                for vlan in vlans:
                        vlan_list.append(vlan.get_id())
                return vlan_list

        def add_vlan(self):
                # Add VLAN
                vlan = NSVLAN()
                vlan.set_id(125)
                return NSVLAN.add(self.nitro, vlan)

        def delete_vlan(self):
                # Delete VLAN
                vlan = NSVLAN()
                vlan.set_id(125)
                return NSVLAN.delete(self.nitro, vlan)

        def list_ips(self):
                # List all IPs
                ips = NSIP.get_all(self.nitro)
                ip_list = []
                for ip in ips:
                        ip_list.append(ip.get_ipaddress())
                return ip_list

        def list_vlan_if_bindings(self):
                # List VLAN/interface bindings
                vifb = NSVLANInterfaceBinding()
                vifb.set_id(125)
                return NSVLANInterfaceBinding.get(self.nitro, vifb)

        def list_vlan_ip_bindings(self):
                # List VLAN/IP address bindings
                vipb = NSVLANNSIPBinding()
                vipb.set_id(125)
                return NSVLANNSIPBinding.get(self.nitro, vipb)

        def add_ip(self):
                # Add IP address
                ip = NSIP()
                ip.set_ipaddress('10.40.12.181')
                ip.set_netmask('255.255.255.224')
                ip.set_vserver('disabled')
                return NSIP.add(self.nitro, ip)

        def delete_ip(self):
                # Delete IP address
                ip = NSIP()
                ip.set_ipaddress('10.40.12.181')
                return NSIP.delete(self.nitro, ip)

        def delete_vipb(self):
                # Unbind VLAN from IP address
                ip = NSVLANNSIPBinding()
                ip.set_id(125)
                ip.set_ipaddress('10.40.12.181')
                ip.set_netmask('255.255.255.224')
                return NSVLANNSIPBinding.delete(self.nitro, ip)

        def delete_vifb(self):
                # Unbind VLAN from interface
                ip = NSVLANInterfaceBinding()
                ip.set_id(125)
                ip.set_ifnum("1/1")
                return NSVLANInterfaceBinding.delete(self.nitro, ip)

        def bind_vlan_to_if(self):
                # Bind VLAN to interface
                vifb = NSVLANInterfaceBinding()
                vifb.set_id(125)
                vifb.set_ifnum("1/1")
                vifb.set_tagged(True)
                return NSVLANInterfaceBinding.add(self.nitro, vifb)

        def bind_vlan_to_ip(self):
                # Bind VLAN to IP address
                vipb = NSVLANNSIPBinding()
                vipb.set_id(125)
                vipb.set_ipaddress('10.40.12.181')
                vipb.set_netmask('255.255.255.224')
                return NSVLANNSIPBinding.add(self.nitro, vipb)

        def disable_feature(self):
                # Disable Netscaler feature
                feature = NSFeature()
                feature.set_feature(['CS', 'LB'])
                return NSFeature.disable(self.nitro, feature)

        def enable_feature(self):
                # Enable Netscaler feature
                feature = NSFeature()
                feature.set_feature(['CS', 'LB'])
                return NSFeature.enable(self.nitro, feature)

        def add_cspolicy(self):
                # Add content-switching policy
                cspol = NSCSPolicy()
                cspol.set_rule("CLIENT.IP.SRC.SUBNET(24).EQ(10.10.42.0)")
                cspol.set_policyname("test_policyname")
                return NSCSPolicy.add(self.nitro, cspol)

        def delete_cspolicy(self):
                # Delete content-switching policy
                cspol = NSCSPolicy()
                cspol.set_rule("CLIENT.IP.SRC.SUBNET(24).EQ(10.10.42.0)")
                cspol.set_policyname("test_policyname")
                return NSCSPolicy.delete(self.nitro, cspol)

        def add_rewriteaction(self):
                # Add rewrite action
                rewriteaction = NSRewriteAction()
                rewriteaction.set_name("test_rewrite_action")
                rewriteaction.set_type("insert_http_header")
                rewriteaction.set_target("ble")
                rewriteaction.set_stringbuilderexpr("CLIENT.IP.SRC")
                return NSRewriteAction.add(self.nitro, rewriteaction)

        def delete_rewriteaction(self):
                # Delete rewrite action
                rewriteaction = NSRewriteAction()
                rewriteaction.set_name("test_rewrite_action")
                return NSRewriteAction.delete(self.nitro, rewriteaction)

        def add_lbmonitor(self):
                # Add load-balancing monitor
                lbmon = NSLBMonitor()
                lbmon.set_monitorname("test_https")
                lbmon.set_type("HTTP")
                lbmon.set_httprequest("HEAD /")
                lbmon.set_rtsprequest("HEAD /")
                lbmon.set_respcode(["200"])
                lbmon.set_interval("5")
                lbmon.set_resptimeout("2")
                lbmon.set_resptimeoutthresh("0")
                return NSLBMonitor.add(self.nitro, lbmon)

        def update_lbmonitor(self):
                # Update load-balancing monitor
                lbmon = NSLBMonitor()
                lbmon.set_monitorname("test_https")
                lbmon.set_type("HTTP")
                lbmon.set_interval("60")
                lbmon.set_resptimeout("24")
                return NSLBMonitor.update(self.nitro, lbmon)

        def add_lbmonitorbinding(self):
                # Bind load-balancing monitor to a service
                lbmonbind = NSLBMonitorServiceBinding()
                lbmonbind.set_servicename("service_nitro_test")
                lbmonbind.set_monitorname("test_https")
                return NSLBMonitorServiceBinding.add(self.nitro, lbmonbind)

        def delete_lbmonitorbinding(self):
                # Unbind load-balancing monitor from a service
                lbmonbind = NSLBMonitorServiceBinding()
                lbmonbind.set_servicename("service_nitro_test")
                lbmonbind.set_monitorname("test_https")
                return NSLBMonitorServiceBinding.delete(self.nitro, lbmonbind)

        def delete_lbmonitor(self):
                # Delete load-balancing monitor
                lbmon = NSLBMonitor()
                lbmon.set_monitorname("test_https")
                lbmon.set_type("HTTP")
                return NSLBMonitor.delete(self.nitro, lbmon)

        def add_cmdpol(self):
                # Add command policy
                cmdpol = NSSystemCMDPolicy()
                cmdpol.set_action('ALLOW')
                cmdpol.set_policyname('nitro-cmdpol-test')
                cmdpol.set_cmdspec('show hardware')
                return NSSystemCMDPolicy.add(self.nitro, cmdpol)

        def update_cmdpol(self):
                # Update command policy
                cmdpol = NSSystemCMDPolicy()
                cmdpol.set_action('DENY')
                cmdpol.set_policyname('nitro-cmdpol-test')
                cmdpol.set_cmdspec('show lb vserver')
                return NSSystemCMDPolicy.update(self.nitro, cmdpol)

        def delete_cmdpol(self):
                # Delete command policy
                cmdpol = NSSystemCMDPolicy()
                cmdpol.set_policyname('nitro-cmdpol-test')
                return NSSystemCMDPolicy.delete(self.nitro, cmdpol)

        def logout(self):
                # Log out of Netscaler
                return self.nitro.logout()
>>>>>>> parent of 04e4b34... Ran AutoPEP8 against project; cleaned up quite a bit.


def main():
    a = test_nitro()
    print 'Login Status Code:                   ' + str(a.login())
    print 'Adding command policy:               ' + str(a.add_cmdpol())
    print 'Updating command policy:             ' + str(a.update_cmdpol())
    print 'Adding server:                       ' + str(a.add_server())
    print 'Disabling server:                    ' + str(a.disable_server())
    print 'Enabling server:                     ' + str(a.enable_server())
    print 'Adding service:                      ' + str(a.add_service())
    print 'Disabling service:                   ' + str(a.disable_service())
    print 'Enabling service:                    ' + str(a.enable_service())
    print 'Updating service:                    ' + str(a.update_service())
    print 'Renaming service:                    ' + str(a.rename_service())
    print 'Adding servicegroup:                 ' + str(a.add_servicegroup())
    print 'Adding VLAN:                         ' + str(a.add_vlan())
    print 'Adding IP address:                   ' + str(a.add_ip())
    print 'Adding LB virtual server:            ' + str(a.add_lbvserver())
    print 'Adding LB monitor:                   ' + str(a.add_lbmonitor())
    print 'Updating LB monitor:                 ' + str(a.update_lbmonitor())
    print 'Adding LB monitor binding:           ' + str(a.add_lbmonitorbinding())
    print 'Binding LB virtual server:           ' + str(a.bind_lbvserver())
    print 'Binding VLAN to interface:           ' + str(a.bind_vlan_to_if())
    print 'Binding VLAN to IP address:          ' + str(a.bind_vlan_to_ip())
#    print 'Adding rewrite action:               ' + str(a.add_rewriteaction())
#    print 'Adding CS policy:                    ' + str(a.add_cspolicy())
#    print 'Disabling features:                  ' + str(a.disable_feature())
#    print 'Enabling features:                   ' + str(a.enable_feature())
#    print 'Deleting CS policy:                  ' + str(a.delete_cspolicy())
#    print 'Deleting rewrite action:             ' + str(a.delete_rewriteaction())
    print 'List of HA nodes:                    ' + str(a.list_hanodes())
    print 'List of IPs:                         ' + str(a.list_ips())
    print 'List of VLANS:                       ' + str(a.list_vlans())
    print 'List of VLAN interface bindings:     ' + str(a.list_vlan_if_bindings())
    print 'List of VLAN IP bindings:            ' + str(a.list_vlan_ip_bindings())
    print 'List LB virtual server binding:      ' + str(a.list_lbvserver_binding())
    print 'Deleting LB monitor binding:         ' + str(a.delete_lbmonitorbinding())
    print 'Deleting LB monitor:                 ' + str(a.delete_lbmonitor())
    print 'Deleting VLAN to IP address binding: ' + str(a.delete_vipb())
    print 'Deleting VLAN to interface binding:  ' + str(a.delete_vifb())
    print 'Deleting LB virtual server binding:  ' + str(a.delete_binding())
    print 'Deleting LB virtual server:          ' + str(a.delete_lbvserver())
    print 'Deleting IP address:                 ' + str(a.delete_ip())
    print 'Deleting VLAN:                       ' + str(a.delete_vlan())
    print 'Deleting servicegroup:               ' + str(a.delete_servicegroup())
    print 'Deleting service:                    ' + str(a.delete_service())
    print 'Deleting server:                     ' + str(a.delete_server())
    print 'Deleting command policy:             ' + str(a.delete_cmdpol())
    print 'Logout Status Code:                  ' + str(a.logout())

if __name__ == '__main__':
        main()
