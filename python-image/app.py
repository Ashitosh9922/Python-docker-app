from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "👋 Hello! Welcome to my Dockerized Flask App!"

@app.route("/time")
def time():
    now = datetime.now()
    return jsonify({"current_time": now.strftime("%Y-%m-%d %H:%M:%S")})

@app.route("/status")
def status():
    return jsonify({"status": "Running", "message": "App is healthy!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
