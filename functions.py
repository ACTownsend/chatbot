from random import *
import requests
import pycountry
import pytz
from google import google
import smtplib

greetings = ["hello", "hi", "hey", "yo"]
farewell = ["goodbye", "cya later", "bye", "cya", "later"]
browser = ["google", "search"]
clock = ["time", "hours", "clock","timezone"]
rollDice = ["roll", "dice", "die"]
weatherList = ["weather", "hot", "temperature"]
emailList = ["email", "send"]
coinList = ["coin", "heads", "tails"]

def greet(user):
    randomGreet = choice(greetings).capitalize()
    return randomGreet

def endFunction(user):
    randomBye = choice(farewell).capitalize()
    return randomBye

def googleSearch(custom, after):
    if after == False:       
        term = input(" Bot : What would you like to search?\n User: ")
    else:
        term = custom
    search_results = google.search(term)
    print(" Bot: Here is what I found for '" + term + "':")
    for result in search_results:
        if result.index == 5:
            break
        else:
            result.name = result.name.replace(result.link,"")
            print("       " +  str(result.index+1) + ": " + result.name + " - " + result.link + "\n")
    
    
    
def weather():
      
    city =  input("Enter the name of your city : ")

    api_address = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=a283f94f4370e92593315243cecd791b'.format(city)       
    url = api_address
    json_data = requests.get(url).json()
    formatted_data = json_data['weather'][0]['description']
    temp = json_data['main']['temp']
    tempc = temp -273.15
    print(' Bot: Today is expected in  '+ city + ' ' + formatted_data)
    print(' Bot: The temperature is ',round(tempc,2),'°C')
    return tempc

def checkTimeZone():
    term = input(" Bot: Enter a country name and I'll tell you the time in that country\n User: ")
    print(" Bot: Please wait...")
    try:
        countinfo = pycountry.countries.get(name=term.title())
        countcode = countinfo.alpha_2
        countzone = pytz.country_timezones(countcode)
    except:
        print(" Bot: Sorry, I don't recognise the name of that country")
    else:
        timereq = requests.get("http://api.timezonedb.com/v2.1/get-time-zone?key=A56Y2B25QKH8&format=json&by=zone&zone={}".format(countzone[0])).json()
        timegot = timereq["formatted"]
        print(" Bot: The current time in {a} is {b}".format(a=term.title(),b=timegot[11:16]))
    return term

def diceRoll(number):
    if number >= 1:
        roll = randint(1,number)
    else:
        sides = int(input(" Bot: How many sides does the die have?\n User: "))
        roll = randint(1,sides)
    print(" Bot: You rolled a " + str(roll) + "!")
    return number	

def emailFunction():
    user_email = input(" Bot: Please enter the email address that you would like to send an email to: ")
     
    print(" ")
     
    subject= (input(" Bot: Enter the subject of the email: "))
     
    print(" ")
         
    body = (input(" Bot: Enter the content of the email: "))
     
    print(" ")
     
    aemail = input(" Bot: Would you like to send this email to anyone else?\n User:  ")
     
    x = 'Subject: {}\n\n{}'.format(subject, body)
     
    if aemail == "yes" or aemail.upper() == "YES":

        print(" ")

        oemail= input("Write the other email --> ")

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

    # chatbot email login
        server.login("chatbottestcu123@gmail.com", "chatbot123")  

    # code to send the email to the user
        server.sendmail("chatbottestcu123@gmail.com", user_email, x)
        server.sendmail("chatbottestcu123@gmail.com", oemail , x)
        server.quit()


    elif aemail.lower() == "no" or aemail.upper()== "N0" :

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        server.login("chatbottestmail2@gmail.com", "chatbottest123")  
        server.sendmail("chatbottestcu123@gmail.com", user_email, x)
        
        print(" Bot: Email sent!")
        
        server.quit()
        
def coin(userGuess):
    side = choice(["Heads", "Tails"])
    if userGuess == side:
        print(" Bot: You guessed correctly! The coin landed " + side + " side up")
    else:
        print(" Bot: You guessed incorrectly! The coin landed " + side + " side up")
    return side
    
