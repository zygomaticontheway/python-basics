import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/users')

data = json.loads(response.text)
print(data[0])