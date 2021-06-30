import requests

url = "http://localhost:3000/upload"
# files = {'Images': open('1nam.PNG', 'rb')}
files = [('Images',open('1nam.PNG', 'rb')),('Images',open('a.png', 'rb'))]
data = requests.post(url, files=files).json()
print(data)
