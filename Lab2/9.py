def is_leap(_year):
    if((_year % 4 == 0 and _year % 100 != 0) or _year % 400 == 0):
        return True
    else: 
        return False
  
def day_of_year(_day,_mount,_year):
    _returnDay = 0
    _dayOfMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(_year):
        _dayOfMonth[1] = 29
    
    for _days in range(_mount - 1):
        _returnDay += _dayOfMonth[_days]
    _returnDay += _day
    return _returnDay

def day_in_year(_year):
    return 366 if is_leap(_year) else 365

def day_in_month(_year):
    return [31,29,31,30,31,30,31,31,30,31,30,31] if is_leap(_year) else [31,28,31,30,31,30,31,31,30,31,30,31]

def date_diff(_strDate1,_strDate2):
    _date1 = [int(date) for date in _strDate1.split("-")]
    _date2 = [int(date) for date in _strDate2.split("-")]

    if(_date1[1] <= 0 or _date1[1] > 12  or _date2[1] <= 0 or _date2[1] > 12):
        return -1

    _check_date1 = day_in_month(_date1[2])
    _check_date2 = day_in_month(_date2[2])

    if(_date1[0] <= 0 or _date1[0] > _check_date1[_date1[1] - 1] or _date1[2] <= 0 or
       _date2[0] <= 0 or _date2[0] > _check_date2[_date2[1] - 1] or _date2[2] <= 0):
       return -1

    _returnDateDiff = 0
    for _year in range(_date1[2],_date2[2]):
        _returnDateDiff += day_in_year(_year)
    _returnDateDiff -= day_of_year(_date1[0],_date1[1],_date1[2]) - 1
    _returnDateDiff += day_of_year(_date2[0],_date2[1],_date2[2])
    return _returnDateDiff

print(date_diff("1-1-2018", "1-1-2020"))
