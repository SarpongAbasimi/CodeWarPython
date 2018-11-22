#Square Every Digit

#Welcome. In this kata, you are asked to square every digit of a number.
#For example, if we run 9119 through the function, 811181 will come out,
#because 92 is 81 and 12 is 1.
#Note: The function accepts an integer and returns an integer

import math

def square_digits(num):
     newArray=[]
     split=list(str(num))
     for i in split:
         newArray.append(str(int(math.pow(int(i),2))))
     return int("".join(newArray))





print square_digits(9119)
