
def maskify(cc):
    if len(cc) < 4:
        return cc
    else:
        index = 0
        my_array=[]
        convertToString =str(cc)
        for i in convertToString:
            my_array.append(i)
        myArray_Lenght=len(my_array)
        for everyting in my_array:
            my_array[index]
            index += 1
        for i in range(myArray_Lenght -4):
            my_array[i]="#"
        return my_array




