# Checking for the leap year
# leap year occurs in the year that is multiple of 4
# except for years evenly divisible by 100 and should be divisible by 400


def check_leap_year(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    else
        return False

year = 2024

if check_leap_year(year):
    print("yes")
else:
    print("no")

