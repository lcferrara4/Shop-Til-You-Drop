#!/usr/bin/env python

# Sentiment Analysis for Data Sets

# Import Modules
# ============================================================================*
import time
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Files
# ============================================================================*
LULULEMON_TWEETS_FILE = 'lululemon_tweets.json'
URBAN_OUTFITTERS_TWEETS_FILE = 'urbanoutfitters_tweets.json'
BURBERRY_TWEETS_FILE = 'burberry_tweets.json'

# Functions
# ============================================================================*


# Main
# ============================================================================*
if __name__ == '__main__':
	analyzer = SentimentIntensityAnalyzer()

	with open(LULULEMON_TWEETS_FILE) as file:    
		lulu_tweets = json.load(file)

	for ID in lulu_tweets:
		vs = analyzer.polarity_scores(lulu_tweets[ID])
		print("{:-<65} {}".format(lulu_tweets[ID], str(vs)))
