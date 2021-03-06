'''
Example call:
python marketsim.py 1000000 orders.csv values.csv
python hw3.py 1000000 orders.csv values.csv

Example orders.csv:
2008, 12, 3, AAPL, BUY, 130
2008, 12, 8, AAPL, SELL, 130
2008, 12, 5, IBM, BUY, 50

Example values.csv:
2008, 12, 3, 1000000
2008, 12, 4, 1000010
2008, 12, 5, 1000250
'''

# QSTK Imports
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import csv
import sys
import copy
import string

if __name__ == '__main__':
  # 1. Read the dates and symbols
  startcash = int(sys.argv[1])
  filename = sys.argv[2]
  outfile = sys.argv[3]
  reader = csv.reader(open(filename, 'rU'), delimiter=',')
  dt_array = []
  symb_array = []
  trade_array = []
  for row in reader:
    symb_array.append(row[3].strip())
    the_date = dt.datetime(int(row[0]), int(row[1]), int(row[2]), 16)
    dt_array.append(the_date)
    #the_date = row[0]+"-"+row[1]+"-"+row[2]+" 16:00:00"
    trade_array.append([row[3].strip(), row[4].strip(), row[5].strip(), the_date])
  print dt_array
  dt_array = sorted(list(set(dt_array)))
  print dt_array
  symb_array = list(set(symb_array))
  print symb_array
  print trade_array

  # 2. Read the data
  read_dt_array = []
  for row in dt_array:
    read_dt_array.append(row - dt.timedelta(days=1))
  print read_dt_array

  dataobj = da.DataAccess('Yahoo')
  #ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
  ls_keys = ['actual_close']
  ldf_data = dataobj.get_data(read_dt_array, symb_array, ls_keys)
  print ldf_data
  d_data = dict(zip(ls_keys, ldf_data))
  print d_data

  # problem with this fill is it only grabs the previous day in the dataset, not last trading day
  for s_key in ls_keys:
      d_data[s_key] = d_data[s_key].fillna(method='ffill')
      d_data[s_key] = d_data[s_key].fillna(method='bfill')
      d_data[s_key] = d_data[s_key].fillna(1.0)
  print d_data

  # 3. Create the matrix of shares
  trade_matrix = copy.deepcopy(d_data)
  for s_key in ls_keys:
    trade_matrix[s_key] = trade_matrix[s_key] * 0.0
  print trade_matrix
  holdings_matrix = copy.deepcopy(trade_matrix)
  for row in trade_array:
    if 'BUY' == row[1]:
      shares = int(row[2])
    else:
      shares = int(row[2]) * (-1)
    traded = row[0]
    day = string.replace((row[3]-dt.timedelta(days=1)).isoformat(),"T"," ")
    print traded + " " + str(shares)
    #trade = d_data['actual_close'][traded] * shares
    #print trade
    multi = d_data['actual_close'][traded].mul(shares)
    print multi[day]
    trade_matrix['actual_close'][traded][day] = multi[day]
  print trade_matrix

  # 4. Calculate the cash timeseries
  #cash = copy.deepcopy(read_dt_array)
  first_date = string.replace((read_dt_array[0]-dt.timedelta(days=1)).isoformat(),"T"," ")
  cash = []
  cash.append([first_date,startcash])
  i=0
  for row in read_dt_array:
    last_cash = cash[i][1]
    this_date = string.replace(row.isoformat(),"T"," ")
    for symbol in symb_array:
      trade_matrix['actual_close'][symbol][this_date]
      last_cash = round(last_cash - trade_matrix['actual_close'][symbol][this_date], 2)
    cash.append([this_date,last_cash])
    i = i+1
  print cash

  # 5. Calculate the fund timeseries

  
  # 6. Write to CSV
