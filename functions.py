from random import *
greetings = ["hello", "hi", "hey", "yo"]
farewell = ["goodbye", "cya later", "bye", "cya", "later"]
def greet(user):
    randomGreet = choice(greetings).capitalize()
    return randomGreet

def endFunction(user):
    randomBye = choice(farewell).capitalize()
    return randomBye