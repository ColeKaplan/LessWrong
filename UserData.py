import requests
import sys
import re
from queries.GetTopUsers import getTopActiveUsers
from queries.GetUserBySlug import getUserBySlug, slugify
from queries.GetTopPosts import getTopPosts

GRAPHQL_URL = "https://www.lesswrong.com/graphql"

slug = slugify("Cole Kaplan")
user = getUserBySlug(slug)
topUsers = getTopActiveUsers(10)
topPosts = getTopPosts(5)

# print(user)

# print(topUsers)

# for post in topPosts:
#     print(post["user"]["displayName"])
