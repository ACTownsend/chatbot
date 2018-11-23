from random import *
from functions import *


user = input(" Bot: Welcome to chatbot! How may I help you?\n User: ")
user = user.lower()
exit = False
after = False
ran = 0
should = 0 
while exit == False:
    should += 1
    split = user.split(" ")    
    for i in split:
        if i in greetings:
            resp = greet(user)
            print(" Bot: " + resp + "!")
            ran = should
        elif i in farewell:
            resp = endFunction(user)
            print(" Bot: " + resp + "!") 
            exit = True
            ran = should
        elif i in browser:
            ran = should 
            if i != split[-1]:
                after = True
                split = user.split(i)
                term = split[1]
                term = term.replace(" ","")
                googleSearch(term,after)
            else:
                googleSearch(0,after)								
        elif i in clock:
            checkTimeZone()
            ran = should
        elif i in weatherList:
            weather()
            ran = should
        elif i in rollDice:
            ran = should 
            if "d" in user:
                dice = user.index("d")
                dice+=1
                if user[dice].isdigit():
                    split = list(user)
                    diceNumber = split[dice:]
                    diceNumber = int("".join(diceNumber))
                    diceRoll(diceNumber)
                else:
                    diceRoll(0)
                    break
            else:
                diceRoll(0)
        elif i in emailList:
            ran = should
            emailFunction()
        elif i in coinList:
            ran = should
            guess = input(" Bot: Heads or Tails?\n User: ")
            guess = guess.capitalize()
            coin(guess) 
    if exit == False:
        if ran != should:
            print(" Bot: Sorry, I didnt quite catch that!")
        user = input(" User: ")
    else:
        break
