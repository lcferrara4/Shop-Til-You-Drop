# Written by Lauren Ferrara

# TextBlob Sentiment Analysis * Number of Followers
# for Tweets in Company Twitter Data Sets

# Import Modules
# ============================================================================*
import time
import json
import os
from textblob import TextBlob

# Functions
# ============================================================================*
def get_analysis(filename):

        score = 0
        num_tweets = 0
 
        with open(filename) as file:    
            tweets = json.load(file)

            # Gets TextBlob score * follower count for each tweet
            for tweet in tweets:
                sentiment = TextBlob(tweet['text']).sentiment.polarity
                try:
                    score += sentiment * tweet['user']['followers_count']
                    num_tweets += 1
                except Exception as e:
                    print(e)

            # Identifies company for csv file name
            company = filename.split('/')[2].split("_")[0]
            data_file = "../../sentiment_data/textblob_followers/" + company + ".csv"
            f = open(data_file, "a+")
            date = filename.split('/')[3].split("_")[1]

            # Writes TextBlob*Follower scores to file
            if num_tweets != 0:
                f.write(date + ',' + str(num_tweets) + ',' + str(score/num_tweets) + '\n')
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
