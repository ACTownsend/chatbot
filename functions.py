from random import *
greetings = ["hello", "hi", "hey", "yo"]

def greet(user):
    randomGreet = choice(greetings).capitalize()
    return randomGreet