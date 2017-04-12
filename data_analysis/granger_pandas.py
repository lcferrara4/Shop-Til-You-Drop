import pandas as pd
import statsmodels.api as sm
import numpy as np

def buildLaggedFeatures(s,lag=2,dropna=True):
    '''
    Builds a new DataFrame to facilitate regressing over all possible lagged features
    '''
    if type(s) is pd.DataFrame:
        new_dict={}
        for col_name in s:
            new_dict[col_name]=s[col_name]
            # create lagged Series
            for l in range(1,lag+1):
                new_dict['%s_lag%d' %(col_name,l)]=s[col_name].shift(l)
        res=pd.DataFrame(new_dict,index=s.index)
    elif type(s) is pd.Series:
        the_range=range(lag+1)
        res=pd.concat([s.shift(i) for i in the_range],axis=1)
        res.columns=['lag_%d' %i for i in the_range]
    else:
        print('Only works for DataFrame or Series')
        return None
    if dropna:
        return res.dropna()
    else:
        return res

# create a vector
brby_data = np.genfromtxt('../sentiment_data/main/burberry_sentiment.csv', delimiter=',')
lulu_data = np.genfromtxt('../sentiment_data/main/lulu_sentiment.csv', delimiter=',')
urbn_data = np.genfromtxt('../sentiment_data/main/urban_sentiment.csv', delimiter=',')


# Burberry
N = len(brby_data[:,6])
s=pd.DataFrame(brby_data[:,6], index = list(range(0,N))).astype(float)
res=buildLaggedFeatures(s,lag=15,dropna=False).astype(float)
df = pd.DataFrame(brby_data, columns=list('ABCDEFGHIJK'), index=list(range(0,N))).astype(float)
df = df.join(res)
print("Burberry:")
with pd.option_context('display.max_rows', 30, 'display.max_columns', 999):
    print(df.corr())
'''
# Lulu
N = len(lulu_data[:,6])
s=pd.DataFrame(lulu_data[:,6], index = list(range(0,N))).astype(float)
res=buildLaggedFeatures(s,lag=15,dropna=False).astype(float)
df = pd.DataFrame(lulu_data, columns=list('ABCDEFGHIJK'), index=list(range(0,N))).astype(float)
df = df.join(res)
print("LuLu:")
with pd.option_context('display.max_rows', 30, 'display.max_columns', 999):
    print(df.corr())

# Urbn
N = len(urbn_data[:,6])
s=pd.DataFrame(urbn_data[:,6], index = list(range(0,N))).astype(float)
res=buildLaggedFeatures(s,lag=15,dropna=False).astype(float)
df = pd.DataFrame(urbn_data, columns=list('ABCDEFGHIJK'), index=list(range(0,N))).astype(float)
df = df.join(res)
print("Urban:")
with pd.option_context('display.max_rows', 30, 'display.max_columns', 999):
    print(df.corr())
'''
# Granger Causality on Lagged data
x = df['0_lag5']
x = x[~np.isnan(x)]
y = df[N-len(x):N]['B']
y = y[~np.isnan(y)]
x = x[0:len(y)]
a_granger = np.zeros(shape=(len(x),2))
a_granger[:,0] = x
a_granger[:,1] = y
print(a_granger)
sm.tsa.stattools.grangercausalitytests(a_granger, 4, True)
  
