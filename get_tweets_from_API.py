import requests
import os
import json

""" 
This file is adapted from the one avaliable at:
https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Likes-Lookup/liked_tweets.py
where major changes have been made they are noted.
"""

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

bearer_token = os.environ.get("BEARER_TOKEN")

# similarly for user id
id = os.environ.get("id")


def create_url(pagination_token):
    # this now deals with pagination
    if pagination_token is not None:
        tweet_fields = "tweet.fields=lang,author_id,attachments&pagination_token="+pagination_token
    else:
        tweet_fields = "tweet.fields=lang,author_id,attachments"
    
    # You can adjust ids to include a single users liked Tweets.
    # Or you can add to up to 100 comma-separated IDs
    url="https://api.twitter.com/2/users/{}/liked_tweets".format(id)
    return url, tweet_fields


def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2LikedTweetsPython"
    return r


def connect_to_endpoint(url, tweet_fields):
    response = requests.request(
        "GET", url, auth=bearer_oauth, params=tweet_fields)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    i = 0 #counter of the number of 'pages' ~ 100 tweets seen
    i_max = 500 # a hard stop on how many 'pages' to pull down
    results = {}
    pagination_token=None #for the first call we need to not have pagination token

    while i < i_max:
        i += 1
        url, tweet_fields = create_url(pagination_token)
        json_response = connect_to_endpoint(url, tweet_fields)
        
        # use a nested dictionary for storage
        results[str(i)]= json_response
        
        # get the pagination token
        try:
            pagination_token = json_response["meta"]["next_token"]
        except KeyError:
            # no more pages to go to
            break
        
    with open('complete_pull.json', "w") as fp:
                json.dump(results,fp) 

if __name__ == "__main__":
    main()
