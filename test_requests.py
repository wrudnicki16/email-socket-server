import requests

req = requests.get('https://api.github.com/events')

json = req.json()

print(json)