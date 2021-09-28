import fade , sys
from os import system
from time import sleep
from colorama import Fore,Back,Style
from cryptography.fernet import Fernet
def slow_print(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     sleep(2./90)
def CLS():
    system("clear")
def Main_Menu():
    print (f"{Fore.BLUE}[{Fore.WHITE}01{Fore.BLUE}] {Fore.GREEN}Android .......... {Fore.WHITE}android payload & Injection Payload")
    print (f"{Fore.BLUE}[{Fore.WHITE}02{Fore.BLUE}] {Fore.BLUE}Windows .......... {Fore.WHITE}windows payload")
    print (f"{Fore.BLUE}[{Fore.WHITE}03{Fore.BLUE}] {Fore.CYAN}Linux ............ {Fore.WHITE}linux payload")
    print (f"{Fore.BLUE}[{Fore.WHITE}04{Fore.BLUE}] {Fore.YELLOW}Mac .............. {Fore.WHITE}mac payload")
    print (f"{Fore.BLUE}[{Fore.WHITE}05{Fore.BLUE}] {Fore.MAGENTA}Install .......... {Fore.WHITE}install metasploit")
def list_Android():
    print (f"{Fore.BLUE}[{Fore.WHITE}01{Fore.BLUE}] {Fore.GREEN}Android {Fore.BLUE}meterpreter {Fore.YELLOW}reverse {Fore.RED}tcp ")
    print (f"{Fore.BLUE}[{Fore.WHITE}02{Fore.BLUE}] {Fore.YELLOW}Injection {Fore.GREEN}android {Fore.WHITE}Payload")
    print (f"{Fore.BLUE}[{Fore.WHITE}00{Fore.BLUE}] {Fore.WHITE}Back to {Fore.RED}main {Fore.YELLOW}menu")
def list_Windows():
    print (f"{Fore.BLUE}[{Fore.WHITE}01{Fore.BLUE}] {Fore.BLUE}Windows {Fore.WHITE}payload")
    print (f"{Fore.BLUE}[{Fore.WHITE}00{Fore.BLUE}] {Fore.WHITE}Back to {Fore.RED}main {Fore.YELLOW}Menu")
def list_linux():
    print (f"{Fore.BLUE}[{Fore.WHITE}01{Fore.BLUE}] {Fore.CYAN}Linux {Fore.WHITE}payload {Fore.BLUE}or {Fore.RED}script")
    print (f"{Fore.BLUE}[{Fore.WHITE}00{Fore.BLUE}] {Fore.WHITE}Back to {Fore.RED}main {Fore.YELLOW}menu")
def list_Mac():
    print (f"{Fore.BLUE}[{Fore.WHITE}01{Fore.BLUE}] {Fore.CYAN}M{Fore.WHITE}a{Fore.BLUE}c {Fore.WHITE}payload")
    print (f"{Fore.BLUE}[{Fore.WHITE}00{Fore.BLUE}] {Fore.WHITE}Back to {Fore.RED}main {Fore.YELLOW}menu")