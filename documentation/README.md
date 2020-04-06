[MIT Taguar258 2019]
# Raven-Storm Toolkit Documentation:
A strong, customizable dos and DDoS framework with over 48 functions/commands for testing your own servers.

## Table of content:

|A|Content|Description|
|:-:|:----------:|:-----------------------:|
|A1|Introduction|What makes Raven-Storm different?|
|A2|Infos|Message by the developer.|
|A3|Visualisation|How does the attack work?|
|A4|Basics|How do I use Raven-Storm?|
|A5|Installation|How to setup Raven-Storm.|
|A6|terms|What is an IP/Port/Thread/...?|

|B|Function|Description|
|:-:|:----------:|:-----------------------:|
|B1|Introduction|What is the definition of functions in Raven-Storm?|
|B2|Self-learning |How does Raven-Storm learn by itself?|
|B3|CFile|How to load in a configuration File.|
|B4|ROS|Run commands on the start of Raven-Storm.|
|B5|Fast Redis start|Start client/server using the command-line.
|B6|Fast run dos|Start a dos attack the fastest way possible.|
|B7|Fast run pod|Start a pod attack the fastest way possible.|

|C|Command|Description|
|:-:|:----------:|:-----------------------:|
|C1|help|Replys with a quick help message|
|C2|set port|Set the target port.|
|C3|set threads|Set the target thread.|
|C4|set ip|Set the target IP.|
|C5|set web|Set the target IP by Domain.|
|C6|set sleep|Set the time between thread.|
|C7|outtxt|Enable/Disable success message on run.|
|C8|values|Return all values of variables.|
|C9|run|Start the attack.|
|C10|update|Update Raven-Storm.|
|C11|quit/exit/q|Exit Raven-Storm.|
||||
|C12|set message|Set (attack-)message to send.|
|C13|method|Change method of attack: UDP, TCP|
|C14|set r|Repeat message, to get length/mb.|
|C15|set mb|Set mb to send to server.
||||
|C16|get port i|Port scann on IP.|
|C17|get port w|Port scann on Domain.|
||||
|C18|stress|Use stress-testing-mode.|
|C19|st wait|Delay between next level in stress-testing-mode.|
||||
|C20|set listip|Attack multiple IPs.|
|C21|set listweb|Attack multiple Domains.|
|C22|set listport|Attack multiple Ports.|
||||
|C23|auto start|Run after X seconds.|
|C24|auto step|Next thread after X seconds.|
|C25|auto stop|Stop after X seconds.|
||||
|C26|server start|Start server.|
|C27|client connect|Start client.|
|C28|server ip|Set redis IP.|
|C29|server port|Set redis Port.|
|C30|hbi|Get IP by domain.|
|C31|lan scan|List all IPs connected to WiFi.|
|C32|pod target|Set Pod target.|
|C33|pod target list|Set multiple Pod targets.|
|C34|pod run|Run pod.|
|C35|pod sleep|Delay between pod thread.|
|C36|pod threads|Set the Pod threads.|
|C37|pod size|Set the pod packet size.|
|C38|pod jammer|Set all devices as target.|
|C39|pod auto stop|Auto stop the pod attack.|
|C40|pod intervall|Set the intervall between the pod requests.|
|C41|speed down|Measure the time a website needs to load.|
|C42|speed ping|Measure the time a ping needs.|


### #A1:
Raven-Storm is a complex DDoS system with many features, for testing, accommodation, and learning.

It's written in Python 2.7 and made for breaking the limit, testing your servers with the most common DDoS method.

It's also faster to define the target info than it looks, because of a self-learning algorithm.

### #A2:
I basically made this tool, for testing the server with the most amount of features possible.

And please commit beta issues because it helps me updating the code.

Taguar

### #A3:
Raven-Storm is based on the UDP and TCP flood, but also ICMP flood.

#### DOS:
The basic dos script is spamming messages to the server.
It supports UDP flood and TCP flood.
TCP flood connects first then sends the spam message.
UDP just floods.

#### DDOS:
You first need to setup Raven-Storm on multiple PCs and connect it to a Database (Topic: C26-C29) and so you can use multiple PCs as one.

### #A4:
Raven-Storm is constructed like a command-line, it requires command inputs with values and executes something.

**First of you need to know how to use the Terminal.**

Raven-Storm can be used with arguments, or basically inside.
You will find the commands in the C-Topic.

### #A5 (INSTALLATION):
Start your Unix terminal and type in following:

```pkg/apt-get/brew install git python2 redis nmap```

```git clone https://github.com/Taguar258/Raven-Storm/```

```cd Raven-Storm```

```pkg/apt-get/brew install iputils-ping (in case needed)```

```pkg/apt-get/brew install python2-pip (in case needed)```

```pip2/python2 -m pip install -r requirements.txt```

```python2 rs.py```

#### OR!:
Use the quick installer: (You might need to install curl)

```curl https://raw.githubusercontent.com/Taguar258/Raven-Storm/master/documentation/installer.txt --output rs-install.sh ; bash rs-install.sh```

To run it again:

```cd Raven-Storm ; python2 rs.py```

### #A6:
First of take a quick internet search to the topics:

DDOS, DOS, IP, Domain, UDP, TCP, Port, TCP Flood, UDP Flood, MB, Ping of Death, pod, ICMP flood, ICMP, Is DOS illegal?.

And then you are ready to go, I guess.



### #B1:
Functions are in Raven-Storm defined as everything you normally don't use/need but is very helpful.


### #B2:
Yes, Raven-Storm learns by itself.
It reads all the values you entered in and save it into: **ravenstorm-automated-list.ravenstormlist**.

On the next startup, you can see the action using the values command.

### #B3:
You will need to create a file with the following values you want to define inside.

```ip = Set ip.
port = Set port.
threads = Set threads.
message = Set message.
repeat = Set repeat.
sleep = Set delay.
output = true/false. Output toggle.
stress = Activate stress mode.
stressstep = Set stress steping count.
mb = Set mb.
autostart = Set start delay.
autostop = Set auto stop.
autostep = Set the automated stepping.
hip = Redis ip.
hport = Redis port.
runonstart = com1, com2 ... Run on start.
method = tcp/udp.
pod target = Pod target.
pod threads = Pod threads.
pod sleep = Pod, time between threads.
pod size = Pod packet size.
pod intervall = Pod intervall between packet.
pod auto stop = Auto atop pod attack.
```

You will then be able to run this config file using:

```python2 rs.py -c filename.txt```

### #B4:
Type:
```python2 rs.py -ros com1, com2, com3...```

To run commands at the startup.

### #B5:
Type:

```python2 rs.py server start```

```python2 rs.py server start IP port```

```python2 rs.py client connect```

```python2 rs.py client connect IP port```

To quickstart the connection to the Redis DB.

### #B6:
Type for a dos attack:

```python2 rs.py -fd {target} {port} {threads}```

### #B7:
Type for a pod attack:

```python2 rs.py -fp {target} {threads} {(size)} {(sleep)} {(intervall)} {(auto stop)}```


### #C1:
Shows the help message.

### #C2:
Define the target port.

### #C3:
Define the number of threads to use.

### #C4:
Define the target IP.

### #C5:
Define the target IP using the domain.

### #C6:
Define the time for the next thread to activate.

### #C7:
Toggle the success output.

### #C8:
Print all defined settings.

### #C9:
Run the attack.

### #C10:
Update Raven-Storm.

### #C11:
Exit Raven-Storm.

### #C12:
Define the message to spam.

### #C13:
Change flood method between UDP flood and TCP flood.

### #C14:
Repeat the message to spam.

### #C15:
Set MB instead of the message.

### #C16:
Port scan an IP.

### #C17:
Port scan a domain.

### #C18:
Activate the stress-testing-mode.
Check how many threads the server can handle.

### #C19:
Define the time for the next level to appear in the stress-testing-mode.

### #C20:
Define multiple target IPs.

### #C21:
Define multiple target Domain.

### #C22:
Define multiple target Ports.

### #C23:
Run after a defined time.

### #C24:
Next thread after a defined time.

### #C25:
Stop threads after a defined time.

### #C26:
First of you need to start the Redis-server using: ```redis server```in the command line.

Then you connect 1 server to the Redis DB.

### #C27:
After topic C26 connect clients to the DDoS mode.

### #C28:
Define the Redis IP.

### #C29:
Define the Redis Port.

### #C30:
Basically get the IP of a domain.

### #C31:
List all IPs connected to the currentWiFi.

### #C32:
Set the ping of death target.

### #C33:
Set multiple Pod targets.

### #C34:
Run a pod.
Use sudo for better/strong pod.

### #C35:
Set the delay between every pod thread.

### #C36:
Set the Pod threads.

### #C37:
Set the pod packet size.

### #C38:
Set all devices as target | WiFi Jammer.

### #C39:
Automatically stop all the pod threads after a specific time.

This only works for Mac, you can deactivate it by setting it to 0.

### #C40:
Define the interval between every pod request.

Disable it by setting it to 0.

### #C41:
Measure the time a website needs to load.

Please do not forget the http(s):// .

### #C42:
Measure the time a ping needs.
