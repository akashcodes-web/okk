from flask import Flask
import os
import datetime
import subprocess
import getpass

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Akash Kumar"
    username = getpass.getuser()  # Replaced os.getlogin() with getpass.getuser()
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Using 'ps aux' as a safer alternative
    top_output = subprocess.getoutput('ps aux')

    return f"""
    <h1>Name: {name}</h1>
    <h2>User: {username}</h2>
    <h3>Server Time (IST): {server_time}</h3>
    <pre>{top_output}</pre>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)