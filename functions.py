from random import *
import webbrowser

greetings = ["hello", "hi", "hey", "yo"]
farewell = ["goodbye", "cya later", "bye", "cya", "later"]
browser = ["google", "search"]

def greet(user):
    randomGreet = choice(greetings).capitalize()
    return randomGreet

def endFunction(user):
    randomBye = choice(farewell).capitalize()
    return randomBye

def googleSearch():
    address = 'http://www.google.com/#q='
    search = input(" Bot : What would you like to search?\n User: ")
    searchterm = address + search
    print("Here is a link for: " + searchterm)
    webbrowser.open_new(searchterm)
    return searchterm
    
    