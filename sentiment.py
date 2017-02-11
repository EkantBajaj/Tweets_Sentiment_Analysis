# importing dependencies
import tweepy
from textblob import TextBlob

# authentication
consumer_key = 'Enter consumer key here'
consumer_secret = 'Enter consumer secret here'

access_token = 'Enter access token here'
access_token_secret = 'Enter acess token secret here'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

# retrieving tweets

public_tweets = api.search('trump')

for tweet in public_tweets:
	print(tweet.text)
	# sentiment analysis of each tweet
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	print("")
