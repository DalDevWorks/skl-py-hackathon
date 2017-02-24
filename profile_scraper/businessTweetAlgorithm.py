import os
from twitterQueries import get_all_tweets
from text_preprocessor import text_preprocessor
from models import Profile

def makeBusinessList():
    pwd = os.path.dirname(__file__)
    in_file = open(pwd + '/business_words.txt', 'r')
    business_list = []
    for line in in_file:
        business_list.append(line.rstrip(' \r\n '))
    return business_list

business_words = makeBusinessList()

weight_company = 5.0
weight_jobTitle = 2.0
weight_industry = 2.0


def determineTweetBusinessWeight(twitter_user):

    # get user data from the DB:
    user = Profile.objects.get(twitterUserName = twitter_user)

    company = user.company
    jobTitle = user.jobTitle
    industry = user.cdIndustry

    #get all tweetData:
    allTweets = get_all_tweets(twitter_user)

    #initialize min and max term weights
    min_weight = 100
    max_weight = 0

    #loop over each tweet and determine what type of tweet it is:
    for tweet in allTweets:
        processed_tweet = text_preprocessor(tweet['tweet'])
        company_weight = businessWeight(company, processed_tweet, weight_company)
        jobTitle_weight = businessWeight(jobTitle, processed_tweet, weight_jobTitle)
        industry_weight = businessWeight(industry, processed_tweet, weight_industry)

        business_term_weight = 0
        for word in processed_tweet:
            if word in business_words:
                business_term_weight += 0.5

        tweet_weight = company_weight + jobTitle_weight + industry_weight + business_term_weight
        if tweet_weight < min_weight: min_weight = tweet_weight
        if tweet_weight > max_weight: max_weight = tweet_weight

        tweet['isBusiness'] = tweet_weight
        tweet['processed_tweet'] = processed_tweet

    for tweet in allTweets:
        orig_weight = tweet['isBusiness']
        normalized_weight = (orig_weight - min_weight)/ (max_weight - min_weight)
        tweet['isBusiness'] = normalized_weight

    return allTweets


def businessWeight( term, processed_tweet, total_weight_value ):

    total_weight = 0

    if len(term) > 0:
        query_terms = text_preprocessor(term)

        tokenized = query_terms.split()
        query_weight = total_weight_value

        for word in tokenized:
            if word in processed_tweet:
                total_weight += query_weight

    return total_weight
