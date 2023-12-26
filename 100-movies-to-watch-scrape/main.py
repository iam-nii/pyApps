import requests
from bs4 import BeautifulSoup
url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=url)
content = response.text

soup = BeautifulSoup(content, "html.parser")

# movies = [movie.getText() for movie in soup.select(selector=".gallery h3")] # one way of doing it

movies = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
# Using the slice to reverse a list
reversed_movies = movies[::-1]
print(reversed_movies)

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in reversed_movies:
        file.write(f"{movie}\n")