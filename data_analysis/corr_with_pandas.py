import numpy as np
import pandas as pd

# create a vector
brby_data = np.genfromtxt('../sentiment_data/main/burberry_sentiment.csv', delimiter=',')
lulu_data = np.genfromtxt('../sentiment_data/main/lulu_sentiment.csv', delimiter=',')
urbn_data = np.genfromtxt('../sentiment_data/main/urban_sentiment.csv', delimiter=',')

df = pd.DataFrame(brby_data, columns=list('ABCDEFGHIJK'))
print("Burberry:")
print(df.corr())

df = pd.DataFrame(lulu_data, columns=list('ABCDEFGHIJK'))
print("LuLu:")
print(df.corr())

df = pd.DataFrame(urbn_data, columns=list('ABCDEFGHIJK'))
print("Urban:")
print(df.corr())
