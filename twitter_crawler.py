#!/usr/bin/env python

# Written by Reilly Kearney and Lauren Ferrara

# Twitter Crawler to Get Information

# Import Modules
# ============================================================================*
import time
import json
import tweepy
from tweepy import OAuthHandler, Stream, Cursor

# Twitter Info for Authenication
# ============================================================================*
f = open("../twitter_credentials.txt", "r")
credentials = f.readlines()

CONSUMER_KEY = credentials[0].rstrip('\n')
CONSUMER_SECRET = credentials[1].rstrip('\n')
ACCESS_TOKEN = credentials[2].rstrip('\n')
ACCESS_TOKEN_SECRET = credentials[3].rstrip('\n')

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
	dates = ["2017-05-20",  "2017-05-21", "2017-05-22", "2017-05-23",
	        "2017-05-24", "2017-05-25", "2017-05-26", "2017-05-27", "2017-05-28"]     
	
	company_file = company.replace(" ", "")


	for date in dates:
		tweets = []
		json_file = './twitter_data/' + company_file + "_data/" +company_file + '_' + date + '_tweets.json'
		with open(json_file, 'w') as file:
			next_date = dates.index(date)+1
			if next_date < len(dates):
				cursor = tweepy.Cursor(api.search, q=company, count=100, since=date, until=dates[next_date], lang="en").items()
				while True:
					try:
						tweet = cursor.next()._json
						tweets.append(tweet)
					except tweepy.TweepError as e:
                                                print(e)
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
	
	#get_tweets_company(api, "lululemon")
	#get_tweets_company(api, "urban outfitters")
	get_tweets_company(api, "burberry")
