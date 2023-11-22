from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
page_content = response.text

soup = BeautifulSoup(page_content, "html.parser")

topics = soup.select(".titleline > a")
print(topics)

article_links = [link.get("href") for link in topics]
print(article_links)

points = soup.find_all(class_="score")
print(points)

for count in range(len(topics) - 1):
    print(topics[count].getText())
    print(article_links[count])
    print(points[count].getText())