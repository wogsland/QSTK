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
import math
import csv
import sys

if __name__ == '__main__':
  # 1. Read the dates and symbols
  startcash = sys.argv[1]
  filename = sys.argv[2]
  outfile = sys.argv[3]
  reader = csv.reader(open(filename, 'rU'), delimiter=',')
  dt_array = []
  symb_array = []
  for row in reader:
    #print row
    #print row[0]
    symb_array.append(row[3].strip())
    #inner_array =[]
    #inner_array.append(dt.datetime(int(row[0]), int(row[1]), int(row[2])))
    #inner_array.append(row[3])
    #inner_array.append(row[4])
    #inner_array.append(row[5])
    #dt_array.append(inner_array)
    dt_array.append(dt.datetime(int(row[0]), int(row[1]), int(row[2])))
  print dt_array
  dt_array = list(set(dt_array))
  symb_array = list(set(symb_array))
  print symb_array

  # 2. Read the data
  read_dt_array = []
  for row in dt_array:
    read_dt_array.append(row + dt.timedelta(days=1))
  print read_dt_array
  
  # 3. Create the matrix of shares
  # 4. Calculate the cash timeseries
  # 6. Write to CSV
  # 5. Calculate the fund timeseries
