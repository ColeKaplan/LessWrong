import requests
import re

GRAPHQL_URL = "https://www.lesswrong.com/graphql"

def slugify(username: str) -> str:
    """Turn 'Cole Kaplan' into 'cole-kaplan'"""
    return re.sub(r'[^a-z0-9-]', '', username.strip().lower().replace(" ", "-"))

def getUserBySlug(slug: str):
    query = """
    query($slug: String!) {
      GetUserBySlug(slug: $slug) {
        displayName
        slug
        pageUrl
        postCount
        commentCount
        karma
      }
    }
    """

    resp = requests.post(GRAPHQL_URL, json={"query": query, "variables": {"slug": slug}})
    data = resp.json()
    user = data.get("data").get("GetUserBySlug")
    # print(user)

    return user