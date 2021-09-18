import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())
url = "http://httpbin.org/post"
payload = dict(key1='value1', key2='value2')
res = requests.post(url, data=payload)

print(res.text)