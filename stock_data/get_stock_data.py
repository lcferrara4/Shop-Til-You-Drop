from datetime import datetime, timedelta
from yahoo_finance import Share
import yahoo_finance

# exports historical closing prices to csv file for graphing in Excel
def export_historical_close(filename, curr_share, start_date, end_date):
    with open(filename, 'w') as f:
        historical_list = curr_share.get_historical(start_date, end_date)
        for day in reversed(historical_list):
            f.write(day['Date'] + ',' + day['Close'] + '\n')
    f.close()

if __name__ == '__main__':
    lulu = Share('LULU') # share data for lululemon stock
    urbn = Share('URBN') # share data for urban outfitters stock
    brby = Share('BRBY.L') # share data for burberry stock
    start = "2017-03-15"
    end = "2017-05-03"
    export_historical_close("lulu.csv", lulu, start, end)
    export_historical_close("urbn.csv", urbn, start, end)
    export_historical_close("brby.csv", brby, start, end)
