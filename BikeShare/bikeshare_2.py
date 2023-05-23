import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city=input("enter the name of the city to analyze (chicago , new york city , washington ) : ").lower()
        if city not in CITY_DATA:
            print("Make sure you enter the name of the city correctly !")

        else :
            break
        
     # get user input for month (all, january, february, ... , june)
    while True :
         month=input("enter the month that you need (january , february , march , april , may , june) or all for all months : ").lower()
         months=["january","february","march","april","may","june"]
         if  month !="all" and month not in months :
            print("please enter a valid month !")
         else:
              break
    



     # get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
          day=input("enter the day that you need (saturday , sunday , tuesday , wednesday , thursday , friday ) or all for all days : ").lower()
          days=["saturday","sunday","tuesday","wednesday","thursday","friday"]
          if  day !="all" and day not in days :
              print("please enter a valid day !")
          else:
              break    
        
    


    print('-'*40)
    return city,month,day



def display_first_rows(city):
    """ display the first rows of raw data uopn request by the user 
    Args :
        city . the city that you want to display the first rows of it 
    """
     #load the data of the city 
    df = pd.read_csv(CITY_DATA[city])
    count=0
    raw_data=input("Do you want to display the first five rows of the data of the city ? if you don't enter 'n' :\n").lower()

    while True :
        if raw_data=="n":
            break
        print(df[count:count+5])
        raw_data=input("do you want to display the next five rows ? y / n :\n").lower()
        count+=5


def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != "all":
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != "all":
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]



    return df








def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month=df['month'].mode()[0]
    print("the most common month :",popular_month)

    # display the most common day of week
    popular_day=df['day'].mode()[0]
    print("the most common day : ", popular_day)


    # display the most common start hour
      # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

      # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

      # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print("the most common start station : ",common_start_station)
 

    # display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print("the most common end station : ",common_end_station)


    # display most frequent combination of start station and end station trip
    combin_first_end=(df["Start Station"]+"_"+df["End Station"]).mode()[0]
    print("the most frequent combination of start and end station trip : ", combin_first_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time=df["Trip Duration"].sum()
    print("The total travel time = ",total_time," seconds")


    # display mean travel time
    mean_of_time=df["Trip Duration"].mean()
    print("The mean travel time = ", mean_of_time," seconds")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("the count of each user type :\n ",user_types)



    # Display counts of gender
    if "Gender" in df :
        user_gender=df["Gender"].value_counts()
        print("\ncounts of gender : \n",user_gender)



    # Display earliest, most recent, and most common year of birth
    if "Birth Year"in df :
        earliest=int(df["Birth Year"].min())
        print("\nthe earliest year : \n",earliest)
        recent=int(df["Birth Year"].max())
        print("\nthe recent year :\n",recent)
        common=int(df["Birth Year"].mode()[0])
        print("\n the most common year : \n ",common)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
     

def main():
    while True:
        city , month , day= get_filters()
        df = load_data(city , month , day)

        display_first_rows(city)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
