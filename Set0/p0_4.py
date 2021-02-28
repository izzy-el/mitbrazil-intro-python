year = 2021
month = 2
day = 1

#w0 = saturday
#w1 = sunday
#w2 = monday
#w3 = tuesday
#w4 = wednesday
#w5 = thursday
#w6 = friday


if(month == 1 or month == 2):
    year -= 1
    month += 12

yearCentury = year % 100
century = int(year / 100)

out = ((day + int(13 * (month + 1) / 5)) + yearCentury + int(yearCentury / 4) + int(century / 4) - (2 * century)) % 7

print(out)
