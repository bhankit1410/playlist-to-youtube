from flask import Blueprint
from flask_restful import Api
from src.main.playlist_to_youtube import PlaylistToYoutube

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(PlaylistToYoutube, '/playlist-to-youtube')
