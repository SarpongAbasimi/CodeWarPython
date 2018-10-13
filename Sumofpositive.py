list=[-1,2,3,4,-5]

def positive_sum(arr):
    count=0 #count is an accumulator
    for i in range(len(arr)): #loop through the lenght of the list
        if (arr[i]>0): #check if the element is greater than 0
            count += arr[i] #if it is add it to count
    return count #return count



print positive_sum(list)
