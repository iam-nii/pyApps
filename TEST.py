import requests

BLOGS = "https://api.npoint.io/c790b4d5cab58020d391"

response = requests.get(BLOGS).json()
POSTS = {
    'ids': [],
    'posts': {},
}

for post_ in range(len(response)):
    POSTS['ids'].append(response[post_]['id'])
    POSTS['posts'][post_ + 1] = {
        'title': response[post_]['title'],
        'subtitle': response[post_]['subtitle'],
        'body': response[post_]['body'],
    }
print(POSTS)
for key in range(len(POSTS) + 1):
    print(POSTS['posts'][key + 1]['subtitle'])


print("\n")
print(POSTS['posts'])
