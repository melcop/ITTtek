from scapy.all import IP, ICMP, sr1

def ping(host):
    packet = IP(dst=host)/ICMP()
    response = sr1(packet, timeout=2, verbose=0)
    if response:
        return f"{host} is online"
    else:
        return f"{host} is offline"
    
host_to_scan = "kea.dk"
result = ping(host_to_scan)
print(result)