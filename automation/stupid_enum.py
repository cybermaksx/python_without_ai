import os
import subprocess
import json


print("Hello friend..... This is a very stupid script ")

target_ip = input("What is your target:\n")




def automated_rec(target_ip):
    subprocess.run(f"sudo nmap -sS -sV -T3 -F {target_ip} -oN nmap.txt", shell=True)


    next_step = int(input("Choose your next step:\n1)Directory bruteforce\n2)Vhost enumeration\n3)Whatweb+curl for info-gathering about web\n"))


    if next_step == 1:
        target_port = int(input("Choose port where we are going to look for directories?\n"))
        subprocess.run(f"ffuf -u http://{target_ip}:{target_port}/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-words.txt -mc 200,301,302,401,403 -t 50", shell=True)



    elif next_step == 2:
       target_port = int(input("Choose port where  web is located?\n"))
       subprocess.run(f"gobuster vhost -u http://{target_ip}:{target_port}  -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain", shell=True)



    elif next_step == 3:
         target_port = int(input("Choose port where  web is located?\n"))
         subprocess.run("whatweb -v http://{target_ip}:{target_port} ", shell = True)
         subprocess.run("curl -I http://{target_ip}:{target_port} ", shell = True) 



    else:
        print("May the force be with you !")       





automated_rec(target_ip)
