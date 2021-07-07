import requests
import json

key = 'c455988e77fc405b8a250cbf4f7a485f'
city = input('please enter your city name: ')
api_url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=' + key +'&lang=tr' + '&units=metric'
api_url2 = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'
api_url3 = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city,key)
api_url4 = 'https://api.openweathermap.org/data/2.5/weather?q={thecity}&appid={keyvalue}'.format(thecity=city,keyvalue=key)

print(api_url)
print(api_url2)
print(api_url3)
print(api_url4)

city_data = requests.get(api_url)
city_json = city_data.json()


temp_c = city_json['main']['temp']
weather_description = city_json['weather'][0]['description']
humidity = city_json['main']['humidity']
wind_speed = city_json['wind']['speed']

print('temperature is : {:.2f} deg c'.format(temp_c))
print('weather is : ' + weather_description)
print('humidity is : {} %'.format(humidity))
print('wind speed is :' , str(wind_speed) , 'km/h')

