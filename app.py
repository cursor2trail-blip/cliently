from flask import Flask, request
from db import get_user_by_id
from utils import read_file, run_command

app = Flask(name)

@app.route("/user")
def get_user():
    user_id = request.args.get("id")   # USER INPUT
    result = get_user_by_id(user_id)   # flows to DB (SQLi)
    return str(result)

@app.route("/file")
def get_file():
    filename = request.args.get("file")  # USER INPUT
    content = read_file(filename)        # PATH TRAVERSAL
    return content

@app.route("/exec")
def exec_cmd():
    cmd = request.args.get("cmd")        # USER INPUT
    output = run_command(cmd)            # COMMAND INJECTION
    return output
