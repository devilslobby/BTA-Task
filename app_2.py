from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/post', methods=['POST'])
def create_post():
    data = request.get_json()
    data['id'] = 101
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
