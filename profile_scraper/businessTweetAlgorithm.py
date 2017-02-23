from twitterQueries import get_all_tweets
from text_preprocessor import text_preprocessor
#from models import profiles

def determineTweetBusinessWeight(twitter_user):

    #TODO: get user data from the DB:
    userData = {}
    userData['businessName'] = ""
    userData['jobTitle'] = ""
    userData['industry'] = ""

    #TODO: pre-process the CSV data

    #get all tweetData:
    allTweets = get_all_tweets(twitter_user)

    #loop over each tweet and determine what type of tweet it is:
    for tweet in allTweets:
        #determine if tweet is business or personal:

        tweet['isBusiness'] = ""

    return allTweets


