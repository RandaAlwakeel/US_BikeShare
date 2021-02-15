import time
import numpy as np
import pandas as pd
from datetime import datetime

CITY_DATA={'chicago':'chicago.csv','new yourk city':'new_yourk_city.csv','washington':'washington.csv'}
months=['january','february','march','april','may','june','july','august','september','october','november','december','all']
days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']


def get_filters():
    print("Hello, the application can make analysis according to city, month, or day")
    
    invalid_input =True
    while invalid_input:
        city = input("Input city by which the data will be filtred").lower()
        month = input("Input month by which the data will be filtred or type 'all to apply no month filter '").lower()
        day = input("Input day by which the data will be filtred or type  'all' to apply no day filter").lower()
        if city in CITY_DATA and month in months and day in days:
            invalid_input = False
        else:
            print("Please, Enter valid city, month and day names!")
    
    
    print("Let\'s explore some US bikeshare data!")
    
    print('-'*40)
    return city, month, day



def load_data(city,month,day):
    df= pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day of week'] = df['Start Time'].dt.dayofweek
    
    
    if month != 'all':
        nmonth = months.index(month)+1
        df=df[df['month']==nmonth]
    if day != 'all':
        nday = days.index(day)+1
        df=df[df['day of week']==nday]
    
    
    
    
    df['End Time'] = pd.to_datetime(df['End Time'])
    return df

  



def time_stats(df):
    
    print('\nCalculating The Most Frequent Times of Travel....\n ')
    start_time = time.time()
    
    df['start month']= df['Start Time'].dt.month
    #print(day)
    if month == 'all':
        
        most_start_month= df['start month'].mode()[0]
        print("most of the trips start in month {} ".format(months[most_start_month-1]))
        tripsnumber_in_months = df['start month'].value_counts(sort=False)   
        min_trips_months = np.min(tripsnumber_in_months)
        
       # print(min_trips_months)
        month_with_min_trips= tripsnumber_in_months[tripsnumber_in_months==min_trips_months].index[0]
        print("Month {} has the minimum number of trips".format(months[month_with_min_trips-1]))
    else:
        print('The data was filtered using month',month)
        print("So in this case all the shown trips start in month ", month)
 
    if day == 'all':
        most_start_day= df['day of week'].mode()[0]
        
        print("most of the trips start on {}s ".format(days[most_start_day-1]))
    
        tripsnumber_in_weekdays = df['day of week'].value_counts(sort=False)
        min_trips_days = np.min(tripsnumber_in_weekdays)
        day_with_min_trips = tripsnumber_in_weekdays[tripsnumber_in_weekdays==min_trips_days].index[0]
        print("Day {} has the minimum number of trips".format(days[day_with_min_trips-1]))
    else:
        print('The data was filtered using day=',day)
        print("So in this case all the shown trips start in day ", day)
    
    df['start hour']= df['Start Time'].dt.hour
    most_start_hour= df['start hour'].mode()[0]
    print("The most start hour is:  ",most_start_hour)
    
    average_start_hour = np.mean(df['start hour'])
    print("The users start the trip on average at {} hour  of the day".format(average_start_hour))
    
    df['end hour']= df['End Time'].dt.hour
    most_end_hour = df['end hour'].mode()[0]
    print("The most end hour is:  ",most_end_hour)
    
    average_end_hour = np.mean(df['end hour'])
    print("The users end the trip on average at {} hour  of the day".format(average_end_hour))
    
    print("\n This took %s seconds." % (time.time()- start_time))
    print('-'*40)
    



def station_stats(df):
   
    print("\nCalculating The Most Popular Stations and Trip\n")
    start_time = time.time()
    most_start_station= df['Start Station'].mode()[0]
    print("Most commonly used start station is ",most_start_station)
    
    most_end_station= df['End Station'].mode()[0]
    print("Most commonly used end station is ",most_end_station)
    
    trips= df.groupby(['Start Station','End Station']).size().reset_index(name='count')
    max_count= np.max(trips['count'])
    common_trip =trips[trips['count']==max_count]
    
    print("The most common trip is:\n",common_trip)
    print("\n This took %s seconds." % (time.time()- start_time))
    print('-'*40)
    
    



def trip_duration_stats(df):
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    average_duration= np.mean(df['Trip Duration'])
    print("The average duration =",average_duration )
    
    standard_deviation = np.std(df['Trip Duration'])
    print("The standard deviation for the trip duration =",standard_deviation )
    
    max_duration = np.max(df['Trip Duration'])
    print("The maximum trips duration =",max_duration )
    
    trip_with_max_duaration = df[df['Trip Duration']==max_duration]
    print("the trip or trips with the max duration is:\n",trip_with_max_duaration)
    
    min_duration = np.min(df['Trip Duration'])
    print("The minimum trip duration =",min_duration )
    
    trip_with_min_duaration = df[df['Trip Duration']==min_duration]
    print("the trip or trips with the minimum duration is:\n",trip_with_min_duaration)
    
    
        
    print("\n This took %s seconds." % (time.time()- start_time))
    print('-'*40)    



def user_stats(df):
    
    print('\nCalculating User Stats ...\n')
    start_time = time.time()
    print("\n========Describing the data on basis of user age=======\n")
    avg_user_age = np.mean(df['Birth Year'])
    print("The average birth year for the users= ", avg_user_age)
    median_user_age = np.median(df['Birth Year'])
    print("The median birth year for the users= ", median_user_age)
    
   
    print("\n========Describing the data on basis of user types and the corresponding types=======\n")
    new_df_user=df['User Type'].value_counts()
    
    for i in range(new_df_user.shape[0]):
        perce = new_df_user[i]/df.shape[0] 
        print("Number of users of type: {} = {} with {} percent of the total number of users".format(new_df_user.index[i],new_df_user[i],perce))
    
    print("\n========Describing the data on the basis of Gender=======\n")
    new_df_user=df['Gender'].value_counts()
    sum_percent=0.0
    for i in range(new_df_user.shape[0]):
        perce = new_df_user[i]/df.shape[0] 
        sum_percent += perce
        print("Number of users of type: {} = {} with {} percent of the total number of users".format(new_df_user.index[i],new_df_user[0],perce))
    if  sum_percent >0.0 :
        print("The remaining users are of Unknown Type and with percent= ", 1.0- sum_percent)
    
    
    print("\n This took %s seconds." % (time.time()- start_time))
    print('-'*40)



def userinput_based_stats(df):
    
    print("\n==============Describing Data on the basis of particular starting and ending stations specified by the user======\n")
    start_time = time.time()
    print("\nDo you want an anlysis for the duration of specific stations? \n")
    
    choice =input("Enter Yes \ No").lower()
    if choice == 'yes':
        st_station= input("Input the starting station")
        end_station= input("Input the ending station")
        #filtering data using the input start and end stations
        new_df=df[df['Start Station']== st_station]
        new_df=new_df[df['End Station']== end_station]
        
        average_duration= np.mean(new_df['Trip Duration'])
        print("\nThe average duration =",average_duration )
    
        standard_deviation = np.std(new_df['Trip Duration'])
        print("\nThe standard deviation for the trip duration =",standard_deviation )
    
        max_duration = np.max(new_df['Trip Duration'])
        print("The maximum trips duration =",max_duration )
    
        trip_with_max_duaration = new_df[new_df['Trip Duration']==max_duration]
        print("the trip or trips with the max duration is:\n",trip_with_max_duaration)
    
        min_duration = np.min(new_df['Trip Duration'])
        print("The minimum trip duration =",min_duration )
    
        trip_with_min_duaration = new_df[new_df['Trip Duration']==min_duration]
        print("the trip or trips with the minimum duration is:\n",trip_with_min_duaration)
        
        
        new_df_user=new_df['Gender'].value_counts()
        sum_percent=0.0
        
        for i in range(new_df_user.shape[0]):
            perce = new_df_user[i]/new_df.shape[0] 
            sum_percent += perce
            print("Number of users of type: {} = {} with {} percent of the total number of users of this stations".format(new_df_user.index[i],new_df_user[i],perce))
        
        sum_percentn = 1-sum_percent
        if  sum_percent >0.0 :
            print("\nThe remaining users are of Unknown Type and with percent= ", sum_percentn)
    
    print("\n This took %s seconds." % (time.time()- start_time))
    print('-'*40)
    

def main():
    while True:
        while True:
            city,month,day = get_filters()
            df = load_data(city,month,day)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            userinput_based_stats(df)
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break


if __name__=="__main__":
    main()
