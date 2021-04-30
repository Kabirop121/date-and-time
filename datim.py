# pip install datetime


import datetime

minyear = datetime.MINYEAR  # The smallest year number allowed in a date or datetime object. MINYEAR is 1.
print(minyear) 

maxyear = datetime.MAXYEAR # The largest year number allowed in a date or datetime object. MAXYEAR is 9999.

# GET CURRENT TIME AND DATE

'''
1ST VALUE = YEAR
2ND '' = MONTH
3RD '' = DATE
4TH '' = HOURS
5TH '' = MINUTES
6TH '' = SECONDS
7TH '' = MINI SECONDS 

'''

dat = datetime.datetime.now()

print(dat)


# strftime() - strftime is a method which is used to take on parameter, format, to specify the format for returned string.

# How to use strftime()

y = datetime.datetime.now()

# HERE WE TAKE THREE PARAMETER (%A = FULL NAME OF WEEKDAY, %B = FULL NAME OF MONTH, %Y = YEAR FULL VERSION)

print(y.strftime("%A-%B-%Y"))

# NOTE = USE % SYMBOL BEFORE YOU USE A PARAMETER IN strftime()
# CHECK NEXT FILE TO GET NAMES OF ALL PARAMETERS
