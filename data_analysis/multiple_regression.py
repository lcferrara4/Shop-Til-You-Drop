import pandas as pd
import numpy as np
import sklearn as sklearn
import statsmodels.api as sm
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from statsmodels.formula.api import ols
from sklearn.feature_selection import SelectKBest, f_regression, chi2
from statsmodels.sandbox.regression.predstd import wls_prediction_std

# create dataframes
brby_data = pd.read_csv('../sentiment_data/BurberrySentiment.csv')
lulu_data = pd.read_csv('../sentiment_data/LuluSentiment.csv')
urbn_data = pd.read_csv('../sentiment_data/UrbanSentiment.csv')
  
predictors = ['NumTweets', 'VaderComp', 'VaderPos', 'VaderNeg', 'VaderNeu', 'ImpactVader', 'FollowVader', 'TB', 'ImpactTB', 'FollowTB', 'Twinword']
Y = ['Stock']
for i in range(1,22):
	Y.append('Lag'+str(i))

# Burberry
N = len(brby_data.index)
df_train = brby_data[1:21]
df_test = brby_data[1:30]
X = df_train[predictors]
y = df_train['Lag14']
X_test = df_test[predictors]
Y_test = df_test['Lag14']

result = sklearn.feature_selection.f_regression(X, y, center=True)
scores = result[0]
pvalues = result[1]
plt.bar(range(len(predictors)), scores)
plt.xticks(range(len(predictors)), predictors, rotation='vertical')
plt.show()

# Lulu
N = len(lulu_data.index)
df_train = lulu_data[1:21]
df_test = lulu_data[1:34]
X = df_train[predictors]
y = df_train['Lag10']
X_test = df_test[predictors]
Y_test = df_test['Lag10']

result = sklearn.feature_selection.f_regression(X, y, center=True)
scores = result[0]
pvalues = result[1]
plt.bar(range(len(predictors)), scores)
plt.xticks(range(len(predictors)), predictors, rotation='vertical')
plt.show()


# Urban
N = len(urbn_data.index)
df_train = urbn_data[1:21]
df_test = urbn_data[1:34]
X = df_train[predictors]
y = df_train['Lag4']
X_test = df_test[predictors]
Y_test = df_test['Lag4']

result = sklearn.feature_selection.f_regression(X, y, center=True)
scores = result[0]
pvalues = result[1]
plt.bar(range(len(predictors)), scores)
plt.xticks(range(len(predictors)), predictors, rotation='vertical')
plt.show()

