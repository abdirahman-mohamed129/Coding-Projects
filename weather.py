import requests #allows you to request from the website

from pprint import pprint #prints the data in a clearer way (it will be jumbled up if you use normal print)

API_Key = 'ca0913c0ac5632c2c5b7038452dbe726' #made account and found on open api 

city = input('Enter a city: ')

base_url = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid='+API_Key+'&q='+city

weather_data = requests.get(base_url).json()  #weather information but in jumbled way

temp_k = weather_data['list'][0]['main']['temp']

temp_c = round(float(temp_k) - 273.15)

pprint(weather_data) #weather data printed in clearer way

print("The temperature is", temp_c, "degrees celcius")