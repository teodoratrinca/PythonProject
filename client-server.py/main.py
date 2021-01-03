import requests
import youtube_search

def getReview(name):
    apikey = '2AsKNH2Nfs60mXg0mx59YRmHOPuS1pHl'
    movieTitle = name
    url = 'https://api.nytimes.com/svc/movies/v2/reviews/search.json?query=' + movieTitle + '&api-key=' + apikey
    params = {'type': 'movie'}
    response = requests.get(url, params=params).json()
    results = response['results']
    moviesReviews=" "
    for x in results:# pt fiecare dictionar afisam titlul si linkul spre pagina de review
        res={'display_title':x["display_title"],'link': x['link'] }
        res1 = res['link']
        res2={'display_title':x["display_title"],'url':res1['url']}
        moviesReviews=moviesReviews+str(res2['display_title'])
        moviesReviews=moviesReviews+str('\n')
        moviesReviews = moviesReviews + str(res2['url'])
        moviesReviews = moviesReviews + str('\n')
        #print(type(moviesReviews))
    return (moviesReviews)
getReview('titanic')

        #for y in res1:
            # res2={'display_title': x["display_title"],'link': y['url']}
            # print(res2)


        # print(type(res2))
        # for y in res1:
        #    res2={'url': y['link']}
        #    print(res2)
        #print(res1)
        #print(res)

getReview('Titanic')

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