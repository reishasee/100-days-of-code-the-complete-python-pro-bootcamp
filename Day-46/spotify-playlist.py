import requests
from bs4 import BeautifulSoup
import spotipy
from datetime import datetime
from spotipy import SpotifyOAuth

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100/"
spotify_endpoint = "https://accounts.spotify.com"

html_id = "title-of-a-story"
html_class = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"
top_one_class = "c-title__link lrv-a-unstyle-link"

client_id = ENV_CLIENT_ID
client_secret = ENV_CLIENT_SECRET
redirect_uri = "http://example.com"
scope = "playlist-modify-private"
username = ENV_USERNAME

hot_100 = []
song_uri_list = []

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope,
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    show_dialog=True,
    cache_path="token.txt",
    username=username
    )
)

user_id = sp.current_user()["id"]

while True:
    try:
        date = input("What year would you like to travel to? Type the date in this format YYYY-MM-DD: ")
        parsed_date = datetime.strptime(date, "%Y-%m-%d")

    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

    else:
        response = requests.get(url=f"{url}{date}", headers=header)
        soup = BeautifulSoup(response.text, "html.parser")
        top_one = soup.find("a", class_=top_one_class).getText()
        top_one = top_one.replace("\n\t\n\t\t\n\t\t\t\t\t", "").replace("\t\t\n\t\t\t\t\t", "")
        hot_100 = [top_one]

        for song_element in soup.find_all("h3", class_=html_class):
            song_title = song_element.getText().replace("\n\n\t\n\t\n\t\t\n\t\t\t\t\t", "").replace("\t\t\n\t\n", "")
            hot_100.append(song_title)

        break

for song_title in hot_100:
    search_song = sp.search(q=f"track:{song_title} year:{parsed_date.year}", type="track")
    try:
        song_uri = search_song["tracks"]["items"][0]["uri"]
        song_uri_list.append(song_uri)
    except IndexError:
        print(f"{song_title} doesn't exist in Spotify. Skipped.")

my_playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False, collaborative=False)
sp.playlist_add_items(playlist_id=my_playlist["id"], items=song_uri_list)
