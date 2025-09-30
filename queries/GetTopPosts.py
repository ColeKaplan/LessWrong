import requests

GRAPHQL_URL = "https://www.lesswrong.com/graphql"

def getTopPosts(limit, maxAge=5):
    query = """
    query multiCommentQuickTakesSectionQuery(
        $selector: CommentSelector, 
        $limit: Int, 
        $enableTotal: Boolean
        ) {
        comments(selector: $selector, limit: $limit, enableTotal: $enableTotal) {
            results {
            ...ShortformComments
            __typename
            }
            totalCount
            __typename
        }
        }

        fragment ShortformComments on Comment {
        ...CommentsList
        post {
            ...PostsMinimumInfo
            __typename
        }
        relevantTags {
            ...TagPreviewFragment
            __typename
        }
        __typename
        }

        fragment CommentsList on Comment {
        _id
        postId
        tag {
            _id
            slug
            __typename
        }
        title
        contents {
            _id
            html
            plaintextMainText
            wordCount
            __typename
        }
        postedAt
        userId
        draft
        deleted
        deletedPublic
        user {
            ...UsersMinimumInfo
            __typename
        }
        currentUserVote
        currentUserExtendedVote
        score
        voteCount
        }

        fragment TagPreviewFragment on Tag {
        ...TagBasicInfo
        isRead
        parentTag {
            ...TagBasicInfo
            __typename
        }
        subTags {
            ...TagBasicInfo
            __typename
        }
        description {
            _id
            htmlHighlight
            __typename
        }
        canVoteOnRels
        isArbitalImport
        __typename
        }

        fragment TagBasicInfo on Tag {
        _id
        userId
        name
        shortName
        slug
        core
        postCount
        adminOnly
        canEditUserIds
        suggestedAsFilter
        needsReview
        descriptionTruncationCount
        createdAt
        wikiOnly
        deleted
        isSubforum
        noindex
        isArbitalImport
        isPlaceholderPage
        baseScore
        extendedScore
        score
        afBaseScore
        afExtendedScore
        voteCount
        currentUserVote
        currentUserExtendedVote
        __typename
        }

        fragment UsersMinimumInfo on User {
        _id
        slug
        createdAt
        username
        displayName
        profileImageId
        karma
        afKarma
        deleted
        isAdmin
        htmlBio
        jobTitle
        organization
        postCount
        commentCount
        sequenceCount
        afPostCount
        afCommentCount
        spamRiskScore
        tagRevisionCount
        reviewedByUserId
        __typename
        }

        fragment PostsMinimumInfo on Post {
        _id
        slug
        title
        draft
        shortform
        hideCommentKarma
        af
        userId
        coauthorUserIds
        rejected
        collabEditorDialogue
        __typename
        }

    """
    
    resp = requests.post(GRAPHQL_URL, json={"query": query, "variables": {"selector": {
        "shortformFrontpage": {
            "showCommunity": False,
            "maxAgeDays": 5
        }
        },
        "enableTotal": True,
        "limit": limit}})
    
    data = resp.json()
    posts = data.get("data").get("comments").get("results")
    # print(posts)

    return posts