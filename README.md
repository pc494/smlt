# smlt
smlt ('Save My Liked Tweets') is a pair of programs that allow users to capture, in a fairly comprehensive form, all of the tweets they have liked as an insurance against the website collapsing.

**Language**: Python    
**Difficulty**: Intermediate    
**Notes**: Limited documentation and no support.   

---

## Usage

### Pull down all tweets

The code first pulls down a complete list of tweets from a user account. This requires you to know your twitter user id and to 
have acquired a developer token from twitter. See their documentation for details. Running ```get_tweets_from_API.py``` will then 
produce a json of all the returns.

### Collect screenshots

This requires you to have completed step one, and to have working installs of selenium, Google Chrome and Jupyter. Running through the notebook (```screenshot_images_from_website.ipynb```)
changing the filepath for the google chrome install should then proceed without issue. Once it's working you'll see an automated browsing window open.

