import json
import random
import unittest
from nsnitro import *

nsnitro_test_netscaler_ipaddress = '10.216.91.222'
nsnitro_test_netscaler_uname = 'nsroot'
nsnitro_test_netscaler_pword = 'nsroot'
nsnitro_test_ip_ipaddress = '10.32.100.' + str(random.randrange(1, 256))
nsnitro_test_ip_netmask = '255.255.255.224'
nsnitro_test_lbvserver_ipaddress = '10.32.110.' + str(random.randrange(1, 256))
nsnitro_test_lbvserver_port = random.randrange(1025, 65536)
nsnitro_test_server_ipaddress = '10.32.120.' + str(random.randrange(1, 256))
nsnitro_test_service_port = random.randrange(1025, 65536)
nsnitro_test_interface_ifnum = '1/1'
nsnitro_test_vlan_id = str(random.randrange(1025, 4096))


class TestNitroFunctions(unittest.TestCase):

    nitro = NSNitro(
        nsnitro_test_netscaler_ipaddress,
        nsnitro_test_netscaler_uname,
        nsnitro_test_netscaler_pword,
        useSSL=False)

    @classmethod
    def setUpClass(cls):
        cls.nitro.login()

    @classmethod
    def tearDownClass(cls):
        cls.nitro.logout()

    def test_00_add_ip(self):
        # Add IP address
        ip = NSIP()
        ip.set_ipaddress(nsnitro_test_ip_ipaddress)
        ip.set_netmask(nsnitro_test_ip_netmask)
        ip.set_vserver('disabled')
        r = NSIP.add(self.nitro, ip)
        self.assertEqual(r.errorcode, 0)

    def test_00_add_lbmonitor(self):
        # Add load-balancing monitor
        lbmonitor = NSLBMonitor()
        lbmonitor.set_monitorname('nsnitro_test_lbmonitor')
        lbmonitor.set_type('HTTP')
        lbmonitor.set_httprequest('HEAD /')
        lbmonitor.set_rtsprequest('HEAD /')
        lbmonitor.set_respcode(['200'])
        lbmonitor.set_interval(5)
        lbmonitor.set_resptimeout(2)
        lbmonitor.set_resptimeoutthresh(0)
        r = NSLBMonitor.add(self.nitro, lbmonitor)
        self.assertEqual(r.errorcode, 0)

    def test_00_add_server(self):
        # Add server
        server = NSServer()
        server.set_name('nsnitro_test_server')
        server.set_ipaddress(nsnitro_test_server_ipaddress)
        r = NSServer.add(self.nitro, server)
        self.assertEqual(r.errorcode, 0)

    def test_00_add_vlan(self):
        # Add VLAN
        vlan = NSVLAN()
        vlan.set_id(nsnitro_test_vlan_id)
        r = NSVLAN.add(self.nitro, vlan)
        self.assertEqual(r.errorcode, 0)

    def test_01_add_cmdpol(self):
        # Add command policy
        cmdpol = NSSystemCMDPolicy()
        cmdpol.set_action('ALLOW')
        cmdpol.set_policyname('nsnitro_test_cmdpol')
        cmdpol.set_cmdspec('show hardware')
        r = NSSystemCMDPolicy.add(self.nitro, cmdpol)
        self.assertEqual(r.errorcode, 0)

#    def test_01_add_cspolicy(self):
#        # Add content-switching policy
#        cspol = NSCSPolicy()
#        cspol.set_rule('CLIENT.IP.SRC.SUBNET(24).EQ(10.10.42.0)')
#        cspol.set_policyname('test_policyname')
#        r = NSCSPolicy.add(self.nitro, cspol)
#        self.assertEqual(r.errorcode, 0)

    def test_01_add_lbvserver(self):
        # Add load-balancing virtual server
        lbvserver = NSLBVServer()
        lbvserver.set_name('nsnitro_test_lbvserver')
        lbvserver.set_ipv46(nsnitro_test_lbvserver_ipaddress)
        lbvserver.set_port(nsnitro_test_lbvserver_port)
        lbvserver.set_clttimeout(180)
        lbvserver.set_persistencetype('NONE')
        lbvserver.set_servicetype('HTTP')
        r = NSLBVServer.add(self.nitro, lbvserver)
        self.assertEqual(r.errorcode, 0)

#    def test_01_add_rewriteaction(self):
#        # Add rewrite action
#        rewriteaction = NSRewriteAction()
#        rewriteaction.set_name('nsnitro_test_rewriteaction')
#        rewriteaction.set_type('insert_http_header')
#        rewriteaction.set_target('ble')
#        rewriteaction.set_stringbuilderexpr('CLIENT.IP.SRC')
#        r = NSRewriteAction.add(self.nitro, rewriteaction)
#        self.assertEqual(r.errorcode, 0)

    def test_01_add_service(self):
        # Add service
        service = NSService()
        service.set_name('nsnitro_test_service')
        service.set_servername('nsnitro_test_server')
        service.set_servicetype('HTTP')
        service.set_port(nsnitro_test_service_port)
        r = NSService.add(self.nitro, service)
        self.assertEqual(r.errorcode, 0)

    def test_01_add_servicegroup(self):
        # Add servicegroup
        servicegroup = NSServiceGroup()
        servicegroup.set_servicegroupname('nsnitro_test_servicegroup')
        servicegroup.set_servicetype('http')
        r = NSServiceGroup.add(self.nitro, servicegroup)
        self.assertEqual(r.errorcode, 0)

    def test_02_bind_lbmonitorservice(self):
        # Bind load-balancing monitor to a service
        lbmonbind = NSLBMonitorServiceBinding()
        lbmonbind.set_servicename('nsnitro_test_service')
        lbmonbind.set_monitorname('nsnitro_test_lbmonitor')
        r = NSLBMonitorServiceBinding.add(self.nitro, lbmonbind)
        self.assertEqual(r.errorcode, 0)

    def test_02_bind_lbvserverservice(self):
        # Bind service to load-balancing virtual server
        lbvserverservice = NSLBVServerServiceBinding()
        lbvserverservice.set_name('nsnitro_test_lbvserver')
        lbvserverservice.set_servicename('nsnitro_test_service')
        lbvserverservice.set_weight(40)
        r = NSLBVServerServiceBinding.add(self.nitro, lbvserverservice)
        self.assertEqual(r.errorcode, 0)

    def test_02_bind_vlan_to_if(self):
        # Bind VLAN to interface
        vifb = NSVLANInterfaceBinding()
        vifb.set_id(nsnitro_test_vlan_id)
        vifb.set_ifnum(nsnitro_test_interface_ifnum)
        vifb.set_tagged(True)
        r = NSVLANInterfaceBinding.add(self.nitro, vifb)
        self.assertEqual(r.errorcode, 0)

    def test_02_bind_vlan_to_ip(self):
        # Bind VLAN to IP address
        vipb = NSVLANNSIPBinding()
        vipb.set_id(nsnitro_test_vlan_id)
        vipb.set_ipaddress(nsnitro_test_ip_ipaddress)
        vipb.set_netmask(nsnitro_test_ip_netmask)
        r = NSVLANNSIPBinding.add(self.nitro, vipb)
        self.assertEqual(r.errorcode, 0)

    def test_03_disable_feature(self):
        # Disable Netscaler features
        feature = NSFeature()
        feature.set_feature(['ssl'])
        r = NSFeature.disable(self.nitro, feature)
        self.assertEqual(r.errorcode, 0)

    def test_03_disable_server(self):
        # Disable server
        server = NSServer()
        server.set_name('nsnitro_test_server')
        r = NSServer.disable(self.nitro, server)
        self.assertEqual(r.errorcode, 0)

    def test_03_disable_service(self):
        # Disable service
        service = NSService()
        service.set_name('nsnitro_test_service')
        r = NSService.disable(self.nitro, service)
        self.assertEqual(r.errorcode, 0)

    def test_04_enable_feature(self):
        # Enable Netscaler features
        feature = NSFeature()
        feature.set_feature(['ssl'])
        r = NSFeature.enable(self.nitro, feature)
        self.assertEqual(r.errorcode, 0)

    def test_04_enable_server(self):
        # Enable server
        server = NSServer()
        server.set_name('nsnitro_test_server')
        r = NSServer.enable(self.nitro, server)
        self.assertEqual(r.errorcode, 0)

    def test_04_enable_service(self):
        # Enable service
        service = NSService()
        service.set_name('nsnitro_test_service')
        r = NSService.enable(self.nitro, service)
        self.assertEqual(r.errorcode, 0)

    def test_05_get_hanodes(self):
        # Get HA node info
        hanodes = NSHANode.get_all(self.nitro)
        hanode_list = []
        for hanode in hanodes:
            hanode_list.append(hanode.get_id())
        self.assertIn('0', hanode_list)

    def test_05_get_ips(self):
        # List all IPs
        ips = NSIP.get_all(self.nitro)
        ip_list = []
        for ip in ips:
            ip_list.append(ip.get_ipaddress())
        self.assertIn(nsnitro_test_netscaler_ipaddress, ip_list)
        self.assertIn(nsnitro_test_ip_ipaddress, ip_list)

    def test_05_get_lbmonitor(self):
        # Get load-balancing monitor info
        lbmonitor = NSLBMonitor()
        lbmonitor.set_monitorname('nsnitro_test_lbmonitor')
        r = NSLBMonitor.get(self.nitro, lbmonitor).__dict__['options']
        self.assertIn('nsnitro_test_lbmonitor', r['monitorname'])
        self.assertIn('HEAD /', r['httprequest'])
        self.assertEqual(5, r['interval'])

    def test_05_get_lbvserver(self):
        # Get load-balanced virtual server info
        lbvserver = NSLBVServer()
        lbvserver.set_name('nsnitro_test_lbvserver')
        r = NSLBVServer.get(self.nitro, lbvserver).__dict__['options']
        self.assertIn('nsnitro_test_lbvserver', r['name'])
        self.assertEqual('180', r['clttimeout'])
        self.assertEqual(nsnitro_test_lbvserver_port, r['port'])

    def test_05_get_lbvserverservice_bindings(self):
        # Get load-balanced virtual server/service binding
        lbvserverservicebinding = NSLBVServerServiceBinding()
        lbvserverservicebinding.set_name('nsnitro_test_lbvserver')
        r = NSLBVServerServiceBinding.get(self.nitro, lbvserverservicebinding).__dict__['options']
        self.assertIn('nsnitro_test_service', r['servicename'])
        self.assertIn('nsnitro_test_lbvserver', r['name'])
        self.assertIn(nsnitro_test_server_ipaddress, r['ipv46'])
        self.assertIn(nsnitro_test_server_ipaddress, r['vsvrbindsvcip'])
        self.assertEqual(nsnitro_test_service_port, r['port'])

    def test_05_get_nsconfig(self):
        # Get system configuration
        r = NSConfig.get_all(self.nitro).__dict__['options']
        self.assertIn(nsnitro_test_netscaler_ipaddress, r['ipaddress'])

    def test_05_get_server(self):
        # Get info on a specific server
        server = NSService()
        server.set_name('nsnitro_test_server')
        r = NSServer.get(self.nitro, server).__dict__['options']
        self.assertIn('nsnitro_test_server', r['name'])
        self.assertIn(nsnitro_test_server_ipaddress, r['ipaddress'])

    def test_05_get_service(self):
        # Get info on a specific service
        service = NSService()
        service.set_name('nsnitro_test_service')
        r = NSService.get(self.nitro, service).__dict__['options']
        self.assertIn('nsnitro_test_service', r['name'])
        self.assertIn('HTTP', r['servicetype'])
        self.assertEqual(nsnitro_test_service_port, r['port'])

    def test_05_get_vlan_if_bindings(self):
        # Get all VLAN/interface bindings
        vlans = NSVLAN.get_all(self.nitro)
        vifb_list = []
        for vlan in vlans:
            vifbs = NSVLANInterfaceBinding.get(self.nitro, vlan)
            vifb = vifbs.__dict__['options']
            vifb_list.append(vifb['id'])
        self.assertIn('1', vifb_list)
        self.assertIn(nsnitro_test_vlan_id, vifb_list)

    def test_05_get_vlan_ip_bindings(self):
        # Get VLAN/IP address bindings
        vlans = NSVLAN.get_all(self.nitro)
        vipb_list = []
        for vlan in vlans:
            vipbs = NSVLANNSIPBinding.get(self.nitro, vlan)
            vipb = vipbs.__dict__['options']
            vipb_list.append(vipb['id'])
        self.assertIn('1', vipb_list)
        self.assertIn(nsnitro_test_vlan_id, vipb_list)

    def test_05_get_vlans(self):
        # Get VLANs
        vlans = NSVLAN.get_all(self.nitro)
        vlan_list = []
        for vlan in vlans:
            vlan_list.append(vlan.get_id())
        self.assertIn('1', vlan_list)
        self.assertIn(nsnitro_test_vlan_id, vlan_list)

    def test_06_rename_server_01(self):
        # Rename service
        server = NSServer()
        server.set_name('nsnitro_test_server')
        server.set_newname('nsnitro_test_server_rename')
        r = NSServer.rename(self.nitro, server)
        self.assertEqual(r.errorcode, 0)

    def test_06_rename_server_02(self):
        # Rename service
        server = NSServer()
        server.set_name('nsnitro_test_server_rename')
        server.set_newname('nsnitro_test_server')
        r = NSServer.rename(self.nitro, server)
        self.assertEqual(r.errorcode, 0)

    def test_06_rename_service_01(self):
        # Rename service
        service = NSService()
        service.set_name('nsnitro_test_service')
        service.set_newname('nsnitro_test_service_rename')
        r = NSService.rename(self.nitro, service)
        self.assertEqual(r.errorcode, 0)

    def test_06_rename_service_02(self):
        # Rename service back to original
        service = NSService()
        service.set_name('nsnitro_test_service_rename')
        service.set_newname('nsnitro_test_service')
        r = NSService.rename(self.nitro, service)
        self.assertEqual(r.errorcode, 0)

    def test_06_update_server(self):
        # Update server
        server = NSServer()
        server.set_name('nsnitro_test_server')
        server.set_comment('test comment')
        r = NSServer.update(self.nitro, server)
        self.assertEqual(r.errorcode, 0)

    def test_06_update_service(self):
        # Update service
        service = NSService()
        service.set_name('nsnitro_test_service')
        service.set_comment('test comment')
        service.set_useproxyport('NO')
        r = NSService.update(self.nitro, service)
        self.assertEqual(r.errorcode, 0)

    def test_06_update_cmdpol(self):
        # Update command policy
        cmdpol = NSSystemCMDPolicy()
        cmdpol.set_action('DENY')
        cmdpol.set_policyname('nsnitro_test_cmdpol')
        cmdpol.set_cmdspec('show lb vserver')
        r = NSSystemCMDPolicy.update(self.nitro, cmdpol)
        self.assertEqual(r.errorcode, 0)

    def test_06_update_lbmonitor(self):
        # Update load-balancing monitor
        lbmon = NSLBMonitor()
        lbmon.set_monitorname('nsnitro_test_lbmonitor')
        lbmon.set_type('HTTP')
        lbmon.set_interval('60')
        lbmon.set_resptimeout('24')
        r = NSLBMonitor.update(self.nitro, lbmon)
        self.assertEqual(r.errorcode, 0)

    def test_07_unbind_lbmonitorservice(self):
        # Unbind load-balancing monitor from a service
        lbmonbind = NSLBMonitorServiceBinding()
        lbmonbind.set_servicename('nsnitro_test_service')
        lbmonbind.set_monitorname('nsnitro_test_lbmonitor')
        r = NSLBMonitorServiceBinding.delete(self.nitro, lbmonbind)
        self.assertEqual(r.errorcode, 0)

    def test_07_unbind_lbvserverservice(self):
        # Unbind service from load-balancing virtual server
        lbvserverservice = NSLBVServerServiceBinding()
        lbvserverservice.set_name('nsnitro_test_lbvserver')
        lbvserverservice.set_servicename('nsnitro_test_service')
        r = NSLBVServerServiceBinding.delete(self.nitro, lbvserverservice)
        self.assertEqual(r.errorcode, 0)

    def test_07_unbind_vifb(self):
        # Unbind VLAN from interface
        ip = NSVLANInterfaceBinding()
        ip.set_id(nsnitro_test_vlan_id)
        ip.set_ifnum(nsnitro_test_interface_ifnum)
        r = NSVLANInterfaceBinding.delete(self.nitro, ip)
        self.assertEqual(r.errorcode, 0)

    def test_07_unbind_vipb(self):
        # Unbind VLAN from IP address
        ip = NSVLANNSIPBinding()
        ip.set_id(nsnitro_test_vlan_id)
        ip.set_ipaddress(nsnitro_test_ip_ipaddress)
        ip.set_netmask(nsnitro_test_ip_netmask)
        r = NSVLANNSIPBinding.delete(self.nitro, ip)
        self.assertEqual(r.errorcode, 0)

    def test_08_delete_cmdpol(self):
        # Delete command policy
        cmdpol = NSSystemCMDPolicy()
        cmdpol.set_policyname('nsnitro_test_cmdpol')
        r = NSSystemCMDPolicy.delete(self.nitro, cmdpol)
        self.assertEqual(r.errorcode, 0)

#    def test_08_delete_cspolicy(self):
#        # Delete content-switching policy
#        cspol = NSCSPolicy()
#        cspol.set_rule('CLIENT.IP.SRC.SUBNET(24).EQ(10.10.42.0)')
#        cspol.set_policyname('test_policyname')
#        r = NSCSPolicy.delete(self.nitro, cspol)
#        self.assertEqual(r.errorcode, 0)

    def test_08_delete_lbvserver(self):
        # Delete load-balancing virtual server
        lbvserver = NSLBVServer()
        lbvserver.set_name('nsnitro_test_lbvserver')
        r = NSLBVServer.delete(self.nitro, lbvserver)
        self.assertEqual(r.errorcode, 0)

#    def test_08_delete_rewriteaction(self):
#        # Delete rewrite action
#        rewriteaction = NSRewriteAction()
#        rewriteaction.set_name('nsnitro_test_rewriteaction')
#        r = NSRewriteAction.delete(self.nitro, rewriteaction)
#        self.assertEqual(r.errorcode, 0)

    def test_08_delete_service(self):
        # Delete service
        service = NSService()
        service.set_name('nsnitro_test_service')
        r = NSService.delete(self.nitro, service)
        self.assertEqual(r.errorcode, 0)

    def test_08_delete_servicegroup(self):
        # Delete servicegroup
        servicegroup = NSServiceGroup()
        servicegroup.set_servicegroupname('nsnitro_test_servicegroup')
        r = NSServiceGroup.delete(self.nitro, servicegroup)
        self.assertEqual(r.errorcode, 0)

    def test_09_delete_ip(self):
        # Delete IP address
        ip = NSIP()
        ip.set_ipaddress(nsnitro_test_ip_ipaddress)
        r = NSIP.delete(self.nitro, ip)
        self.assertEqual(r.errorcode, 0)

    def test_09_delete_lbmonitor(self):
        # Delete load-balancing monitor
        lbmon = NSLBMonitor()
        lbmon.set_monitorname('nsnitro_test_lbmonitor')
        lbmon.set_type('HTTP')
        r = NSLBMonitor.delete(self.nitro, lbmon)
        self.assertEqual(r.errorcode, 0)

    def test_09_delete_server(self):
        # Delete server
        server = NSServer()
        server.set_name('nsnitro_test_server')
        r = NSServer.delete(self.nitro, server)
        self.assertEqual(r.errorcode, 0)

    def test_09_delete_vlan(self):
        # Delete VLAN
        vlan = NSVLAN()
        vlan.set_id(nsnitro_test_vlan_id)
        r = NSVLAN.delete(self.nitro, vlan)
        self.assertEqual(r.errorcode, 0)

    def test_10_save_config(self):
        config = NSConfig()
        r = config.save(self.nitro)
        self.assertEqual(r.errorcode, 0)

if __name__ == '__main__':
    unittest.main()
