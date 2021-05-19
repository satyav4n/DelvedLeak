import enquiries
import requests
import json
import subprocess
import os
from colorama import init, Fore, Back, Style


def Pwndb():
	proxy = '127.0.0.1:9050'
	session = requests.session()
	session.proxies = {'http': 'socks5h://{}'.format(proxy), 'https': 'socks5h://{}'.format(proxy)}
	email = input(Style.BRIGHT + Back.YELLOW + Fore.RED+'Enter a email>>'+Style.RESET_ALL + Back.RESET + Fore.RESET)
	domain = "%"
	url = "http://pwndb2am4tzkvold.onion/"

	if("@" in email):
		username = email.split("@")[0]
		domain = email.split("@")[1]
		if(not username):
			username = '%'
	request_data = {'luser': username, 'domain': domain, 'luseropr': 1, 'domainopr': 1, 'submitform': 'em'}
	r = session.post(url, data=request_data)
	if("Array" not in r.text):
		return None
	leaks = r.text.split("Array")[1:]
	emails =[]
	for leak in leaks:
		leaked_email = ''
		domain = ''
		password = ''

		try:
			leaked_email = leak.split("[luser] =>")[1].split("[")[0].strip()
			domain = leak.split("[domain] =>")[1].split("[")[0].strip()
			password = leak.split("[password] =>")[1].split(")")[0].strip()
		except:
			pass
		if (leaked_email):
			emails.append({'username': leaked_email, 'domain': domain, 'password': password})

	emails.pop(0)
	if(emails != []):

		print ("\n"+Style.BRIGHT+ Fore.RED + Back.YELLOW + "Leaks Found:"+ Style.RESET_ALL + Fore.RESET + Back.RESET+"\n")
		print (Style.BRIGHT+Fore.BLUE+"------------------------------------------"+Fore.RESET+Style.RESET_ALL)

		for email in emails:
			username = email.get('username', '')
			domain = email.get('domain', '')
			password = email.get('password', '')

			print(Style.BRIGHT+ Fore.WHITE+ username + "@" + domain + Fore.RESET + Fore.RED+ ":"+Fore.RESET+ Fore.WHITE+ Back.RED + password + Fore.RESET + Back.RESET)
		print (Style.BRIGHT+Fore.BLUE+"------------------------------------------"+Fore.RESET+Style.RESET_ALL)

	else:	
		print (Style.BRIGHT+ Fore.GREEN + Back.YELLOW +" Leaks not Found"+ Style.RESET_ALL + Fore.RESET + Back.RESET)