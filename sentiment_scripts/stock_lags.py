# Written by Lauren Ferrara
# Exports historical closing stock prices from Yahoo Finance
# to csv file for given companies over given time frame

import pandas as pd
from datetime import datetime, timedelta

OLD_FILES= ['../stock_data/lulu.csv', '../stock_data/urbn.csv', '../stock_data/brby.csv']
NEW_FILES = ['../stock_data/lululemon.csv', '../stock_data/urbanoutfitters.csv', '../stock_data/burberry.csv']

START_LAG = 0
END_LAG = 21

def get_lags(old_filename, new_filename, start_lag, end_lag):
    df = pd.read_csv(old_filename, index_col=0, header=None)
    df.index.name = 'Date'
    df.columns = ["Stock"]
    df.to_csv(new_filename)


def main():
    for i in range(0, 3):
        get_lags(OLD_FILES[i], NEW_FILES[i], START_LAG, END_LAG)
