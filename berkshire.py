from typing import Union

import pandas as pd
import glob
from datetime import datetime
import numpy as np
from pandas import DataFrame, Series

path = r'C:\Users\SujathaSubramaniam\OneDrive - Index Analytics\Documents\Python\cobolparser\mainframe-data-utilities-main'
all_files = glob.glob(path + "/*.csv")
li =[]
print (all_files)

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    print (filename)
    if "chicago" in filename:
        print ("true1")
        df['city'] = "Chicago"
    if "washington" in filename:
        df["city"]= "washington"
    if "new_york_city" in filename:
        df["city"]="New_York"
    li.append(df)

frame: Union[DataFrame, Series] = pd.concat(li, axis=0)
#print (frame.head())
#print (frame.describe())
#print(frame.groupby('Start Time').mean())

#Identify Most Common Month,Day of week,common hour of the day


# Add three new columns ton the dataframe by parsing timestamp column into Month
frame["Start Time"] = pd.to_datetime(frame["Start Time"]) #I want to work with the dates in the column datetime as datetime objects instead of plain text
frame['month'] = frame ["Start Time"].dt.month
frame['Year'] = frame ["Start Time"].dt.year
frame['Day'] = frame ["Start Time"].dt.day_name()
frame['Hour'] = frame ["Start Time"].dt.hour
print (frame['city'])
print ("The length of frame data frame is",len(frame))
value = input("Please enter an name of the city:\n")
print( frame['city'] == value)
frame2= frame.query("city ==@value")
print("The length of frame2 data frame is",len(frame2))
most_common_month = frame2['month'].mode()
most_common_day = frame2['Day'].mode()
most_common_hour = frame2['Hour'].mode()
print(most_common_month,most_common_day,most_common_hour)


#Identify Most Common Month,Day of week,common hour of the day


