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
        print("Which city would you like to view data for: Chicago, New York, Washington? \n")
        city = input("\nPlease write Chicago, New York or Washington: ")
        city = city.lower()
        print(city)
        
        if city == 'chicago' or city == 'new york city' or city == 'washington' or city == 'all':
            break
        

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        print("Would you like to filter by month? \n")
        month = input("\nPlease type a month from January to June or type all: \n")
        month = month.lower()
        print(month)

        if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month ==  'may' or month == 'june' or month == 'all':
                    
            break
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print("Would you like to filter by day of week? \n")
        day = input("\n Please select all or type a day of the week Monday through Sunday: \n")
        day = day.lower()

        if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day ==  'friday' or day == 'saturday' or day == 'sunday' or day == 'all':
            break


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
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

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
    popular_month = df['month'].mode()[0]
    print('The most popular month is: ', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most popular day of the week is: ', popular_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular day of the week is: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most popular Start Station is: ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most popular End Station is: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_stations = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('The most frequent combination of Start and End Stations is: ', popular_start_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('The average trip duration is: ', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The total type of users are:\n', user_types)

    # TO DO: Display counts of gender
    
    gender_types = df['Gender'].fillna('N/A')
    gender_types = gender_types.value_counts()
    print('The total type of genders are:\n', gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth_year = df['Birth Year'].min()
    print('The earliest year of birth is: ', earliest_birth_year)

    recent_birth_year = df['Birth Year'].max()
    print('The most recent year of birth is: ', recent_birth_year)

    common_birth_year = df['Birth Year'].mode()[0]
    print('The most common Birth Year is: ', common_birth_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
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
