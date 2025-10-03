from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

HTML = """
<h1>TerminalCraft</h1>
<form method="post">
    <input type="text" name="cmd" autofocus style="width: 300px;">
    <input type="submit" value="Run">
</form>
<pre>{{ output }}</pre>
"""

def run_command(cmd):
    if cmd == "ls":
        return "\n".join(os.listdir("files"))
    elif cmd.startswith("cat "):
        filename = cmd.split(" ", 1)[1]
        try:
            with open(os.path.join("files", filename), "r") as f:
                return f.read()
        except FileNotFoundError:
            return f"File '{filename}' not found."
    elif cmd == "whoami":
        return os.getlogin()
    elif cmd == "help":
        return "Available commands: ls, cat <filename>, whoami, help, clear, submit, slack"
    elif cmd == "clear":
        return ""
    elif cmd == "submit":
        return "Submission simulated..."
    elif cmd == "slack":
        return "Slack channel simulated..."
    else:
        return "Unknown command."

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        cmd = request.form.get("cmd")
        output = run_command(cmd)
    return render_template_string(HTML, output=output)

if __name__ == "__main__":
    app.run(debug=True, port=8080)