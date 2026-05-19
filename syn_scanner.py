import socket
import struct

ip = input("What is your target IP : \n")
port = int(input("Which port do you want to check: \n"))

def syn_scan(ip, port):
    source_port = 1234  # our source port
    
    # TCP header fields
    seq = 0             # sequence number
    ack = 0             # acknowledgement number
    offset_flags = 0    # data offset + flags (SYN bit here)
    window = 0          # window size
    checksum = 0        # checksum
    urgent = 0          # urgent pointer
    
    tcp_header = struct.pack("!HHLLHHHH", source_port, port, seq, ack, offset_flags, window, checksum, urgent)
    
    # IP header fields
    ihl_version = 69      # version 4, header length 20 bytes
    tos = 0               # type of service
    total_length = 40     # 20 IP + 20 TCP
    identification = 1    # random number
    frag_offset = 0       # no fragmentation
    ttl = 64              # time to live
    protocol = 6          # TCP
    checksum = 0          # OS will calculate
    source_ip = socket.inet_aton("192.168.100.111") # your IP
    dest_ip = socket.inet_aton(ip)               # target IP

    ip_header = struct.pack("!BBHHHBBH4s4s", ihl_version,tos,total_length,identification,frag_offset,ttl,protocol,checksum,source_ip,dest_ip)
    # combine headers
    packet = ip_header + tcp_header
    # send packet

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        s.sendto(packet, (ip, 0))
        s.recvfrom(1024)
        

        
        

syn_scan(ip, port)

