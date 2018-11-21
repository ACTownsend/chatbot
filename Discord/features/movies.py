#BEGINNING OF DRAGOS CODE
## THIS CODE IS NOTE WORKING 
import requests
from tmdbv3api import TMDb
from tmdbv3api import Movie
tmdb = TMDb()
tmdb.api_key = 'c3878d04ab03d603fc5b9eecb2074283'
def movie(name):
    response = "Searching for 2 similar movies for "+name
    movie = Movie()
    search = movie.search(name)
    i=0
    for result in search:
        if i<2:
            response+= result.title+"\n"
            response+=result.overview+"\n"
            response+="https://image.tmdb.org/t/p/w500" + p.poster_path + "\n"
            i=i+1
        else:
            break
    return response
#END OF DRAGOS MOVIE RECOMANDATION CODE
