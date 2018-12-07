a= [ 0, 0, 0.55, 0, 0 ]

def findUniq(arr):
    newarray=[]
    mydic = dict()
    for numbers in arr:
        mydic[numbers]=arr.count(numbers)
        if mydic[numbers] <= 1:
            newarray.append(numbers)
    return newarray[0]

print findUniq([ 1, 1, 1, 2, 1, 1])

#second Solution

def find_uniq(arr):
    # your code here
    arr.sort()
    if(arr[0] < arr[len(arr)-1] and arr[0] < arr[len(arr)-2]):
        n = arr[0]
    else:
        n = arr[len(arr)-1]
    return n   # n: unique integer in the array

#3rd solution
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
