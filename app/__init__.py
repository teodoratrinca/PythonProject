from flask import Blueprint
from flask_restx import Api

from .main.controllers.movie_controller import api as movies_api


blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='Movies API',
    version='1.0'
)

api.add_namespace(movies_api, path='/')

