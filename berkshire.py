from typing import Union
import pandas as pd
import glob
from datetime import datetime
import numpy as np
from pandas import DataFrame, Series
import calendar

path = r'/home/workspace'

class berkshire():
      def load_data(self):
          all_files = glob.glob(path + "/*.csv")
          li =[]
          print (all_files)

          for filename in all_files:
              df = pd.read_csv(filename, index_col=None, header=0)
              if "chicago" in filename:
                  print ("true1")
                  df['city'] = "chicago"
              if "washington" in filename:
                 df["city"]= "washington"
              if "new_york_city" in filename:
                 df["city"]="New_York"
              li.append(df)
          frame: Union[DataFrame, Series] = pd.concat(li, axis=0)
          print(len(frame))
          return frame
      def calc_mostcommon_city_time_day(self,value,value1,value2,frame):
           frame["Start Time"] = pd.to_datetime(frame["Start Time"]) #I want to work with the dates in the column datetime as datetime objects instead of plain text
           frame['month'] = frame ["Start Time"].dt.month
           frame['month'] = frame ["Start Time"].dt.month_name()
           #frame['month'] = frame['month'].dt.strptime()
           frame['Year'] = frame ["Start Time"].dt.year
           frame['Day'] = frame ["Start Time"].dt.day_name()
           frame['Hour'] = frame ["Start Time"].dt.hour
           #change to lowercase
           frame['city'] =frame['city'].astype(str)
           frame['Day'] =frame['Day'].astype(str)
           frame['month'] =frame['month'].astype(str)
           frame['city'] =frame['city'].str.lower()
           frame['Day'] = frame['Day'].str.lower()
           frame['month']= frame['month'].str.lower()
           #print( frame.dtypes )    
          # print (frame['city'])
           #print ("The length of frame data frame is",len(frame))
           #print( frame['city'] == value)
           #frame2= frame.query("city ==@value")
           print(frame.head())
           frame2=frame.query('(city== @value)') # Apply filter based on input
           if value2 != 'all':
              frame2=frame2.query('(month==@value2)') #skip this filter is input is all
           if value1 != 'all':
              frame2=frame2.query('(Day==@value1)') #skip this filter if input is all
           #print(len(frame))
           print("The length of frame2 data frame is",len(frame2))
           most_common_month = frame2['month'].mode()
           most_common_day = frame2['Day'].mode()
           most_common_hour = frame2['Hour'].mode()
           print("The most common month is:\n",most_common_month ,"\n","The most common day is\n", most_common_day,"\n","The most common hour is \n", most_common_hour,"\n")
           return frame2
        
      def most_common_stations_trip(self,frame2):
           most_common_start_station = frame2['Start Station'].mode()
           most_common_end_station = frame2['End Station'].mode()
           print(most_common_start_station,"\n",most_common_end_station,"\n")
           #frame2['startEndStation'] = frame2["Start Station"].astype(str) +" "+frame2["End Station"].astype(str)
           #most_common_start_end_station = frame2['startEndStation'].mode()
           #print(most_common_start_end_station)
           #print(frame2['startEndStation'])
           count_series = frame2.groupby(['Start Station', 'End Station']).size()
           new_df = count_series.to_frame(name = 'size').reset_index()
           print (new_df)
           print(new_df.loc[new_df['size'].idxmax()])
           print (new_df.query('(size ==8)'))
           print(frame2.groupby('User Type').size())
           print(frame2.groupby('Gender').size())
        
      def total_avg_travel_time(self,frame2):
           total = frame2['Trip Duration'].sum()
           avg = frame2['Trip Duration'].mean()
           
           print("Total Trip Duration is","\n",total)
           print("Average Trip Duration is","\n",avg),
     
       
      def trip_duration(self,frame2):
           minbirthyear = frame2['Birth Year'].min()
           maxbirthyear = frame2['Birth Year'].max()
           mostcommonyear = frame2['Birth Year'].mode()
           print("Minimum Birth Year is","\n",minbirthyear)
           print("Maximum Birth Year is","\n",maxbirthyear)
           print("Most Common Birth Year","\n",mostcommonyear)
           
          
            


     
def test_berkshire():
    
    value = input("Please enter a name of the city all lower case:\n").lower()
    value1 = input("Please enter a  name of the day Monday, Sunday etc.. or enter all for all days\n").lower()
    value2 = input("Please enter a  name of the month or enter all for all months\n").lower()
    run = berkshire()
    frame=run.load_data()
    frame2=run.calc_mostcommon_city_time_day(value,value1,value2,frame)
    run.most_common_stations_trip(frame2)
    run.total_avg_travel_time(frame2)
    run.trip_duration(frame2)
    

if __name__=="__main__":
    test_berkshire()
