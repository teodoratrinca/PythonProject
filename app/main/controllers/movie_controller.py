from flask import request
from flask_restx import Resource
from ..util.dto import MovieDTO
from ..services.movie_service import get_movies

api = MovieDTO.api
_movie = MovieDTO.movie


@api.route('movies')
class Movie(Resource):

    # specifies the fields to use for serialization
    @api.doc(
        description="""
        Returns all movies with a given title.
        """,
        params={
            'title': {
                'description': 'The title of the movie <br>',
                'type': 'string'
            }
        }
    )
    @api.marshal_list_with(_movie, envelope='movies')
    @api.response(200, 'Success')
    def get(self):
        title = request.args.get('title')

        get_movies(title)

        return [{
            'title': title,
            'rating': 9.8
        }]
