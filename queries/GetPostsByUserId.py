import requests

# GraphQL endpoint
url = "https://www.lesswrong.com/graphql"

def getPostsByUserId(userId, limit=50):
    query = """
    query postsByUser($selector: PostSelector, $limit: Int, $enableTotal: Boolean) {
    posts(selector: $selector, limit: $limit, enableTotal: $enableTotal) {
        results {
        _id
        title
        userId
        voteCount
        extendedScore
        tags {
            _id
            name
            slug
        }
        }
        totalCount
    }
    }
    """

    variables = {
        "selector": {
            "userPosts": {
                "userId": userId
            }
        },
        "limit": limit,
        "enableTotal": True
    }

    response = requests.post(url, json={"query": query, "variables": variables})
    data = response.json().get("data").get("posts").get("results")
    return data
