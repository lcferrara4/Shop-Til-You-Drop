#!/usr/bin/env python

# Twitter Crawler to Get Information

# Import Modules
# ============================================================================*
import time
import json
import tweepy
from tweepy import OAuthHandler, Stream

# Twitter Info for Authenication
# ============================================================================*
consumer_key = 'WTVkon00o5Cw6GM7zRkVR35JK'
consumer_secret = '9tFDBYEYq0dAWU2eIc6PNQ138U2FX5fyMteWP557fJVz1nkZps'
access_token = '1317444872-ab3pwAHwfB3WKtXnL1XSKLlmm29vQm085tPrANW'
access_token_secret = 'SFT0uVZWeFFdhhYeVaCgDbNV26H9M1jKHelE0P8tQ32wF'

# Stream Listener Class
# ============================================================================*
class StreamListener(tweepy.StreamListener):

	def on_status(self, status):
		print '-' * 30
		print(status.text)

	def on_error(self, status_code):
		if status_code == 420:
			#returning False in on_data disconnects the stream
			return False

# Functions
# ============================================================================*
def authenticate():
	try:
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		api = tweepy.API(auth)
	except tweepy.TweepError, e:
		print 'error: authenticate'

	return api

def get_tweet_keyword(api, keywords):
	stream_listener = StreamListener()
	stream = tweepy.Stream(auth = api.auth, listener=StreamListener())
	try: 
		stream.filter(track = keywords)
	except:
		print "error: get_tweet_keyword"
		stream.disconnect()

	keys = ['Lululemon', 'Urban Outfitters' ,'Burberry']
	get_tweet_keyword(api, keys)

# Main
# ============================================================================*
if __name__ == '__main__':
	api = authenticate();


