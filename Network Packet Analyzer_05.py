from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        
        # Get protocol name
        if protocol == 6:
            proto_name = "TCP"
        elif protocol == 17:
            proto_name = "UDP"
        elif protocol == 1:
            proto_name = "ICMP"
        else:
            proto_name = "Other"

        print(f"IP Packet - Source: {ip_src}, Destination: {ip_dst}, Protocol: {proto_name}")
        
        # Display payload data if it's a known protocol
        if proto_name == "TCP" and TCP in packet:
            print(f"Payload: {bytes(packet[TCP].payload)}")
        elif proto_name == "UDP" and UDP in packet:
            print(f"Payload: {bytes(packet[UDP].payload)}")
        elif proto_name == "ICMP" and ICMP in packet:
            print(f"Payload: {bytes(packet[ICMP].payload)}")

# Start sniffing
print("Starting packet sniffer...")
sniff(prn=packet_callback, store=0)
