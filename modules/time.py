from datetime import datetime
import json

"""
    Reference: https://docs.python.org/3.8/library/datetime.html

    Datetime Format:
        Microsecond
            %f      - Microsecond (700167)
        Second
            %S      - Second (00-59)
        Minute
            %M      - Minute (00-59)
        Hour
            %I      - Hour in 12 hour format (01-12)
            %H      - Hour in 24 hour format (00-23)
        Day
            %d      - Day of month (01)
            %j      - Day of year (001-366)
        Week
            %U      - Week number of the year (01-53)
            %a      - Weekday abbreviated (Sun-Sat)
            %A      - Weekday full (Sunday-Saturday)
            %w      - Weekday as decimal (0-6)
        Month
            %b      - Abbreviated month name (Jan)
            %B      - Full month name (January)
            %m      - Month as decimal (06)
        Year
            %y      - Year without century (21)
            %Y      - Year with century (2021)
        AM/PM
            %p      - Locale's equivalent of either AM or PM (PM
        Presets
            %c      - Locale's appropriate date and time (Sat Jun 26 20:35:33 2021)
            %x      - Locale's appropriate date (06/26/21)
            %X      - Locale's appropriate time (20:35:33)
    Invalid
        UTC Offset
            %z      - UTC Offset (couldn't get it to work)
        Timezone
            %Z      - Time zone name (couldn't get it to work)
"""


configs = {
    'preset_date': '%x',
    'preset_time': '%X',
    'preset_date_and_time': '%c',
    'day_of_year': '%j of 365',
    'time_and_am_pm': '%'
}


preset_date_time = "%c"
preset_date = "%x"
preset_time = "%X"


def load_directives():
    f = open('directives.json', 'r')
    directives = f.read()
    print(directives)


"""
    All of my modules are going to have to have the exact same keyboard controls (consistency is key)
        Enter TAB to jump to the next module 
        Enter module number to jump to that module

    The main screen will need to have a console at the bottom for entering commands 

    Default display:
        11:23:48 PM     June 29 2021
        

    Select your function
    1. Time & Date
        a. Adjust clock settings   
    2. Stopwatch
        a. Set stopwatch
        b. Add or remove stopwatch
    3. Timer 
        c. 
    4. Alarm
    5. GMT (second time zone)

"""

"""
    The best way to go about it is to let the user decide which directives they want to allow
    To do this, let them pick between preset formats (ones that I make) or custom formats (ones they make)
    In custom formatted strings, let them either pick the options they'd like, or enter in a string literal (ex: %s%d)
"""
"""
    Since this is mostly joyless, let's do this part later

    Time
        [Hour]  (12 or 24)
        [Minute]
        [Second]
        [Microsecond]


    Date
        [Day]
            %d      - Day of month (01)
            %j      - Day of year (001-366)
        Week
            %U      - Week number of the year (01-53)
            %a      - Weekday abbreviated (Sun-Sat)
            %A      - Weekday full (Sunday-Saturday)
            %w      - Weekday as decimal (0-6)
        Month
            %b      - Abbreviated month name (Jan)
            %B      - Full month name (January)
            %m      - Month as decimal (06)
        Year
            %y      - Year without century (21)
            %Y      - Year with century (2021)
"""


def display(format):
    now = datetime.now()


if __name__ == "__main__":
    directives = load_directives()

    while(True):
        now = datetime.now()
        print("Enter type: %", end="")
        user_input = input()
        try:
            curr_time = now.strftime("%" + user_input)
            print(curr_time)

        except:
            print(user_input + " is not a valid format")
