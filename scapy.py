from scapy.all import IP, ICMP

pkt = IP(dst="google.com") / ICMP()
pkt.show()
