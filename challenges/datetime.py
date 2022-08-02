import datetime
import pytz

pdx = datetime.datetime.now()
pdxopen = "Open"
if (int(pdx.strftime("%H")) < 9) or (int(pdx.strftime("%H")) > 17):
    pdxopen = "Closed"

print("Portland Time is: \n{} {}\nThe office is {}".format(pdx.strftime("%I"),pdx.strftime("%p"),pdxopen))

nytz = pytz.timezone("America/New_York")
nyc = datetime.datetime.now(nytz)
nycopen = "Open"
if (int(nyc.strftime("%H")) < 9) or (int(nyc.strftime("%H")) > 17):
    nycopen = "Closed"

print("New York Time is: \n{} {}\nThe office is {}".format(nyc.strftime("%I"),nyc.strftime("%p"),nycopen))
