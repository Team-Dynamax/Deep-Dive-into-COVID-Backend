

#Please note, postman is a much more useful way to test

import requests

BASE = "http://127.0.0.1:5000"

response = requests.get(BASE + "/hew")
print(response.json())
