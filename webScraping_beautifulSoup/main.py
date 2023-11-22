from bs4 import BeautifulSoup

with open("website.html") as web_page:
    content = web_page.read()

# Making soup and parsing the elements
soup = BeautifulSoup(content, "html.parser")

# print(soup.title)
# print(soup.a) # Returns the first a tag element

# Returning multiple elements
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags) # Returns a list of all anchor tags
# for tag in all_anchor_tags:
#     print(tag.getText()) # Gets the text in the anchor tags
#     print(tag.get("href")) # Gets the href attribute
#     print(tag.get("class")) # Gets the class att if available. returns none if no class is found
#

# authors_name = soup.find(name="h1", id="name") # Returns the h1 tag with corresponding id
# print(authors_name)

# Returning a list of all h3 headings with the  corresponding class attribute
# headings = soup.find_all(name="h3", class_="heading")
# print(headings)
# select_headings = soup.select(".heading")
# print(select_headings)
#
#
# # Narrowing down to an element using selectors
# app_brewery = soup.select_one(selector="p a")
# print(app_brewery)
#
# select_id = soup.select_one(selector="#name")
# print(select_id)
