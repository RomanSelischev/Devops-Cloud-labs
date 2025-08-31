from flask import Flask, jsonify
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="/bad_docker/.env")
app = Flask(__name__)
@app.route('/')

def HelloWorld():
    secret_token = os.getenv("SECRET_TOKEN", "Токен не найден")
    return jsonify({"message": "Hello, DevOps World!", "token": secret_token})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
