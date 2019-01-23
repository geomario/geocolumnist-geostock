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
from bokeh.models import Legend

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
print (df_listings.head()) #Checking the shape of only one DF

#Graphs in matplotlib
listings[1]["Close"].plot()
# plt.show()

#Graph in bokeh
curdoc().theme ="dark_minimal"
p = figure(plot_width=980, plot_height=390, x_axis_type="datetime", title = "Geothermal Stocks")

l0 = p.line(listings[0].index, listings[0]["Close"] ,color="greenyellow", alpha=0.5) # HTM
l1 = p.line(listings[1].index, listings[1]["Close"], color="red", alpha=0.5) #ORA
# l2 = p.line(listings[2].index, listings[2]["Close"] ,color="deepskyblue", alpha=0.5) #CVX most expensive
l3 = p.line(listings[3].index, listings[3]["Close"] ,color="aqua", alpha=0.5) #BRK-A
l4 = p.line(listings[4].index, listings[4]["Close"] ,color="deeppink", alpha=0.5) #ENEL.MI
l5 = p.line(listings[5].index, listings[5]["Close"] ,color="gold", alpha=0.5) #PIF.TO
l6 = p.line(listings[6].index, listings[6]["Close"] ,color="ivory", alpha=0.5) #INE.TO
# l7 = p.line(listings[7].index, listings[7]["Close"] ,color="yellow", alpha=0.5) #LXV
# p.line(listings[8].index, listings[8]["Close"] ,color="aqua", alpha=0.5) #CLIME-B.ST

legend1 = Legend(items=[("HTM", [l0]),("ORA", [l1]), ("BRK-A", [l3]), ("ENEL.MI", [l4]), ("PIF.TO", [l5]), ("INE.TO", [l6]) ], location=(70,20), orientation="horizontal")
p.add_layout(legend1, "below")
output_file("geostock.html")
show(p)
