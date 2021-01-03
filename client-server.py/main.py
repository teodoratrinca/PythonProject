import youtube_search
apikey='188e5a4dfea40a0e39893fe16b9c9aae'
language='en-US'
url='https://api.themoviedb.org/3/movie/{movie_id}?api_key='+apikey+'&language='+language


results = youtube_search.YoutubeSearch('titanic trailer', max_results=10).to_dict()

print(results)
# returns a dictionary
# import requests
# from pprint import PrettyPrinter
# pp = PrettyPrinter()
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["MovieDB"]
# mycol = mydb["movies"]
# apiKey = 'c69e149a'
# URL = 'http://www.omdbapi.com/?apikey='+ apiKey
# year = ''
# title = input("Numele filmului: ")
# movie = f'{title}'
# #movie = 'Fast & Furious'
# params = {
#     't': movie,
#     'type': 'movie',
#     'y': year,
#     'plot': 'full'
# }
# response = requests.get(URL, params=params).json()
# pp.pprint(response)
# #pp.pprint(response['Actors'])
# #pp.pprint(response['Ratings'])
#
# def getRating(name):
#     gasit=0
#     myquery = {'Title': name}
#     mydoc = mycol.find(myquery)
#     for x in mydoc:
#         gasit=1
#         return (x['imdbRating'])
#     if(gasit == 0):
#        params = {
#             't': name,
#             'type': 'movie'}
#        response = requests.get(URL, params=params).json()
#        return (response)
#     #return ("Nu s a gasit filmul")
#
# getRating('The One')