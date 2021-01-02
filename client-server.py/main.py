import pymongo
import requests
from pprint import PrettyPrinter

pp = PrettyPrinter()

apiKey = 'c69e149a'
URL = 'http://www.omdbapi.com/?apikey=' + apiKey


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["MovieDB"]
mycol = mydb["movies"]

# pp.pprint(response['Actors'])
# pp.pprint(response['Ratings'])


