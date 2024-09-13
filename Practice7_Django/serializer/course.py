import requests
import json

URL = "http://127.0.0.1:8000/addCourse/"

data = {
    'title' : 'Quantum Computing',
    'description' : 'This is Quantum Computing course',
    'instructor' : 'Dr Ali Kazmi',
    'duration' : 3
}

json_data = json.dumps(data)

r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)
