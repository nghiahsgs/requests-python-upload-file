import requests

url = 'http://localhost:8000/api/upload'
files = {'file': open('damme.jpg', 'rb')}
data = requests.post(url, files=files).json()
print(data)