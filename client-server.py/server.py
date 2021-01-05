import pymongo
import socket
import requests
import youtube_search

apiKey = 'c69e149a'#pentru omdb db
URL = 'http://www.omdbapi.com/?apikey='+ apiKey
apikey1 = '2AsKNH2Nfs60mXg0mx59YRmHOPuS1pHl'# pentru reviews db
format = "utf-8"

host = '127.0.0.1'
port = 2727
# Address is stored as a tuple
#address = (host, port)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["MovieDB"]
mycol = mydb["movies"]


def getRating(name):
    gasit=0
    myquery = {'Title': name}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        return (x['imdbRating'])
    if (gasit == 0 ):
        params = {
            't': name,
            'type': 'movie'}
        response = requests.get(URL, params=params).json()
        if response['Response']=='False':# daca nu a gasit nici aici
           return "Movie not found"
        else:
            x = mycol.insert_one(response)
            return (response['imdbRating'])
    # return ("Nu s a gasit filmul")

def getRatingByActor( actor):
    gasit = 0
    allmovie = ""
    for x in mycol.find():
        actors = {"title": x['Title'], "actors": x['Actors'], "imdbRating": x['imdbRating']}
        words = actors['actors'].split(', ')
        print(words)
        if actor in words:
            gasit = 1
            allmovie = allmovie + str(actors['title'])
            allmovie = allmovie + str(" with rating: ")
            allmovie = allmovie + str(actors['imdbRating'])
            allmovie = allmovie + str(" \n")
    if (gasit == 0):
        return ("Movie not found                                            ")
    else:
        return (allmovie)

def getRatingByWord( word):
    gasit = 0
    allmovie = ""
    for x in mycol.find():
        titles = {"title": x['Title'], "imdbRating": x['imdbRating']}
        words = titles['title'].split(' ')
        if word in words:
            print(word)
            gasit = 1
            allmovie = allmovie + str(titles['title'])
            allmovie = allmovie + str(" with rating: ")
            allmovie = allmovie + str(titles['imdbRating'])
            allmovie = allmovie + str(" \n")
    if (gasit == 0):
        return ("Movie not found                                            ")
    else:
        return (allmovie)

def getTriler(name):
    results = youtube_search.YoutubeSearch(name+" trailer", max_results=10).to_dict()#lista de dictionare
    x = results[1]
    print(type(x))
    link = 'https://www.youtube.com/'+x['url_suffix']
    print(link)
    return(link)

def getReview(name):
        url = 'https://api.nytimes.com/svc/movies/v2/reviews/search.json?query=' + name + '&api-key=' + apikey1
        params = {'type': 'movie'}
        response = requests.get(url, params=params).json()
        results = response['results']
        moviesReviews = " "
        for x in results:  # pt fiecare dictionar afisam titlul si linkul spre pagina de review
            res = {'display_title': x["display_title"], 'link': x['link']}
            res1 = res['link']
            res2 = {'display_title': x["display_title"], 'url': res1['url']}
            moviesReviews = moviesReviews + str(res2['display_title'])
            moviesReviews = moviesReviews + str('\n')
            moviesReviews = moviesReviews + str(res2['url'])
            moviesReviews = moviesReviews + str('\n')
        if moviesReviews!= " ":
            return(moviesReviews)
        else:
            return ("Review not found")

def start():
    print("Server is working on " + host)
    s.listen()
    while True:
        conn, addr = s.accept()
        while True:
            message = conn.recv(1024).decode(format)
            if message =='REVIEW':
                message1 = conn.recv(1024).decode(format)
                print(getReview(message1))
                conn.send((getReview(message1)).encode(format))
            if message == 'TITLE':
                message1 = conn.recv(1024).decode(format)
                conn.send((getRating(message1)).encode(format))
            if message =='ACTOR':
                message1 = conn.recv(1024).decode(format)
                conn.send((getRatingByActor(message1)).encode(format))
            if message =='WORD':
                message1 = conn.recv(1024).decode(format)
                conn.send((getRatingByWord(message1)).encode(format))
            if message =='TRILER':
                message1 = conn.recv(1024).decode(format)
                conn.send((getTriler(message1)).encode(format))


start()











