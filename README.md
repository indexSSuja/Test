Statistics Computed
You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, you'll write code to provide the following information:

#1 **Popular times of travel (i.e., occurs most often in the start time)**

 -  most common month
 -  most common day of week
 -  most common hour of day

#2 **.Popular stations and trip**

-  most common start station
-  most common end station
-  most common trip from start to end (i.e., most frequent combination of start station and end station)


#3 **Trip duration

-  total travel time
-  average travel time

#4 **User info

-   counts of each user type
-   counts of each gender (only available for NYC and Chicago)
-   earliest, most recent, most common year of birth (only available for NYC and Chicago)


The approach for this project is summarized in the main function

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
    
