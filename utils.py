import os

def read_file(filename):
    with open(filename, "r") as f:
        return f.read()

def run_command(cmd):
    return os.popen(cmd).read()
