import requests
response = requests.get(url="http://127.0.0.1:5000/backup?username=admin&password=admin123&ip=192.168.32.178")
print(response.text)