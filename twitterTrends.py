"""
Twitter trending topics
"""

import sys
import os
import tweepy
from tweepy import OAuthHandler
import json


consumer_key= ''
consumer_secret= ''
access_token='-'
access_token_secret=''
#boilerplate 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



def get_trends(place, locationid):
	trendingTopic = api.trends_place(id=locationid)	
	
	for locations in trendingTopic:
		#print(json.dumps(locations))		#prints the entire py dict --> use this to confirm WOEID & location name
		for trend in locations["trends"]:
			print(place, trend["name"].encode("utf-8"), trend['tweet_volume'], trend['promoted_content'], sep="\t")

if __name__ == '__main__':
	
	print("Location	Trend	Tweet Volume	Promoted")
	#get_trends("Global", 1)
	#get_trends("India", 23424848)
	#get_trends("USA", 23424977)
	#get_trends("UK", 23424975)
	#get_trends("Mumbai", 2295411)
	get_trends("Bengaluru", 2295420)
	#get_trends("Chennai", 2295424)
	#get_trends("Kolkata", 2295386)
	#get_trends("Lucknow", 2295377)
	#get_trends("Pune", 2295412)
	#get_trends("Hyderabad", 2295414)
	
	
	#pass
	#get_trends("UK", 23424975)
	
