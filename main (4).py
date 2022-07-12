def is_year_leap(year):
    if year %4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_year_leap(year) and month == 2:
        return 29
    return days[month - 1]

def day_of_year(year, month, day):
    if year < 1582:
        return None
    if month > 12 or month < 1:
        return None
    if day < 1 or day > days_in_month(year,month):
        return None
        
    # Calculamos los dias
    totalDays = day
    month -= 1
    while month > 0:
        totalDays += days_in_month(year,month)
        month -= 1
    return totalDays

print(day_of_year(1500, 11, 35))
