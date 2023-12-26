from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
page_content = response.text

soup = BeautifulSoup(page_content, "html.parser")

topics = soup.select(".titleline > a")
topic_list = [item.getText() for item in topics]

article_links = [link.get("href") for link in topics]
# print(article_links)

points = soup.find_all(class_="score")
filtered_points = [int(point.getText().split()[0]) for point in points]
# print(points)

# print(topic_list)
# print(article_links)
# print(filtered_points)

# Getting the index of the highest upvote
# My approach
# max_ = 0
# index = 0
# for score in filtered_points:
#     if score > max_:
#         max_ = score
#         index = filtered_points.index(score)

# Tutors solution
max_ = max(filtered_points)
index = filtered_points.index(max_)
print(topic_list[index])
print(article_links[index])
print(max_)