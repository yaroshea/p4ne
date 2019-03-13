from pysnmp.hlapi import *  # Импортировать только High-level API

community_name = "public"
ipaddr_string = "10.31.70.107"
port_int = "161"

result = getCmd(SnmpEngine(),
                CommunityData(community_name, mpModel=0),
                UdpTransportTarget((ipaddr_string, port_int)),
                ContextData(),
                ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', '0')))

result2 = nextCmd(SnmpEngine(),
                CommunityData(community_name, mpModel=0),
                UdpTransportTarget((ipaddr_string, port_int)),
                ContextData(),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')), lexicographicMode = False)

for i in result:
    p= list(i[3])
    for x in p:
        print(x)
p=""
for i in result2:
    p = list(i[3])
    for z in p:
        print(z)
