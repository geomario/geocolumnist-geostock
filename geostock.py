import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
from pandas_datareader import DataReader
import fix_yahoo_finance as yf
from datetime import date
import matplotlib.pyplot as plt
from bokeh.plotting import figure,output_file, show
from bokeh.themes import built_in_themes
from bokeh.io import curdoc

yf.pdr_override() #To fix the downloading in DataReader

#Defining the dates to work in
start = date(2016, 1, 1) #Default_ Jan 1,2010 (year,month,date)
end = date(2018,1,1)  #Default: today

#Defining the stocks to import
stock_tickers = ["HTM","ORA","CVX","BRK-A","ENEL.MI","PIF.TO","INE.TO","LXV","CLIME-B.ST"]
#Loop creating the geothermal stock dataframe
listings = []
for stock in stock_tickers:
    print ("The stocks to download are: " + stock) #Checking the stocks to print
    try:
        listing = pdr.get_data_yahoo(stock, start)
        listing["Exchange"] = stock
        listings.append(listing)
    except ValueError:
        pass

#Creating a big dataframe for all the stocks
df_listings = pd.concat(listings)
# print (df_listings.head()) #Checking the shape of only one DF

#Graphs in matplotlib
listings[1]["Close"].plot()
# plt.show()

#Graph in bokeh
curdoc().theme ="dark_minimal"
p = figure(plot_width=980, plot_height=390, x_axis_type="datetime", title = "Geothermal Stocks")
p.line(listings[1].index, listings[1]["Close"] ,color="greenyellow", alpha=0.5)
output_file("geostock.html")
show(p)
