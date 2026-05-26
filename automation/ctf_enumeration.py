import os
import subprocess
import json

target_ip = input("What is your target's ip  : \n")

level_of_enumeration = int(input("What kind of enumeration you want to do ?\n1)Fast enumeration \n2)Deep enumeration\n  " ))


def web_enumeration(target_url):
    output_file = "dirsearch_results.json"
    try:
        print(f"Running dirsearch against {target_url}")
        subprocess.run(f"dirsearch -u {target_url} --format=json -o {output_file}",shell=True check=True) #check = True that python will interpret mistake as exception if one occurs
        with open(output_file, "r") as f:
                    data = json.load(f)


        directories = []

        for entry in data.get("results", []):
                    directories.append({
                        "url": entry.get("url"),
                        "status": entry.get("status"),
                        "size": entry.get("content-length"),
                    })



        return directories

    except subprocess.CalledProcessError as e:
        print(f"dirsearch doesn't work {e} ")

    





def fast_scan(target_ip):
    try:
        print(f"[*] Running nmap scan against {target_ip}")
        subprocess.run(f"sudo nmap -sS -sV -sC -F {target_ip} -oN nmap.txt", shell=True)
        
        ports = []
        with open("nmap.txt") as f:
            for line in f:
                if "open" in line:
                    port = line.split("/")[0]
                    ports.append(port)
        
        ports = ",".join(ports)
        print("[+] Open ports:", ports)
        
        if not ports:
            print("No open ports has been found")
    
    except Exception as e:
        print(f"Error: {e}")
                             


def deep_scan(target_ip):
    pass







if level_of_enumeration == 1:
    fast_enumeration(target_ip)
elif level_of_enumeration == 2:
    deep_enumeration(target_ip)

else:
    print(" Please choose the right method !!! ")





















