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
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington?\n").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please enter either Chicago, New York City, or Washington.")

    # get user input for month (all, january, february, ... , june)
    month = input("Which month? January, February, March, April, May, or June? Or type 'all' for all months.\n").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day of the week? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? Or type 'all' for all days.\n").lower()

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

    df = pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def subscriber_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating Subscriber Stats...\n')
    start_time = time.time()
    
    #Average Trip Duration of subscribers
    avg_trip_duration_subscribers = df[df['User Type'] == 'Subscriber']['Trip Duration'].mean()
    print("\nAverage Trip Duration of Subscribers:", avg_trip_duration_subscribers)
   
    #Average Trip Duration of non-subscribers
    avg_trip_duration_customers = df[df['User Type'] == 'Customer']['Trip Duration'].mean()
    print("Average Trip Duration of Non-Subscribers:", avg_trip_duration_customers)

    #Percentage of subscribers vs non-subscribers. 
    total_users = len(df)
    subscribers = len(df[df['User Type'] == 'Subscriber'])
    non_subscribers = len(df[df['User Type'] == 'Customer'])
    percent_subscribers = (subscribers / total_users) * 100
    percent_non_subscribers = (non_subscribers / total_users) * 100
    print("\nPercentage of Subscribers:", percent_subscribers)
    print("Percentage of Non-Subscribers:", percent_non_subscribers)
    
    # Most popular route taken by non-subscribers
    if 'Start Station' in df and 'End Station' in df:
        popular_route_non_subscribers = df[df['User Type'] == 'Customer'].groupby(['Start Station', 'End Station']).size().idxmax()
        # Most popular route taken by subscribers
        popular_route_subscribers = df[df['User Type'] == 'Subscriber'].groupby(['Start Station', 'End Station']).size().idxmax()

        if popular_route_non_subscribers == popular_route_subscribers:
            print("\nMost Popular Route is the Same for Subscribers and Non-Subscribers:")
            print(popular_route_non_subscribers)
        else:
            print("\nMost Popular Route is Different for Subscribers and Non-Subscribers:")
            print("Route for Subscribers:", popular_route_subscribers)
            print("Route for Non-Subscribers:", popular_route_non_subscribers)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data upon user request."""
    start_index = 0
    while True:
        raw_inp = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        raw = raw_inp.lower().strip()
        if raw == 'yes':
            print(df.iloc[start_index:start_index + 5])
            start_index += 5
        elif raw == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' if you'd like to see raw data and 'no'otherwise.")
 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        subscriber_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
