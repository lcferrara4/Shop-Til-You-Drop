# Written by Lauren Ferrara

# Run this script to run all sentiment scripts
# and compile their results for a certain date range

import pandas as pd
import os
import vader_sentiment
import vader_follow
import vader_impact
import textblob_sentiment
import textblob_follow
import textblob_impact
import twinword_sentiment
import get_stock_data
import stock_lags
from datetime import datetime

START = datetime.strptime('2017-05-10', "%Y-%m-%d")
END = datetime.strptime('2017-05-10', "%Y-%m-%d")

# Get sentiment data
#vader_sentiment.main(START, END)
#vader_follow.main(START, END)
#vader_impact.main(START, END)
#textblob_sentiment.main(START, END)
#textblob_follow.main(START, END)
#textblob_impact.main(START, END)
#twinword_sentiment.main(START, END)
get_stock_data.main(START, END)
stock_lags.main()

brby_list = []
urbn_list = []
lulu_list = []

brby_df = pd.DataFrame()
urbn_df = pd.DataFrame()
lulu_df = pd.DataFrame()

for subdir, dirs, files in os.walk("../sentiment_data"):
    if subdir != "../sentiment_data":
        for f in files:
            path = os.path.join(subdir,f)
            df = pd.read_csv(path, index_col=0, header=None)
            df.columns = [subdir.split('/')[2] + str(col) for col in df.columns]
            if f == 'burberry.csv':
                brby_list.append(df)
            elif f == 'urbanoutfitters.csv':
                urbn_list.append(df)
            elif f == 'lululemon.csv':
                lulu_list.append(df)


for subdir, dirs, files in os.walk("../stock_data"):
    for f in files:
        path = os.path.join(subdir, f)
        if f == 'burberry.csv':
            df = pd.read_csv(path, index_col = 0, header = None)
            df.columns = ["Stock_" + str(i) for i in range(0, 22)]
            brby_list.append(df)
        elif f == 'urbanoutfitters.csv':
            df = pd.read_csv(path, index_col = 0, header = None)
            df.columns = ["Stock_" + str(i) for i in range(0, 22)]
            urbn_list.append(df)
        elif f == 'lululemon.csv':
            df = pd.read_csv(path, index_col = 0, header = None)
            df.columns = ["Stock_" + str(i) for i in range(0, 22)]
            lulu_list.append(df)

brby_df = pd.concat(brby_list,axis=1)
brby_df.index.name = 'Date'
urbn_df = pd.concat(brby_list,axis=1)
urbn_df.index.name = 'Date'
lulu_df = pd.concat(brby_list,axis=1)
lulu_df.index.name = 'Date'
    
brby_df.to_csv('BurberryData.csv')
urbn_df.to_csv('UrbanData.csv')
lulu_df.to_csv('LuluData.csv')
