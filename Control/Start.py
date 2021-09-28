#!/bin/python
#Modules
from os import system
from time import sleep
from colorama import Fore
import fade , sys , base64 , colorama
from sys import platform as _platform
from lib.design.Banners import *
from lib.processing.processing import *
from lib.design.list import *
from lib.processing.Payloads import *
def Main_Control():
    Banner()
    Main_Menu()
    q = input ("Enter Your Selection : ")
    if q == "1" or q == "01":
        CLS()
        Android_Banner()
        list_Android()
        qq = input ("Enter Your Selection : ")
        if qq == "1" or qq == "01":
            Android()
            listner_Android()
    elif q == "2" or qq == "02":
        list_Windows()
        q = input ("Enter Your Selection : ")
        if q == "1" or q == "01":
            Windows()
            qq = input ("Enter Your Selection : ")
            if qq == "1" or qq == "01":
                Windows()
                listner_Windows()
    elif q == "3" or q == "03":
        list_linux()
        qq = input ("Enter Your Selection : ")
        if qq == "1" or qq == "01":
            Linux()
            listner_Linux()
    elif q == "4" or q == "04":
        list_Mac()
        qq = input ("Enter Your Selection : ")
        if qq == "1" or qq == "01":
            Mac()
            listner_Mac()
Main_Control()
