def Descending_Order(num):
    sort =sorted(list(str(num)));
    join="".join(sort)
    return int(join[::-1])
print (Descending_Order(0))


#Better Solutuion
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
