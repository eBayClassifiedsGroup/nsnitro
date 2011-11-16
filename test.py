import nsnitro
from nsresources.nsservice import *
import json

nitro = nsnitro.NSNitro('localhost', 'api_user', 'api_user')
nitro.login()


service = NSService.get(nitro, "aurora_userservice_mp-be008")
print service
print service.get_svrstate()

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
