import requests


def get_movies(title):
    api_key = 'c69e149a'
    url = 'http://www.omdbapi.com/?apikey=' + api_key
    params = {
        't': title,
        'type': 'movie',
        'plot': 'full'
    }
    response = requests.get(url, params=params).json()
    print(response)

