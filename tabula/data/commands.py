"""

"""

import json

def load_commands():
    global commands
    commands = json.load(open("commands.json"))

def commands_loaded():
    if 'commands' in globals():
        return True
    else:
        return False

def open_commands():
    if commands_loaded() is False:
        load_commands()

def is_command(cmd):
    if cmd.startswith(('@', '\\', ':')):
        cmd = cmd[1:]
    else:
        return False
    if cmd.endswith(':'):
        cmd = cmd[:-1]
    global commands
    if cmd in commands:
        return True
    else:
        return False
