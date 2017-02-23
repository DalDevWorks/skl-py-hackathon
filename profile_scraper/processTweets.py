"""
Takes a twitterUserName and tweets object and converts them to Tweet models and saves to database
"""
from .models import Profile
def addTweets(twitterUserName, tweets):
    user = Profile.objects.get(twitterUserName=twitterUserName)
    user.statuses_counts = len(tweets)
    user.save()
    for tweet in tweets:
        t =user.tweet_set.create(tweetId = tweet['id'],
                              tweetRawText = tweet['tweet'],
                              tweetProcText = tweet['processed_tweet'],
                              isBusiness = tweet['isBusiness'])
        t.save()


