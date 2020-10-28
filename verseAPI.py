import requests

response = requests.get('http://www.ourmanna.com/verses/api/get?format=text&order=random')
print(response.text)

