from random import *
from functions import *


print(chr(27) + "[2J")


user = input(" Bot: Welcome to chatbot! How may I help you?\n User: ")
user = user.lower()
exit = False
while exit == False:
    user = user.split(" ")

    for i in user:
        if i in greetings:
            resp = greet(user)
            user = input(" Bot: " + resp + "! What can I do for you?\n User: ")
        elif i in farewell:
            resp = endFunction(user)
            user = print(" Bot: " + resp + "!") 
            exit = True
        else:
            a = input(" Bot: Sorry I didn't quite catch that!\n User: ")



    

    