from flask_restx import Namespace, fields


class MovieDTO:
    # A namespaces group resources together.
    api = Namespace('movies')

    # In the global namespace, we'll register a single model called movie with
    #   the following fields:
    movie = api.model('movie', {
        'title': fields.String(required=True),
        'rating': fields.Float(required=True)
    })
