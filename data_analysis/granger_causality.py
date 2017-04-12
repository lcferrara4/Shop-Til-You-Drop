import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Make csv into list
def csv_to_list(filename, column):
    column_data = []
    with open(filename, 'r') as f:
        for line in f:
            column_data.append(line.split(",")[column])
    return column_data

# create a vector
vector_vader = np.array(csv_to_list('../sentiment_data/burberry_data.csv', 2), dtype=float)
vector_stocks = np.array(csv_to_list('../stock_data/brby.csv', 1), dtype=float)

a = np.zeros(shape=(len(vector_vader),2))
a[:,0] = vector_stocks
a[:,1] = vector_vader
sm.tsa.stattools.grangercausalitytests(a, 3, True)


vector_twinword = np.array(csv_to_list('../sentiment_data/burberry_twinword_data.csv', 2), dtype=float)
a[:,1] = vector_twinword
sm.tsa.stattools.grangercausalitytests(a, 3, True)


vector_ntweets = np.array(csv_to_list('../sentiment_data/burberry_data.csv', 1), dtype=float)
a[:,1] = vector_ntweets
sm.tsa.stattools.grangercausalitytests(a, 3, True)

brby_data = np.genfromtxt('../sentiment_data/main/burberry_sentiment.csv', delimiter=',')
lulu_data = np.genfromtxt('../sentiment_data/main/lulu_sentiment.csv', delimiter=',')
urbn_data = np.genfromtxt('../sentiment_data/main/urban_sentiment.csv', delimiter=',')

fig.xcorr(lulu_data[:,0], lulu_data[:,6], usevlines=True)
