import pandas as pd

# create a vector
brby_data = pd.read_csv('../sentiment_data/BurberrySentiment.csv')
lulu_data = pd.read_csv('../sentiment_data/LuluSentiment.csv')
urbn_data = pd.read_csv('../sentiment_data/UrbanSentiment.csv')

X = ['NumTweets', 'VaderComp', 'VaderPos', 'VaderNeg', 'VaderNeu', 'ImpactVader', 'FollowVader', 'TB', 'ImpactTB', 'FollowTB', 'Twinword']
Y = ['Stock']
for i in range(1,22):
    Y.append('Lag'+str(i))

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
