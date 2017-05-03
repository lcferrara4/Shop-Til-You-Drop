#!/usr/bin/env python

# Sentiment Analysis for Data Sets

# Import Modules
# ============================================================================*
import time
import json
import os
import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Functions
# ============================================================================*
def get_analysis(analyzer, filename):

        tot_pos = 0
        tot_neg = 0
        tot_comp = 0
        tot_neutral = 0
        num_tweets = 0
 
        with open(filename) as file:    
            tweets = json.load(file)
            for tweet in tweets:
                vs = analyzer.polarity_scores(tweet['text'])
                try:
                    tot_comp += vs['compound'] * tweet['user']['followers_count']
                    num_tweets += 1
                except Exception as e:
                    print(e)

            company = filename.split('/')[2].split("_")[0]
            data_file = "../sentiment_data/followers/" + company + ".csv"
            f = open(data_file, "a+")
            date = filename.split('/')[3].split("_")[1]
            if num_tweets != 0:
                f.write(date + ',' + str(num_tweets) + ',' + str(tot_comp/num_tweets) + '\n')
            else:
                f.write(date + ',' + str(num_tweets) + ',0\n')
            f.close()

# Main
# ============================================================================*
if __name__ == '__main__':
        analyzer = SentimentIntensityAnalyzer()
        for subdir, dirs, files in os.walk("../twitter_data"):
            for f in files:
                get_analysis(analyzer, os.path.join(subdir, f))
