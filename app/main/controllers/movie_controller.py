from flask_restx import Resource
from ..util.dto import MovieDTO

api = MovieDTO.api
_movie = MovieDTO.movie


@api.route('movies')
class Movie(Resource):

    # specifies the fields to use for serialization
    @api.marshal_list_with(_movie, envelope='movies')
    @api.response(200, 'Success')
    def get(self):
        return [{
            'title': 'Avengers',
            'rating': 9.8
        }]
