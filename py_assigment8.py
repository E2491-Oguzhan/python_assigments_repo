year = int(input("Enter a year to be checked: "))

if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "is a Leap year.")

else:
    print(year, "is not a Leap year!")
