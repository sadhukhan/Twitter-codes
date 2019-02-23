# CODE TO PRINT THE TWITTER TL. PRINTS DATA ALL THE TWEETS POSTED BY THE ACCOUNTS THAT ARE BEING FOLLOWED ON TWITTER BY THE USER

import os  
import tweepy 
from tweepy import Stream 
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import datetime

# declare
consumer_key= ''
consumer_secret= ''
access_token=''
access_token_secret=''

# so much fucking boilerplate !!! This comment has become a static boilerplate!!
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

startTime = datetime.datetime.now().strftime('%d%m%Y-%H%M%S')
f = open(startTime, 'w')	#save file name !!!

cntr = 0
print('Tracking Twitter Daily for MA')
print('Counter', 'Twitter Handle', 'User Location', 'Tweet', 'Tweet Time', 'Favorite count', 'RT', 'In Reply to Another User', 'URL in the Tweet', 'Hashtags in Tweet', file=f, sep="\t")
for status in tweepy.Cursor(api.home_timeline).items():	
	cntr += 1
	#print(cntr, status, sep="\t")
	#print(cntr, status.user.screen_name, status.user.location, status.text.encode("utf-8"), status.created_at, status.favorite_count, status.retweeted, status.in_reply_to_user_id,  status.entities['urls'], status.entities['hashtags'], sep="\t")
	try:
			print(cntr, status.user.screen_name, status.user.location.encode("utf-8"), status.text.encode("utf-8"), status.created_at, status.favorite_count, status.retweeted, status.in_reply_to_user_id,  status.entities['urls'], status.entities['hashtags'], file=f, sep="\t")
	except:
		continue
#
f.close()
