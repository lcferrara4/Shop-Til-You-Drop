# Written by Lauren Ferrara

# Twinword Sentiment Analysis for Twitter Data Sets

# Import Modules
# ============================================================================*
import time
import json
import os
import requests

# Functions
# ============================================================================*
def get_analysis(filename):

        content = ""

        tot_comp = 0
        num_tweets = 0
 
        with open(filename) as file:    
            tweets = json.load(file)

            for tweet in tweets:
                # Sections tweets into maximum length strings to limit HTTP request
                if len(content + tweet['text'] ) > 1500 or len((content + tweet['text']).split(' ')) > 100:
                    try:
                        # Sends request to twinword API
                        r = requests.post("https://twinword-sentiment-analysis.p.mashape.com/analyze/", headers={"X-Mashape-Key": "A8rCDjzh31mshG7mYQ8lKb1GMuUZp1XxR2qjsnKZiutvdaK5tm", "Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}, params={ "text": content})
                        results = r.json()
                        tot_comp += results['score']
                        num_tweets += 1
                    except Exception as e:
                        print(e)
                    content = tweet['text']
                else:
                    content += tweet['text']

            # Gets remainder of tweets for last HTTP request
            if len(content) <= 1500 and len(content.split(' ')) <= 100:
                try:
                    r = requests.post("https://twinword-sentiment-analysis.p.mashape.com/analyze/", headers={"X-Mashape-Key": "A8rCDjzh31mshG7mYQ8lKb1GMuUZp1XxR2qjsnKZiutvdaK5tm", "Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}, params={ "text": content})
                    results = r.json()
                    tot_comp += results['score']
                    print(results['score'])
                    num_tweets += 1
                except Exception as e:
                    print(e)

            # Identifies company for csv file name
            company = filename.split('/')[2].split("_")[0]
            data_file = "../../sentiment_data/twinword/" + company + ".csv"
            f = open(data_file, "a+")
            date = filename.split('/')[3].split("_")[1]

            # Writes twinword scores to file
            if num_tweets != 0:
                f.write(date + ',' + str(num_tweets) + ',' + str(tot_comp/num_tweets) + '\n')
            else:
                f.write(date + ',' + str(num_tweets) + ',0\n')
            f.close()

# Main
# ============================================================================*
if __name__ == '__main__':
        # Iterates through files in twitter data folder
        for subdir, dirs, files in os.walk("../../twitter_data"):
            for f in files:
                get_analysis(os.path.join(subdir, f))
