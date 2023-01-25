sday,smonth,syear = input().split("-")

day = int(sday)
month = int(smonth)
year = int(syear)

dayOfMonth = [31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(_month):
    if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        return True
    else: 
        return False

if(is_leap(month)):
    dayOfMonth[1] = 29
    
print(dayOfMonth)    
def day_of_year(_day,_mount,_year):
    _returnDay = 0
    for _days in range(_mount - 1):
        _returnDay += dayOfMonth[_days]
    _returnDay += _day
    return _returnDay

print(day_of_year(day,month,year))
