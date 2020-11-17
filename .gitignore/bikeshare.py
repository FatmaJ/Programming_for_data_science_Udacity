import time
import pandas as pd
import numpy as np
import datetime 

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
cities = ('Chicago', 'New York', 'Washington')
while True:
city = input('Choose one of these cities: Chicago, New York or Washington? \n> ').lower()
if city in cities:
break

    # TO DO: get user input for month (all, january, february, ... , june)

months = ['january', 'february', 'march', 'april', 'may', 'june']
month = input('Filter data by months result) \n> ' hs) .lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]
day = input('Filter data by week result result) \n> ', days).lower()

    print('-'*40)
    return city, month, day


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
# load data file into a dataframe
df = pd.read_csv(CITY_DATA[city])

# convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract hour,month and day from the Start Time column to create new column
df['hour'] = df['Start Time'].dt.hour
df['month'] = df['Start Time'].dt.month
df['day_of_week'] = df['Start Time'].dt.weekday_name

# filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
         # filter by month to create the new dataframe
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
    
most_common_month = df['month'].mode()[0]
print('The most common month is:', most_common_month)

    # TO DO: display the most common day of week

most_common_day = df['day_of_week'].mode()[0]
print('The most common day is:', most_common_day)
    # TO DO: display the most common start hour
most_common_start_hour = df['hour'].mode()[0]
print('The most common day is:', most_common_day)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
  start_station = df['Start Station'].mode()[0]
   print('The most commonly used start station is ' ,start_station)

    # TO DO: display most commonly used end station
  end_station = df['End Station'].mode()[0]
   print('The most commonly used end station is ' ,end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination_of_start_end'] = df['Start Station'] + ' , ' + df['End Station']
  common_combination = df['combination_of_start_end'].mode()[0]
  print('The most frequent combination of start station and end station is ' ,common_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
   total_travel = df['trip_duration'].sum()
     print('Total Travel Time: ',total_travel)

    # TO DO: display mean travel time
    mean_travel = df['trip_duration'].mean()
     print('Mean Travel Time: ' ,mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
     print(user_types)

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
     print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
     earliest_year = int(df['Birth Year'].min())
     print('Earliest Year Of Birth: ',earliest_year)
    most_recent_year = int(df['Birth Year'].max())
     print('Most Recent Year Of Birth: ',most_recent_year)
    most_common_year = int(df['Birth Year'].mode()[0])
     print('Most common Year Of Birth: ',most_common_year)
    else:
      print('The year of birth error')  
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    # If the user answers 'yes,' then the script should print 5 rows of the data
    row = 0
    while True:     
    ans = input("Do you want to see the raw data? Yes or No").lower()
     df['Start Time'] = df['Start Time'].dt.strftime('%Y-%m-%d %H:%M:%S')
     if ans == 'yes':  
      raw += 5
    print(df.iloc[raw : raw + 5])
    
    elif ans not in ['yes', 'no']:
        ans = input ('Wrong! Please select Yes or No').lower()
     ans = input("Do you want to see more? Yes or No").lower()
    elif ans == 'no':
     break
    else ans == 'no':
    return


        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
