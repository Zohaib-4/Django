import requests

url1 = "http://127.0.0.1:8000/stu-info/"

r =requests.get(url=url1)
data = r.json()

print(data)
