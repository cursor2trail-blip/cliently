from flask import Flask, request
from db import get_user_by_id
from utils import read_file, run_command
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

@app.route("/user")
def get_user():
    user_id = request.args.get("id")   # USER INPUT
    if not user_id.isdigit():           # Validate user_id to be numeric
        raise BadRequest("Invalid user ID")
    result = get_user_by_id(int(user_id))   # Use parameterized query
    return str(result)

@app.route("/file")
def get_file():
    filename = request.args.get("file")  # USER INPUT
    safe_filenames = {"file1.txt", "file2.txt"}  # Whitelist of allowed filenames
    if filename not in safe_filenames:   # Validate filename against whitelist
        raise BadRequest("Invalid filename")
    content = read_file(filename)        # Safe file read
    return content

@app.route("/exec")
def exec_cmd():
    cmd = request.args.get("cmd")        # USER INPUT
    allowed_commands = {"ls", "pwd"}     # Whitelist of allowed commands
    if cmd not in allowed_commands:       # Validate command against whitelist
        raise BadRequest("Invalid command")
    output = run_command(cmd)            # Safe command execution
    return output