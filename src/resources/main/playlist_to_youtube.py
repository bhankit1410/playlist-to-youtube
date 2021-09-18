# python3

import pandas as pd
from flask import request
from flask_restful import Resource


class PlaylistToYoutube(Resource):

    def post(self):
        headers = dict((k.lower(), v) for k, v in request.headers.items())
        json_data = request.get_json()
        # todo: call spotify

        # todo: call youtube
        return pd.Series(json_data)


def main():
    print("x")


if __name__ == '__main__':
    main()
