# Written by Lauren Ferrara

# Sentiment Scores for Twitter Data Sets based on
# Vader Compound * Number of retweets * Number of favorites

# Import Modules
# ============================================================================*
import time
import json
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Functions
# ============================================================================*
def get_analysis(analyzer, filename):

        tot_comp = 0
        num_tweets = 0
 
        with open(filename) as file:    
            tweets = json.load(file)

            # Gets vader compound score * retweets * favorites
            for tweet in tweets:
                vs = analyzer.polarity_scores(tweet['text'])
                tot_comp += vs['compound'] * (tweet['retweet_count'] + 1) * (tweet['favorite_count']+1)
                num_tweets += 1

            # Identifies company for csv file name
            company = filename.split('/')[2].split("_")[0]
            data_file = "../../sentiment_data/impact_eval/" + company + ".csv"
            f = open(data_file, "a+")
            date = filename.split('/')[3].split("_")[1]

            # Writes vader * rt * favorites score to file
            if num_tweets != 0:
                f.write(date + ',' + str(num_tweets) + ',' + str(tot_comp/num_tweets) + '\n')
            else:
                f.write(date + ',' + str(num_tweets) + ',0\n')
            f.close()

# Main
# ============================================================================*
if __name__ == '__main__':
        analyzer = SentimentIntensityAnalyzer()

        # Iterates through files in twitter data folder
        for subdir, dirs, files in os.walk("../../twitter_data"):
            for f in files:
                get_analysis(analyzer, os.path.join(subdir, f))
