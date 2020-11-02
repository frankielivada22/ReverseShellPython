# ReverseShellPython
Memo: Makes a reverse shell on windows 10 computers (also had usb rubberducky compatibilaty)

# How to use:
Setup:
1) Download ncat.exe from here. -(http://nmap.org/dist/ncat-portable-5.59BETA1.zip)
2) Extract the exe and put it in the same folder as NCPY.py.
3) Run NCPY.exe.
4) Check if info at the top of the console is correct. If not enter settings and change it in there.
5) Start listener and wait for console to say "Listining on IP:PORT"

# How does it work?
When you start listening on the python script it will start a ncat listener and a https service (for the usb rubber ducky) after you have everything set up (need to port forward if not doing it on a local network) send the victim the payload.ps1 file and have them run it.

# Disclaimer
I am not responsible for what you do with this, this is for educational purposes only
