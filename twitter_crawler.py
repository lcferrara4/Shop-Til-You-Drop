#!/usr/bin/env python

# Written by Reilly Kearney

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
		print('-' * 30)
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
	except tweepy.TweepError as e:
		print('error: authenticate')

	return api

def get_tweets_company(api, company):
	dates = ["2017-04-27", "2017-04-28", "2017-04-29", "2017-04-30", "2017-05-01", "2017-05-02", 
                "2017-05-03", "2017-05-04"]
	
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
						tweets.append(tweet)
					except tweepy.TweepError as e:
						print('waiting on rate limit...')
						time.sleep(60*15)
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
