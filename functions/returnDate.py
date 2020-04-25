# Import time and date library
import time as tm
import datetime as dt
# end

# Function that returns current date and time
def returnDate (date):

    date=f"{dt.datetime.now():%a, %b %d %Y}"
    return (date)
