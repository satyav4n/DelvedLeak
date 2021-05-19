#!/bin/usr/python3
# -*- coding: utf-8 -*-

# Creator: Chungo
#Twitter: @Chungo_0
#Instagram: chungo.0

import enquiries
import modules
from colorama import init, Fore, Back, Style
import os
import subprocess
import time
import sys

# Initializes Colorama
init(autoreset=True)

print("\n"+Style.BRIGHT+"Starting TorGhost....", end="")
print("\r", end="")

#start torghost
subprocess.getoutput('torghost -s')

print(Style.BRIGHT + Fore.GREEN+" [✓]"+Fore.RED+"TorGhost running.")
print (Style.BRIGHT+Fore.BLUE+"----------------------"+Fore.RESET+Style.RESET_ALL)
print (Style.BRIGHT+Fore.RED+"⬤ "+Fore.RESET+Style.RESET_ALL + " = High risk")
print (Style.BRIGHT+Fore.GREEN+"⬤ "+Fore.RESET+Style.RESET_ALL + " = Low risk")
print (Style.BRIGHT+Fore.BLUE+"----------------------"+Fore.RESET+Style.RESET_ALL)


def Main():


	title = "\n"+ Style.BRIGHT + Back.YELLOW + Fore.WHITE+"Choose one of these options: "
	options = ['1. Password Breach', '2. Email pwned', '0. Exit']

	choice = enquiries.choose(title, options)
	option = choice[0]



	if(option == "1"):
		modules.Pwndb()

	elif(option == "2"):
		modules.emailInfo()

	elif(option == "0"):
		ExitScript()



def ExitScript():
	print("\n"+"Stop TorGhost service...")
	
	print("\n"+ Style.BRIGHT + Back.YELLOW + Fore.RED+"Network error detect, please wait...")
	os.system("airmon-ng check kill > /dev/null 2>&1")
	os.system("service NetworkManager start")
	os.system("torghost -x > /dev/null 2>&1")
	print("\n"+Style.BRIGHT + Fore.GREEN+" [-]"+Fore.RED+"TorGhost Stop.")
	print (Style.BRIGHT+Fore.BLUE+"----------------------"+Fore.RESET+Style.RESET_ALL)
	print (Style.BRIGHT + Back.BLUE+" Twitter: "+Style.RESET_ALL + Back.RESET+" https://twitter.com/Chungo_0")
	print (Style.BRIGHT + Back.YELLOW+" Patreon: "+Style.RESET_ALL + Back.RESET+" https://www.patreon.com/HackingPills")
	print (Style.BRIGHT+Fore.BLUE+"----------------------"+Fore.RESET+Style.RESET_ALL)
	sys.exit()



if __name__ == "__main__":

	try:
		while True:
			Main()

	except KeyboardInterrupt:
		ExitScript()








