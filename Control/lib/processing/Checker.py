import os.path
from os import system
from time import sleep
import requests
def Linux_Checker():
    system("clear")
    if os.path.exists('/usr/share/metasploit-framework'):
        sleep(0.5)
        print ("metasploit Installed!")
    else:
        sleep(0.5)
        print ("metasploit Not Installed!")
    if os.path.exists('/usr/share/metasploit-framework/msfvenom'):
        sleep(0.5)
        print ("msfvenom Found!")
    else:
        print ("msfvenom Not Found!")
    if os.path.exists('/usr/share/metasploit-framework/msfconsole'):
        sleep(0.5)
        print ("msfconsole Found!")
    else:
        sleep(0.5)
        print ("msfconsole Not Found!")
    if os.path.exists('/usr/local/lib/python3.9/dist-packages/fade'):
        sleep(0.5)
        print ("Fade Installed!")
    else:
        sleep(0.5)
        print ("Fade Not Installed!")
    url = "https://google.com"
    timeout = 10
    try:
            request = requests.get(url, timeout=timeout)
            print ("Internet Connected")
    except (requests.ConnectionError, requests.Timeout) as exception:
            print ("Internet Not Connected")
    if os.path.exists('/bin/ruby'):
        sleep(0.5)
        print ("Rupy Installed!")
    else:
        sleep(0.5)
        print ("Rupy not Installed!")
    if os.path.exists('/usr/local/bin/lolcat'):
        sleep(0.5)
        print ("lolcat Installed!")
    else:
        print ("lolcat Not Installed!")
    sleep(0.5)
    print ("[+] Starting SAT-BCH.........!!!")
def Termux_Checker():
    system("clear")
    if os.path.exists('/data/data/com.termux/files/home/metasploit-framework'):
        sleep(0.5)
        print ("metasploit Installed!")
    else:
        sleep(0.5)
        print ("metasploit Not Installed!")
    if os.path.exists('data/data/com.termux/files/home/metasploit-framework/msfvenom'):
        sleep(0.5)
        print ("msfvenom Found!")
    else:
        print ("msfvenom Not Found!")
    if os.path.exists('/data/data/com.termux/files/home/metasploit-framework/msfconsole'):
        sleep(0.5)
        print ("msfconsole Found!")
    else:
        sleep(0.5)
        print ("msfconsole Not Found!")
    if os.path.exists('/data/data/com.termux/files/usr/lib/python3.9/site-packages/fade/):
        sleep(0.5)
        print ("Fade Installed!")
    else:
        sleep(0.5)
        print ("Fade Not Installed!")
    url = "https://google.com"
    timeout = 10
    try:
            request = requests.get(url, timeout=timeout)
            print ("Internet Connected")
    except (requests.ConnectionError, requests.Timeout) as exception:
            print ("Internet Not Connected")
    if os.path.exists('/data/data/com.termux/files/usr/bin/ruby'):
        sleep(0.5)
        print ("Rupy Installed!")
    else:
        sleep(0.5)
        print ("Rupy not Installed!")
    if os.path.exists('/data/data/com.termux/files/usr/bin/lolcat'):
        sleep(0.5)
        print ("lolcat Installed!")
    else:
        print ("lolcat Not Installed!")
    sleep(0.5)
    print ("[+] Starting SAT-BCH.........!!!")
if sys.platform.startswith('linux'):
    Linux_Checker()