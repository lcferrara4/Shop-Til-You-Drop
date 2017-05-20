# Written by Lauren Ferrara
# Exports historical closing stock prices from Yahoo Finance
# to csv file for given companies over given time frame

from datetime import datetime, timedelta
from yahoo_finance import Share
import yahoo_finance

SYMBOLS = ['LULU', 'URBN', 'BRBY.L']
FILE_NAMES = ['../stock_data/lulu.csv', '../stock_data/urbn.csv', '../stock_data/brby.csv']

# Calls Yahoo Finance API to get data
def export_historical_close(filename, curr_share, start_date, end_date):
    with open(filename, 'w') as f:
        historical_list = curr_share.get_historical(start_date, end_date)
        for day in reversed(historical_list):
            f.write(day['Date'] + ',' + day['Close'] + '\n')
    f.close()

def main(start_date, end_date):
    for i in range(0, 3):
        stock = Share(SYMBOLS[i]) # share data for given stock
        export_historical_close(FILE_NAMES[i], stock, start_date, end_date)
