import nsnitro
from nsresources.nsservice import *
import json

nitro = nsnitro.NSNitro('localhost', 'api_user', 'api_user')
nitro.login()


service = NSService.get(nitro, "aurora_userservice_mp-be002")
print service
print service.get_svrstate()

# add service cas_casbuyside_mp-casfe002 mp-casfe002 HTTP 10460 -gslb NONE -maxClient 0 -maxReq 0 -cip DISABLED -usip NO -useproxyport YES -sp OFF -cltTimeout 180 -svrTimeout 360 -CKA NO -TCPB NO -CMP NO

addservice = NSService()
addservice.set_name("aurora_testnitroadd")
addservice.set_servername("mp-be002")
addservice.set_servicetype("HTTP")
addservice.set_port(11111)
NSService.add(nitro, addservice)

#disservice = NSService()
#disservice.set_name("aurora_userservice_mp-be002")
#NSService.disable(nitro, disservice)


#enservice = NSService()
#enservice.set_name("aurora_userservice_mp-be002")
#NSService.enable(nitro, enservice)

#renservice = NSService()
#renservice.set_name("aurora_userservice_mp-be002")
#renservice.set_newname("aurora_foobar")
#NSService.rename(nitro, renservice)

#renservice = NSService()
#renservice.set_name("aurora_foobar")
#renservice.set_newname("aurora_userservice_mp-be002")
#NSService.rename(nitro, renservice)
