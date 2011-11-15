import json
import urllib
from nsutil import *
from nsbaseresource import NSBaseResource

class NSLBVServer(NSBaseResource):

# Configuration for Load Balancing Virtual Server resource.

def lbvserver extends base_resource
        def __init__(self):¶
                super(NSService, self).__init__()¶

                self.options={
                        'name' : '',
                        'servicetype' : '',
                        'ipv46' : '',
                        'ippattern' : '',
                        'ipmask' : '',
                        'port' : '',
                        'range' : '',
                        'persistencetype' : '',
                        'timeout' : '',
                        'persistencebackup' : '',
                        'backuppersistencetimeout' : '',
                        'lbmethod' : '',
                        'hashlength' : '',
                        'netmask' : '',
                        'v6netmasklen' : '',
                        'rule' : '',
                        'listenpolicy' : '',
                        'listenpriority' : '',
                        'resrule' : '',
                        'persistmask' : '',
                        'v6persistmasklen' : '',
                        'pq' : '',
                        'sc' : '',
                        'rtspnat' : '',
                        'm' : '',
                        'tosid' : '',
                        'datalength' : '',
                        'dataoffset' : '',
                        'sessionless' : '',
                        'state' : '',
                        'connfailover' : '',
                        'redirurl' : '',
                        'cacheable' : '',
                        'clttimeout' : '',
                        'somethod' : '',
                        'sopersistence' : '',
                        'sopersistencetimeout' : '',
                        'sothreshold' : '',
                        'redirectportrewrite' : '',
                        'downstateflush' : '',
                        'backupvserver' : '',
                        'disableprimaryondown' : '',
                        'insertvserveripport' : '',
                        'vipheader' : '',
                        'authenticationhost' : '',
                        'authentication' : '',
                        'authn401' : '',
                        'authnvsname' : '',
                        'push' : '',
                        'pushvserver' : '',
                        'pushlabel' : '',
                        'pushmulticlients' : '',
                        'tcpprofilename' : '',
                        'httpprofilename' : '',
                        'comment' : '',
                        'weight' : '',
                        'servicename' : '',
                        'redirurlflags' : '',
                        'newname' : ''
                }

#        ------- Read only Parameter ---------' : '',
                self.options_readonly={
                        'value' : '',
                        'ipmapping' : '',
                        'type' : '',
                        'curstate' : '',
                        'effectivestate' : '',
                        'status' : '',
                        'lbrrreason' : '',
                        'redirect' : '',
                        'precedence' : '',
                        'homepage' : '',
                        'dnsvservername' : '',
                        'domain' : '',
                        'cachevserver' : '',
                        'health' : '',
                        'gotopriorityexpression' : '',
                        'ruletype' : '',
                        'groupname' : '',
                        'cookiedomain' : '',
                       'map' : '',
                        'gt2gb' : '',
                        'thresholdvalue' : '',
                        'bindpoint' : '',
                        'invoke' : '',
                        'labeltype' : '',
                        'labelname' : '',
                        'version' : '',
                        'totalservices' : '',
                        'activeservices' : '',
                        'statechangetimeseconds' : '',
                        'statechangetimemsec' : '',
                        'tickssincelaststatechange' : '',
                        '__count' : ''
                }

# The name of the load balancing virtual server being added.<br> Default value: 0<br> Minimum length =  1.
        def set_name(String name):
                self.name = name

# The name of the load balancing virtual server being added.<br> Default value: 0<br> Minimum length =  1.
        def get_name():
                return self.name

# The service type.<br> Default value: 0
        def set_servicetype(String servicetype):
                self.servicetype = servicetype

# The service type.<br> Default value: 0
        def get_servicetype():
                return self.servicetype

# The IP address of the virtual server.<br> Default value: 0
        def set_ipv46(String ipv46):
                self.ipv46 = ipv46

# The IP address of the virtual server.<br> Default value: 0
        def get_ipv46():
                return self.ipv46

# The IP Pattern of the virtual server.<br> Default value: 0
        def set_ippattern(String ippattern):
                self.ippattern = ippattern

# The IP Pattern of the virtual server.<br> Default value: 0
        def get_ippattern():
                return self.ippattern


# The IP Mask of the virtual server IP Pattern.
        def set_ipmask(String ipmask):
                self.ipmask = ipmask


# The IP Mask of the virtual server IP Pattern.
        def get_ipmask():
                return self.ipmask


# A port number for the virtual server.<br> Default value: 0<br> Range 1 - 65535.
        def set_port(int port):
                self.port = new Integer(port)


# A port number for the virtual server.<br> Default value: 0<br> Range 1 - 65535.
        def set_port(Integer port):
                self.port = port


# A port number for the virtual server.<br> Default value: 0<br> Range 1 - 65535.
        def get_port():
                return self.port


# The IP range for the network vserver.<br> Default value: 1<br> Minimum value =  1<br> Maximum value =  254
        def set_range(long range):
                self.range = new Long(range)


# The IP range for the network vserver.<br> Default value: 1<br> Minimum value =  1<br> Maximum value =  254
        def set_range(Long range):
                self.range = range


# The IP range for the network vserver.<br> Default value: 1<br> Minimum value =  1<br> Maximum value =  254
        def get_range():
                return self.range

# Persistence type for the virtual server.
#Note:
#The <persistenceType> parameter can take one of the following options:
#        SOURCEIP - When configured, the system selects a physical service based on the Load Balancing method,
#and then directs all the subsequent requests arriving from the same IP as the first request to the same
#physical service.
#        COOKIEINSERT - When configured, the system inserts an HTTP cookie into the client responses. The cookie
#is inserted into the "Cookie" header field of the HTTP response. The client stores the cookie (if enabled) and
#includes it in all the subsequent requests, which then match the cookie criteria. The cookie contains
#information about the service where the requests have to be sent.
#        SSLSESSION ID - When configured, the system creates a persistence that is session based on the arriving
#SSL Session ID, which is part of the SSL handshake process. All requests with the same SSL session ID are
#directed to the initially selected physical service.
#        CUSTOM SERVER ID -This mode of Persistence requires the server to provide its Server-ID in such a way
#that it can be extracted from subsequent requests. The system extracts the Server-ID from subsequent client
#requests and uses it to select a server. The server embeds the Server-ID into the URL query of the HTML links,
#accessible from the initial page that has to generate persistent HTTP requests.
#        RULE - When configured, the system maintains persistence based on the contents of the matched rule. This
#persistence requires an expression to be configured. The expression is created using the add expression CLI
#command and is configured on a virtual server, using the -rule option of the add lb vserver or set lb vserver CLI
#command.After successful evaluation of the expression, a persistence session is created and all subsequent
#matching client requests are directed to the previously selected server.
#        URLPASSIVE - This mode of Persistence requires the server to provide its Server-ID in such a way that it
#can be extracted from subsequent requests.The system extracts the Server-ID from subsequent client requests and uses
#it to select a server. The servers which require persistence, embed the Server-ID into the URL query of the HTML
#links, accessible from the initial page. The Server-ID is its IP address and port specified as a hexadecimal number.
#URL Passive persistence type requires an expression to be configured that specifies the location of the Server-ID
#in the client's requests. The expression is created using the CLI command add expression. This expression is
#configured on a virtual server, using option -rule of the add lb vserver or set lb vserver CLI command.
#        DESTIP -When configured, the system selects a physical service based on the Load Balancing method, and then
#directs all the subsequent requests with the same destination as the first packet to the same physical service. This
#will be used in LLB deployment scenarios.
#        SRCIPDESTIP - When configured, the system selects a physical service based on the Load Balancing method, and
#then directs all the subsequent requests with the same Source IP and Destination IP as the first packet to the same
#physical service. This will be used in IDS LB depolyments.
#        CALLID - When configured, the system maintains persistence based on CALLID used in the SIP transactions. All
#the SIP transactions with same CALLID are directed to the same server.
#        RTSPSID - When configured, the system maintains persistence based on RTSP sessionID provided by the server.
#The client also sends the same RTSP sessionID in the subsequent requests which are then directed to the same server.
        def set_persistencetype(String persistencetype):
                self.persistencetype = persistencetype

# Persistence type for the virtual server.
#Note:
#The <persistenceType> parameter can take one of the following options:
#        SOURCEIP - When configured, the system selects a physical service based on the Load Balancing method, and then
#directs all the subsequent requests arriving from the same IP as the first request to the same physical service.
#        COOKIEINSERT - When configured, the system inserts an HTTP cookie into the client responses. The cookie is
#inserted into the "Cookie" header field of the HTTP response. The client stores the cookie (if enabled) and includes
#it in all the subsequent requests, which then match the cookie criteria. The cookie contains information about the
#service where the requests have to be sent.
#        SSLSESSION ID - When configured, the system creates a persistence that is session based on the arriving SSL
#Session ID, which is part of the SSL handshake process. All requests with the same SSL session ID are directed to the
#initially selected physical service.
#        CUSTOM SERVER ID -This mode of Persistence requires the server to provide its Server-ID in such a way that it
#can be extracted from subsequent requests. The system extracts the Server-ID from subsequent client requests and uses
#it to select a server. The server embeds the Server-ID into the URL query of the HTML links, accessible from the initial
#page that has to generate persistent HTTP requests.
#        RULE - When configured, the system maintains persistence based on the contents of the matched rule. This
#persistence requires an expression to be configured. The expression is created using the add expression CLI command and
#is configured on a virtual server, using the -rule option of the add lb vserver or set lb vserver CLI command. After
#successful evaluation of the expression, a persistence session is created and all subsequent matching client requests
#are directed to the previously selected server.
#        URLPASSIVE - This mode of Persistence requires the server to provide its Server-ID in such a way that it can be
#extracted from subsequent requests.The system extracts the Server-ID from subsequent client requests and uses it to
#select a server. The servers which require persistence, embed the Server-ID into the URL query of the HTML links,
#accessible from the initial page. The Server-ID is its IP address and port specified as a hexadecimal number.URL Passive
#persistence type requires an expression to be configured that specifies the location of the Server-ID in the client's
#requests. The expression is created using the CLI command add expression. This expression is configured on a virtual
#server, using option -rule of the add lb vserver or set lb vserver CLI command.
#        DESTIP -When configured, the system selects a physical service based on the Load Balancing method, and then
#directs all the subsequent requests with the same destination as the first packet to the same physical service. This
#will be used in LLB deployment scenarios.
#        SRCIPDESTIP - When configured, the system selects a physical service based on the Load Balancing method, and
#then directs all the subsequent requests with the same Source IP and Destination IP as the first packet to the same
#physical service. This will be used in IDS LB depolyments.
#        CALLID - When configured, the system maintains persistence based on CALLID used in the SIP transactions. All
#the SIP transactions with same CALLID are directed to the same server.
#        RTSPSID - When configured, the system maintains persistence based on RTSP sessionID provided by the server.
#The client also sends the same RTSP sessionID in the subsequent requests which are then directed to the same server.
        def get_persistencetype():
                return self.persistencetype

# The time period for which the persistence is in effect for a specific client. The value ranges from 2 to 1440 minutes.<br> Default value: 2<br> Minimum value =  0<br> Maximum value =  1440
        def set_timeout(long timeout):
                self.timeout = new Long(timeout)

# The time period for which the persistence is in effect for a specific client. The value ranges from 2 to 1440 minutes.<br> Default value: 2<br> Minimum value =  0<br> Maximum value =  1440
        def set_timeout(Long timeout):
                self.timeout = timeout

# The time period for which the persistence is in effect for a specific client. The value ranges from 2 to 1440 minutes.<br> Default value: 2<br> Minimum value =  0<br> Maximum value =  1440
        def get_timeout():
                return self.timeout

# Use this parameter to specify a backup persistence type for the virtual server.
#The Backup persistence option is used when the primary configured persistence mechanism on virtual server fails.
#The <persistenceBacup> parameter can take one of the following options:
#    SOURCEIP
#    NONE.<br> Default value: 0
        def set_persistencebackup(String persistencebackup):
                self.persistencebackup = persistencebackup

# Use this parameter to specify a backup persistence type for the virtual server.
#The Backup persistence option is used when the primary configured persistence mechanism on virtual server fails.
#The <persistenceBacup> parameter can take one of the following options:
#    SOURCEIP
#    NONE.<br> Default value: 0
        def get_persistencebackup():
                return self.persistencebackup

# The maximum time backup persistence is in effect for a specific client.<br> Default value: 2<br> Minimum value =  2<br> Maximum value =  1440
        def set_backuppersistencetimeout(long backuppersistencetimeout):
                self.backuppersistencetimeout = new Long(backuppersistencetimeout)

# The maximum time backup persistence is in effect for a specific client.<br> Default value: 2<br> Minimum value =  2<br> Maximum value =  1440
        def set_backuppersistencetimeout(Long backuppersistencetimeout):
                self.backuppersistencetimeout = backuppersistencetimeout

# The maximum time backup persistence is in effect for a specific client.<br> Default value: 2<br> Minimum value =  2<br> Maximum value =  1440
        def get_backuppersistencetimeout():
                return self.backuppersistencetimeout

# The load balancing method for the virtual server. The valid options for this parameter are:
#ROUNDROBIN, LEASTCONNECTION, LEASTRESPONSETIME, URLHASH, DOMAINHASH, DESTINATIONIPHASH, SOURCEIPHASH, SRCIPDESTIPHASH,LEASTBANDWIDTH, LEASTPACKETS, TOKEN, SRCIPDESTIPHASH, CUSTOMLOAD, SRCIPSRCPORTHASH, LRTM, CALLIDHASSH. 
#When the load balancing policy is configured as:
#        ROUNDROBIN - When configured, the system distributes incoming requests to each server in rotation, regardless of the load. When different weights are assigned to services then weighted round robin occurs and requests go to services according to how much weighting has been set.
#        LEASTCONNECTION (default value)- When configured, the system selects the service that has the least number of connections. For TCP, HTTP, HTTPS and SSL_TCP services the least number of connections includes:
#        Established, active connections to a service. Connection reuse applies to HTTP and HTTPS. Hence the count includes only those connections which have outstanding HTTP or HTTPS requests, and does not include inactive, reusable connections.
#        Connections to a service waiting in the Surge Queue, which exists only if the Surge Protection feature is enabled.
#For UDP services the least number of connections includes:
#        The number of sessions between client and a physical service. These sessions are the logical, time-based entities, created on first arriving UDP packet. If configured, weights are taken into account when server selection is performed.
#        LEASTRESPONSETIME - When configured, the system selects the service with the minimum average response time. The response time is the time interval taken when a request is sent to a service and first response packet comes back from the service, that is Time to First Byte (TTFB).
#        URLHASH - The system selects the service based on the hashed value of the incoming URL.To specify the number of bytes of the URL that is used to calculate the hash value use the optional argument [-hashLength <positive_integer>] in either the add lb vserver or set lb vserver CLI command. The default value is 80.
#        DOMAINHASH - When configured with this load balancing method, the system selects the service based on the hashed value of the domain name in the HTTP request. The domain name is taken either from the incoming URL or from the Host header of the HTTP request.
#Note:   The system defaults to LEASTCONNECTION if the request does not contain a domain name.
#If the domain name appears in both the URL and the host header, the system gives preference to the URL domain.
#
#        DESTINATIONIPHASH - The system selects the service based on the hashed value of the destination IP address in the TCP IP header.
#        SOURCEIPHASH - The system selects the service based on the hashed value of the client's IP address in the IP header.
#        LEASTBANDWIDTH - The system selects the service that is currently serving the least traffic, measured in megabits per second.
#        LEASTPACKETS - The system selects the service that is currently serving the lowest number of packets per second.
#        Token -The system selects the service based on the value, calculated from a token, extracted from the client's request (location and size of the token is configurable). For subsequent requests with the same token, the systems will select the same physical server.
#        SRCIPDESTIPHASH - The system selects the service based on the hashed value of the client's SOURCE IP and DESTINATION IP address in the TCP IP header.
#        CUSTOMLOAD - The system selects the service based on the it load which was determined by the LOAD monitors bound to the service.
#        SRCIPSRCPORTHASH - The system selects the service based on the hashed value of the client's SOURCE IP and SOURCE PORT in the TCP/UDP+IP header.
#        LRTM - When configured, the system selects the service with least response time learned through probing(number of active connections taken into account in addition to the response time). 
#        CALLIDHASSH - The system selects the service based on the hashed value of SIP callid.<br> Default value: LEASTCONNECTION
        def set_lbmethod(String lbmethod):
                self.lbmethod = lbmethod

# The load balancing method for the virtual server. The valid options for this parameter are:
#ROUNDROBIN, LEASTCONNECTION, LEASTRESPONSETIME, URLHASH, DOMAINHASH, DESTINATIONIPHASH, SOURCEIPHASH, SRCIPDESTIPHASH,LEASTBANDWIDTH, LEASTPACKETS, TOKEN, SRCIPDESTIPHASH, CUSTOMLOAD, SRCIPSRCPORTHASH, LRTM, CALLIDHASSH. 
#When the load balancing policy is configured as:
#        ROUNDROBIN - When configured, the system distributes incoming requests to each server in rotation, regardless of the load. When different weights are assigned to services then weighted round robin occurs and requests go to services according to how much weighting has been set.
#        LEASTCONNECTION (default value)- When configured, the system selects the service that has the least number of connections. For TCP, HTTP, HTTPS and SSL_TCP services the least number of connections includes:
#        Established, active connections to a service. Connection reuse applies to HTTP and HTTPS. Hence the count includes only those connections which have outstanding HTTP or HTTPS requests, and does not include inactive, reusable connections.
#        Connections to a service waiting in the Surge Queue, which exists only if the Surge Protection feature is enabled.
#For UDP services the least number of connections includes:
#        The number of sessions between client and a physical service. These sessions are the logical, time-based entities, created on first arriving UDP packet. If configured, weights are taken into account when server selection is performed.
#        LEASTRESPONSETIME - When configured, the system selects the service with the minimum average response time. The response time is the time interval taken when a request is sent to a service and first response packet comes back from the service, that is Time to First Byte (TTFB).
#        URLHASH - The system selects the service based on the hashed value of the incoming URL.To specify the number of bytes of the URL that is used to calculate the hash value use the optional argument [-hashLength <positive_integer>] in either the add lb vserver or set lb vserver CLI command. The default value is 80.
#        DOMAINHASH - When configured with this load balancing method, the system selects the service based on the hashed value of the domain name in the HTTP request. The domain name is taken either from the incoming URL or from the Host header of the HTTP request.
#Note:   The system defaults to LEASTCONNECTION if the request does not contain a domain name.
#If the domain name appears in both the URL and the host header, the system gives preference to the URL domain.
#
#        DESTINATIONIPHASH - The system selects the service based on the hashed value of the destination IP address in the TCP IP header.
#        SOURCEIPHASH - The system selects the service based on the hashed value of the client's IP address in the IP header.
#        LEASTBANDWIDTH - The system selects the service that is currently serving the least traffic, measured in megabits per second.
#        LEASTPACKETS - The system selects the service that is currently serving the lowest number of packets per second.
#        Token -The system selects the service based on the value, calculated from a token, extracted from the client's request (location and size of the token is configurable). For subsequent requests with the same token, the systems will select the same physical server.
#        SRCIPDESTIPHASH - The system selects the service based on the hashed value of the client's SOURCE IP and DESTINATION IP address in the TCP IP header.
#        CUSTOMLOAD - The system selects the service based on the it load which was determined by the LOAD monitors bound to the service.
#        SRCIPSRCPORTHASH - The system selects the service based on the hashed value of the client's SOURCE IP and SOURCE PORT in the TCP/UDP+IP header.
#        LRTM - When configured, the system selects the service with least response time learned through probing(number of active connections taken into account in addition to the response time). 
#        CALLIDHASSH - The system selects the service based on the hashed value of SIP callid.<br> Default value: LEASTCONNECTION
        def get_lbmethod():
                return self.lbmethod


# This parameter is used when the URLHASH or DOMAINHASH policy is set. Enter the number of bytes that will be hashed in the URL or DOMAIN name. Valid values are from 1 to 4096 bytes.<br> Default value: 80<br> Minimum value =  1<br> Maximum value =  4096
        def set_hashlength(long hashlength):
                self.hashlength = new Long(hashlength)


# This parameter is used when the URLHASH or DOMAINHASH policy is set. Enter the number of bytes that will be hashed in the URL or DOMAIN name. Valid values are from 1 to 4096 bytes.<br> Default value: 80<br> Minimum value =  1<br> Maximum value =  4096
        def set_hashlength(Long hashlength):
                self.hashlength = hashlength


# This parameter is used when the URLHASH or DOMAINHASH policy is set. Enter the number of bytes that will be hashed in the URL or DOMAIN name. Valid values are from 1 to 4096 bytes.<br> Default value: 80<br> Minimum value =  1<br> Maximum value =  4096
        def get_hashlength():
                return self.hashlength


# Use this parameter to set the DESTINATIONIPHASH or SOURCEIPHASH policy.
#Enter the netmask to be used in modifying the destination or source IP address or network.<br> Minimum length =  1.
        def set_netmask(String netmask):
                self.netmask = netmask


# Use this parameter to set the DESTINATIONIPHASH or SOURCEIPHASH policy.
Enter the netmask to be used in modifying the destination or source IP address or network.<br> Minimum length =  1.
        def get_netmask():
                return self.netmask


# The Network mask. Use this parameter if you are setting the DESTINATIONIPHASH or SOURCEIPHASH policy. Enter the netmask to be used in modifying the destination or source IP address or network.<br> Default value: 128<br> Minimum value =  1<br> Maximum value =  128
        def set_v6netmasklen(long v6netmasklen):
                self.v6netmasklen = new Long(v6netmasklen)


# The Network mask. Use this parameter if you are setting the DESTINATIONIPHASH or SOURCEIPHASH policy. Enter the netmask to be used in modifying the destination or source IP address or network.<br> Default value: 128<br> Minimum value =  1<br> Maximum value =  128
        def set_v6netmasklen(Long v6netmasklen):
                self.v6netmasklen = v6netmasklen


# The Network mask. Use this parameter if you are setting the DESTINATIONIPHASH or SOURCEIPHASH policy. Enter the netmask to be used in modifying the destination or source IP address or network.<br> Default value: 128<br> Minimum value =  1<br> Maximum value =  128
        def get_v6netmasklen():
                return self.v6netmasklen


# Use this parameter to specify the string value used to set the RULE persistence type.
#The string can be either an existing rule name (configured using add rule command) or else it can be an in-line expression with a maximum of 256 characters.<br> Default value: "none"
        def set_rule(String rule):
                self.rule = rule


# Use this parameter to specify the string value used to set the RULE persistence type.
#The string can be either an existing rule name (configured using add rule command) or else it can be an in-line expression with a maximum of 256 characters.<br> Default value: "none"
        def get_rule():
                return self.rule


# Use this parameter to specify the listen policy for LB Vserver.
#The string can be either an existing expression name (configured using add policy expression command) or else it can be an in-line expression with a maximum of 1500 characters.<br> Default value: "none"
        def set_listenpolicy(String listenpolicy):
                self.listenpolicy = listenpolicy


# Use this parameter to specify the listen policy for LB Vserver.
#The string can be either an existing expression name (configured using add policy expression command) or else it can be an in-line expression with a maximum of 1500 characters.<br> Default value: "none"
        def get_listenpolicy():
                return self.listenpolicy


# Use this parameter to specify the priority for listen policy of LB Vserver.<br> Default value: 101<br> Minimum value =  0<br> Maximum value =  100
        def set_listenpriority(long listenpriority):
                self.listenpriority = new Long(listenpriority)


# Use this parameter to specify the priority for listen policy of LB Vserver.<br> Default value: 101<br> Minimum value =  0<br> Maximum value =  100
        def set_listenpriority(Long listenpriority):
                self.listenpriority = listenpriority


# Use this parameter to specify the priority for listen policy of LB Vserver.<br> Default value: 101<br> Minimum value =  0<br> Maximum value =  100
        def get_listenpriority():
                return self.listenpriority


# Use this parameter to specify the expression to be used in response for RULE persistence type.
#The string  is an in-line expression with a maximum of 1500 characters.<br> Default value: "none"
        def set_resrule(String resrule):
                self.resrule = resrule


# Use this parameter to specify the expression to be used in response for RULE persistence type.
#The string  is an in-line expression with a maximum of 1500 characters.<br> Default value: "none"
        def get_resrule():
                return self.resrule


# Use this parameter to specify if the persistency is IP based. This parameter is Optional.<br> Minimum length =  1.
        def set_persistmask(String persistmask):
                self.persistmask = persistmask


# Use this parameter to specify if the persistency is IP based. This parameter is Optional.<br> Minimum length =  1.
        def get_persistmask():
                return self.persistmask


# The persistence mask. Use this parameter if you are using IP based persistence type on a ipv6 vserver.<br> Default value: 128<br> Minimum value =  1<br> Maximum value =  128
        def set_v6persistmasklen(long v6persistmasklen):
                self.v6persistmasklen = new Long(v6persistmasklen)


# The persistence mask. Use this parameter if you are using IP based persistence type on a ipv6 vserver.<br> Default value: 128<br> Minimum value =  1<br> Maximum value =  128
        def set_v6persistmasklen(Long v6persistmasklen):
                self.v6persistmasklen = v6persistmasklen


# The persistence mask. Use this parameter if you are using IP based persistence type on a ipv6 vserver.<br> Default value: 128<br> Minimum value =  1<br> Maximum value =  128
        def get_v6persistmasklen():
                return self.v6persistmasklen


# Use this parameter to enable priority queuing on the specified virtual server.<br> Default value: OFF
        def set_pq(String pq):
                self.pq = pq


# Use this parameter to enable priority queuing on the specified virtual server.<br> Default value: OFF
        def get_pq():
                return self.pq


# Use this parameter to enable SureConnect on the specified virtual server.<br> Default value: OFF
        def set_sc(String sc):
                self.sc = sc


# Use this parameter to enable SureConnect on the specified virtual server.<br> Default value: OFF
        def get_sc():
                return self.sc


# Use this parameter to enable natting for RTSP data connection.<br> Default value: OFF
        def set_rtspnat(String rtspnat):
                self.rtspnat = rtspnat


# Use this parameter to enable natting for RTSP data connection.<br> Default value: OFF
        def get_rtspnat():
                return self.rtspnat


# Use this parameter to specify the LB mode. If the value is specified as IP then the traffic is sent to the physical servers by changing the destination IP address to that of the physical server. If the value is MAC then the traffic is sent to the physical servers , by changing the destination MAC address to that of one of the physical servers, the destination IP is not changed. MAC mode is used mostly in Firewall Load Balancing scenario.<br> Default value: IP
        def set_m(String m):
                self.m = m


# Use this parameter to specify the LB mode. If the value is specified as IP then the traffic is sent to the physical servers by changing the destination IP address to that of the physical server. If the value is MAC then the traffic is sent to the physical servers , by changing the destination MAC address to that of one of the physical servers, the destination IP is not changed. MAC mode is used mostly in Firewall Load Balancing scenario.<br> Default value: IP
        def get_m():
                return self.m


# Use this parameter to specify the TOS ID of this vserver. Applicable only when the LB mode is TOS.<br> Default value: 0<br> Minimum value =  1<br> Maximum value =  63
        def set_tosid(long tosid):
                self.tosid = new Long(tosid)


# Use this parameter to specify the TOS ID of this vserver. Applicable only when the LB mode is TOS.<br> Default value: 0<br> Minimum value =  1<br> Maximum value =  63
        def set_tosid(Long tosid):
                self.tosid = tosid


# Use this parameter to specify the TOS ID of this vserver. Applicable only when the LB mode is TOS.<br> Default value: 0<br> Minimum value =  1<br> Maximum value =  63
        def get_tosid():
                return self.tosid


# Use this parameter to specify the length of the token in bytes. Applicable to TCP virtual servers, when Token Load Balancing method is selected. The datalength should not be more than 24k.<br> Default value: 0<br> Minimum value =  0<br> Maximum value =  100
        def set_datalength(long datalength):
                self.datalength = new Long(datalength)


# Use this parameter to specify the length of the token in bytes. Applicable to TCP virtual servers, when Token Load Balancing method is selected. The datalength should not be more than 24k.<br> Default value: 0<br> Minimum value =  0<br> Maximum value =  100
        def set_datalength(Long datalength):
                self.datalength = datalength


# Use this parameter to specify the length of the token in bytes. Applicable to TCP virtual servers, when Token Load Balancing method is selected. The datalength should not be more than 24k.<br> Default value: 0<br> Minimum value =  0<br> Maximum value =  100
        def get_datalength():
                return self.datalength


# Use this parameter to specifies offset of the data to be taken as token. Applicable to the TCP type virtual servers, when Token load balancing method is used.  Must be within the first 24k of the client TCP data.<br> Default value: 0<br> Minimum value =  0<br> Maximum value =  25400
        def set_dataoffset(long dataoffset):
                self.dataoffset = new Long(dataoffset)


# Use this parameter to specifies offset of the data to be taken as token. Applicable to the TCP type virtual servers, when Token load balancing method is used.  Must be within the first 24k of the client TCP data.<br> Default value: 0<br> Minimum value =  0<br> Maximum value =  25400
        def set_dataoffset(Long dataoffset):
                self.dataoffset = dataoffset


# Use this parameter to specifies offset of the data to be taken as token. Applicable to the TCP type virtual servers, when Token load balancing method is used.  Must be within the first 24k of the client TCP data.<br> Default value: 0<br> Minimum value =  0<br> Maximum value =  25400
        def get_dataoffset():
                return self.dataoffset


# Use this parameter to enable sessionless load balancing.<br> Default value: DISABLED
        def set_sessionless(String sessionless):
                self.sessionless = sessionless


# Use this parameter to enable sessionless load balancing.<br> Default value: DISABLED
        def get_sessionless():
                return self.sessionless


# The state of the load balancing virtual server.<br> Default value: ENABLED
        def set_state(String state):
                self.state = state


# The state of the load balancing virtual server.<br> Default value: ENABLED
        def get_state():
                return self.state


# Specifies the connection failover mode of the virtual server.<br> Default value: DISABLED
        def set_connfailover(String connfailover):
                self.connfailover = connfailover


# Specifies the connection failover mode of the virtual server.<br> Default value: DISABLED
        def get_connfailover():
                return self.connfailover


# The URL where traffic is redirected if the virtual server in the system becomes unavailable. You can enter up to 127 characters as the URL argument.
#WARNING!        Make sure that the domain you specify in the URL does not match the domain specified in the -d domainName argument of the add cs policy CLI command. If the same domain is specified in both arguments, the request will be
# continuously redirected to the same unavailable virtual server in the system  -  then the user may not get the requested content.<br> Default value: 0<br> Minimum length =  1.
        def set_redirurl(String redirurl):
                self.redirurl = redirurl


# The URL where traffic is redirected if the virtual server in the system becomes unavailable. You can enter up to 127 characters as the URL argument.
#WARNING!        Make sure that the domain you specify in the URL does not match the domain specified in the -d domainName argument of the add cs policy CLI command. If the same domain is specified in both arguments, the request will be
# continuously redirected to the same unavailable virtual server in the system  -  then the user may not get the requested content.<br> Default value: 0<br> Minimum length =  1.
        def get_redirurl():
                return self.redirurl


# Use this option to specify whether a virtual server, used for load balancing or content switching, routes requests to the cache redirection virtual server before sending it to the configured servers.<br> Default value: NO
        def set_cacheable(String cacheable):
                self.cacheable = cacheable


# Use this option to specify whether a virtual server, used for load balancing or content switching, routes requests to the cache redirection virtual server before sending it to the configured servers.<br> Default value: NO
        def get_cacheable():
                return self.cacheable


# The timeout value in seconds for idle client connection.<br> Default value: 0<br> Minimum value =  0<br> Maximum value =  31536000
        def set_clttimeout(long clttimeout):
                self.clttimeout = new Long(clttimeout)


# The timeout value in seconds for idle client connection.<br> Default value: 0<br> Minimum value =  0<br> Maximum value =  31536000
        def set_clttimeout(Long clttimeout):
                self.clttimeout = clttimeout


# The timeout value in seconds for idle client connection.<br> Default value: 0<br> Minimum value =  0<br> Maximum value =  31536000
        def get_clttimeout():
                return self.clttimeout


# The spillover factor based on which the traffic will be given to the backupvserver once the main virtual server reaches the spillover threshold.<br> Default value: 0
        def set_somethod(String somethod):
                self.somethod = somethod


# The spillover factor based on which the traffic will be given to the backupvserver once the main virtual server reaches the spillover threshold.<br> Default value: 0
        def get_somethod():
                return self.somethod


# The state of the spillover persistence.<br> Default value: DISABLED
        def set_sopersistence(String sopersistence):
                self.sopersistence = sopersistence


# The state of the spillover persistence.<br> Default value: DISABLED
        def get_sopersistence():
                return self.sopersistence


# The spillover persistency entry timeout.<br> Default value: 2<br> Minimum value =  2<br> Maximum value =  1440
        def set_sopersistencetimeout(long sopersistencetimeout):
                self.sopersistencetimeout = new Long(sopersistencetimeout)


# The spillover persistency entry timeout.<br> Default value: 2<br> Minimum value =  2<br> Maximum value =  1440
        def set_sopersistencetimeout(Long sopersistencetimeout):
                self.sopersistencetimeout = sopersistencetimeout


# The spillover persistency entry timeout.<br> Default value: 2<br> Minimum value =  2<br> Maximum value =  1440
        def get_sopersistencetimeout():
                return self.sopersistencetimeout


# In case of CONNECTION (or) DYNAMICCONNECTION type spillover method this value is treated as Maximum number of connections an lb vserver will handle before spillover takes place. In case of BANDWIDTH type spillover method this value is treated as the amount of incoming and outgoing traffic (in Kbps) a Vserver will handle before spillover takes place. In case of HEALTH type spillover method if the percentage of active services (by weight) becomes lower than this value, spillover takes place .<br> Default value: 0<br> Minimum value =  1<br> Maximum value =  4294967287
        def set_sothreshold(long sothreshold):
                self.sothreshold = new Long(sothreshold)


# In case of CONNECTION (or) DYNAMICCONNECTION type spillover method this value is treated as Maximum number of connections an lb vserver will handle before spillover takes place. In case of BANDWIDTH type spillover method this value is treated as the amount of incoming and outgoing traffic (in Kbps) a Vserver will handle before spillover takes place. In case of HEALTH type spillover method if the percentage of active services (by weight) becomes lower than this value, spillover takes place .<br> Default value: 0<br> Minimum value =  1<br> Maximum value =  4294967287
        def set_sothreshold(Long sothreshold):
                self.sothreshold = sothreshold


# In case of CONNECTION (or) DYNAMICCONNECTION type spillover method this value is treated as Maximum number of connections an lb vserver will handle before spillover takes place. In case of BANDWIDTH type spillover method this value is treated as the amount of incoming and outgoing traffic (in Kbps) a Vserver will handle before spillover takes place. In case of HEALTH type spillover method if the percentage of active services (by weight) becomes lower than this value, spillover takes place .<br> Default value: 0<br> Minimum value =  1<br> Maximum value =  4294967287
        def get_sothreshold():
                return self.sothreshold


# The state of port rewrite while performing HTTP redirect.<br> Default value: DISABLED
        def set_redirectportrewrite(String redirectportrewrite):
                self.redirectportrewrite = redirectportrewrite


# The state of port rewrite while performing HTTP redirect.<br> Default value: DISABLED
        def get_redirectportrewrite():
                return self.redirectportrewrite


# Perform delayed clean up of connections on this vserver.<br> Default value: ENABLED
        def set_downstateflush(String downstateflush):
                self.downstateflush = downstateflush


# Perform delayed clean up of connections on this vserver.<br> Default value: ENABLED
        def get_downstateflush():
                return self.downstateflush


# The Backup Virtual Server.<br> Default value: 0<br> Minimum length =  1.
        def set_backupvserver(String backupvserver):
                self.backupvserver = backupvserver


# The Backup Virtual Server.<br> Default value: 0<br> Minimum length =  1.
        def get_backupvserver():
                return self.backupvserver


# When this argument is enabled, traffic will continue reaching backup vservers even after primary comes UP from DOWN state.<br> Default value: DISABLED
        def set_disableprimaryondown(String disableprimaryondown):
                self.disableprimaryondown = disableprimaryondown


# When this argument is enabled, traffic will continue reaching backup vservers even after primary comes UP from DOWN state.<br> Default value: DISABLED
        def get_disableprimaryondown():
                return self.disableprimaryondown


# The virtual IP and port header insertion option for the vserver.
#        VIPADDR         - Header contains the vserver's IP address and port number without any translation.
#        OFF             - The virtual IP and port header insertion option is disabled.
#        V6TOV4MAPPING   - Header contains the mapped IPv4 address corresponding to the IPv6 address of the vserver and the port number. An IPv6 address can be mapped to a user-specified IPv4 address using the set ns ip6 command.<br> Default value: OFF
        def set_insertvserveripport(String insertvserveripport):
                self.insertvserveripport = insertvserveripport


# The virtual IP and port header insertion option for the vserver.
#        VIPADDR         - Header contains the vserver's IP address and port number without any translation.
#        OFF             - The virtual IP and port header insertion option is disabled.
#        V6TOV4MAPPING   - Header contains the mapped IPv4 address corresponding to the IPv6 address of the vserver and the port number. An IPv6 address can be mapped to a user-specified IPv4 address using the set ns ip6 command.<br> Default value: OFF
        def get_insertvserveripport():
                return self.insertvserveripport


# The name of virtual IP and port header.<br> Default value: 0<br> Minimum length =  1.
        def set_vipheader(String vipheader):
                self.vipheader = vipheader


# The name of virtual IP and port header.<br> Default value: 0<br> Minimum length =  1.
        def get_vipheader():
                return self.vipheader


# FQDN of authentication vserver.<br> Default value: 0<br> Minimum length =  3.<br> Maximum length =  252.
        def set_authenticationhost(String authenticationhost):
                self.authenticationhost = authenticationhost


# FQDN of authentication vserver.<br> Default value: 0<br> Minimum length =  3.<br> Maximum length =  252.
        def get_authenticationhost():
                return self.authenticationhost


# This option toggles on or off the application of authentication of incoming users to the vserver.<br> Default value: OFF
        def set_authentication(String authentication):
                self.authentication = authentication


# This option toggles on or off the application of authentication of incoming users to the vserver.<br> Default value: OFF
        def get_authentication():
                return self.authentication


# This option toggles on or off the HTTP 401 response based authentication.<br> Default value: OFF
        def set_authn401(String authn401):
                self.authn401 = authn401


# This option toggles on or off the HTTP 401 response based authentication.<br> Default value: OFF
        def get_authn401():
                return self.authn401


# Name of authentication vserver.<br> Default value: 0<br> Minimum length =  1.<br> Maximum length =  252.
        def set_authnvsname(String authnvsname):
                self.authnvsname = authnvsname


# Name of authentication vserver.<br> Default value: 0<br> Minimum length =  1.<br> Maximum length =  252.
        def get_authnvsname():
                return self.authnvsname


# Process traffic on bound Push vserver.<br> Default value: DISABLED
        def set_push(String push):
                self.push = push


# Process traffic on bound Push vserver.<br> Default value: DISABLED
        def get_push():
                return self.push


# The lb vserver of type PUSH/SSL_PUSH to which server pushes the updates received on the client facing non-push lb vserver.<br> Default value: 0<br> Minimum length =  1.
        def set_pushvserver(String pushvserver):
                self.pushvserver = pushvserver


# The lb vserver of type PUSH/SSL_PUSH to which server pushes the updates received on the client facing non-push lb vserver.<br> Default value: 0<br> Minimum length =  1.
        def get_pushvserver():
                return self.pushvserver


# Use this parameter to specify the expression to extract the label in response from server.
#The string can be either a named expression (configured using add policy expression command) or else it can be an in-line expression with a maximum of 63 characters.<br> Default value: "none"
        def set_pushlabel(String pushlabel):
                self.pushlabel = pushlabel


# Use this parameter to specify the expression to extract the label in response from server.
#The string can be either a named expression (configured using add policy expression command) or else it can be an in-line expression with a maximum of 63 characters.<br> Default value: "none"
        def get_pushlabel():
                return self.pushlabel


# Specify if multiple web 2.0 connections from the same client can connect to this vserver and expect updates.<br> Default value: NO
        def set_pushmulticlients(String pushmulticlients):
                self.pushmulticlients = pushmulticlients


# Specify if multiple web 2.0 connections from the same client can connect to this vserver and expect updates.<br> Default value: NO
        def get_pushmulticlients():
                return self.pushmulticlients


# The name of the TCP profile.<br> Default value: 0<br> Minimum length =  1.<br> Maximum length =  127.
        def set_tcpprofilename(String tcpprofilename):
                self.tcpprofilename = tcpprofilename


# The name of the TCP profile.<br> Default value: 0<br> Minimum length =  1.<br> Maximum length =  127.
        def get_tcpprofilename():
                return self.tcpprofilename


# Name of the HTTP profile.<br> Default value: 0<br> Minimum length =  1.<br> Maximum length =  127.
        def set_httpprofilename(String httpprofilename):
                self.httpprofilename = httpprofilename


# Name of the HTTP profile.<br> Default value: 0<br> Minimum length =  1.<br> Maximum length =  127.
        def get_httpprofilename():
                return self.httpprofilename


# Comments associated with this virtual server.<br> Default value: 0
        def set_comment(String comment):
                self.comment = comment


# Comments associated with this virtual server.<br> Default value: 0
        def get_comment():
                return self.comment


# The weight for the specified service.<br> Default value: 0<br> Minimum value =  1<br> Maximum value =  100
        def set_weight(long weight):
                self.weight = new Long(weight)


# The weight for the specified service.<br> Default value: 0<br> Minimum value =  1<br> Maximum value =  100
        def set_weight(Long weight):
                self.weight = weight


# The weight for the specified service.<br> Default value: 0<br> Minimum value =  1<br> Maximum value =  100
        def get_weight():
                return self.weight


# The service name bound to the selected load balancing virtual server.<br> Default value: 0<br> Minimum length =  1.
        def set_servicename(String servicename):
                self.servicename = servicename


# The service name bound to the selected load balancing virtual server.<br> Default value: 0<br> Minimum length =  1.
        def get_servicename():
                return self.servicename


# The redirect URL to be unset.
        def set_redirurlflags(boolean redirurlflags):
                self.redirurlflags = new Boolean(redirurlflags)


# The redirect URL to be unset.
        def set_redirurlflags(Boolean redirurlflags):
                self.redirurlflags = redirurlflags


# The redirect URL to be unset.
        def get_redirurlflags():
                return self.redirurlflags


# The new name of the virtual server.<br> Default value: 0<br> Minimum length =  1.
        def set_newname(String newname):
                self.newname = newname


# The new name of the virtual server.<br> Default value: 0<br> Minimum length =  1.
        def get_newname():
                return self.newname


# SSL status.<br> Default value: 0
        def get_value():
                return self.value


# The permanent mapping for the V6 Address.<br> Default value: 0
        def get_ipmapping():
                return self.ipmapping


# Type of LB vserver.<br> Default value: 0
        def get_type():
                return self.type


# Current LB vserver state.<br> Default value: 0
        def get_curstate():
                return self.curstate


# Effective state of the LB vserver , based on the state of backup vservers.<br> Default value: 0
        def get_effectivestate():
                return self.effectivestate


# Current status of the lb vserver. During the initial phase if the configured lb method is not round robin , the vserver will adopt round robin to distribute traffic for a predefined number of requests.<br> Default value: 0
        def get_status():
                return self.status


# Reason why a vserver is in RR. The following are the reasons:
#1  - MEP is DOWN (GSLB)
#2  - LB method has changed
#3  - Bound service's state changed to UP
#4  - A new service is bound
#5  - Startup RR factor has changed
#6  - LB feature is enabled
#7  - Load monitor is not active on a service
#8  - Vserver is Enabled
#9  - SSL feature is Enabled
#10 - All bound services have reached threshold. Using effective state to load balance (GSLB)
#11 - Primary state of bound services are not UP. Using effective state to load balance (GSLB)
#12 - No LB decision can be made as all bound services have either reached threshold or are not UP (GSLB)
#13 - All load monitors are active
#.<br> Default value: 0
        def get_lbrrreason():
                return self.lbrrreason


# Cache redirect type.<br> Default value: 0
        def get_redirect():
                return self.redirect


# Precedence.<br> Default value: 0
        def get_precedence():
                return self.precedence


# Home page.<br> Default value: 0
        def get_homepage():
                return self.homepage


# DNS vserver name.<br> Default value: 0
        def get_dnsvservername():
                return self.dnsvservername


# Domain.<br> Default value: 0
        def get_domain():
                return self.domain


# Cache virtual server.<br> Default value: 0
        def get_cachevserver():
                return self.cachevserver


# Health of vserver based on percentage of weights of active svcs/all svcs. This does not consider administratively disabled svcs.<br> Default value: 0
        def get_health():
                return self.health


# Expression specifying the priority of the next policy which will get evaluated if the current policy rule evaluates to TRUE.<br> Default value: 0
        def get_gotopriorityexpression():
                return self.gotopriorityexpression


# Rule type.<br> Default value: 0
        def get_ruletype():
                return self.ruletype


# LB group to which the lb vserver is to be bound.<br> Default value: 0
        def get_groupname():
                return self.groupname


# Domain name to be used in the set cookie header in case of cookie persistence.<br> Default value: 0
        def get_cookiedomain():
                return self.cookiedomain


# Map.<br> Default value: 0
        def get_map():
                return self.map


# Allow for greater than 2 GB transactions on this vserver.<br> Default value: 0
        def get_gt2gb():
                return self.gt2gb


# Tells whether threshold exceeded for this service participating in CUSTOMLB.<br> Default value: 0
        def get_thresholdvalue():
                return self.thresholdvalue


# The bindpoint to which the policy is bound.<br> Default value: 0
        def get_bindpoint():
                return self.bindpoint


# Invoke flag.<br> Default value: 0
        def get_invoke():
                return self.invoke


# The invocation type.<br> Default value: 0
        def get_labeltype():
                return self.labeltype


# Name of the label invoked.<br> Default value: 0
        def get_labelname():
                return self.labelname


# Cookie version.<br> Default value: 0
        def get_version():
                return self.version


# Total number of services bound to the vserver.<br> Default value: 0
        def get_totalservices():
                return self.totalservices


# Total number of active services bound to the vserver.<br> Default value: 0
        def get_activeservices():
                return self.activeservices


# Time when last state change happened. Seconds part.<br> Default value: 0
        def get_statechangetimeseconds():
                return self.statechangetimeseconds


# Time at which last state change happened. Milliseconds part.<br> Default value: 0
        def get_statechangetimemsec():
                return self.statechangetimemsec


# Time in 10 millisecond ticks since the last state change.<br> Default value: 0
        def get_tickssincelaststatechange():
                return self.tickssincelaststatechange

#TODO
# converts nitro response into object and returns the object array in case of get request.
#        protected base_resource[] get_nitro_response(nitro_service service, String response):
#                lbvserver_response result = (lbvserver_response) service.get_payload_formatter().string_to_resource(lbvserver_response.class, response)
#                if(result.errorcode != 0) {
#                        if (result.errorcode == 444) {
#                                service.clear_session()
#
#                        throw new nitro_exception(result.message,result.errorcode)
#
#                return result.lbvserver


# Returns the value of object identifier argument

        protected String get_object_name() {
                return self.name


# Use this API to add lbvserver.
        def base_response add(nitro_service client, lbvserver resource):
                lbvserver addresource = new lbvserver()
                addresource.name = resource.name
                addresource.servicetype = resource.servicetype
                addresource.ipv46 = resource.ipv46
                addresource.ippattern = resource.ippattern
                addresource.ipmask = resource.ipmask
                addresource.port = resource.port
                addresource.range = resource.range
                addresource.persistencetype = resource.persistencetype
                addresource.timeout = resource.timeout
                addresource.persistencebackup = resource.persistencebackup
                addresource.backuppersistencetimeout = resource.backuppersistencetimeout
                addresource.lbmethod = resource.lbmethod
                addresource.hashlength = resource.hashlength
                addresource.netmask = resource.netmask
                addresource.v6netmasklen = resource.v6netmasklen
                addresource.rule = resource.rule
                addresource.listenpolicy = resource.listenpolicy
                addresource.listenpriority = resource.listenpriority
                addresource.resrule = resource.resrule
                addresource.persistmask = resource.persistmask
                addresource.v6persistmasklen = resource.v6persistmasklen
                addresource.pq = resource.pq
                addresource.sc = resource.sc
                addresource.rtspnat = resource.rtspnat
                addresource.m = resource.m
                addresource.tosid = resource.tosid
                addresource.datalength = resource.datalength
                addresource.dataoffset = resource.dataoffset
                addresource.sessionless = resource.sessionless
                addresource.state = resource.state
                addresource.connfailover = resource.connfailover
                addresource.redirurl = resource.redirurl
                addresource.cacheable = resource.cacheable
                addresource.clttimeout = resource.clttimeout
                addresource.somethod = resource.somethod
                addresource.sopersistence = resource.sopersistence
                addresource.sopersistencetimeout = resource.sopersistencetimeout
                addresource.sothreshold = resource.sothreshold
                addresource.redirectportrewrite = resource.redirectportrewrite
                addresource.downstateflush = resource.downstateflush
                addresource.backupvserver = resource.backupvserver
                addresource.disableprimaryondown = resource.disableprimaryondown
                addresource.insertvserveripport = resource.insertvserveripport
                addresource.vipheader = resource.vipheader
                addresource.authenticationhost = resource.authenticationhost
                addresource.authentication = resource.authentication
                addresource.authn401 = resource.authn401
                addresource.authnvsname = resource.authnvsname
                addresource.push = resource.push
                addresource.pushvserver = resource.pushvserver
                addresource.pushlabel = resource.pushlabel
                addresource.pushmulticlients = resource.pushmulticlients
                addresource.tcpprofilename = resource.tcpprofilename
                addresource.httpprofilename = resource.httpprofilename
                addresource.comment = resource.comment
                return addresource.add_resource(client)


# Use this API to add lbvserver resources.
        def base_responses add(nitro_service client, lbvserver resources[]):
                base_responses result = null
                if (resources != null && resources.length > 0) {
                        lbvserver addresources[] = new lbvserver[resources.length]
                        for (int i=0;i<resources.length;i++){
                                addresources[i] = new lbvserver()
                                addresources[i].name = resources[i].name
                                addresources[i].servicetype = resources[i].servicetype
                                addresources[i].ipv46 = resources[i].ipv46
                                addresources[i].ippattern = resources[i].ippattern
                                addresources[i].ipmask = resources[i].ipmask
                                addresources[i].port = resources[i].port
                                addresources[i].range = resources[i].range
                                addresources[i].persistencetype = resources[i].persistencetype
                                addresources[i].timeout = resources[i].timeout
                                addresources[i].persistencebackup = resources[i].persistencebackup
                                addresources[i].backuppersistencetimeout = resources[i].backuppersistencetimeout
                                addresources[i].lbmethod = resources[i].lbmethod
                                addresources[i].hashlength = resources[i].hashlength
                                addresources[i].netmask = resources[i].netmask
                                addresources[i].v6netmasklen = resources[i].v6netmasklen
                                addresources[i].rule = resources[i].rule
                                addresources[i].listenpolicy = resources[i].listenpolicy
                                addresources[i].listenpriority = resources[i].listenpriority
                                addresources[i].resrule = resources[i].resrule
                                addresources[i].persistmask = resources[i].persistmask
                                addresources[i].v6persistmasklen = resources[i].v6persistmasklen
                                addresources[i].pq = resources[i].pq
                                addresources[i].sc = resources[i].sc
                                addresources[i].rtspnat = resources[i].rtspnat
                                addresources[i].m = resources[i].m
                                addresources[i].tosid = resources[i].tosid
                                addresources[i].datalength = resources[i].datalength
                                addresources[i].dataoffset = resources[i].dataoffset
                                addresources[i].sessionless = resources[i].sessionless
                                addresources[i].state = resources[i].state
                                addresources[i].connfailover = resources[i].connfailover
                                addresources[i].redirurl = resources[i].redirurl
                                addresources[i].cacheable = resources[i].cacheable
                                addresources[i].clttimeout = resources[i].clttimeout
                                addresources[i].somethod = resources[i].somethod
                                addresources[i].sopersistence = resources[i].sopersistence
                                addresources[i].sopersistencetimeout = resources[i].sopersistencetimeout
                                addresources[i].sothreshold = resources[i].sothreshold
                                addresources[i].redirectportrewrite = resources[i].redirectportrewrite
                                addresources[i].downstateflush = resources[i].downstateflush
                                addresources[i].backupvserver = resources[i].backupvserver
                                addresources[i].disableprimaryondown = resources[i].disableprimaryondown
                                addresources[i].insertvserveripport = resources[i].insertvserveripport
                                addresources[i].vipheader = resources[i].vipheader
                                addresources[i].authenticationhost = resources[i].authenticationhost
                                addresources[i].authentication = resources[i].authentication
                                addresources[i].authn401 = resources[i].authn401
                                addresources[i].authnvsname = resources[i].authnvsname
                                addresources[i].push = resources[i].push
                                addresources[i].pushvserver = resources[i].pushvserver
                                addresources[i].pushlabel = resources[i].pushlabel
                                addresources[i].pushmulticlients = resources[i].pushmulticlients
                                addresources[i].tcpprofilename = resources[i].tcpprofilename
                                addresources[i].httpprofilename = resources[i].httpprofilename
                                addresources[i].comment = resources[i].comment

                        result = add_bulk_request(client, addresources)

                return result


# Use this API to delete lbvserver of given name.
        def base_response delete(nitro_service client, String name):
                lbvserver deleteresource = new lbvserver()
                deleteresource.name = name
                return deleteresource.delete_resource(client)


# Use this API to delete lbvserver.
        def base_response delete(nitro_service client, lbvserver resource):
                lbvserver deleteresource = new lbvserver()
                deleteresource.name = resource.name
                return deleteresource.delete_resource(client)


# Use this API to delete lbvserver resources of given names.
        def base_responses delete(nitro_service client, String name[]):
                base_responses result = null
                if (name != null && name.length > 0) {
                        lbvserver deleteresources[] = new lbvserver[name.length]
                        for (int i=0;i<name.length;i++){
                                deleteresources[i] = new lbvserver()
                                deleteresources[i].name = name[i]

                        result = delete_bulk_request(client, deleteresources)

                return result


# Use this API to delete lbvserver resources.
        def base_responses delete(nitro_service client, lbvserver resources[]):
                base_responses result = null
                if (resources != null && resources.length > 0) {
                        lbvserver deleteresources[] = new lbvserver[resources.length]
                        for (int i=0;i<resources.length;i++){
                                deleteresources[i] = new lbvserver()
                                deleteresources[i].name = resources[i].name

                        result = delete_bulk_request(client, deleteresources)

                return result


# Use this API to update lbvserver.
        def base_response update(nitro_service client, lbvserver resource):
                lbvserver updateresource = new lbvserver()
                updateresource.name = resource.name
                updateresource.ipv46 = resource.ipv46
                updateresource.ippattern = resource.ippattern
                updateresource.ipmask = resource.ipmask
                updateresource.weight = resource.weight
                updateresource.servicename = resource.servicename
                updateresource.persistencetype = resource.persistencetype
                updateresource.timeout = resource.timeout
                updateresource.persistencebackup = resource.persistencebackup
                updateresource.backuppersistencetimeout = resource.backuppersistencetimeout
                updateresource.lbmethod = resource.lbmethod
                updateresource.hashlength = resource.hashlength
                updateresource.netmask = resource.netmask
                updateresource.v6netmasklen = resource.v6netmasklen
                updateresource.rule = resource.rule
                updateresource.resrule = resource.resrule
                updateresource.persistmask = resource.persistmask
                updateresource.v6persistmasklen = resource.v6persistmasklen
                updateresource.pq = resource.pq
                updateresource.sc = resource.sc
                updateresource.rtspnat = resource.rtspnat
                updateresource.m = resource.m
                updateresource.tosid = resource.tosid
                updateresource.datalength = resource.datalength
                updateresource.dataoffset = resource.dataoffset
                updateresource.sessionless = resource.sessionless
                updateresource.connfailover = resource.connfailover
                updateresource.backupvserver = resource.backupvserver
                updateresource.redirurl = resource.redirurl
                updateresource.cacheable = resource.cacheable
                updateresource.clttimeout = resource.clttimeout
                updateresource.somethod = resource.somethod
                updateresource.sothreshold = resource.sothreshold
                updateresource.sopersistence = resource.sopersistence
                updateresource.sopersistencetimeout = resource.sopersistencetimeout
                updateresource.redirectportrewrite = resource.redirectportrewrite
                updateresource.downstateflush = resource.downstateflush
                updateresource.insertvserveripport = resource.insertvserveripport
                updateresource.vipheader = resource.vipheader
                updateresource.disableprimaryondown = resource.disableprimaryondown
                updateresource.authenticationhost = resource.authenticationhost
                updateresource.authentication = resource.authentication
                updateresource.authn401 = resource.authn401
                updateresource.authnvsname = resource.authnvsname
                updateresource.push = resource.push
                updateresource.pushvserver = resource.pushvserver
                updateresource.pushlabel = resource.pushlabel
                updateresource.pushmulticlients = resource.pushmulticlients
                updateresource.listenpolicy = resource.listenpolicy
                updateresource.listenpriority = resource.listenpriority
                updateresource.tcpprofilename = resource.tcpprofilename
                updateresource.httpprofilename = resource.httpprofilename
                updateresource.comment = resource.comment
                return updateresource.update_resource(client)


# Use this API to update lbvserver resources.
        def base_responses update(nitro_service client, lbvserver resources[]):
                base_responses result = null
                if (resources != null && resources.length > 0) {
                        lbvserver updateresources[] = new lbvserver[resources.length]
                        for (int i=0;i<resources.length;i++){
                                updateresources[i] = new lbvserver()
                                updateresources[i].name = resources[i].name
                                updateresources[i].ipv46 = resources[i].ipv46
                                updateresources[i].ippattern = resources[i].ippattern
                                updateresources[i].ipmask = resources[i].ipmask
                                updateresources[i].weight = resources[i].weight
                                updateresources[i].servicename = resources[i].servicename
                                updateresources[i].persistencetype = resources[i].persistencetype
                                updateresources[i].timeout = resources[i].timeout
                                updateresources[i].persistencebackup = resources[i].persistencebackup
                                updateresources[i].backuppersistencetimeout = resources[i].backuppersistencetimeout
                                updateresources[i].lbmethod = resources[i].lbmethod
                                updateresources[i].hashlength = resources[i].hashlength
                                updateresources[i].netmask = resources[i].netmask
                                updateresources[i].v6netmasklen = resources[i].v6netmasklen
                                updateresources[i].rule = resources[i].rule
                                updateresources[i].resrule = resources[i].resrule
                                updateresources[i].persistmask = resources[i].persistmask
                                updateresources[i].v6persistmasklen = resources[i].v6persistmasklen
                                updateresources[i].pq = resources[i].pq
                                updateresources[i].sc = resources[i].sc
                                updateresources[i].rtspnat = resources[i].rtspnat
                                updateresources[i].m = resources[i].m
                                updateresources[i].tosid = resources[i].tosid
                                updateresources[i].datalength = resources[i].datalength
                                updateresources[i].dataoffset = resources[i].dataoffset
                                updateresources[i].sessionless = resources[i].sessionless
                                updateresources[i].connfailover = resources[i].connfailover
                                updateresources[i].backupvserver = resources[i].backupvserver
                                updateresources[i].redirurl = resources[i].redirurl
                                updateresources[i].cacheable = resources[i].cacheable
                                updateresources[i].clttimeout = resources[i].clttimeout
                                updateresources[i].somethod = resources[i].somethod
                                updateresources[i].sothreshold = resources[i].sothreshold
                                updateresources[i].sopersistence = resources[i].sopersistence
                                updateresources[i].sopersistencetimeout = resources[i].sopersistencetimeout
                                updateresources[i].redirectportrewrite = resources[i].redirectportrewrite
                                updateresources[i].downstateflush = resources[i].downstateflush
                                updateresources[i].insertvserveripport = resources[i].insertvserveripport
                                updateresources[i].vipheader = resources[i].vipheader
                                updateresources[i].disableprimaryondown = resources[i].disableprimaryondown
                                updateresources[i].authenticationhost = resources[i].authenticationhost
                                updateresources[i].authentication = resources[i].authentication
                                updateresources[i].authn401 = resources[i].authn401
                                updateresources[i].authnvsname = resources[i].authnvsname
                                updateresources[i].push = resources[i].push
                                updateresources[i].pushvserver = resources[i].pushvserver
                                updateresources[i].pushlabel = resources[i].pushlabel
                                updateresources[i].pushmulticlients = resources[i].pushmulticlients
                                updateresources[i].listenpolicy = resources[i].listenpolicy
                                updateresources[i].listenpriority = resources[i].listenpriority
                                updateresources[i].tcpprofilename = resources[i].tcpprofilename
                                updateresources[i].httpprofilename = resources[i].httpprofilename
                                updateresources[i].comment = resources[i].comment

                        result = update_bulk_request(client, updateresources)

                return result


# Use this API to unset the properties of lbvserver resource.
# Properties that need to be unset are specified in args array.
        def base_response unset(nitro_service client, String name, String args[]):
                lbvserver unsetresource = new lbvserver()
                unsetresource.name = name
                return unsetresource.unset_resource(client, args)


# Use this API to unset the properties of lbvserver resource.
# Properties that need to be unset are specified in args array.
        def base_response unset(nitro_service client, lbvserver resource, String[] args):
                lbvserver unsetresource = new lbvserver()
                unsetresource.name = resource.name
                unsetresource.backupvserver = resource.backupvserver
                unsetresource.clttimeout = resource.clttimeout
                unsetresource.redirurlflags = resource.redirurlflags
                unsetresource.authenticationhost = resource.authenticationhost
                unsetresource.authnvsname = resource.authnvsname
                unsetresource.pushvserver = resource.pushvserver
                unsetresource.pushlabel = resource.pushlabel
                unsetresource.tcpprofilename = resource.tcpprofilename
                unsetresource.httpprofilename = resource.httpprofilename
                unsetresource.rule = resource.rule
                unsetresource.sothreshold = resource.sothreshold
                unsetresource.servicename = resource.servicename
                unsetresource.persistencetype = resource.persistencetype
                unsetresource.timeout = resource.timeout
                unsetresource.persistencebackup = resource.persistencebackup
                unsetresource.backuppersistencetimeout = resource.backuppersistencetimeout
                unsetresource.lbmethod = resource.lbmethod
                unsetresource.hashlength = resource.hashlength
                unsetresource.netmask = resource.netmask
                unsetresource.v6netmasklen = resource.v6netmasklen
                unsetresource.resrule = resource.resrule
                unsetresource.persistmask = resource.persistmask
                unsetresource.v6persistmasklen = resource.v6persistmasklen
                unsetresource.pq = resource.pq
                unsetresource.sc = resource.sc
                unsetresource.rtspnat = resource.rtspnat
                unsetresource.m = resource.m
                unsetresource.tosid = resource.tosid
                unsetresource.datalength = resource.datalength
                unsetresource.dataoffset = resource.dataoffset
                unsetresource.sessionless = resource.sessionless
                unsetresource.connfailover = resource.connfailover
                unsetresource.redirurl = resource.redirurl
                unsetresource.cacheable = resource.cacheable
                unsetresource.somethod = resource.somethod
                unsetresource.sopersistence = resource.sopersistence
                unsetresource.sopersistencetimeout = resource.sopersistencetimeout
                unsetresource.redirectportrewrite = resource.redirectportrewrite
                unsetresource.downstateflush = resource.downstateflush
                unsetresource.insertvserveripport = resource.insertvserveripport
                unsetresource.vipheader = resource.vipheader
                unsetresource.disableprimaryondown = resource.disableprimaryondown
                unsetresource.authentication = resource.authentication
                unsetresource.authn401 = resource.authn401
                unsetresource.push = resource.push
                unsetresource.pushmulticlients = resource.pushmulticlients
                unsetresource.listenpolicy = resource.listenpolicy
                unsetresource.listenpriority = resource.listenpriority
                unsetresource.comment = resource.comment
                return unsetresource.unset_resource(client,args)


# Use this API to unset the properties of lbvserver resources.
# Properties that need to be unset are specified in args array.
        def base_responses unset(nitro_service client, String name[], String args[]):
                base_responses result = null
                if (name != null && name.length > 0) {
                        lbvserver unsetresources[] = new lbvserver[name.length]
                        for (int i=0;i<name.length;i++){
                                unsetresources[i] = new lbvserver()
                                unsetresources[i].name = name[i]

                        result = unset_bulk_request(client, unsetresources,args)

                return result


# Use this API to unset the properties of lbvserver resources.
# Properties that need to be unset are specified in args array.
        def base_responses unset(nitro_service client, lbvserver resources[],  String[] args):
                base_responses result = null
                if (resources != null && resources.length > 0) {
                        lbvserver unsetresources[] = new lbvserver[resources.length]
                        for (int i=0;i<resources.length;i++){
                                unsetresources[i] = new lbvserver()
                                unsetresources[i].name = resources[i].name
                                unsetresources[i].backupvserver = resources[i].backupvserver
                                unsetresources[i].clttimeout = resources[i].clttimeout
                                unsetresources[i].redirurlflags = resources[i].redirurlflags
                                unsetresources[i].authenticationhost = resources[i].authenticationhost
                                unsetresources[i].authnvsname = resources[i].authnvsname
                                unsetresources[i].pushvserver = resources[i].pushvserver
                                unsetresources[i].pushlabel = resources[i].pushlabel
                                unsetresources[i].tcpprofilename = resources[i].tcpprofilename
                                unsetresources[i].httpprofilename = resources[i].httpprofilename
                                unsetresources[i].rule = resources[i].rule
                                unsetresources[i].sothreshold = resources[i].sothreshold
                                unsetresources[i].servicename = resources[i].servicename
                                unsetresources[i].persistencetype = resources[i].persistencetype
                                unsetresources[i].timeout = resources[i].timeout
                                unsetresources[i].persistencebackup = resources[i].persistencebackup
                                unsetresources[i].backuppersistencetimeout = resources[i].backuppersistencetimeout
                                unsetresources[i].lbmethod = resources[i].lbmethod
                                unsetresources[i].hashlength = resources[i].hashlength
                                unsetresources[i].netmask = resources[i].netmask
                                unsetresources[i].v6netmasklen = resources[i].v6netmasklen
                                unsetresources[i].resrule = resources[i].resrule
                                unsetresources[i].persistmask = resources[i].persistmask
                                unsetresources[i].v6persistmasklen = resources[i].v6persistmasklen
                                unsetresources[i].pq = resources[i].pq
                                unsetresources[i].sc = resources[i].sc
                                unsetresources[i].rtspnat = resources[i].rtspnat
                                unsetresources[i].m = resources[i].m
                                unsetresources[i].tosid = resources[i].tosid
                                unsetresources[i].datalength = resources[i].datalength
                                unsetresources[i].dataoffset = resources[i].dataoffset
                                unsetresources[i].sessionless = resources[i].sessionless
                                unsetresources[i].connfailover = resources[i].connfailover
                                unsetresources[i].redirurl = resources[i].redirurl
                                unsetresources[i].cacheable = resources[i].cacheable
                                unsetresources[i].somethod = resources[i].somethod
                                unsetresources[i].sopersistence = resources[i].sopersistence
                                unsetresources[i].sopersistencetimeout = resources[i].sopersistencetimeout
                                unsetresources[i].redirectportrewrite = resources[i].redirectportrewrite
                                unsetresources[i].downstateflush = resources[i].downstateflush
                                unsetresources[i].insertvserveripport = resources[i].insertvserveripport
                                unsetresources[i].vipheader = resources[i].vipheader
                                unsetresources[i].disableprimaryondown = resources[i].disableprimaryondown
                                unsetresources[i].authentication = resources[i].authentication
                                unsetresources[i].authn401 = resources[i].authn401
                                unsetresources[i].push = resources[i].push
                                unsetresources[i].pushmulticlients = resources[i].pushmulticlients
                                unsetresources[i].listenpolicy = resources[i].listenpolicy
                                unsetresources[i].listenpriority = resources[i].listenpriority
                                unsetresources[i].comment = resources[i].comment

                        result = unset_bulk_request(client, unsetresources,args)

                return result


# Use this API to enable lbvserver of given name.
        def base_response enable(nitro_service client, String name):
                lbvserver enableresource = new lbvserver()
                enableresource.name = name
                return enableresource.perform_operation(client,"enable")


# Use this API to enable lbvserver.
        def base_response enable(nitro_service client, lbvserver resource):
                lbvserver enableresource = new lbvserver()
                enableresource.name = resource.name
                return enableresource.perform_operation(client,"enable")


# Use this API to enable lbvserver resources of given names.
        def base_responses enable(nitro_service client, String name[]):
                base_responses result = null
                if (name != null && name.length > 0) {
                        lbvserver enableresources[] = new lbvserver[name.length]
                        for (int i=0;i<name.length;i++){
                                enableresources[i] = new lbvserver()
                                enableresources[i].name = name[i]

                        result = perform_operation_bulk_request(client, enableresources,"enable")

                return result


# Use this API to enable lbvserver resources.
        def base_responses enable(nitro_service client, lbvserver resources[]):
                base_responses result = null
                if (resources != null && resources.length > 0) {
                        lbvserver enableresources[] = new lbvserver[resources.length]
                        for (int i=0;i<resources.length;i++){
                                enableresources[i] = new lbvserver()
                                enableresources[i].name = resources[i].name

                        result = perform_operation_bulk_request(client, enableresources,"enable")

                return result


# Use this API to disable lbvserver of given name.
        def base_response disable(nitro_service client, String name):
                lbvserver disableresource = new lbvserver()
                disableresource.name = name
                return disableresource.perform_operation(client,"disable")


# Use this API to disable lbvserver.
        def base_response disable(nitro_service client, lbvserver resource):
                lbvserver disableresource = new lbvserver()
                disableresource.name = resource.name
                return disableresource.perform_operation(client,"disable")


# Use this API to disable lbvserver resources of given names.
        def base_responses disable(nitro_service client, String name[]):
                base_responses result = null
                if (name != null && name.length > 0) {
                        lbvserver disableresources[] = new lbvserver[name.length]
                        for (int i=0;i<name.length;i++){
                                disableresources[i] = new lbvserver()
                                disableresources[i].name = name[i]

                        result = perform_operation_bulk_request(client, disableresources,"disable")

                return result


# Use this API to disable lbvserver resources.
        def base_responses disable(nitro_service client, lbvserver resources[]):
                base_responses result = null
                if (resources != null && resources.length > 0) {
                        lbvserver disableresources[] = new lbvserver[resources.length]
                        for (int i=0;i<resources.length;i++){
                                disableresources[i] = new lbvserver()
                                disableresources[i].name = resources[i].name

                        result = perform_operation_bulk_request(client, disableresources,"disable")

                return result


# Use this API to rename a lbvserver resource.
        def base_response rename(nitro_service client, lbvserver resource, String new_name):
                lbvserver renameresource = new lbvserver()
                renameresource.name = resource.name
                return renameresource.rename_resource(client,new_name)


# Use this API to rename a lbvserver resource.
        def base_response rename(nitro_service client, String name, String new_name):
                lbvserver renameresource = new lbvserver()
                renameresource.name = name
                return renameresource.rename_resource(client,new_name)


# Use this API to fetch all the lbvserver resources that are configured on netscaler.
        def lbvserver[] get(nitro_service service):
                lbvserver obj = new lbvserver()
                lbvserver[] response = (lbvserver[])obj.get_resources(service)
                return response

# Use this API to fetch all the lbvserver resources that are configured on netscaler.
        def lbvserver[] get(nitro_service service, options option):
                lbvserver obj = new lbvserver()
                lbvserver[] response = (lbvserver[])obj.get_resources(service,option)
                return response

# Use this API to fetch lbvserver resource of given name .
        def lbvserver get(nitro_service service, String name):
                lbvserver obj = new lbvserver()
                obj.set_name(name)
                lbvserver response = (lbvserver) obj.get_resource(service)
                return response


# Use this API to fetch lbvserver resources of given names .
        def lbvserver[] get(nitro_service service, String name[]):
                if (name !=null && name.length>0) {
                        lbvserver response[] = new lbvserver[name.length]
                        lbvserver obj[] = new lbvserver[name.length]
                        for (int i=0;i<name.length;i++) {
                                obj[i] = new lbvserver()
                                obj[i].set_name(name[i])
                                response[i] = (lbvserver) obj[i].get_resource(service)

                        return response

                return null

# Use this API to fetch filtered set of lbvserver resources.
# filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
        def lbvserver[] get_filtered(nitro_service service, String filter):
                lbvserver obj = new lbvserver()
                options option = new options()
                option.set_filter(filter)
                lbvserver[] response = (lbvserver[]) obj.getfiltered(service, option)
                return response


# Use this API to fetch filtered set of lbvserver resources.
# set the filter parameter values in filtervalue object.
        def lbvserver[] get_filtered(nitro_service service, filtervalue[] filter):
                lbvserver obj = new lbvserver()
                options option = new options()
                option.set_filter(filter)
                lbvserver[] response = (lbvserver[]) obj.getfiltered(service, option)
                return response


# Use this API to count the lbvserver resources configured on NetScaler.
        def count(nitro_service service):
                lbvserver obj = new lbvserver()
                options option = new options()
                option.set_count(true)
                lbvserver[] response = (lbvserver[])obj.get_resources(service, option)
                if (response != null) {
                        return response[0].__count

                return 0


# Use this API to count filtered the set of lbvserver resources.
# filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
        def count_filtered(nitro_service service, String filter):
                lbvserver obj = new lbvserver()
                options option = new options()
                option.set_count(true)
                option.set_filter(filter)
                lbvserver[] response = (lbvserver[]) obj.getfiltered(service, option)
                if (response != null) {
                        return response[0].__count

                return 0


# Use this API to count the filtered set of lbvserver resources.
# set the filter parameter values in filtervalue object.
        def count_filtered(nitro_service service, filtervalue[] filter):
                lbvserver obj = new lbvserver()
                options option = new options()
                option.set_count(true)
                option.set_filter(filter)
                lbvserver[] response = (lbvserver[]) obj.getfiltered(service, option)
                if (response != null) {
                        return response[0].__count

                return 0



