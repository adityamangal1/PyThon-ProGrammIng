'''
Author: Aditya Mangal 
Date:  21 september,2020
Purpose: python practise problem

'''
# reduce function
# from functools import reduce


# def add(a, b):
#     return a + b


# sum = reduce(add, [1, 2, 3, 4])
# print(sum)

# map function

def factorial(n):

    fact = 1
    for i in range(n):
        fact *= i+1

    return fact


list1 = [5, 6, 4, 6, 8, 19, 34]

print(list(map(factorial, list1)))
