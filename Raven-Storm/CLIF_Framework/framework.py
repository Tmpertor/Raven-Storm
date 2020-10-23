# The CLIF Framework has been programmed by Taguar258 and is published under the MIT License.

import importlib


class console_read_only(type):
	def __setattr__(self, name, value):
		if name == "objects":
			raise Exception("Variable cannot be called objects.")


class console:
	__metaclass__ = console_read_only

	def __init__(self):
		self.objects = []
		self.ps1 = ":: "
		self.command_split = " "
		self.running = True
		self.command_log = []
		self.debug_command = False
		self.run_command = []

	def add(self, object_item, event):
		self.objects.append([object_item, event])

	def stop(self):
		self.running = False

	def input(self, command, show_print):
		self.run_command = [command, show_print]

	def _run_event(self, name):
		self.command_log.append(str(name))
		if isinstance(name, list):
			for object_item in self.objects:
				event_object = object_item[1]
				for event in event_object.event_events:
					for n in name:
						if event.__name__ == n:
							event()
		elif isinstance(name, str):
			for object_item in self.objects:
				event_object = object_item[1]
				for event in event_object.event_events:
					if event.__name__ == name:
						event()

	def event(self, name):
		self._run_event(name)

	def run(self):
		self.running = True
		self._run_event(["on_start", "on_ready"])

		while self.running:
			self._run_event("on_input")
			if len(self.run_command) == 2:
				console_command = str(self.run_command[0])
				if self.run_command[1]:
					print(self.ps1 + self.run_command[0])
			else:
				try:
					console_command = input(self.ps1)
				except KeyboardInterrupt:
					self._run_event("on_interrupt")
					break
			if console_command == "" or console_command == " ":
				continue

			for object_item in self.objects:
				event_object = object_item[1]
				for event in event_object.event_events:
					if event.__name__ == "on_command":
						try:
							event(console_command)
						except Exception:
							event()

			self.command_log.append(str(console_command))

			command_found = False

			for object_item in self.objects:
				event_object = object_item[1]
				for command in event_object.event_commands:
					if self.debug_command:
						print(command[0].replace("_", self.command_split), self.command_split.join(console_command.split(self.command_split)[:(1 + (command[0].replace("_", self.command_split).count(self.command_split)))]))
					if command[0].replace("_", self.command_split) == self.command_split.join(console_command.split(self.command_split)[:(1 + (command[0].replace("_", self.command_split).count(self.command_split)))]):
						command_found = True
						self._run_event("on_command_found")
						parser_exists = False
						for parser in event_object.event_parsers:
							if isinstance(parser[0], list):
								for parser_command in parser[0]:
									if parser_command[0] == command[0]:
										command[1](parser_command[1](console_command))
										parser_exists = True
										break
								if parser_exists:
									break
							elif isinstance(parser[0], str):
								if parser[0] == command[0]:
									command[1](parser[1](console_command))
									parser_exists = True
									break
						try:
							if not parser_exists:
								command[1](console_command)
						except Exception:
							command[1]()

			if not command_found:
				self.command_log.append(str("on_command_not_found"))
				for object_item in self.objects:
					event_object = object_item[1]
					for event in event_object.event_events:
						if event.__name__ == "on_command_not_found":
							try:
								event(console_command)
							except Exception:
								event()


def module(module, console, *args):
	new = importlib.import_module(module)
	if len(args) == 0:
		new.setup(console)
	else:
		new.setup(console, args)
	del(new)


class tools:
	def __init__(self):
		pass

	def arg(self, label, comname, com):
		if len(com.split(comname)) == 2:
			if com.split(comname)[1] == "":
				zw = input("%s" % label)
			else:
				zw = com.split(comname)[1]
				print("%s%s" % (label, zw))
		else:
			zw = input("%s" % label)
		return zw

	def help(self, startline, splitter, event):
		if event.help_text_title != "":
			print(event.help_text_title)
		max_len = 0
		for help_item in event.help_list:
			if len(help_item) == 2:
				if isinstance(help_item[0], list):
					if len(", ".join(help_item[0])) > max_len:
						max_len = len(", ".join(help_item[0]))
				elif isinstance(help_item[0], str):
					if len(help_item[0]) > max_len:
						max_len = len(help_item[0])
		for help_item in event.help_list:
			# print(help_item)
			if len(help_item) == 2:
				if "[" in help_item[0]:
					split_help = help_item[0].strip('][').split(', ')
					help_item[0] = (", ".join(split_help[:-1]) + " or " + split_help[-1]).replace("'", "")
				length = (" " * (max_len - len(help_item[0])))
				print(startline + ("%s%s" % (length, splitter)).join(help_item))
			elif len(help_item) == 1:
				print(help_item[0])

	def question(self, question):
		ans = input(question + " (Y/N) ").lower()
		if ans == "y":
			return True
		else:
			return False


class event:
	def __init__(self):
		self.event_events = []
		self.event_commands = []
		self.event_parsers = []
		self.help_list = []
		self.help_text_title = ""

	def log(self):
		print("Events:", self.event_events)
		print("Commands:", self.event_commands)
		print("Parsers:", self.event_parsers)
		print("Help:", self.help_list)

	def event(self, function):
		self.event_events.append(function)

	def command(self, function):
		self.event_commands.append([function.__name__, function])

	def help(self, function_name, message):
		if isinstance(function_name, list):
			self.help_list.append([str(function_name), message])
		elif isinstance(function_name, str):
			self.help_list.append([function_name, message])

	def help_title(self, title):
		self.help_text_title = str(title)

	def help_comment(self, comment):
		self.help_list.append([comment])

	def commands(self, function, lt):
		if isinstance(lt, list):
			for name in lt:
				self.event_commands.append([name, function])
		elif isinstance(lt, str):
			self.event_commands.append([lt, function])

	def parser(self, function, command):
		self.event_parsers.append([command, function])

# get_tools = tools()
# get_event = event()
