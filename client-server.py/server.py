import pymongo
import socket
from pprint import PrettyPrinter
import requests

pp = PrettyPrinter()
apiKey = 'c69e149a'
URL = 'http://www.omdbapi.com/?apikey='+ apiKey
format = "utf-8"

host = '127.0.0.1'
port = 2727
# Address is stored as a tuple
#address = (host, port)

# Create a new socket for
# the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["MovieDB"]
mycol = mydb["movies"]


def getRating(name):
    gasit = 0
    myquery = {'Title': name}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        gasit = 1
        return (x['imdbRating'])
    if (gasit == 0):
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
        return ("Nu s-a putu gasi film")
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
        return ("Nu s-a putu gasi film")
    else:
        return (allmovie)

def getTriler(name):
    print(name)

def start():
    print("Server is working on " + host)
    s.listen()
    while True:
        conn, addr = s.accept()
        message = conn.recv(1024).decode(format)
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










