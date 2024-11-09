import requests
import json

url = 'http://127.0.0.1:5000/predict'

data = {
    "features": [5.1, 4.5, 6.4, 5.2]
}

response = requests.post(url, json=data)

print('\nStatus Code: ', response.status_code)
print(response.json(), '\n')
