from random import *
greetings = ["Hello", "Hi", "Hey", "Yo"]

def greet(user):
    randomGreet = choice(greetings)
    return randomGreet