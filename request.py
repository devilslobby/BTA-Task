import requests

response = requests.get("http://127.0.0.1:5000/api/hello")
print(response.json())
data = response.json()