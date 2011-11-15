import nsnitro
from nsresources.nsservice import *
import json

nitro = nsnitro.NSNitro('localhost', 'api_user', 'api_user')
nitro.login()


service = NSService()
service.get(nitro, "aurora_userservice_mp-be002")
print service.get_name()
service.reset()

service.disable(nitro, "aurora_userservice_mp-be002")

service.get(nitro, "aurora_userservice_mp-be002")
print service.get_svrstate()
service.reset()

service.enable(nitro, "aurora_userservice_mp-be002")

service.get(nitro, "aurora_userservice_mp-be002")
print service.get_svrstate()

service.reset()

service.rename(nitro, "aurora_userservice_mp-be002", "aurora_test_service")
service.reset()
service.get(nitro, "aurora_test_service")
print service.get_name()
print service.get_svrstate()

service.reset()

service.rename(nitro,  "aurora_test_service", "aurora_userservice_mp-be002")
service.reset()
service.get(nitro, "aurora_userservice_mp-be002")
print service.get_name()
print service.get_svrstate()
