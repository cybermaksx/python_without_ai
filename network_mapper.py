import socket
import struct
import os

target_ip = input("What is your target's ip adress ? \n")

my_ip_raw = os.popen("ip -4 addr show wlan0 | awk '/inet/ {print $2}' | cut -d/ -f1").read().strip() #Could have been done easier but i like it this way

my_ip = my_ip_raw

port_range = int(input("\n What type of port scanning you would like to do ?  \n 1) Standart Ports for enumerating Standart services \n 2) I want to check all ports on my target \n  "))


type_of_scan = int(input("\n What type of scan you want to do : \ n 1) TCP SCAN   \n  2_  SYN Scan  \n Please choose :   "))

if port_range == 1:
    ports = [21, 22, 80, 443] #I will add all default ports here 
elif port_range == 2:
    ports = range(1, 65536)

def tcp_scan (target_ip,target_port ):
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        settimeout(3)
        s.connect((target_ip,target_port))
        
        print (f"[*] {target_port}  is  open ")
    except socket.timeout:
        print(" Target is unreacheable  ")

    except ConnectionRefusedError:
        print (f" {target_port} seems to be closed | filtered")










