from random import *
import webbrowser
import requests
import pycountry
import pytz

greetings = ["hello", "hi", "hey", "yo"]
farewell = ["goodbye", "cya later", "bye", "cya", "later"]
browser = ["google", "search"]
clock = ["time", "hours", "clock","timezone"]

def greet(user):
    randomGreet = choice(greetings).capitalize()
    return randomGreet

def endFunction(user):
    randomBye = choice(farewell).capitalize()
    return randomBye

def googleSearch():
    address = 'http://www.google.com/#q='
    search = input(" Bot : What would you like to search?\n User: ")
    searchterm = address + search
    print("Here is a link for: " + searchterm)
    webbrowser.open_new(searchterm)
    return searchterm
    
    
def weather():
      
    city =  input("Enter the name of your city : ")

    api_address = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=a283f94f4370e92593315243cecd791b'.format(city)       
    url = api_address
    json_data = requests.get(url).json()
    formatted_data = json_data['weather'][0]['description']
    temp = json_data['main']['temp']
    tempc = temp -273.15
    print('Today is expected in  '+ city + ' ' + formatted_data)
    print('The temperature is ',round(tempc,2),'°C')
    return tempc

def checkTimeZone():
	
		search = input("Bot: Enter a country name and I'll tell you the time in that country\n User:")
		try:
				countinfo = pycountry.countries.get(name=search.title())
				countcode = countinfo.alpha_2
				countzone = pytz.country_timezones(countcode)
		except:
				print("Bot: Sorry, I don't recognise the name of that country")
		else:
				timereq = requests.get("http://api.timezonedb.com/v2.1/get-time-zone?key=A56Y2B25QKH8&format=json&by=zone&zone={}".format(countzone[0])).json()
				timegot = timereq["formatted"]
				print("Bot: The current time in {a} is {b}".format(a=search.title(),b=timegot[11:16]))
				