import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import  SpotifyOAuth

date = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD ")

URL = "https://www.billboard.com/charts/hot-100/" + date
HEADER = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

response = requests.get(URL, headers=HEADER)
movies = response.text

soup = BeautifulSoup(movies, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# for song in song_names_spans:
#     song_name = song.getText().strip()
#     print(song_name)


#spotify


CLIENT_ID = your_client_id
CLIENT_SECRET = your_client_secret
REDIRECT_URI = "http://example.com"

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                                    client_id=CLIENT_ID,
                                    client_secret=CLIENT_SECRET,
                                    redirect_uri=REDIRECT_URI,
                                    scope="playlist-modify-private",
                                    show_dialog=True,
                                    cache_path="token.txt",
                                    username="Lakindu Perera"
                                    ))

user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]

# Searching Spotify for songs by title
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


# Create a new private playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(f"Playlist created: {playlist['name']}")

# Add the songs to the playlist
if song_uris:
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
    print(f"Added {len(song_uris)} songs to the playlist.")
else:
    print("No songs were found to add.")

