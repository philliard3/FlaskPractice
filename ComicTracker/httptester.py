import requests
import time
from datetime import datetime
from decimal import Decimal

'''

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
'''

# this section is meant to test the viability of rapid requests to the server (as would be the case in a search bar or in a game)
lasttime = datetime.now()
currenttime = lasttime
transmission_cycles = 0
total_seconds = 30.0
framerate = 60.0
while(currenttime-lasttime).total_seconds()<total_seconds:
    r = requests.get('http://127.0.0.1:5000/api')
    #print(r.json()['message'])

    r = requests.post('http://127.0.0.1:5000/api', data={'greeting': 'The greeting exists'})
    #print(r.json()['message'])

    currenttime = datetime.now()
    #print("frame time is "+str(1.0/60.0))
    #print("time this took is "+str((Decimal((currenttime-lasttime).total_seconds())%Decimal(1.0/60.0))))
    timetosleep = 1.0/framerate - float(Decimal((currenttime-lasttime).total_seconds())%Decimal(1.0/framerate))
    if timetosleep>0.0:
        time.sleep(timetosleep)
    transmission_cycles+=1

print("completed "+str(transmission_cycles)+" transmission cycles")
print("dropped "+str(framerate*total_seconds - transmission_cycles))



