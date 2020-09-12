'''
Author: Aditya Mangal 
Date:  12 september,2020
Purpose: python practise problem

'''


def next_palindrome(number):
    number += 1
    while not is_palindrome(number):
        number += 1
    return number


def is_palindrome(number):
    return str(number) == str(number)[::-1]


if __name__ == '__main__':
    user = int(input('How many numbers are there in your list?\n'))
    user_list = []

    for i in range(user):
        user_list_input = int(
            input(f'Enter your {i+1} number in your list.\n'))
        user_list.append(user_list_input)

    for i in range(user):
        print(
            f'Your next palindrome of {user_list[i]} is {next_palindrome(user_list[i])}.\n')
