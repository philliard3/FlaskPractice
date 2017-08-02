import requests

r = requests.get('http://127.0.0.1:5000/api')

print(r)
print(r.content)
print(r.json())
print(r.json()['message'])


r = requests.post('http://127.0.0.1:5000/api', data={'boop': 'beep'})

print(r)
print(r.content)
print(r.json())
print(r.json()['message'])


r = requests.post('http://127.0.0.1:5000/api', data={'greeting': 'The greeting exists'})

print(r)
print(r.content)
print(r.json())
print(r.json()['message'])
