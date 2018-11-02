from random import *
from functions import *


user = input(" Bot: Welcome to chatbot! How may I help you?\n User: ")
user = user.lower()
exit = False
ran = 0
should = 0 
while exit == False:
    user = user.split(" ")    
    for i in user:
        should += 1
        for j in greetings:
            if i == j:
                resp = greet(user)
                user = input(" Bot: " + resp + "! What can I do for you?\n User: ")
                ran = should
        for j in farewell:
            if i == j:
                resp = endFunction(user)
                user = print(" Bot: " + resp + "!") 
                exit = True
                ran = should
        for j in browser:
            if i == j:
                googleSearch()
                ran = should 
                user = input(" Bot: Anything else I can help you with?\n User: ")								
        for j in clock:
            if i == j:
                checkTimeZone()
                ran = should
                user = input(" Bot: Anything else I can help you with?\n User: ")               
    if ran != should:
        user = input(" Bot: Sorry, I didnt quite catch that\n User: ")




    

    