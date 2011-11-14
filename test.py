import nsnitro
import nsresources
import json

nitro = nsnitro.NSNitro('localhost', 'api_user', 'api_user')
nitro.login()
service = nsresources.NSService(nitro)

service.get("aurora_userservice_mp-be002")

print service.get_name()

payload = service.json()
print json.dumps(payload)
