
"""
Write a function, persistence, that takes in a positive parameter 
num and returns its multiplicative persistence, which is the number of 
times you must multiply the digits in num until you reach a single digit.

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

persistence(4) => 0   # Because 4 is already a one-digit number.

"""


from functools import reduce

def persistence(n,count=0):
    if n < 10 : return 0

    split_n = list(str(n))
    mylambda = lambda  x,y: int(x)*int(y)
    product = reduce(mylambda,split_n)

    if product >= 10:
        count += 1
        return persistence(product,count)
    
    return count+1


#Solutuion 2 

from functools import reduce

def persistence(n):
    if n < 10 : return 0
    
    conter = 0
    while n >= 10: 
        split_n = list(str(n))
        mylambda = lambda  x,y: int(x)*int(y)
        n= reduce(mylambda,split_n)
        conter+= 1
        persistence(n)
    return conter
