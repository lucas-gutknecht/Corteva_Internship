import requests

response = requests.get("http://localhost:5000/get_data")

print(response.content)