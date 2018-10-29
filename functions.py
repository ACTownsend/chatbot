from random import *
greetings = ["Hello", "Hi", "Hey", "Yo"]

def greet():
    randomGreet = choice(greetings)
    return randomGreet