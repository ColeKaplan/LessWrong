import sys
from pathlib import Path

# Add the project root to sys.path so `queries` can be found
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

charts_dir = project_root / "charts"
charts_dir.mkdir(exist_ok=True)

# Now we can import queries
from queries.GetTopUsers import getTopActiveUsers
from queries.GetPostsByUserId import getPostsByUserId
import matplotlib.pyplot as plt
import json


def popularTags(limit=10):
    topUsers = getTopActiveUsers(limit)
    tagCount = {}
    
    # count tags
    for user in topUsers:
        userPosts = getPostsByUserId(user["_id"], limit=user["postCount"])
        for post in userPosts:
            for tag in post["tags"]:
                name = tag["name"]
                tagCount[name] = tagCount.get(name, 0) + 1
    
    # compute total tags
    totalTags = sum(tagCount.values())
    
    # filter tags >= 5%
    filteredTags = {k: v for k, v in tagCount.items() if v / totalTags >= 0.01}
    
    # sort by count descending
    filteredTags = dict(sorted(filteredTags.items(), key=lambda x: x[1], reverse=True))
    
    # plot
    plt.figure(figsize=(10,6))
    plt.bar(filteredTags.keys(), filteredTags.values(), color='skyblue')
    plt.ylabel("Count")
    plt.title("Popular Tags (≥1% of all tags)")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(charts_dir / "popular_tags_chart.png")
    plt.close() 