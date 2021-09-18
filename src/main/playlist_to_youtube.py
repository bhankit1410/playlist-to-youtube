# python3

from flask import request
from flask_restful import Resource
import json
from src.main.spotify.helper import parse_spotify_playlist


class PlaylistToYoutube(Resource):

    def post(self):
        headers = dict((k.lower(), v) for k, v in request.headers.items())
        spotify_playlist = request.get_json()
        list_of_songs = parse_spotify_playlist(spotify_playlist)
        # todo: call spotify

        # todo: call youtube
        return jsonify(spotify_playlist)


def main():
    path = 'resources/hit_rewind.json'
    f = open(path, )
    spotify_playlist = json.load(f)
    playlist_name, list_of_songs = parse_spotify_playlist(spotify_playlist)
    for song in list_of_songs:
        print(song)


if __name__ == '__main__':
    main()
