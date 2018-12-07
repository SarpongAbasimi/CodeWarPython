import math

def centuryFromYear(year):
    newYear=year/float(100)
    return int(math.ceil(newYear))

print (centuryFromYear(number))
