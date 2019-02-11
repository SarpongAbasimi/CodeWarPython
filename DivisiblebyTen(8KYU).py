"""
Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.
Return the amount of numbers in that list that are divisible by 10.
"""

def divisible_by_ten(num):
   return len([nums for nums in num if nums%10==0])


""" 
Example 2
Create a function named add_greetings() which takes a list of strings named names as a parameter.
In the function, create an empty list that will contain each greeting. Add the string 
"Hello, " in front of each name in names and append the greeting to the list.
Return the new list containing the greetings.
"""

def add_greetings(names):
  return ["Hello " + word for word in names]
