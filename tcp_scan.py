import socket

target_ip = input("\nTarget IP : \n  ")
target_port = int(input("\nWhich port do you want to check: \n"))

def tcp_scan(target_ip,target_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip,target_port))
        print("[*] Port is open")

    except socket.timeout:
        print("Connection is time out")


    except ConnectionRefusedError:
        print("Looks like this port is closed !")


tcp_scan(target_ip,target_port)    
    
    
        
        
























