import os
import subprocess

target_ip = input("What is your target's ip  : \n")

level_of_enumeration = int(input("What kind of enumeration you want to do ?\n1)Fast enumeration \n2)Deep enumeration\n  " ))


def fast_enumeration (target_ip):
    try:
        print(f"[*] Running nmap scan against {target_ip} ")
        subprocess.run(f"sudo nmap -sS -sV -sC -F {target_ip} -oN nmap.txt", shell=True)

        ports = []


        with open(f"{options.ip}/nmap_portscan.txt") as f:
                for line in f:
                    if "open" in line:
                        port = line.split("/")[0]
                        ports.append(port)          
        
            ports = ",".join(ports)
            print("[+] Open ports:", ports)
    

    
    


def deep_enumeration(target_ip):
    pass




if level_of_enumeration == 1:
    fast_enumeration(target_ip)
elif level_of_enumeration == 2:
    deep_enumeration(target_ip)

else:
    print(" Please choose the right method !!! ")





















