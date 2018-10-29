from random import *
from functions import *


print(chr(27) + "[2J")


user = input(" Bot: Welcome to chatbot! How may I help you?\n User: ")
user = user.capitalize()

if user in greetings:
    resp = greet()
    print(" Bot: " + resp + "! What can I do for you?\n ")
else:
    print(" Bot: Sorry I didn't quite catch that\n")


    
   

    