#!/usr/bin/python3

import quandl
import numpy as np
import datetime
import pandas

q_api_key = "bB4wp5--7XrkpGZ7-gxJ"
quandl.ApiConfig.api_key = q_api_key

data = quandl.get_table('WIKI/PRICES', ticker = ['AAPL', 'MSFT', 'WMT'], qopts = { 'columns': ['ticker', 'date', 'volume', 'adj_close'] }, date = { 'gte': '2015-12-31', 'lte': '2016-12-31' }, paginate=False)

print(data)
