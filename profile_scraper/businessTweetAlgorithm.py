from twitterQueries import get_all_tweets
from text_preprocessor import text_preprocessor
from models import Profile

def determineTweetBusinessWeight(twitter_user):

    user = Profile.objects.get(twitterUserName = twitter_user)

    #TODO: get user data from the DB:
    userData = {}
    userData['company'] = user['company']
    userData['jobTitle'] = user['jobTitle']
    userData['industry'] = user['cdIndustry']

    #TODO: pre-process the CSV data

    #get all tweetData:
    allTweets = get_all_tweets(twitter_user)

    #loop over each tweet and determine what type of tweet it is:
    for tweet in allTweets:
        #determine if tweet is business or personal:

        tweet['isBusiness'] = ""

    return allTweets

def businessWeight( term, tweet, total_weight_value ): 

    query_terms = text_preprocessor(term)
    processed_tweet = text_preprocessor(tweet)
    tokenized = query_terms.split()
    query_weight = total_weight_value / len(tokenized)

    total_weight = 0

    for word in tokenized:
        if word in processed_tweet:
            total_weight += query_weight

    return total_weight
