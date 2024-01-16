# 1. Write a Python program to find the sum of all multiples of 3 and 5 below 100.
from functools import reduce
sum = 0
def find_sum(limit):
    sum = [sum for sum in range(limit) if sum % 3 == 0 or sum % 5 == 0]         #list comprehension
    result_sum= reduce(lambda x, y: x + y, sum) #lambda function
    print(result_sum)


    

find_sum(100)