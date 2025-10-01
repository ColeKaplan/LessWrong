import requests
import sys
import re
from queries.GetTopUsers import getTopActiveUsers
from queries.GetUserBySlug import getUserBySlug, slugify
from queries.GetTopPosts import getTopPosts
from queries.GetPostsByUserId import getPostsByUserId
from visualizers.popularTags import popularTags

GRAPHQL_URL = "https://www.lesswrong.com/graphql"


import matplotlib.pyplot as plt
    
popularTags(10)

