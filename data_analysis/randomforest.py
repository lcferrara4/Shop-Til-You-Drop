# Written by Lauren Ferrara

# Create Random Forest Models to predict company stock with given lags

# Import Modules
# ============================================================================
import pandas as pd
import numpy as np
import sklearn as sklearn
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.cross_validation import cross_val_score, ShuffleSplit
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

# Set dates for prediction
dates = ['3/17/17','3/18/17','3/19/17','3/20/17','3/21/17',
        '3/22/17','3/23/17','3/24/17','3/25/17','3/26/17',
        '3/27/17','3/28/17','3/29/17','3/31/17','4/1/17',
        '4/2/17','4/3/17','4/4/17','4/5/17','4/6/17', 
        '4/7/17','4/8/17', '4/9/17', '4/10/17', '4/11/17', 
        '4/12/17','4/13/17', '4/14/17', '4/17/17']

# Create Pandas DataFrames from Features and Stock Lags
brby_data = pd.read_csv('../sentiment_data/BurberrySentiment.csv')
lulu_data = pd.read_csv('../sentiment_data/LuluSentiment.csv')
urbn_data = pd.read_csv('../sentiment_data/UrbanSentiment.csv')

# Set all possible features
predictors = ['NumTweets', 'VaderComp', 'VaderPos', 'VaderNeg', 'VaderNeu', 'ImpactVader', 'FollowVader', 'TB', 'ImpactTB', 'FollowTB', 'Twinword']

# Burberry
# ============================================================================
df_train = brby_data[1:22]
df_test = brby_data[1:30]

# Set Y to stock data with lag of 14 days
y = df_train['Lag14']
Y_test = df_test['Lag14']

# Set X to all possible predictors
X = df_train[predictors]
X_test = df_test[predictors]

# Fit Random Forest Regressor
rf = RandomForestRegressor(n_estimators=20)
rf.fit(X,y)
           
# Plot importance of features
plt.bar(range(len(predictors)), rf.feature_importances_)
plt.xticks(range(len(predictors)), predictors, rotation='vertical')
plt.show()

# Plot prediction against actual
fig = plt.figure()
Y_predict = rf.predict(X_test)
dates = [pd.to_datetime(d) for d in dates]
plt.plot(dates, Y_predict, 'r--', dates, Y_test, 'bs')
plt.title("Burberry RF Results")
plt.show()

# Calculate mean squares error and r^2 for model comparison
mse = mean_squared_error(Y_test, Y_predict)
print('mse: ', mse)
print('rsquared: ', rf.score(X_test, Y_test))
   
# Lulu
# ============================================================================
df_train = lulu_data[1:22]
df_test = lulu_data[1:34]

# Set Y to stock data with lag of 10 days
y = df_train['Lag10']
Y_test = df_test['Lag10']

# Set X to all possible features
X = df_train[predictors]
X_test = df_test[predictors]

# Fit Random Forest Regressor
rf = RandomForestRegressor(n_estimators=20)
rf.fit(X,y)
             
# Plot importance of features
plt.bar(range(len(predictors)), rf.feature_importances_)
plt.xticks(range(len(predictors)), predictors, rotation='vertical')
plt.show()

# Predict and plot against actual
fig = plt.figure()
Y_predict = rf.predict(X_test)

# add dates (error in data collection made BRBY set smaller)
dates2 = dates
dates = ['3/15/17','3/16/17']
dates.extend(dates2)
dates.extend(['4/18/17', '4/19/17'])
dates = [pd.to_datetime(d) for d in dates]

plt.plot(dates, Y_predict, 'r--', dates, Y_test, 'bs')
plt.title("LuluLemon RF Results")
plt.show()

# Calculate mean squares error and r^2 for model comparison
mse = mean_squared_error(Y_test, Y_predict)
print('mse: ', mse)
print('rsquared: ', rf.score(X_test, Y_test))

 # Urban
# ============================================================================
df_train = urbn_data[1:22]
df_test = urbn_data[1:34]

# Set Y to stock data with lag of 4 days
y = df_train['Lag4']
Y_test = df_test['Lag4']

# Set X to all possible features
X = df_train[predictors]
X_test = df_test[predictors]

# Fit Random Forest Regressor
rf = RandomForestRegressor(n_estimators=20)
rf.fit(X,y)
             
# Plot importance of features
plt.bar(range(len(predictors)), rf.feature_importances_)
plt.xticks(range(len(predictors)), predictors, rotation='vertical')
plt.show()

# Predict and plot against actual
fig = plt.figure()
Y_predict = rf.predict(X_test)
dates = [pd.to_datetime(d) for d in dates]
plt.plot(dates, Y_predict, 'r--', dates, Y_test, 'bs')
plt.title("Urban Outfitters RF Results")
plt.show()

# Calculate mean squares error and r^2 for model comparison
mse = mean_squared_error(Y_test, Y_predict)
print('mse: ', mse)
print('rsquared: ', rf.score(X_test, Y_test))
