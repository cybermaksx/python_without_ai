import os

ip = os.popen("ip addr show wlan0").read()
# парсим строку с inet
for line in ip.split('\n'):
    if 'inet ' in line:
        ip = line.strip().split()[1].split('/')[0]
        print(ip)  


        
