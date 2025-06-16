from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def say_hello():
    return jsonify({"message": "Hello I'm Akhilesh. I'm working as a Cloud Intern at StepAhead"})

if __name__ == '__main__':
    app.run(debug=True)

