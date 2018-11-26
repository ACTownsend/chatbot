from random import *
import requests
import pycountry
import pytz
from google import google
import smtplib
import datetime
import os
import time

greetList = ["hello", "hi", "hey", "yo"]
byeList = ["goodbye", "cya later", "bye", "cya", "later"]
browserList = ["google", "search"]
timeList = ["time", "hours", "clock","timezone"]
dieList = ["roll", "dice", "die"]
weatherList = ["weather", "hot", "temperature"]
emailList = ["email", "send"]
coinList = ["coin", "heads", "tails"]
shopList = ["shopping", "list"]
featureList = ["info", "help", "features"]

def greet(user):
    randomGreet = choice(greetList).capitalize()
    print(" Bot: " + randomGreet + "!")
    return randomGreet

def endFunction(user):
    randomBye = choice(byeList).capitalize()
    print(" Bot: " + randomBye + "!") 
    exit = True
    return exit

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

def shoppingList():
    file = open( "shoppinglist.txt", "w")
    file.write("    Your Shopping List : " + "\n    ")

    n = int(input(" Bot: How many items would you like to add to your shopping list?\n User: "))

    i=0

    # loop to write the number of items that the user needs

    for i in range(n):

        content = str(input(" Bot: Please enter item " + str(i+1) + " to add to your shopping list\n User: "))

        file.write(content + "\n    ")

        if i == n :
            break

    print("")        
    file = open( "shoppinglist.txt", "r")
    print (file.read())
    
def listOfFeatures():
     options = ['features','go back']
    features = ['timezone','web browser','alarms','weather','go back']
 
    print('Bot: What can I help you with?')
    for i in options:
        print(i)
   
    while True:
        answer = input('\nUser: ').lower()
        answered1 = False
       
        if answer == 'features':
            answered1 = True
            print('\nBot: Which feature can I tell you more about?\n')
            for i in features:
                print(i)
               
            while True:
                answer = input('\nUser: ').lower()
                answered2 = False
               
                if answer == 'timezone':
                    answered2 = True
                    print('\nBot: Give me a country name and I will give you the time in that countries timezone or timezones\n. ')
                   
                elif answer == 'weather':
                    answered2 = True
                    print('\nBot: Give me a country name and I will give you the weather currently in that country\n')
                   
                elif answer == 'web browser':
                    answered2 = True
                    print('\nBot: Give me a item to search for and I will display the first five results\n')    
                                       
                elif answer == 'alarms':
                    answered2 = True
                    print('\nBot: Give me a time in which you want the alarm to go off\n')    
                   
                elif answer == 'go back':
                   
                    break  
                   
                else:
                    print("\nBot: Sorry, I didn't understand that")
               
                if answered2 == True:
                    print('\nBot: Is there anything else I can help you with?\n')
                    for i in features:
                        print(i)
 
        elif answer == 'go back':
            break
        else:
            print("\nBot: Sorry, I didn't understand that")
       
        if answered1 == True:
                    print('\nBot: Is there anything else I can help you with?\n')
                    for i in options:
                        print(i)                
        
def alarm():
    def check_alarm_input(alarm_time):
        if len(alarm_time) == 1:
            if alarm_time[0] < 24 and alarm_time[0] >= 0:
                return True
        if len(alarm_time) == 2:
            if alarm_time[0] < 24 and alarm_time[0] >= 0 and alarm_time[1] < 60 and alarm_time[1] >= 0:
                return True
        elif len(alarm_time) == 3:
            if alarm_time[0] < 24 and alarm_time[0] >= 0 and alarm_time[1] < 60 and alarm_time[1] >= 0 and alarm_time[2] < 60 and alarm_time[2] >= 0:
                return True
        return False
 
    note = str(input(" Bot: What note do you want to leave when the alarm goes off?\n User: " ))
    print(" Bot: Set a time for the alarm (Ex. 06:30 or 18:30:00)")
    while True:
        alarm_input = input(" Bot: Enter a time that you would like to set an alarm for\n User: ")
 
        try:
          alarm_time = [int(n) for n in alarm_input.split(":")]
          if check_alarm_input(alarm_time):
            break
          else:
            raise ValueError
        except ValueError:
          print(" Bot: !ERROR! Enter time in HH:MM or HH:MM:SS format")
 
    seconds_hms = [3600, 60, 1]
    alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])
 
    now = datetime.datetime.now()
    current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])
 
    time_diff_seconds = alarm_seconds - current_time_seconds
 
    if time_diff_seconds < 0:
        time_diff_seconds += 86400
 
    print(" Bot: Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))
 
 
    time.sleep(time_diff_seconds)
 
 
    print("\n     " + note +"\n")
      
   
        

    
    
