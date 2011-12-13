from nsnitro import nsnitro
from nsnitro.nsresources.nsserver import NSServer
a = nsnitro.NSNitro("10.11.254.29","ddosadmin","ddosAdmin")

def test_login():
    return a.login()

def test_logout():
    a.logout()

    addserver = NSServer()
    addserver.set_name("mpnitroserver")
    addserver.set_ipaddress("192.168.1.2")
    addserver.add(a,addserver)
    delserver = NSServer()
    delserver.set_name("mpnitroserver")
    NSServer.delete(a,delserver)

def main():
    test_login()
    test_logout()

if __name__ == '__main__':
    main()
