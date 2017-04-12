import numpy as np
from scipy.signal import correlate

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
'''
# perform cross-correlation for all data points
output = np.correlate(vector_vader, vector_stocks, "full")
max_value = np.amax(output)
max_index = np.argmax(output)
print(max_value)
print(max_index)
N = len(vector_stocks)
time = np.arange(1-N, N)
print(time[max_index])
print(np.corrcoef(vector_vader, vector_stocks))

vector_twinword = np.array(csv_to_list('../sentiment_data/burberry_twinword_data.csv', 1), dtype=float)
output = np.correlate(vector_twinword, vector_stocks, 'full')
max_value = np.amax(output)
max_index = np.argmax(output)
print(max_value)
print(max_index)
print(time[max_index])
print(np.corrcoef(vector_twinword, vector_stocks))
'''
brby_data = np.genfromtxt('../sentiment_data/main/burberry_sentiment.csv', delimiter=',')
lulu_data = np.genfromtxt('../sentiment_data/main/lulu_sentiment.csv', delimiter=',')
urbn_data = np.genfromtxt('../sentiment_data/main/urban_sentiment.csv', delimiter=',')


N = len(lulu_data[:,0])
time = np.arange(1-N, N)

print(lulu_data[:,0])
print(lulu_data[:,6])
output = np.correlate(lulu_data[:,0], lulu_data[:,6], 'full')
max_value = np.amax(output)
max_index = np.argmax(output)
print(output)
print(max_value)
print(max_index)
print(time[max_index])
print(np.corrcoef(lulu_data[:,0], lulu_data[:,6]))


