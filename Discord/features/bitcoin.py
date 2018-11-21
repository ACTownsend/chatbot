#BEGINNING OF DRAGOS CODE
import requests

def coin():
    coin = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    time = coin.json()['time']['updated']
    value = coin.json()['bpi']['GBP']['rate']
    sym = coin.json()['bpi']['GBP']['description']
    msg = "For "+time+" Bitcoin is "+value+" "+sym
    return msg
#END OF DRAGOS BITCOIN VALUE CODE
