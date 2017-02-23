from twitterQueries import get_all_tweets
from text_preprocessor import text_preprocessor
from models import Profile

weight_company = 1.0
weight_jobTitle = 0.5
weight_industry = 0.5

def determineTweetBusinessWeight(twitter_user):

    # get user data from the DB:
    user = Profile.objects.get(twitterUserName = twitter_user)

    company = user['company']
    jobTitle = user['jobTitle']
    industry = user['cdIndustry']

    #get all tweetData:
    allTweets = get_all_tweets(twitter_user)

    #loop over each tweet and determine what type of tweet it is:
    for tweet in allTweets:
        processed_tweet = text_preprocessor(tweet)
        company_weight = businessWeight(company, processed_tweet, weight_company)
        jobTitle_weight = businessWeight(jobTitle, processed_tweet, weight_jobTitle)
        industry_weight = businessWeight(industry, processed_tweet, weight_industry)

        tweet['isBusiness'] = company_weight + jobTitle_weight + industry_weight
        tweet['processed_tweet'] = processed_tweet

    return allTweets


def businessWeight( term, processed_tweet, total_weight_value ):

    query_terms = text_preprocessor(term)

    tokenized = query_terms.split()
    query_weight = total_weight_value / len(tokenized)

    total_weight = 0

    for word in tokenized:
        if word in processed_tweet:
            total_weight += query_weight

    return total_weight
