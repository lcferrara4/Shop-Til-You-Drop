# Written by Lauren Ferrara

# Determines correlation (r^2) values between Features and Stock Data with Lags
# Used for choosing optimal stock lag -> how far out we should predict
# and for choosing the features to include in regression model

import pandas as pd

# Create Pandas Data Frames based on Features and Stock Data/Lags
brby_data = pd.read_csv('../sentiment_data/BurberrySentiment.csv')
lulu_data = pd.read_csv('../sentiment_data/LuluSentiment.csv')
urbn_data = pd.read_csv('../sentiment_data/UrbanSentiment.csv')

# X is list of all possible features
X = ['NumTweets', 'VaderComp', 'VaderPos', 'VaderNeg', 'VaderNeu', 'ImpactVader', 'FollowVader', 'TB', 'ImpactTB', 'FollowTB', 'Twinword']

# Y is list of stock price and stock prices with different day lags
Y = ['Stock']
for i in range(1,22):
    Y.append('Lag'+str(i))

# Using Pandas corr function to find correlations between X and Y for all 3 companies
print("Burberry:")
corr_df = brby_data.corr()
with pd.option_context('display.max_rows', 30, 'display.max_columns', 999):
    print(corr_df.loc[X,Y])

print("\nLuLu:")
corr_df = lulu_data.corr()
with pd.option_context('display.max_rows', 30, 'display.max_columns', 999):
    print(corr_df.loc[X,Y])

print("\nUrban:")
corr_df = urbn_data.corr()
with pd.option_context('display.max_rows', 30, 'display.max_columns', 999):
    print(corr_df.loc[X,Y])
