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
    print('\t\tHello!')
    user = int(input('How many numbers are there in your list?\n'))
    user_list = []

    for i in range(user):
        user_list_input = int(
            input(f'Enter your {i+1} number in your list.\n'))
        user_list.append(user_list_input)

    for i in range(user):

        if user_list[i] > 10:

            print(
                f'Your next palindrome of number {user_list[i]} is {next_palindrome(user_list[i])}.\n')

        elif user_list[i] < 10:
            # exit()
            print(f'Your number {user_list[i]} is lesser than 10 so palindrome cant be find.\n')

        else:
            print('Something gone Wrong!')
