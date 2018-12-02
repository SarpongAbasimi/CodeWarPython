def accum(s):
    newList=[]
    splitInput =list(s[:].lower())
    for i in range(len(splitInput)):
        newList.append((splitInput[i] * (i+1)).capitalize())
    return "-".join(newList)

print accum("ZpglnRxqenU")