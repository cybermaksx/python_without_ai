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
    
    # IP header

    #



    
    # combine headers
    packet = ip_header + tcp_header
    
    # send packet

syn_scan(ip, port)

