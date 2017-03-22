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
def get_analysis(analyzer, filename):
        with open(filename) as file:    
                tweets = json.load(file)

        tot_pos = 0
        tot_neg = 0
        tot_comp = 0
        tot_neutral = 0
        num_tweets = 0

        for ID in tweets:
                #if tweets['date']
                vs = analyzer.polarity_scores(tweets[ID])
                tot_pos += vs['pos']
                tot_neg += vs['neg']
                tot_comp += vs['compound']
                tot_neutral += vs['neu']
                num_tweets += 1

        print(filename,':')
        print('-------------------------------')
        print('Number of tweets: ', num_tweets)
        print('Average compound: ', tot_comp/num_tweets)
        print('Average positive: ', tot_pos/num_tweets)
        print('Average negative: ', tot_neg/num_tweets)
        print('Average neutral: ', tot_neutral/num_tweets)

# Main
# ============================================================================*
if __name__ == '__main__':
        analyzer = SentimentIntensityAnalyzer()
        get_analysis(analyzer, LULULEMON_TWEETS_FILE)
        get_analysis(analyzer, URBAN_OUTFITTERS_TWEETS_FILE)
        get_analysis(analyzer, BURBERRY_TWEETS_FILE)
