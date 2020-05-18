import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
city = 'washington'
#  setting default value to washington since conditional on bottom,
#  looks for if city value is chicago or washington.
#  this is a way to prevent it from looking for gender and birth year,
#  since Washington
#  Does not contain a column for Gender or Birth year.

def sleep(seconds):
    time.sleep(seconds)
    # sleep function takes one argument for seconds to delay


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze

        (str) month - name of the month to filter by,
        or "all" to apply no month filter

        (str) day - name of the day of week to filter by,
        or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    sleep(1)
    # TO DO: get user input for city (chicago,
    # new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    while True:
        print("Which city would you like to view data for: "
              "Chicago, New York City, Washington? \n")
        sleep(1)
        city = input("\nPlease write Chicago, New York City or Washington: \n")
        city = city.lower() 
        # changing input to lower case to prevent problems with case letters
        # print(city)

        if city in ('chicago', 'new york city', 'washington'):

            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        sleep(1)
        print("\nWould you like to filter by month? \n")
        sleep(1)
        month = input("\nPlease type a month from January to June"
                      " (full month name) or type all: \n")
        month = month.lower()
        # changing input to lower case to prevent problems with case letters
        # print(month)

        if month in ('january', 'february', 'march', 'april',
                     'may', 'june', 'all'):

            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        sleep(1)
        print("\nWould you like to filter by day of week? \n")
        sleep(1)
        day = input("\n Please select all or type a day of "
                    "the week Monday through Sunday: \n")
        day = day.lower()
        # changing input to lower case to prevent problems with case letters

        if day in ('monday', 'tuesday', 'wednesday',
                   'thursday', 'friday', 'saturday', 'sunday', 'all'):

            break

    print('-'*40) # prints one line of 40 dashes to draw separation
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and
    filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze

        (str) month - name of the month to filter by,
        or "all" to apply no month filter

        (str) day - name of the day of week to filter by,
        or "all" to apply no day filter

    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    # converting month text to number. Example January == 1

    df['day_of_week'] = df['Start Time'].dt.day_name()
    # converting day of week to number example
    
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
    sleep(1)
    print('\nCalculating The Most Frequent Times of Travel...\n')
    sleep(1)
    start_time = time.time()
    sleep(1)
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The most popular month is: ', popular_month)
    sleep(1)
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most popular day of the week is: ', popular_day)
    sleep(1)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular hour of the day is: ', popular_hour)
    sleep(1)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) # prints one line of 40 dashes to draw separation
    sleep(5)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    sleep(3)
    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most popular Start Station is: ', popular_start_station)
    sleep(2)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most popular End Station is: ', popular_end_station)
    sleep(2)

    # TO DO: display most frequent combination of
    # start station and end station trip

    popular_start_end_stations = df.groupby(['Start Station',
                                             'End Station']).size().idxmax()
    print('The most frequent combination of Start'
          'and End Stations is: ', popular_start_end_stations)
    sleep(2)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) # prints one line of 40 dashes to draw separation
    sleep(2)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    sleep(2)
    print('\nCalculating Trip Duration...\n')
    sleep(1)
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: ', total_travel_time)
    sleep(1)
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('The average trip duration is: ', mean_travel)
    sleep(1)
    print("\nThis took %s seconds." % (time.time() - start_time))
    sleep(3)
    print('-'*40) # prints one line of 40 dashes to draw separation


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    sleep(1)
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The total type of users are:\n', user_types)
    sleep(1)
    # TO DO: Display counts of gender

    #  Setting a conditional since Washington csv
    #  does not have Gender or Birth Year columns.
    #  This is to prevent an error
    if CITY_DATA[city] == 'chicago' or CITY_DATA[city] == 'new york city':

        gender_types = df['Gender'].fillna('N/A')
        gender_types = gender_types.value_counts()
        print('The total type of genders are:\n', gender_types)

        sleep(1)
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        print('The earliest year of birth is: ', earliest_birth_year)

        sleep(1)

        recent_birth_year = df['Birth Year'].max()
        print('The most recent year of birth is: ', recent_birth_year)
        sleep(1)

        common_birth_year = df['Birth Year'].mode()[0]
        print('The most common Birth Year is: ', common_birth_year)
        sleep(1)

    print("\nThis took %s seconds." % (time.time() - start_time))
    sleep(3)
    print('-'*40) # prints one line of 40 dashes to draw separation


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df) # function frequent times of travel
        station_stats(df) # function to calculate frequent start,
        # end, stations
        trip_duration_stats(df) # function to calculate total travel time
        user_stats(df)

        count = 1  # counter used to multiply the count number * 5
        # to display 5 more rows each time

        while True:
            print('Would you like to see 5 rows of raw data? \n')
            sleep(1)
            answer = input('Please enter yes or no: \n')
            answer = answer.lower()

            if answer == 'yes' or answer == 'y' or answer == 'ye':
                print(df.head(count*5))
                # used to print 5 more rows of the raw data.
                sleep(1)
                count += 1
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        sleep(1)
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
    pd.show_versions() # to show versions of packages and libraries used. 
