from nsnitro import nsnitro
from nsnitro.nsresources.nsservicegroup import NSServiceGroup

__author__ = 'vlazarenko'

nitro = nsnitro.NSNitro("localhost","api_user","api_user")
nitro.login()

svcg = NSServiceGroup()
svcg.set_servicegroupname("testsvcgroup")
#NSServiceGroup.add(nitro, svcg)

NSServiceGroup.delete(nitro, svcg)
