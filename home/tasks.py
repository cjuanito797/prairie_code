from celery import shared_task
from datetime import datetime, timedelta, date

@shared_task
def slidingWindow():
    today = date.today()
    print("Running the scheduled sliding window task!")
    myDates = []
    f = open("dates.txt", "r")

    for x in f:
        myDates.append(x)
    f.close()


    print("Moving the window one spot to the right.")
    # append to list but first remove first value from list and get the next day that should be in our sliding window.

    # delete yesterday's calendar entry.
    # convert myDates[0] (yesterdays date into actual date)
    yesterday = datetime.strptime (myDates[0].strip ('\n'), "%Y-%m-%d").date ( )

    myDates.pop (0)
    today = date.today()
    nextDayInWindow = today + timedelta (days=30)

    myDates.append (str (nextDayInWindow) + '\n')

    # so with our new myDates file we can write them to our file.

    f = open ("dates.txt", "w")

    for day in myDates:
        f.write (day)

    f.close ( )

    myDates.clear()
