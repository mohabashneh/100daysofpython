second = 1
minute = second * 60
hour = minute * 60
day = hour * 24
NormalYear = day * 365
LeapYear = day * 366
year = input("Is it a normal or a leap year? ")
if year == "Normal" or year == "normal":
    print("A normal year has", NormalYear, "seconds")
else:
    print("A leap year has", LeapYear, "seconds")