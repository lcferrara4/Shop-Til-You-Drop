# Written by Reilly Kearney and Lauren Ferrara

# Vader Sentiment Analysis for Twitter Data Sets

# Import Modules
# ============================================================================*
import time
import json
import os
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

            # Gets cumulative vader scores for tweets on one day
            for tweet in tweets:
                vs = analyzer.polarity_scores(tweet['text'])
                tot_pos += vs['pos']
                tot_neg += vs['neg']
                tot_comp += vs['compound']
                tot_neutral += vs['neu']
                num_tweets += 1

            # Identifies company for csv file name
            company = filename.split('/')[2].split("_")[0]
            data_file = "../../sentiment_data/" + company + ".csv"
            f = open(data_file, "a+")
            date = filename.split('/')[3].split("_")[1]

            # Writes vader analysis to file
            if num_tweets != 0:
                f.write(date + ',' + str(num_tweets) + ',' + str(tot_comp/num_tweets) + ',' 
                        + str(tot_pos/num_tweets) + ',' + str(tot_neg/num_tweets) + ',' 
                        + str(tot_neutral/num_tweets) + '\n')
            else:
                f.write(date + ',' + str(num_tweets) + ',0,0,0,0\n')
            f.close()

# Main
# ============================================================================*
if __name__ == '__main__':
        analyzer = SentimentIntensityAnalyzer()

        # Iterates through files in twitter data folder
        for subdir, dirs, files in os.walk("../../twitter_data"):
            for f in files:
                get_analysis(analyzer, os.path.join(subdir, f))
