import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
pprint(all_movies)

all_titles = []

for movie in all_movies:
    all_titles.append(movie.getText())


movies = all_titles[::-1]

with open("day_45/day_45_project/movies_final.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
