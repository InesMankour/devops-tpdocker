import requests
import os

def weather(lat,lon,apiKey):
    url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'.format(lat,lon,apiKey)
    res=requests.get(url)
    data=res.json()
    return data
#print(res)

lat = os.environ['LAT']
lon = os.environ['LONG']
apiKey = os.environ['API_KEY']

print(weather(lat,lon,apiKey))