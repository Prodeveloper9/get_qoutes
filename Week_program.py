import calendar as calend

print("Enter the date you want and you will know what day you were born.")

try:
    year = int(input("Year ====>\t"))
    month = int(input("Month ====>\t"))
    day = int(input("Day ====>\t"))
except ValueError:
    print("Enter a number not a text.")

calender = calend.weekday(year, month, day)


if calender == 0:
    print("The day you were born is monday.")
elif calender == 1:
    print("The day you were born is tuesday.")
elif calender == 2:
    print("The day you were born is wednesday.")
elif calender == 3:
    print("The day you were born is thursday.")
elif calender == 4:
    print("The day you were born is friday.")
elif calender == 5:
    print("The day you were born is saturday.")
elif calender == 6:
    print("The day you were born is sunday.")
else:
    print("ERROR!!!!!!!!!!!!!!\nPlease try again because we have probleme")

