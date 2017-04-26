import pandas as pd
import numpy as np
import sklearn as sklearn
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.datasets import load_iris

from sklearn.feature_selection import SelectFromModel

def selectKImportance(model, X, k=5):
         return X[:,model.feature_importances_.argsort()[::-1][:k]]

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
#print("Urban:")
with pd.option_context('display.max_rows', 30, 'display.max_columns', 999):
    print(df_urbn.corr())

df_urbn = df_urbn[13:21]
X = df_urbn[['TB', 'VaderNeg']]
y = df_urbn['lag_13']

# fit OLS model
X = sm.add_constant(X)
est = sm.OLS(y,X,missing = 'drop').fit()
print(est.summary())

predictors = ['NumTweets', 'VaderComp', 'VaderPos', 'VaderNeg', 'VaderNeu', 'TB','ImpactVader', 'FollowVader', 'TW', 'TWPub']
X = df_urbn[predictors]

iris = load_iris()
X, y = iris.data, iris.target
forest = ExtraTreesClassifier()
forest = forest.fit(X,y)
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
                     axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")
'''
for f in range(X.shape[1]):
        print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

        # Plot the feature importances of the forest
        plt.figure()
        plt.title("Feature importances")
        plt.bar(range(X.shape[1]), importances[indices],
                       color="r", yerr=std[indices], align="center")
        plt.xticks(range(X.shape[1]), indices)
        plt.xlim([-1, X.shape[1]])
        plt.show()
'''
newX = selectKImportance(forest,X,2)
print(newX)
#print(X)
#model = SelectFromModel(clf, prefit=True)
#X_new = model.transform(X)
#print(X_new)
