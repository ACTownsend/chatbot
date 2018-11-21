#BEGINNING OF DRAGOS CODE
import requests
# Returns a link to a random cat gif
def getCatGif():
    catGif = requests.get('http://thecatapi.com/api/images/get?format=src&type=gif')
    if catGif.status_code == 200:
        catGif = catGif.url
        return catGif
    else:
        return 'Website may be down'
#END OF DRAGOS CATGIF CODE
