[MIT Taguar258 2019]
# Raven-Storm Toolkit Documentation:
A strong, costomizable dos and ddos framework with over 30 functions/commands for testing your own servers.

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
|B2|Self learning|How does Raven-Storm learn by it self?|
|B3|CFile|How to load in a configuration File.|
|B4|ROS|Run commands on start of Raven-Storm.|
|B5|Fast Redis start|Start client/server using the command-line.

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


### #A1:
Raven-Storm is complex ddos system with many features, for testing, accommodation and learning.

It's written in Python 2.7 and made for breaking the limit, testing your servers with the most common ddos method.

It's also faster to define the target infos than it looks, because of a self learning algorithm.

### #A2:
I basically made this tool, for testing the server with the most amount of features possible.

Have fun using it.

And please commit beta issues because it helps me updating the code.

Taguar

### #A3:
Raven-Storm is based on the UDP and TCP flood.

#### DOS:
The basic dos script is spaming messages to the server.
It supports UDP flood and TCP flood.
TCP flood connects first then sends the spam message.
UDP just floods.

#### DDOS:
You first need to setup Raven-Storm on multiple PCs and connect it to an Database (Topic: C26-C29) and so you can use multiple PCs as one.

### #A4:
Raven-Storm is constructed like a command-line, it requires command inputs with values and executes something.

**First of you need to know how to use the Terminal.**

Raven-Storm can be used with arguments, or basically inside.
You will find the commands in the C-Topic.

### #A5:
Start your unix terminal and type in following:

```git clone https://github.com/Taguar258/Raven-Storm/```

```cd Raven-Storm```

```pkg/apt-get/brew install redis```

```pkg/apt-get/brew install python2```

```pip2 install -r requirements.txt```

```python2 rs.pyo```

To run it again:

```cd Raven-Storm ; python2 rs.pyo```

### #A6:
First of take a quick internet search to the topics:

DDOS, DOS, IP, Domain, UDP, TCP, Port, TCP Flood, UDP Flood, MB, Is DOS illegal?.

And then you are ready to go, I guess.



### #B1:
Functions are in Raven-Storm defined as everything you normally don't use/need but is very helpful.


### #B2:
Yes, Raven-Storm learns by it self.
It reads all the values you entered and save it into: **ravenstorm-automated-list.ravenstormlist**.

On the next startup you can see the action using the values command.

### #B3:
You will need to create a file with following values you want to define inside.

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
```

You will then be able to run this config file using:

```python2 rs.pyo -c filename.txt```

### #B4:
Type:
```python2 rs.pyo -ros com1, com2, com3...```

To run commands at the startup.

### #B5:
Type:

```python2 rs.pyo server start```

```python2 rs.pyo server start ip port```

```python2 rs.pyo client connect```

```python2 rs.pyo client connect ip port```

To quickstart the connection to the Redis DB.

### #C1:
_Not native english speakers are welcome._

### #C2:
Define the target port.

### #C3:
Define the amount of threads to use.

### #C4:
Define the target ip.

### #C5:
Define the target ip using the domain.

### #C6:
Define the time for the next thread to activate.

### #C7:
Toggle the sucess output.

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
Set MB instead of message.

### #C16:
Port scann an ip.

### #C17:
Port scann an domain.

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
Run after defined time.

### #C24:
Next thread after defined time.

### #C25:
Stop threads after defined time.

### #C26:
First of you need to start the redis-server using: ```redis server```in the command line.

Then you connect 1 server to the Redis DB.

### #C27:
After topic C26 connect clients to the ddos mode.

### #C28:
Define the Redis IP.

### #C29:
Define the Redis Port.
