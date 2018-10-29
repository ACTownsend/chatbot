from random import *
from functions import *


print(chr(27) + "[2J")


user = input(" Bot: Welcome to chatbot! How may I help you?\n User: ")
user = user.lower()
while user != "go away":
    user = user.split(" ")

    for i in user:
        if i in greetings:
            resp = greet(user)
            user = input(" Bot: " + resp + "! What can I do for you?\n User: ")
        else:
            user = input(" Bot: Sorry I didn't quite catch that!\n User: ")

print("Fine then....")

    
   

    