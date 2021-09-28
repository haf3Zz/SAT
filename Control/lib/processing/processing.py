#!/bin/python
#Modules
from os import system
from time import sleep
from colorama import Fore
import fade , sys , base64 , colorama
from sys import platform as _platform
#Clear Screen                    #<?>
def CLS():
    system("clear")
#Slow Print Text                 #<?>
def slow_print(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     sleep(2./90)
#Platform Check                  #<?>
def Platform():
    if sys.platform.startswith('linux'):
        slow_print (f"{Fore.BLUE}[{Fore.WHITE}-{Fore.BLUE}] {Fore.YELLOW} This Tool Works Automatically Pleasse Dont Turn Off \n")
    if not sys.platform.startswith('linux'):
        slow_print (f"{Fore.BLUE}[{Fore.WHITE}-{Fore.BLUE}] {Fore.YELLOW} This Tool Works Automatically Pleasse Dont Turn Off \n")

Platform()
