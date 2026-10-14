from scapy.all import * 
# a lookup table that turns protocol numbers into names
protocols = {1: "ICMP", 6: "TCP", 17: "UDP"}
# this function runs every time a packet is captured, and decides what to print
def show_packet(packet):
    if packet.haslayer(IP):
# grabs the source and destination port numbers from the packet so we know which service it's talking to
        ports = ""
        if packet.haslayer(TCP):
            ports = str(packet[TCP].sport) + " -> " + str(packet[TCP].dport)
        if packet.haslayer(UDP):
             ports = str(packet[UDP].sport) + " -> " + str(packet[UDP].dport)
        print (packet[IP].src, "->", packet[IP].dst, protocols.get(packet[IP].proto, "OTHER"), ports)
        if packet.haslayer(Raw):
            data = packet[Raw].load[:60]
# prints out the actual data being carried inside the packet, if there is any
            print("    payload:", data)
# starts the actual sniffing, capturing packets live and sending each one to show_packet 
sniff(iface="eth0", prn=show_packet, store=0)
