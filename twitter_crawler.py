#!/usr/bin/env python

# Twitter Crawler to Get Information

# Import Modules
# ============================================================================*
import time
import json
import tweepy
from tweepy import OAuthHandler, Stream, Cursor

# Twitter Info for Authenication
# ============================================================================*
CONSUMER_KEY = 'WTVkon00o5Cw6GM7zRkVR35JK'
CONSUMER_SECRET = '9tFDBYEYq0dAWU2eIc6PNQ138U2FX5fyMteWP557fJVz1nkZps'
ACCESS_TOKEN = '1317444872-ab3pwAHwfB3WKtXnL1XSKLlmm29vQm085tPrANW'
ACCESS_TOKEN_SECRET = 'SFT0uVZWeFFdhhYeVaCgDbNV26H9M1jKHelE0P8tQ32wF'

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
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
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

def get_tweets_company(api, company):
	dates = ["2017-04-15", "2017-04-16", "2017-04-17", "2017-04-18", "2017-04-19", "2017-04-20", "2017-04-21", "2017-04-22", "2017-04-23", "2017-04-24", "2017-04-25", "2017-04-26"]
	
	company_file = company.replace(" ", "")


	for date in dates:
		tweets = []
		json_file = company_file + '_' + date + '_tweets.json'
		with open(json_file, 'w') as file:
			next_date = dates.index(date)+1
			if next_date < len(dates):
				cursor = tweepy.Cursor(api.search, q=company, count=100, since=date, until=dates[next_date], lang="en").items()
				while True:
					try:
						tweet = cursor.next()._json
						#print '-' * 30
						#tweet = tweet._json
						#tweets[tweet.id] = tweet.text.encode("utf-8")
						tweets.append(tweet)
					except tweepy.TweepError as e:
						print('waiting on rate limit...')
						time.sleep(60*15)
						#print('waiting on rate limit...\t10 minutes to go')
						#time.sleep(60*5)
						#print('waiting on rate limit...\t 5 minutes to go')
						#time.sleep(60*5)
						print('continuing...')
						continue
					except StopIteration:
						break
			json.dump(tweets, file)


# Main
# ============================================================================*
if __name__ == '__main__':
	api = authenticate();
	
	get_tweets_company(api, "lululemon")
	get_tweets_company(api, "urban outfitters")
	get_tweets_company(api, "burberry")




