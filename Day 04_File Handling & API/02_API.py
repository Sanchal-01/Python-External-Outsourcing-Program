# Authentication: Authentication verifies who you are (identity)
# Authorization: Authorization determines what you can do (permissions).

# Global API:

# Local API:

import requests 

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
data = response.json()
for users in data:
    print(f"Name: {users['name']}")
    print(f"Email: {users['email']}")
    print(f"City: {users['address']['city']}")

#-------------------------------------------------------#-------------------------------------------------


import requests

# 1. Added quotes around the URL string
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()

# 2. Loop through the list of users returned by the API
for user in data:
    # 3. Added quotes around dictionary keys and fixed f-string syntax
    print(f"Name: {user['name']}")
    print(f"Email: {user['email']}")
    print(f"City: {user['address']['city']}")
    print("-" * 20)

#-------------------------------------------------------#-------------------------------------------------
# TASK 1 : import requests 
# url = "https://jsonplaceholder.typicode.com/users"
# response = requests.get(url)
# data = response.json()
# for user in data:
#     print(f"Name: {user['name']} - Email: {user['email']}")


import requests

# 1. Added quotes around the URL string
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()

for user in data[:5]:

    print(f"Post_ID: {user['id']}")
    print(f"Title: {user['title']}")
    print("-" * 20)