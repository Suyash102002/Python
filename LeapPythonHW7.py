year = 2015
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("This is leap year")
else:
     print("This is not leap year")