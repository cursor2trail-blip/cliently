import subprocess

def read_file(filename):
    with open(filename, "r") as f:
        return f.read()

def run_command(cmd):
    # Validate and sanitize the input command
    if not isinstance(cmd, str) or not cmd.isprintable():
        raise ValueError("Invalid command input.")
    
    # Split the command into a list for subprocess
    command_list = cmd.split()
    return subprocess.run(command_list, capture_output=True, text=True).stdout