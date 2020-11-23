import datetime
import calendar

def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %y')
    day = born.weekday()
    return (calendar.day_name[day])


#day of month
date = '24 06 1998'
print(findDay(date))