# ------------------------------------------------------------------------------------------------ #
#                                Automatic Spoftify Playlist Builder                               #
# ------------------------------------------------------------------------------------------------ #

import requests
import spotipy
from bs4 import BeautifulSoup
from pprint import pprint
from dotenv import dotenv_values
from spotipy.oauth2 import SpotifyOAuth

config = dotenv_values()
CLIENT_ID = config["SPOTIFY_CLIENT_ID"]
CLIENT_SECRET = config["SPOTIFY_CLIENT_SECRET"]
USERNAME = config["SPOTIFY_USER_NAME"]
URL = "https://www.billboard.com/charts/hot-100/"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="day_46/day_46_project/token.txt",
        username=USERNAME,
    )
)

user_id = sp.current_user()["id"]
date = input(
    "What year do you want to travel to? Type the date in this format [YYYY-MM-DD]: "
)
response = requests.get(URL + date)
soup = BeautifulSoup(response.text, "html.parser")

web_song_names_ = soup.select("li ul li h3")
web_song_artists = soup.select(
    "li ul li span.c-label.a-no-trucate.a-font-primary-s.lrv-u-font-size-14\@mobile-max.u-line-height-normal\@mobile-max.u-letter-spacing-0021.lrv-u-display-block.a-truncate-ellipsis-2line.u-max-width-330.u-max-width-230\@tablet-only"
)

song_names = [name.getText().strip() for name in web_song_names_]
artist_names = [artist.getText().strip() for artist in web_song_artists]


year = date.split("-")[0]
song_URIs = []

for song, artist in zip(song_names, artist_names):
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    pprint(artist)
    pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_URIs.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False,
    collaborative=False,
    description=f"Top Billboard 100 Songs from {date}",
)

playlist_id = playlist["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=song_URIs)
