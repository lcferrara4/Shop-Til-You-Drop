#!/usr/bin/env python

# Sentiment Analysis for Data Sets

# Import Modules
# ============================================================================*
import time
import json
import os
import requests

# Files
# ============================================================================*
LULULEMON_TWEETS_FILE = 'lululemon_tweets.json'
URBAN_OUTFITTERS_TWEETS_FILE = 'urbanoutfitters_tweets.json'
BURBERRY_TWEETS_FILE = 'burberry_tweets.json'

# Functions
# ============================================================================*
def get_analysis(filename):

        content = ""

        tot_comp = 0
        num_tweets = 0
 
        with open(filename) as file:    
            tweets = json.load(file)
            for tweet in tweets:
    
                if len(content + tweet['text'] ) > 1500 or len((content + tweet['text']).split(' ')) > 100:
                    try:
                        r = requests.post("https://twinword-sentiment-analysis.p.mashape.com/analyze/", headers={"X-Mashape-Key": "A8rCDjzh31mshG7mYQ8lKb1GMuUZp1XxR2qjsnKZiutvdaK5tm", "Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}, params={ "text": content})
                        results = r.json()
                        tot_comp += results['score']
                        print(results['score'])
                        num_tweets += 1
                    except Exception as e:
                        print(e)
                    content = tweet['text']
                else:
                    content += tweet['text']

            if len(content) <= 1500 and len(content.split(' ')) <= 100:
                try:
                    r = requests.post("https://twinword-sentiment-analysis.p.mashape.com/analyze/", headers={"X-Mashape-Key": "A8rCDjzh31mshG7mYQ8lKb1GMuUZp1XxR2qjsnKZiutvdaK5tm", "Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}, params={ "text": content})
                    results = r.json()
                    tot_comp += results['score']
                    print(results['score'])
                    num_tweets += 1
                except Exception as e:
                    print(e)

            company = filename.split('/')[2].split("_")[0]
            data_file = "./sentiment_data/twinword2/" + company + ".csv"
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
        data_dir = "./sentiment_data/"
        for subdir, dirs, files in os.walk("./twitter_data"):
            #for s in dirs:
            #    open(data_dir + s, "w+")
            for f in files:
                get_analysis(os.path.join(subdir, f))
                #get_analysis(analyzer, URBAN_OUTFITTERS_TWEETS_FILE)
                #get_analysis(analyzer, BURBERRY_TWEETS_FILE)
