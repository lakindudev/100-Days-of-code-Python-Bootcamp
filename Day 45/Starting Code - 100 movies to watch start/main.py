# Challenge code : get the great 100 movies from the 'The 100 Greater Movies' using web scraping

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
the_100_gretest_movie =  response.text

soup = BeautifulSoup(the_100_gretest_movie, "html.parser")

movie_arr = []

movie_names = soup.find_all(name="h3" , class_= "title")
for movie in movie_names:
    movie_name = movie.text
    movie_arr.append(movie_name)

reviersed_arr = movie_arr[::-1]

for movie in reviersed_arr:
    print(movie)