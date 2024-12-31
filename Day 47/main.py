import requests
from bs4 import BeautifulSoup


date = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD ")

URL = "https://www.billboard.com/charts/hot-100/" + date
HEADER = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

response = requests.get(URL, headers=HEADER)
movies = response.text

soup = BeautifulSoup(movies, "html.parser")

song_names_spans = soup.select("li ul li h3")

for song in song_names_spans:
    song_name = song.getText().strip()
    print(song_name)


