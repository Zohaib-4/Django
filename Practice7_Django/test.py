import requests
import json

URL = "http://127.0.0.1:8000/addStudent/"

data = {
    'roll' : 9090,
    'name' : 'Rohan',
    'city' : 'Sukhar'  
}

json_data = json.dump(data)

r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)