# Written by Lauren Ferrara

# Create Ordinary Least Squares (OLS) Regression models
# For company stock with given features and lags in stock prices

# Import Modules
# ============================================================================
import pandas as pd
import numpy as np
import sklearn as sklearn
import statsmodels.api as sm
import matplotlib.pyplot as plt
from math import sqrt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from statsmodels.formula.api import ols
from sklearn.feature_selection import SelectKBest, f_regression, chi2
from sklearn.metrics import mean_squared_error
from statsmodels.sandbox.regression.predstd import wls_prediction_std

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

# Burberry
# ============================================================================
df_train = brby_data[1:22]
df_test = brby_data[1:30]

# Set Y to stock data with lag of 14 days
y = df_train['Lag14']
Y_test = df_test['Lag14']

# Set X to the following features
features = ['VaderNeg', 'NumTweets', 'FollowVader', 'TB']
X = df_train[features]
X_test = df_test[features]

# Add y-intercept
X = sm.add_constant(X)
X_test = sm.add_constant(X_test)

# Fit the model
model = sm.OLS(y,X).fit()

# Print the summary
print(model.summary())

# Predict and plot against actual
Y_predict = model.predict(X_test)

dates = [pd.to_datetime(d) for d in dates]
plt.plot(dates, Y_predict, 'r--', dates, Y_test, 'bs')
plt.title("Burberry OLS Results")
plt.show()

# Find mean squared error to compare models later
mse = mean_squared_error(Y_test, Y_predict)
print('mse: ', mse)

# Lulu
# ============================================================================
df_train = lulu_data[1:22]
df_test = lulu_data[1:34]

# Set Y to stock data with lag of 10 days
y = df_train['Lag10']
Y_test = df_test['Lag10']

# Set X to the following features
features = ['FollowVader','ImpactTB', 'Twinword']
X = df_train[features]
X_test = df_test[features]

# Add y-intercept
X = sm.add_constant(X)
X_test = sm.add_constant(X_test)

# Fit the model
model = sm.OLS(y,X).fit()
print(model.summary())

# Predict and plot against actual
Y_predict = model.predict(X_test)
 
# add dates (error in data collection made BRBY set smaller)
dates2 = dates
dates = ['3/15/17','3/16/17']
dates.extend(dates2)
dates.extend(['4/18/17', '4/19/17'])
dates = [pd.to_datetime(d) for d in dates]

plt.plot(dates, Y_predict, 'r--', dates, Y_test, 'bs')
plt.title("LuluLemon OLS Results")
plt.show()

# Find mean squared error to compare models later
mse = mean_squared_error(Y_test, Y_predict)
print('mse: ', mse)

# Urban
# ============================================================================
df_train = urbn_data[1:22]
df_test = urbn_data[1:34]

# Set Y to stock data with lag of 4 days
y = df_train['Lag4']
Y_test = df_test['Lag4']

# Set X to the following features
features = ['VaderComp', 'TB', 'Twinword']
X = df_train[features]
X_test = df_test[features]

# Add y-intercept
X = sm.add_constant(X)
X_test = sm.add_constant(X_test)

# Fit the model
model = sm.OLS(y,X).fit()

# Print the summary
print(model.summary())

# Predict and plot against actual
Y_predict = model.predict(X_test)
  
dates = [pd.to_datetime(d) for d in dates]
plt.plot(dates, Y_predict, 'r--', dates, Y_test, 'bs')
plt.title("Urban Outfitters OLS Results")
plt.show()

# Find mean squared error to compare models later
mse = mean_squared_error(Y_test, Y_predict)
print('mse: ', mse)
