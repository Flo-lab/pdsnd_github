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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input ("Which City do you want to analyze? (chicago / new york city / washington) ").lower()
        if city in (CITY_DATA):
            print ("OK, Let\'s analyze for the city", city)
            break  
        else:
            print ("Please try again to enter a valid city name")              


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        m = input ("Which month do you want to analyze? (all / january - june) ").lower()
        if m in ("all", "january", "february", "march", "april", "may", "june"):
            print ("OK, Let\'s analyze for the month", m)
            break  
        else:
            print ("Please try again to enter a valid month name") 

            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input ("Which weekday do you want to analyze? (all / monday - sunday) ").lower()
        if day in ("all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"):
            print ("OK, Let\'s analyze for the weekday", day)
            break  
        else:
            print ("Please try again to enter a valid weekday name")

    print('-'*40)
    
    return city, m, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        # use index of months list to get corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to creat new dataframe df
        df = df[df['month'] == month]
        
         # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Month:', popular_month)
    
    """ Activate this code to get an additional print of the month counts"""
    #month_count =  df['month'].value_counts()
    #print ('Start month count:\n', month_count)
  

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Start Day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)
    
    """ Activate this code to get an additional print of the stations counts"""
    #station_count =  df['End Station'].value_counts()
    #print ('End station count:\n', station_count.head())

    # TO DO: display most frequent combination of start station and end station trip    
    df['Start - End'] = df['Start Station'] + ' - ' + df['End Station']
    most_frequend_combination = df['Start - End'].mode()[0]
    print('Most Popular combination of Start and End Station:', most_frequend_combination)
    
    """ Activate this code, to view the above created dateframe Start-End """
    #print(df['Start - End'].head())
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time =  df['Trip Duration'].sum()
    print ('The total travel time is ', total_travel_time, ' s')

    # TO DO: display mean travel time
    mean_travel_time =  df['Trip Duration'].mean()
    print ('The mean travel time is ', mean_travel_time, ' s')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print("The count of user types is:\n", user_types_count)
    print ('\n')

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('The count of Genders is:\n', gender_count)
    else: 
        print('There is no Gender information available for the chosen City')
        
    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        earliest_year = df['Birth Year'].max()
        print ('The earliest year of birth is ',earliest_year)
        most_recent_year = df['Birth Year'].min()
        print ('The most recent year of birth is ',most_recent_year)
        most_common_year = df['Birth Year'].value_counts().idxmax()
        print ('The most common year of birth is ', most_common_year)
    else:
        print('There is no birth year information available for the chosen City')
    
    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)
      
    
def raw_data(df):
    """Displays bikeshare raw data if requested"""  
    i=0
    while True:
        check_request = input ('Do you request to display 5 lines of raw data? (yes/no) ').lower()
        if check_request in ('yes') and df.shape[0] > i :
            i += 5
            print ('OK, here is the code:')
            print (df.head(i))
        if check_request in ('no'):
            print ('OK, no raw data')
            i=0
            break
        else:
            print ('Please try again. Do you request to display 5 lines of raw data? (yes/no) ')  
                     


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
