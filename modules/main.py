from CLIF_Framework.framework import event
from CLIF_Framework.framework import tools
from CLIF_Framework.framework import console
from CLIF_Framework.framework import module
from os import system
try:
	import readline  # noqa: F401
except Exception:
	pass
event = event()
tools = tools()


class Main:
	def __init__(selfie, console):
		global var
		global self
		self = selfie
		var = console

		var.modules = {}
		self._add_commands()

		# Colors
		var.C_None = "\x1b[0;39m"
		var.C_Bold = "\x1b[1;39m"
		var.C_Green = "\x1b[32m"
		var.C_Violet = "\x1b[34m"
		var.C_Dark_Blue = "\x1b[35m"
		var.C_Red = "\x1b[31m"

		# var.C_Blink = "\x1b[5;39m"
		var.C_Yellow = "\x1b[33m"
		var.C_Cyan = "\x1b[36m"
		# #var.C_Magenta = "\x1b[35m"
		# var.C_BRed = "\x1b[1;31m"
		# var.C_BGreen = "\x1b[1;32m"
		# var.C_BYellow = "\x1b[1;33m"
		# var.C_BBlue = "\x1b[1;34m"
		# #var.C_BCyan = "\x1b[1;36m"
		# #var.C_BMagenta = "\x1b[1;35m"

	def banner(self):
		print(("""C_Bo-----------------------------------------------------------C_W
C_G (
 )\\ )                                 )                C_WC_Bov.""" + var.rsversion + """C_WC_G
(()/(    )   )      (              ( /(      (       )
 /(_))( /(  /((    ))\\  (      (   )\\()) (   )(     (
(C_DB_C_G))  )(_))(_))\\  /((_) )\\ )   )\\ (C_DB_C_G))/  )\\ (()\\    )\\  'C_DB
| _ \\C_G((C_DB_C_G)C_DB_ _C_G)((C_DB_C_G)(C_DB_C_G))  C_DB_C_G(C_DB_C_G/(  ((C_DB_C_G)C_DB| |C_G  ((C_DB_C_G) ((C_DB_C_G) C_DB_C_G((C_DB_C_G))C_DB
|   // _` |\\ V / / -_)| ' \\)) (_-<|  _|/ _ \\| '_|| '  \\C_G()C_V
|_|_\\\\__,_| \\_/  \\___||_||_|  /__/ \\__|\\___/|_|  |_|_|_|C_W

C_BoStress-Testing-Toolkit by Taguar258 (c) | MIT 2020
Based on the CLIF Framework by Taguar258 (c) | MIT 2020C_W

The creators of Raven-Storm are not responsible
for any of your activitys or issues caused by Raven-Storm!
It is strictly illegal to exploit servers
which are not owned by you.
C_Bo----------------------------------------------------------C_W""").replace("C_W", var.C_None).replace("C_G", var.C_Cyan).replace("C_Bo", var.C_Bold).replace("C_DB", var.C_Dark_Blue).replace("C_V", var.C_Violet))

	@event.event
	def on_ready():
		system("clear || cls")
		self.banner()
		self.help()

	@event.event
	def on_command_not_found(command):
		print("")
		print("The command you entered does not exist.")
		print("")

	def exit_console(self):
		print("\033[1;32;0mHave a nice day.")
		quit()

	def _add_commands(self):
		event.commands(self.exit_console, ["exit", "quit", "e", "q"])
		event.commands(self.run_shell, ".")
		event.commands(self.debug, "$")
		event.commands(self.help, "help")
		event.parser(self.run_debug_arg, "$")
		event.parser(self.run_shell_arg, ".")
		event.help(["exit", "quit", "e", "q"], "Exit Raven-Storm.")
		event.help("help", "View all commands.")
		event.help("upgrade", "Upgrade Raven-Storm.")
		event.help(".", "Run a shell command.")
		event.help("clear", "Clear the screen.")
		event.help("l4", "Load the layer4 module. (UDP/TCP)")
		event.help("l3", "Load the layer3 module. (ICMP)")
		event.help("scanner", "Load the scanner module.")
		event.help("flood", "Load a very simple but effective dos module.")

		var.modules["Layer4"] = console()
		var.modules["Layer3"] = console()
		var.modules["Scanner"] = console()
		var.modules["Flood"] = console()

	def run_shell(self, command):
		system(command)

	def run_shell_arg(self, command):
		return tools.arg("Enter shell command: \033[1;32;0m", ". ", command)
		print("\033[1;32;0m", end="")

	def debug(self, command):
		eval(command)

	def run_debug_arg(self, command):
		return tools.arg("Enter debug command: \033[1;32;0m", "$ ", command)
		print("\033[1;32;0m", end="")

	@event.command
	def l4():
		module("modules.l4.main", var.modules["Layer4"])
		var.modules["Layer4"].run()

	@event.command
	def l3():
		module("modules.l3.main", var.modules["Layer3"])
		var.modules["Layer3"].run()

	@event.command
	def scanner():
		module("modules.scanner.main", var.modules["Scanner"])
		var.modules["Scanner"].run()

	@event.command
	def flood():
		module("modules.downflood.main", var.modules["Flood"])
		var.modules["Flood"].run()

	def help(self):
		event.help_title("\x1b[1;39mHelp:\x1b[0;39m")
		tools.help("|-- ", " :: ", event)
		print("\033[1;32;0m")

	@event.command
	def upgrade():
		try:
			system("git pull")
		except Exception:
			print("Cound not upgrade Raven-Storm.")

	@event.command
	def clear():
		system("clear || cls")

	@event.event
	def on_command():
		print("\033[1;32;0m", end="")

	@event.event
	def on_interrupt():
		self.exit_console()


def setup(console):
	console.ps1 = "\033[1;32;0m>> "
	console.add(Main(console), event)
