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
  i = 1
  for row in reader:
    print row
    dt_array[i] = dt.datetime(2008, 1, 1)
    i = i+1
  print dt_array

  # 2. Read the data
  # 3. Create the matrix of shares
  # 4. Calculate the cash timeseries
  # 6. Write to CSV
  # 5. Calculate the fund timeseries
