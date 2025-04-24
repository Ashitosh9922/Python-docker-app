from flask import Flask, jsonify, request
from datetime import datetime
import random

app = Flask(__name__)

# Route 1: Home page
@app.route('/')
def home():
    return jsonify(message="👋 Hello! Welcome to my Dockerized Flask App!")

# Route 2: Get current server time
@app.route('/time')
def time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify(current_time=current_time)

# Route 3: Health check
@app.route('/status')
def status():
    return jsonify(message="App is healthy!", status="Running")

# Route 4: Random quote
@app.route('/quote')
def quote():
    quotes = [
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Life is what happens when you're busy making other plans. – John Lennon",
        "It does not matter how slowly you go as long as you do not stop. – Confucius",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill"
    ]
    return jsonify(quote=random.choice(quotes))

# Route 5: Greet the user
@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Stranger')
    return jsonify(message=f"Hello, {name}!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
