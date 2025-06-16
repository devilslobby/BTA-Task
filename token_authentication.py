from flask import Flask, request, jsonify

app = Flask(__name__)

# Example token (in real apps, use secure tokens)
AUTH_TOKEN = "StepAhead101"

# Protected route with token-based authentication
@app.route('/secure/data', methods=['GET'])
def get_secure_data():
    # Get token from headers
    token = request.headers.get('Authorization')

    if token == f"Bearer {AUTH_TOKEN}":
        return jsonify({
            "message": "Access granted",
            "data": {"secret":"This data is protected"}
        })
    else:
        return jsonify({
            "error": "Unauthorized. Invalid or missing token."
        }), 401

if __name__ == '__main__':
    app.run(debug=True)
