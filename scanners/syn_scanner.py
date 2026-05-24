import socket
import struct
import os

ip = input("What is your target IP : \n")
port = int(input("Which port do you want to check: \n"))
my_ip_raw = os.popen("ip -4 addr show wlan0 | awk '/inet/ {print $2}' | cut -d/ -f1").read().strip()
my_ip = my_ip_raw



def calculate_checksum(data):
    if len(data) % 2 != 0:
        data += b'\x00'
    s = 0
    for i in range(0, len(data), 2):
        word = (data[i] << 8) + data[i + 1]
        s += word
    s = (s >> 16) + (s & 0xFFFF)
    s += (s >> 16)
    return ~s & 0xFFFF

def syn_scan(ip, port):
    source_port = 1234  # our source port

    # TCP header fields
    seq = 0
    ack = 0
    offset_flags = (5 << 12) | 0x002
    window = 0
    checksum = 0
    urgent = 0

    tcp_header = struct.pack("!HHLLHHHH", source_port, port, seq, ack, offset_flags, window, checksum, urgent)

    # TCP checksum requires pseudo-header: src_ip + dst_ip + zero + protocol + tcp_length
    src_ip_bytes = socket.inet_aton(my_ip)
    dst_ip_bytes = socket.inet_aton(ip)
    pseudo_header = struct.pack("!4s4sBBH", src_ip_bytes, dst_ip_bytes, 0, 6, 20)
    tcp_checksum = calculate_checksum(pseudo_header + tcp_header)
    tcp_header = struct.pack("!HHLLHHHH", source_port, port, seq, ack, offset_flags, window, tcp_checksum, urgent)

    # IP header fields
    ihl_version = 69
    tos = 0
    total_length = 40
    identification = 1
    frag_offset = 0
    ttl = 64
    protocol = 6
    checksum = 0
    source_ip = socket.inet_aton(my_ip)
    dest_ip = socket.inet_aton(ip)

    ip_header = struct.pack("!BBHHHBBH4s4s", ihl_version, tos, total_length, identification, frag_offset, ttl, protocol, checksum, source_ip, dest_ip)
    packet = ip_header + tcp_header

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        s.settimeout(3)
        s.sendto(packet, (ip, 0))
        response = s.recvfrom(1024)
        tcp = response[0][20:40]
        tcp_fields = struct.unpack("!HHLLHHHH", tcp)
        flags = tcp_fields[4] & 0x1FF
        if flags == 0x012:
            print("[*] Port is open")
        elif flags & 0x004:
            print("[*] Port is closed")
        print(f"Flags: {hex(flags)}")

    except Exception as e:
        print(f"Error: {e}")


syn_scan(ip, port)

