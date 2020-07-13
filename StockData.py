import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
#pandas is a data analysis library
import pandas as pd
import pandas_datareader.data as web
style.use('ggplot')
# start = dt.datetime(2019,1,1)
# end = dt.datetime(2020,7,13)
#
# #df is a dataframe, think of link a spreadsheet, TSLA is tesla stock
# #adj close
# df = web.DataReader('MSFT', 'yahoo', start, end)
# df.to_csv('MSFT.csv')
df = pd.read_csv('tesla.csv', parse_dates=True, index_col = 0)

df[['High','Close']].plot()
plt.show()
