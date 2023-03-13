import requests
import json
import pandas as pd



city = input('Ваше місто: ')
data = requests.get('https://api.openweathermap.org/data/2.5/weather?q=%s&appid=707dcab2f693b897ebaf37a81ba710d7' % city).json()
data = {'Погода': data['weather'][0]['main'], 'Опис': data['weather'][0]['description'], 'Температура': str(int(data['main']['temp']-273))+' C'}
print(pd.DataFrame([data]))
