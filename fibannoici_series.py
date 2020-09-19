
'''
Author: Aditya Mangal 
Date:  19 september,2020
Purpose: python practise problem

'''


def iter_method(number):

    prevnum = 0
    currentnum = 1

    for i in range(1, number):
        prevprevnum = prevnum
        prevnum = currentnum
        currentnum = prevprevnum + prevnum

    return currentnum


if __name__ == "__main__":

    user = int(input('Enter your number\n'))
    fib_num = iter_method(user)
    print(f'Your number on fib({user}) is {fib_num}')

# 0 1 1 2 3 5