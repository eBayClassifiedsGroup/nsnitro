import time
from nsnitro import *

nitro = NSNitro('localhost', 'api_user', 'api_user')
nitro.login()

# add server test
addserver = NSServer()
addserver.set_name("mp-nitroserver")
addserver.set_ipaddress("10.32.110.99")
NSServer.add(nitro, addserver)

server = NSServer()
server.set_name("mp-nitroserver")
server = server.get(nitro, server)
print server.get_name() + ": " + server.get_state()

# disable server test
server = NSServer()
server.set_name("mp-nitroserver")
NSServer.disable(nitro, server)

time.sleep(2)

server = NSServer()
server.set_name("mp-nitroserver")
server = server.get(nitro, server)
print server.get_name() + ": " + server.get_state()


# enable server test
server = NSServer()
server.set_name("mp-nitroserver")
NSServer.enable(nitro, server)

time.sleep(2)

server = NSServer()
server.set_name("mp-nitroserver")
server = server.get(nitro, server)
print server.get_name() + ": " + server.get_state()

# add service test

addservice = NSService()
addservice.set_name("aurora_testnitroadd")
addservice.set_servername("mp-nitroserver")
addservice.set_servicetype("HTTP")
addservice.set_port(11111)
NSService.add(nitro, addservice)

# add lbvserver test
lbvserver = NSLBVServer()
lbvserver.set_name("nitro_lbvserver_test")
lbvserver.set_ipv46("10.32.110.55")
lbvserver.set_port(11111)
lbvserver.set_clttimeout(180)
lbvserver.set_persistencetype("NONE")
lbvserver.set_servicetype("HTTP")
NSLBVServer.add(nitro, lbvserver)
#
print "LB vserver added"

# bind service to lbvserver test
lbbinding = NSLBVServerServiceBinding()
lbbinding.set_name("nitro_lbvserver_test")
lbbinding.set_servicename("aurora_testnitroadd")
lbbinding.set_weight(40)
NSLBVServerServiceBinding.add(nitro, lbbinding)

print "Binding added"

lbbinding = NSLBVServerServiceBinding()
lbbinding.set_name("nitro_lbvserver_test")
lbbindings = NSLBVServerServiceBinding.get(nitro, lbbinding)

for lbb in lbbindings:
        print "sgn: " + lbb.get_servicegroupname()

# delete binding test
lbbinding = NSLBVServerServiceBinding()
lbbinding.set_name("nitro_lbvserver_test")
lbbinding.set_servicename("aurora_testnitroadd")
NSLBVServerServiceBinding.delete(nitro, lbbinding)

print "Binding removed"

# delete lbvserver test
lbvserver = NSLBVServer()
lbvserver.set_name("nitro_lbvserver_test")
NSLBVServer.delete(nitro, lbvserver)

# get service test

service = NSService()
service.set_name("aurora_testnitroadd")
service = service.get(nitro, service)
print service.get_name() + ": " + service.get_svrstate()
print service.get_name() + ": %s %s" % (service.get_port(), service.get_useproxyport())

#update service test
updateservice = NSService()
updateservice.set_name("aurora_testnitroadd")
updateservice.set_comment("test comment")
updateservice.set_useproxyport("NO")
NSService.update(nitro, updateservice)

# get service test

service = NSService()
service.set_name("aurora_testnitroadd")
service = service.get(nitro, service)
print service.get_name() + ": " + service.get_svrstate()
print service.get_name() + ": %s %s %s" % (service.get_port(), service.get_comment(), service.get_useproxyport())

# disable service test

disservice = NSService()
disservice.set_name("aurora_testnitroadd")
NSService.disable(nitro, disservice)

service = NSService()
service.set_name("aurora_testnitroadd")
service = service.get(nitro, service)
print service.get_name() + ": " + service.get_svrstate()

# enable service test

enservice = NSService()
enservice.set_name("aurora_testnitroadd")
NSService.enable(nitro, enservice)

service = NSService()
service.set_name("aurora_testnitroadd")
service = service.get(nitro, service)
print service.get_name() + ": " + service.get_svrstate()


# rename service test

renservice = NSService()
renservice.set_name("aurora_testnitroadd")
renservice.set_newname("aurora_testnitroadd_rename")
NSService.rename(nitro, renservice)

# rename service back test

renservice = NSService()
renservice.set_name("aurora_testnitroadd_rename")
renservice.set_newname("aurora_testnitroadd")
NSService.rename(nitro, renservice)

# delete service test

delservice = NSService()
delservice.set_name("aurora_testnitroadd")
NSService.delete(nitro, delservice)

try:
        service = NSService()
        service.set_name("aurora_testnitroadd")
        service = service.get(nitro, service)
        print service.get_name() + ": " + service.get_svrstate()
except NSNitroError, e:
        print e.message


# delete server test
delserver = NSServer()
delserver.set_name("mp-nitroserver")
NSServer.delete(nitro, delserver)

try:
        server = NSServer()
        server.set_name("mp-nitroserver")
        server = server.get(nitro, server)
        print server.get_name() + ": " + server.get_state()
except NSNitroError, e:
        print e.message


# add a snmp community string
addsnmpstring = SNMPCommunity()
addsnmpstring.set_communityname('nitroExample')
addsnmpstring.set_permissions('GET')

SNMPCommunity.add(nitro, addsnmpstring)

# get the community string
snmpstring = SNMPCommunity.get(nitro, 'nitroExample')

# get all the community strings
snmpstrings = SNMPCommunity.get_all(nitro)

# delete the community string that was initially added
SNMPCommunity.delete(nitro, addsnmpstring)

# Add a test user
test_user = SystemUser({'username' : 'nsnitro-example', 'password' : 'test123'})
SystemUser.add(nitro, test_user)

# Get all the users
users = SystemUser.get_all(nitro)

# Get a user
user = SystemUser.get(nitro, test_user)

# Update the password of a user
SystemUser.update(nitro, SystemUser({'username' : 'nsnitro-example', 'password' :'321test'}))

# Delete the test user
SystemUser.delete(nitro, test_user)


# Get the ns version
nsversion = NSVersion().get(nitro)
