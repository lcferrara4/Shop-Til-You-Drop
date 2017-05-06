# Written by Lauren Ferrara

# Alternate way to correlation matrices to choose features
# Did not end up using for final product

# Import Modules
# ============================================================================
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

# Create dataframes
brby_data = pd.read_csv('../sentiment_data/BurberrySentiment.csv')
lulu_data = pd.read_csv('../sentiment_data/LuluSentiment.csv')
urbn_data = pd.read_csv('../sentiment_data/UrbanSentiment.csv')
  
# Set all possible predictors
predictors = ['NumTweets', 'VaderComp', 'VaderPos', 'VaderNeg', 'VaderNeu', 'ImpactVader', 'FollowVader', 'TB', 'ImpactTB', 'FollowTB', 'Twinword']

# Burberry
# ============================================================================
df_train = brby_data[1:21]
df_test = brby_data[1:30]

# Set Y to Stocks with Lag 14
Y_test = df_test['Lag14']
y = df_train['Lag14']

# Set X to all possible Predictors
X = df_train[predictors]
X_test = df_test[predictors]

# Feature selection
result = sklearn.feature_selection.f_regression(X, y, center=True)
scores = result[0]
pvalues = result[1]

# Plot Scores
plt.bar(range(len(predictors)), scores)
plt.xticks(range(len(predictors)), predictors, rotation='vertical')
plt.show()

# Lulu
# ============================================================================
df_train = lulu_data[1:21]
df_test = lulu_data[1:34]

# Set Y to Stocks with Lag 10
y = df_train['Lag10']
Y_test = df_test['Lag10']

# Set X to all possible Predictors
X = df_train[predictors]
X_test = df_test[predictors]

# Feature selection
result = sklearn.feature_selection.f_regression(X, y, center=True)
scores = result[0]
pvalues = result[1]

# Plot Scores
plt.bar(range(len(predictors)), scores)
plt.xticks(range(len(predictors)), predictors, rotation='vertical')
plt.show()

# Urban
# ============================================================================
df_train = urbn_data[1:21]
df_test = urbn_data[1:34]

# Set Y to Stocks with Lag 10
y = df_train['Lag4']
Y_test = df_test['Lag4']

# Set X to all possible Predictors
X = df_train[predictors]
X_test = df_test[predictors]

# Feature selection
result = sklearn.feature_selection.f_regression(X, y, center=True)
scores = result[0]
pvalues = result[1]

# Plot Scores
plt.bar(range(len(predictors)), scores)
plt.xticks(range(len(predictors)), predictors, rotation='vertical')
plt.show()

