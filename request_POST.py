import requests

payload = {
    "title": "POST Request",
    "body": "Task Number 9 of BTA Tasks.",
    "userId": 1
}

# Send POST request
response = requests.post("http://127.0.0.1:5000/api/post", json=payload)

# Parse JSON response
data = response.json()

# Print the returned data
print("POST response:")
print("ID:", data["id"])
print("Title:", data["title"])
print("Body:", data["body"])
