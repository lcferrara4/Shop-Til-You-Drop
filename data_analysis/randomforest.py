import pandas as pd
import numpy as np
import sklearn as sklearn
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.cross_validation import cross_val_score, ShuffleSplit
from sklearn.metrics import r2_score

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
#brby_data = np.genfromtxt('../sentiment_data/main/burberry_sentiment.csv', delimiter=',')
#lulu_data = np.genfromtxt('../sentiment_data/main/lulu_sentiment.csv', delimiter=',')
#urbn_data = np.genfromtxt('../sentiment_data/main/urban_sentiment.csv', delimiter=',')
df_urbn = pd.read_csv('urbn2.csv')
'''

# Burberry
N = len(brby_data[:,6])
s=pd.DataFrame(brby_data[:,6], index = list(range(0,N))).astype(float)
res=buildLaggedFeatures(s,lag=10,dropna=False).astype(float)
df = pd.DataFrame(brby_data, columns=list('ABCDEFGHIJK'), index=list(range(0,N))).astype(float)
df = df.join(res)
print("Burberry:")
with pd.option_context('display.max_rows', 30, 'display.max_columns', 999):
    print(df.corr())

# Lulu
N = len(lulu_data[:,6])
s=pd.DataFrame(lulu_data[:,6], index = list(range(0,N))).astype(float)
res=buildLaggedFeatures(s,lag=15,dropna=False).astype(float)
df = pd.DataFrame(lulu_data, columns=list('ABCDEFGHIJK'), index=list(range(0,N))).astype(float)
df = df.join(res)
print("LuLu:")
with pd.option_context('display.max_rows', 30, 'display.max_columns', 999):
    print(df.corr())

'''
# Urbn
N = len(df_urbn.index)
#s=pd.DataFrame(df_urbn["Stocks"], index = list(range(0,N))).astype(float)
s = df_urbn["Stock"].copy()
res=buildLaggedFeatures(s,lag=15,dropna=False)
#df = pd.DataFrame(df_urbn, columns=list('ABCDEFGHIJK'), index=list(range(0,N))).astype(float)
df_urbn = df_urbn.join(res)

#df_urbn = df_urbn[13:21]
df_train = df_urbn[13:17]
df_test = df_urbn[18:21]
df_urbn = df_train
X = df_urbn[['TB', 'VaderComp', 'VaderNeg']]
y = df_urbn['lag_13']

predictors = ['NumTweets', 'VaderComp', 'VaderPos', 'VaderNeg', 'VaderNeu', 'TB','ImpactVader', 'FollowVader', 'TW', 'TWPub']
X = df_urbn[predictors]
X_test = df_test[predictors]
Y_test = df_test['lag_13']
err_down = []
err_up = []
percentile=95

rf = RandomForestRegressor(n_estimators=20)
rf.fit(X,y)

print(predictors)
print(rf.feature_importances_)

print(sorted(zip(map(lambda x: round(x, 6), rf.feature_importances_), predictors), 
                     reverse=True))

r2 = r2_score(Y_test, rf.predict(X_test)) # need to switch to train before and then test data here
mse = np.mean((Y_test - rf.predict(X_test)**2))
# 0.41566442422680094

plt.figure()

plt.scatter(Y_test, rf.predict(X_test))
#plt.plot(np.arange(8, 15), np.arange(8, 15), label="r^2=" + str(r2), c="r")
plt.title("RandomForest Regression with scikit-learn")
plt.show()

'''
for x in range(size):
    preds = []
    for pred in rf.estimators_:
        preds.append(pred.predict(X[x+1])['TB'])
    err_down.append(np.percentile(preds, (100 - percentile) / 2. ))
    err_up.append(np.percentile(preds, 100 - (100 - percentile) / 2.))

print(preds)
correct = 0.
for i, val in enumerate(y):
    if err_down[i] <= val <= err_up[i]:
        correct += 1

print(correct/len(y))


for pred in rf.estimators_:
    print((pred.predict(X))[5])
'''
