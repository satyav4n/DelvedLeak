import enquiries
import requests
import json
import subprocess
import os
import mechanize
from bs4 import BeautifulSoup
from colorama import init, Fore, Back, Style
import re

def emailInfo():

	print(Style.BRIGHT + Back.YELLOW + Fore.WHITE+'\nSearch for possible email passwords\n')
	email = input(Style.BRIGHT + Back.YELLOW + Fore.RED+'Enter a email>>'+Style.RESET_ALL + Back.RESET + Fore.RESET)
	url = "https://emailrep.io/"+email
	SearchReputation(url)
	LeakSources(email)


def SearchReputation(url):
	r = requests.get(url)
	data = r.json()

	if("status" not in data):
		credentials_leaked = Style.BRIGHT+Fore.RED+"⬤"+Fore.RESET if data["details"]["credentials_leaked"] == True else Fore.GREEN+"⬤"
		data_breach = Style.BRIGHT+Fore.RED+"⬤"+Fore.RESET if  data["details"]["data_breach"] == True else Fore.GREEN+"⬤"
		spoofable = Style.BRIGHT+Fore.RED+"⬤"+Fore.RESET if data["details"]["spoofable"] == True else Fore.GREEN+"⬤"
		reputation = Style.BRIGHT+Fore.RED + "High" + Style.RESET_ALL + Fore.RESET if data["reputation"] == "high" else Style.BRIGHT+Fore.GREEN + "Low" + Style.RESET_ALL + Fore.RESET
		profiles = data["details"]["profiles"]


		print("\n"+"Reputation: "+reputation)
		print("Data breach: "+data_breach)
		print("Credentials leaked: "+credentials_leaked)
		print("Spoofable: "+spoofable)
		print("Profiles with this email:")
		if(len(profiles)):
			for profile in profiles:
				print("[+] "+profile)

		else:
			print("    No profiles found")	


	else:
		print("\n"+Style.BRIGHT + Back.YELLOW + Fore.RED+"Fail conection, wait for new IP ...",end="")
		print("\r", end="")

		#Get new ip to bypass search attemps limit
		subprocess.getoutput('torghost -r')
		SearchReputation(url)



def LeakSources(email):


	print("\nGetting source leaks, please wait....")
	os.system("airmon-ng check kill > /dev/null 2>&1")
	os.system("service NetworkManager start")
	os.system("torghost -x > /dev/null 2>&1")
	b = mechanize.Browser()
	b.set_handle_robots(False)
	b.set_handle_equiv(False)
	b.set_handle_refresh(False)
	b.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	url = "https://www.fasterbroadband.co.uk/tools/data-breach-search"

	response = b.open(url)

	b.form = list(b.forms())[0]
	b.form.controls[0].value = "cosculluela@gmail.com"

	response = b.submit()

	soup = BeautifulSoup(response.read(), "html.parser" )
	classP = soup.find_all("div", {"class": "breach-data"})
	tileLeak = []
	infoLeak = []

	for x in classP[0]:
		if('<strong>' in str(x)):
			tileLeak.append(x.find('strong').text)

		if('<p>' in str(x)):

			line = x.find('p').text
			p = re.compile("\n(.*)")
			line = re.findall(p,str(line))
			infoLeak.append(line)
			#infoLeak.append(x.find('p').text)

	infoLeak.pop(0)

	print ("\n"+Style.BRIGHT+Fore.BLUE+"-----------------------------------------------------------------------------------------------------------"+Fore.RESET+Style.RESET_ALL)
	count = 0
	for info in infoLeak:

		link = tileLeak[count].replace(':','')
		link = link.replace(' ','-')
		print(Style.BRIGHT+Fore.RED+Back.YELLOW+ tileLeak[count]+Style.RESET_ALL+Fore.RESET+Back.RESET+"\n")
		print(info[0]+Style.BRIGHT+Fore.RED+info[1]+Style.RESET_ALL+Fore.RESET+Back.RESET)
		print("\n"+Style.BRIGHT+Fore.BLUE+"Link to download leaks: "+Fore.RESET+"https://raidforums.com/Thread-"+link+"Database-Leaked-Download")
		count = count+1
		print ("\n"+Style.BRIGHT+Fore.BLUE+"-----------------------------------------------------------------------------------------------------------"+Fore.RESET+Style.RESET_ALL)

	