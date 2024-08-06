#Date extraction tool

import re

text = "07/04-2552 08.04.2552 29/02/290 29/02/2400 2.6.3851 31/04/2900 29/02/3712 31/01/2900"

#Regex pattern that's being used on variable text. Years can range from 1000 to 9999
date_regex = re.compile(r"""
    ([1-9]|0[1-9]|[12][0-9]|3[01])       #day
    ([/.-])                              #seperator
    ([1-9]|0[1-9]|1[0-2])                #month
    \2                                   #seperator
    (\d{4})                              #year
""", re.VERBOSE)
matches = date_regex.findall(text)

correct_dates = []
incorrect_dates = []

#Checking for valid dates (excluding leap days initially)
for i in matches:
    day, sep, month, year = i[0], i[1], i[2], i[3]
    date = (day, month, year)
    day, month, year = int(day), int(month), int(year), 
    if (month in [4, 6, 9, 11] and day == 31) or (month == 2 and day > 29):
        incorrect_dates.append(f"{day:02d}{sep}{month:02d}{sep}{year}")
        continue

#Checking for valid leap year dates
    if month == 2 and day == 29:
        if not(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
            incorrect_dates.append(f"{day:02d}{sep}{month:02d}{sep}{year}")
            continue

    correct_dates.append(f"{day:02d}{sep}{month:02d}{sep}{year}")

print("Incorrect dates found:".center(40, '-'))
for i in incorrect_dates:
    print(f" - {i}")
print("Correct dates found:".center(40, '-'))
for i in correct_dates:
    print(f" - {i}")
