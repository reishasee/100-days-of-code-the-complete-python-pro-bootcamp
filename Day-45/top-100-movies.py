import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
top_movies = requests.get(url=URL)
soup = BeautifulSoup(top_movies.text, "html.parser")
movie_list = [movie.getText() for movie in soup.find_all("h3", class_="title")]
movie_list.reverse()
with open(r"movies.txt", mode="w", encoding="utf-8") as file:
    [file.write(f"{movie}\n") for movie in movie_list]




