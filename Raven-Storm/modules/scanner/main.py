# 2020
# The Raven-Storm Toolkit was programmed and developed by Taguar258.
# The Raven-Storm Toolkit is published under the MIT Licence.
# The Raven-Storm Toolkit is based on the CLIF-Framework.
# The CLIF-Framework is programmed and developed by Taguar258.
# The CLIF-Framework is published under the MIT Licence.

import socket
from os import system
from time import sleep, time

import requests
import urllib3
from CLIF_Framework.framework import event  # noqa: I003, I900
from CLIF_Framework.framework import tools  # noqa: I900

try:
	import nmap
except ImportError:
	print("Please install the nmap module.")
	quit()

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

		var.nm = None
		var.nmapinstalled = False

	def _add_commands(self):
		event.commands(self.exit_console, ["exit", "quit", "e", "q"])
		event.command(self.help)

		event.commands(self.run_shell, ".")
		event.commands(self.debug, "$")

		event.help_comment("|\n|-- Port scanning:")
		event.help("ports ip", "Get port of IP (get port i).")
		event.help("ports web", "Get port of web (get port w).")
		event.help_comment("|\n|-- Network scanning:")
		event.help("lan scan", "Get all Ips of Wifi.")
		event.help_comment("|\n|-- Domain scanning:")
		event.help("domain ip", "Get the IP by host.")
		# event.help("post scan", "Get all post variables of a Website.")
		event.help_comment("|\n|-- Speed testing:")
		event.help("speed down", "Return the time it needs to open a website.")
		event.help("speed ping", "Return the time it needs to ping an IP.")

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
		try:
			var.nm = nmap.PortScanner()
			var.nmapinstalled = True
		except Exception as e:
			system("clear || cls")
			print("Please install the nmap package.")
			print("Some functions will not work without it.")
			print(e)
			try:
				input("[Press enter to continue without nmap]")  # noqa: S322
			except Exception:
				quit()
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

	def help(self):
		event.help_title("\x1b[1;39mScanner Help:\x1b[0;39m")
		tools.help("|   |-- ", " :: ", event)
		print("\033[1;32;0m")

	def portscan(self, ip):
		try:
			for p in range(1, 1500):
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				res = sock.connect_ex((ip, p))
				if res == 0:
					print("Port: %s" % str(p))
					sock.close()
		except Exception as e:
			print("There was an error while executing.", e)

	def lanscan(self):
		try:
			gateways = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			gateways.connect(("8.8.8.8", 80))
			gateway = ".".join((gateways.getsockname()[0].split("."))[:len(gateways.getsockname()[0].split(".")) - 1])
			gateways.close()
			var.nm.scan(hosts=("%s.0/24" % gateway), arguments="-sP")
			lanscandev = [(x, var.nm[x]['status']['state'], var.nm[x]["hostnames"][0]["name"], var.nm[x]["hostnames"][0]["type"]) for x in var.nm.all_hosts()]
			print("Gate way: %s.0" % gateway)
			for lanscandevice in lanscandev:
				print("%s  %s  %s  %s" % (lanscandevice[0], lanscandevice[1], lanscandevice[2], lanscandevice[3]))
		except Exception as e:
			print("There was an error while executing.", e)

	def hbi(self, ip):
		return socket.gethostbyname(ip)

	def speedtest(self, url):
		try:
			if "http" not in url or "://" not in url:
				url = ("https://%s" % url)
			print("Testing download speed...")
			start = time()
			http = urllib3.PoolManager()
			response = http.request('GET', url)
			data = response.data  # noqa: F841
			end = time()
			result = (end - start)
			return result
		except Exception as e:
			print("There was an error while executing.", e)

	def speedping(self, ip):
		try:
			print("Testing ping speed... (May require sudo)")
			start = time()
			system("ping -c 1 %s > /dev/null" % ip)
			end = time()
			result = (end - start)
			return result
		except Exception as e:
			print("There was an error while executing.", e)

	@event.command
	def domain_ip(command):
		print("")
		try:
			zw = (tools.arg("Domain: ", "domain ip ", command).replace("https://", "").replace("http://", ""))
			print(self.hbi(zw))
		except Exception as e:
			print("There was an error while executing.", e)
		print("")

	@event.command
	def lan_scan(command):
		print("")
		if var.nmapinstalled:
			self.lanscan()
		else:
			print("Please install nmap.")
		print("")

	@event.command
	def ports_ip(command):
		print("")
		try:
			psi = tools.arg("IP: ", "ports ip ", command)
			self.portscan(psi)
		except Exception as e:
			print("There was an error while executing.", e)
		print("")

	@event.command
	def ports_web(command):
		print("")
		try:
			psw = tools.arg("Website: ", "ports web ", command)
			psww = socket.gethostbyname(psw.replace("https://", "").replace("http://", ""))
			self.portscan(psww)
		except Exception as e:
			print("There was an error while executing.", e)
		print("")

	@event.command
	def speed_down(command):
		print("")
		zw = self.speedtest(tools.arg("Website: ", "speed down ", command))
		print("Result: %s seconds" % zw)
		print("")

	@event.command
	def speed_ping(command):
		print("")
		zw = self.speedping(tools.arg("IP: ", "speed ping ", command))
		print("Result: %s seconds" % zw)
		print("")


def setup(console):
	console.ps1 = "\033[1;32;0mScanner> "
	console.add(Main(console), event)
