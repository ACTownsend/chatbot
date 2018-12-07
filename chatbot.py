from functions import *    #All the functions are kept in a separate file to help abstract the code


user = input(" Bot: Welcome to chatbot! How may I help you?\n User: ")
user = user.lower()
exit = False
after = False
ran = 0     #These two variables are used to determine if any of the functions have been ran 
should = 0 
while exit == False:      #The code is ran until one of the exit words are triggered
    should += 1
    split = user.split(" ")    #Splits the user input into a list so that we can search for key terms to trigger functions
    for i in split:
        if i in greetList:      #No switch cases in python so if statements will have to do
            ran = should
            greet()
        elif i in byeList:
            ran = should
            exit = endFunction()           
        elif i in browserList:
            ran = should 
            if i != split[-1]:            #Checks to see if the user has already specified what they would like to google
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
            if "d" in user:          #Checks to see if the user has already specified which die they would like to roll
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
        elif i in imdbList:
            ran = should
            movieSearch()
        elif i in holidayList:
            ran = should
            holidayCheck()            
        if ran == should:       #This IF statement was implemented to make it so that if the user enters more than one of the keywords
            break               #to trigger a function, it will not run twice
    if exit == False:
        if ran != should:       #Using the two aforementioned variables to check if a function has been ran
            print(" Bot: Sorry, I didnt quite catch that!")
        user = input(" Bot: Anything else I can help you with?\n User: ")
    else:
        break
