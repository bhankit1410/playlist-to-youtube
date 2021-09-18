def parse_spotify_playlist(json_data):
    playlist_name = json_data['name']
    list_of_songs = [item['track']['name'] for item in json_data['tracks']['items']]
    return playlist_name, list_of_songs
