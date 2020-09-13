'''
Author: Aditya Mangal 
Date:  13 september,2020
Purpose: python practise problem

'''

import random


def rohan_function(number):

    wrong = random.randint(1, 9)
    list = [number*(i+1) for i in range(10)]
    list[wrong] = list[wrong] + random.randint(1, 10)
    return list


def is_correct(table, number):
    for i in range(1, 11):
        if table[i-1] != i*number:
            return i - 1

        else:
            None


if __name__ == "__main__":
    print('Welcome!')
    user_input = int(input('Enter the number whose table you want?\n'))
    mytable = rohan_function(user_input)
    print(mytable)
    wrong = is_correct(mytable, user_input)
    print(f'table is wrong at index {wrong}.')
