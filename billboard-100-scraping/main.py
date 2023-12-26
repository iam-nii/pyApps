import requests
from bs4 import BeautifulSoup

# Working with Spotify
import spotipy, os
from spotipy.oauth2 import SpotifyOAuth


SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

# sp = spotipy.oauth2.SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, scope=scope,
# redirect_uri=SPOTIPY_REDIRECT_URI)
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="95e4c713fefc4bbab2988b7f33c1e9c1",
        client_secret="db453b9f710240daac0678e3abbf497e",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt",
        username='adjeiboyejnr',
        redirect_uri="https://example.com/"
    )
)

user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# Scraping the Billboard page

url = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(url=url).text
# print(response)

soup = BeautifulSoup(response, "html.parser")

songs_list = soup.select(selector="li ul li h3")
songs = [song.getText().strip("\n\t") for song in songs_list]

authors_list = soup.select(selector="ul li ul li span")
artists = [artist.getText().strip("\n\t") for artist in authors_list]
filtered_artists = []
for artist in artists:
    new_artists = artist
    try:
        new_artists = int(artist)
    except (TypeError, ValueError):
        filtered_artists.append(new_artists)
    else:
        continue

print(songs)
print(filtered_artists)


song_uris = []
year = date.split("-")[0]

playlist = sp.user_playlist_create(user=user_id, name=f"My Top 100 for{year}", public=False)
playlist_id = playlist["id"]

for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


for song_uri in song_uris:
    try:
        sp.playlist_add_items(playlist_id=playlist_id, items=song_uri)
    except:
        continue
print(playlist['id'])


