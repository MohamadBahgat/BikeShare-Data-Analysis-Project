import time
import pandas as pd

# Global Variables

cities = {'c': ['Chicago', 'chicago.csv'],
          'n': ['New York city', 'new_york_city.csv'],
          'w': ['Washington', 'washington.csv']}

months = {"1": "January",
          "2": "February",
          "3": "March",
          "4": "April",
          "5": "May",
          "6": "June",
          "a": "All"}

days = {"sat": "Saturday",
        "sun": "Sunday",
        "mon": "Monday",
        "tue": "Tuesday",
        "wed": "Wednesday",
        "thu": "Thursday",
        "fri": "Friday",
        "a": "All"
        }

# ---------

# Functions


def get_filters():
    print("\n")
    # get user input for City
    while True:
        city = input("Enter 'c' if you want to choose Chicago " +
                     "or 'n' for choosing New-York or " +
                     "'w' for Washington: \n").lower()
        if(city in cities.keys()):
            break
        print('Invalid input!')

    # get user input for Month
    while True:
        month = input("Enter the number of the month you want to filter with" +
                      "(1 <---> 6) " +
                      "for example type '1' if you want to choose January " +
                      "or '2' to choose February' or .... '5' for May " +
                      "or '6' for June **AND** if you want them all just " +
                      "type 'a': \n").lower()
        if(month in months.keys()):
            break
        print('Invalid input!')

    # get user input for Day
    while True:
        day = input("Enter the first three letters of the day you want to " +
                    "filter with for example type 'sat' if you want to " +
                    "choose Saturday or 'sun' to choose Sunday' .... " +
                    " 'fri' for Friday **AND** if you want them all just type" +
                    "'a': \n").lower()
        if(day in days.keys()):
            break
        print('Invalid input!')

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(cities[city][1])

    # Convert Start Time Column To Be as Date Type
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Add Month column to our DataFrame
    df['Month'] = df['Start Time'].dt.month

    # Add Day_of_week column to our DataFrame
    df['Day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by the choosen month if any selected
    if month != 'a':  # all months are not chosen
        df = df[df['Month'] == int(month)]

    # Filter by the choosen day if any selected
    if day != 'a':  # all days are not chosen
        df = df[df['Day_of_week'] == days[day]]

    #print(df['day_of_week'])
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel ...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['Month'].mode()[0]
    print('Most Popular Start Month:', popular_month)

    # display the most common day of week
    popular_day = df['Day_of_week'].mode()[0]
    print('Most Popular Start Day:', popular_day)

    # Add Hour column to our DataFrame
    df['Hour'] = df['Start Time'].dt.hour

    # display the most common start hour
    popular_hour = df['Hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip ...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # Add Trip column to our DataFrame
    #df['Trip'] = df[['Start Station', 'End Station']].agg(' --> '.join, axis=1)
    df['Trip'] = df['Start Station'] + " --> " + df['End Station']

    # display most frequent combination of start station and end station trip
    popular_station = df['Trip'].mode()[0]
    print('Most Popular Trip:', popular_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration ...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time:", total_travel_time)

    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print("Total Travel Time:", average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, chosen_city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats ...\n')
    start_time = time.time()

    # Display counts of user types
    num_of_user_type = df['User Type'].value_counts()
    print("Count Of Our Users: \n")
    print(num_of_user_type)

    # for (New-York and Chicago)
    if chosen_city == 'n' or chosen_city == 'c':
        print("\n")
        # Display counts of gender
        num_of_gender = df['Gender'].value_counts()
        print("Count Of Genders: \n")
        print(num_of_gender)
        print("\n")
        # Display earliest, most recent, and most common year of birth
        # Earliest Year Of Birth
        earliest_year = df['Birth Year'].min()
        print("Earliest Year Of Birth:", int(earliest_year))
        # Most Recent Year Of Birth
        most_recent_year = df['Birth Year'].max()
        print("Most Recent Year Of Birth:", int(most_recent_year))
        # Most Common Year Of Birth
        most_common_year = df['Birth Year'].mode()[0]
        print("Most Common Year Of Birth:", int(most_common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def show_data(df):
    user_input = input("Do you want to view 5 rows? type 'y' if " +
                       "yes or any other letter for no! \n").lower()
    if user_input == 'y':
        current_row = 0 
        #pd.set_option('display.max_columns', None)
        while True:
            print(df.iloc[current_row : current_row + 5])
            user_input = input("Do you want to view 5 more rows? type y for " +
                               "yes or any other letter for no! \n").lower()
            current_row += 5
            if user_input != 'y':
                break

def main():
    while True:
        city, month, day = get_filters()
        print("The chosen City is: {}".format(cities[city][0]))
        print("The chosen Month is:", months[month])
        print("The chosen Day is:", days[day])
        print('-' * 40)
        df = load_data(city, month, day)
        #pd.set_option('display.max_columns', None)
        print(df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        show_data(df)
        restart = input(
            '\nWould you like to restart? Type "y" for yes or any other letter for no!\n')
        if restart.lower() != 'y':
            print("\nBye ...")
            break

if __name__ == "__main__":
    main()
