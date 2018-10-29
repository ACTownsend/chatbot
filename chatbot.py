from random import *
from functions import *


print(chr(27) + "[2J")


user = input("Welcome to chatbot! How may I help you?\n>>> ")
user = user.capitalize()

if user in greetings:
    resp = greet(user)
    print(resp + "! What can I do for you?\n>>> ")
else:
    print("Sorry I didn't quite catch that\n")


    
   

    