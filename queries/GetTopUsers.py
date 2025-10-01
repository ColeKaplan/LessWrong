import requests

GRAPHQL_URL = "https://www.lesswrong.com/graphql"

def getTopActiveUsers(limit):
    query = """
    query($limit: Int!) {
        SuggestedTopActiveUsers(limit: $limit) {
            results {
                _id
                postCount
                commentCount
                karma
                displayName
                slug
                pageUrl
            }
        }
    }
    """
    
    resp = requests.post(GRAPHQL_URL, json={"query": query, "variables": {"limit": limit}})
    data = resp.json()
    users = data.get("data").get("SuggestedTopActiveUsers").get("results")
    # print(users)

    return users