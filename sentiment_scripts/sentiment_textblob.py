#!/usr/bin/env python

# Sentiment Analysis for Data Sets

# Import Modules
# ============================================================================*
import time
import json
import os
from textblob import TextBlob

# Functions
# ============================================================================*
def get_analysis(filename):

        tot_comp = 0
        num_tweets = 0
 
        with open(filename) as file:    
            tweets = json.load(file)
            for tweet in tweets:
                sentiment_pa = TextBlob(tweet['text']) # Pattern Analyzer by default
                tot_comp += sentiment_pa.sentiment.polarity
                num_tweets += 1

            print(num_tweets)
            company = filename.split('/')[2].split("_")[0]
            data_file = "../sentiment_data/textblob/" + company + ".csv"
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
        for subdir, dirs, files in os.walk("../twitter_data"):
            for f in files:
                get_analysis(os.path.join(subdir, f))
