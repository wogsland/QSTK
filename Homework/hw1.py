'''
(c) 2011, 2012 Georgia Tech Research Corporation
This source code is released under the New BSD license.  Please see
http://wiki.quantsoftware.org/index.php?title=QSTK_License
for license details.

Created on October 5, 2014 (fork of Examples/Basic/tutorial1.py)

@author: Bradley Wogsland
@contact: bradley@wogsland.org
@summary: Solution to Homework 1
'''

# QSTK Imports
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

# Example call of function:
# vol, daily_ret, sharpe, cum_ret = simulate(startdate, enddate, ['GOOG','AAPL','GLD','XOM'], [0.2,0.3,0.4,0.1])
# The function should return:
#   Standard deviation of daily returns of the total portfolio
#   Average daily return of the total portfolio
#   Sharpe ratio (Always assume you have 252 trading days in an year. And risk free rate = 0) of the total portfolio
#   Cumulative return of the total portfolio
def simulate(startdate, endate, symbols, allocations):
    ''' Main Function'''
    print "In the simulate function\n"

    # We need closing prices so the timestamp should be hours=16.
    timeofday = dt.timedelta(hours=16)

    # Get a list of trading days between the start and the end.
    ldt_timestamps = du.getNYSEdays(startdate, endate, timeofday)

    # Creating an object of the dataaccess class with Yahoo as the source.
    c_dataobj = da.DataAccess('Yahoo')

    # Keys to be read from the data, it is good to read everything in one go.
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    # Reading the data, now d_data is a dictionary with the keys above.
    # Timestamps and symbols are the ones that were specified before.
    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))

    # Filling the data for NAN
    for s_key in ls_keys:
        d_data[s_key] = d_data[s_key].fillna(method='ffill')
        d_data[s_key] = d_data[s_key].fillna(method='bfill')
        d_data[s_key] = d_data[s_key].fillna(1.0)

    # Getting the numpy ndarray of close prices.
    na_price = d_data['close'].values

    # Normalizing the prices to start at 1 and see relative returns
    na_normalized_price = na_price / na_price[0, :]

    # Copy the normalized prices to a new ndarry to find returns.
    na_rets = na_normalized_price.copy()

    # Calculate the daily returns of the prices. (Inplace calculation)
    # returnize0 works on ndarray and not dataframes.
    tsu.returnize0(na_rets)
