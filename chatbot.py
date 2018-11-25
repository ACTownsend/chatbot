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
        if i in greetList:
            ran = should
            greet(user)
        elif i in byeList:
            ran = should
            exit = endFunction(user)           
        elif i in browserList:
            ran = should 
            if i != split[-1]:
                after = True
                split = user.split(i)
                term = split[1]
                term = term.replace(" ","")
                googleSearch(term,after)
            else:
                googleSearch(0,after)								
        elif i in timeList:
            ran = should
            checkTimeZone()            
        elif i in weatherList:
            ran = should
            weather()            
        elif i in dieList:
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
        elif i in shopList:
            ran = should
            shoppingList()
        elif i in featureList:
            ran = should
            listOfFeatures()
        elif i == "alarm":
            ran = should
            alarm()
        if ran == should:
            break
    if exit == False:
        if ran != should:
            print(" Bot: Sorry, I didnt quite catch that!")
        user = input(" Bot: Anything else I can help you with?\n User: ")
    else:
        break




    

    
