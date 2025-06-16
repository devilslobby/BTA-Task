
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def say_hello():
    return jsonify({"message": "Hello!"})


