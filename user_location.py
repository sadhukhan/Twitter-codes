# CODE TO PRINT USER LOCATIONS OF ALL THE FOLLOWERS OF A GIVEN TWITTER ACCOUNT

import os
import time
import tweepy
from tweepy import OAuthHandler

"""
# declare
consumer_key= ''
consumer_secret= ''
access_token=''
access_token_secret=''
"""
consumer_key= ''								#new app
consumer_secret= ''
access_token='-'
access_token_secret=''


# authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

sleeptime = 5
pages = tweepy.Cursor(api.followers, screen_name = 'disclosure').pages()
while True:
	try:
		page = next(pages)
		time.sleep(sleeptime)
	except tweepy.TweepError: #taking extra care of the "rate limit exceeded"
		time.sleep(60*15)
		page = next(pages)
	except StopIteration:
		break
	for user in page:
		print([user.screen_name, user.location], sep='\t')
