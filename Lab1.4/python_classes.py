from ipaddress import IPv4Network
import random


class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        ip = random.randint(0x0B000000, 0xDF000000)
        mask = random.randint(8, 24)
        IPv4Network.__init__(self, (ip, mask), strict=False)

    def regular(self):
        return not self.is_multicast or self.is_link_local or self.is_loopback or self.is_private or self.is_reserved or self.is_unspecified
    def key_value(self):
        return int(self.netmask), int(self.network_address)


rlist=[]
while len(rlist) <= 50:
    rnet = IPv4RandomNetwork()
    if rnet.regular:
        rlist.append(rnet)
        print(rnet)
print()
print("Sorted: ")
def sortfunc(x):
    return x.key_value()

for n in sorted(rlist, key=sortfunc):
    print(n)


