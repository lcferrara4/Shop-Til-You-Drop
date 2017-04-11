#!/usr/bin/env python

# Sentiment Analysis for Data Sets

# Import Modules
# ============================================================================*
import time
import json
import os
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

# Files
# ============================================================================*
LULULEMON_TWEETS_FILE = 'lululemon_tweets.json'
URBAN_OUTFITTERS_TWEETS_FILE = 'urbanoutfitters_tweets.json'
BURBERRY_TWEETS_FILE = 'burberry_tweets.json'

# Functions
# ============================================================================*
def get_analysis(filename):

        tot_pos = 0
        tot_neg = 0
        num_tweets = 0
 
        with open(filename) as file:    
            tweets = json.load(file)
            for tweet in tweets:
                #if tweets['date']
                sentiment_nb = TextBlob(tweet['text'], analyzer=NaiveBayesAnalyzer()) # Naive Bayes override
                print(type(sentiment_nb.sentiment))
                tot_pos += sentiment_nb.sentiment.p_pos
                tot_neg += sentiment_nb.sentiment.p_neg
                num_tweets += 1

            print(num_tweets)
            company = filename.split('/')[2].split("_")[0]
            data_file = "./sentiment_data/textblob_nb/" + company + ".csv"
            f = open(data_file, "a+")
            date = filename.split('/')[3].split("_")[1]
            if num_tweets != 0:
                f.write(date + ',' + str(num_tweets) + ',' + str(tot_pos/num_tweets) + ',' + str(tot_neg/num_tweets) + '\n')
            else:
                f.write(date + ',' + str(num_tweets) + ',0,0\n')
            f.close()

# Main
# ============================================================================*
if __name__ == '__main__':
        data_dir = "./sentiment_data/"
        for subdir, dirs, files in os.walk("./twitter_data"):
            #for s in dirs:
            #    open(data_dir + s, "w+")
            for f in files:
                get_analysis(os.path.join(subdir, f))
                #get_analysis(analyzer, URBAN_OUTFITTERS_TWEETS_FILE)
                #get_analysis(analyzer, BURBERRY_TWEETS_FILE)