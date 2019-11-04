import json
import requests
def weather(my_input):
    city = my_input
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=d88ce41afbcf7f04e679e5227db5484a&units=metric'.format(city)
    r = requests.get(url)
    data = r.json()
    temp = data['main']['temp']
    wind_speed = data['wind']['speed']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    description = data['weather'][0]['description']
    x = "The Current condition in {} is Temperature : {} degree celsius \n Wind Speed : {} m/s \n Latitude : {}\n Longitude : {} It's look like some {} in your area".format(city,temp, wind_speed, latitude, longitude, description)
    return x
