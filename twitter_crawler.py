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
	dates = ["2017-03-13", "2017-03-14", "2017-03-15", "2017-03-16", "2017-03-17", "2017-03-18", "2017-03-19", "2017-03-20"]
	tweets = {}
	for date in dates:
		next_date = dates.index(date)+1
		if next_date < len(dates):
			cursor = tweepy.Cursor(api.search, q=company, count=100, since=date, until=dates[next_date], lang="en").items()
			while True:
				try:
					tweet = cursor.next()
					tweets[tweet.id] = tweet.text.encode("utf-8")
				except tweepy.TweepError as e:
					time.sleep(60*15)
					print('waiting on rate limit...')
					continue
				except StopIteration:
					break
			#for tweet in cursor:
				#tweets[tweet.id] = tweet.text.encode("utf-8")
				#print '-' * 30
				#print(tweet.text)

	company = company.replace(" ", "")
	json_file = company + '_tweets.json'
	text_file = company + '_tweets.txt'

	with open(json_file, 'w') as f:
		json.dump(tweets, f)

	with open(text_file, "w") as f:
		for tweet in tweets:
			f.write(str(tweet) + ':\t' + tweets[tweet])


# Main
# ============================================================================*
if __name__ == '__main__':
	api = authenticate();
	
	get_tweets_company(api, "lululemon")
	get_tweets_company(api, "urban outfitters")
	get_tweets_company(api, "burberry")




