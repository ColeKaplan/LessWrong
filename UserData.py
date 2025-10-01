import requests
import sys
import re
from queries.GetTopUsers import getTopActiveUsers
from queries.GetUserBySlug import getUserBySlug, slugify
from queries.GetTopPosts import getTopPosts
from queries.GetPostsByUserId import getPostsByUserId

GRAPHQL_URL = "https://www.lesswrong.com/graphql"

slug = slugify("Cole Kaplan")
user = getUserBySlug(slug)
topUsers = getTopActiveUsers(10)
topPosts = getTopPosts(5)
userPosts = getPostsByUserId(topUsers[0]["_id"], limit=10)


# print(user)

# print(topUsers[0])

# for post in topPosts:
#     print(post["user"]["displayName"])

# for userPost in userPosts:
#     print(userPost, "\n")

# for post in myPosts.get("data", {}).get("posts", {}).get("results", []):
#     print(post)



