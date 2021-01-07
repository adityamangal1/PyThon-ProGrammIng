'''
Author: Aditya Mangal 
Date:  17 september,2020
Purpose: python mini project

'''
import string
import random


if __name__ == '__main__':

    s = string.ascii_lowercase
    # print(s)
    s2 = string.ascii_uppercase

    s3 = string.digits
    # print(s3)

    pass_len = int(input('Enter the length of your password.\n'))
    pass_list = []
    pass_list.extend(list(s))
    pass_list.extend(list(s2))
    pass_list.extend(list(s3))

    random.shuffle(pass_list)
    # print(pass_list)

    pass_generated = "".join(pass_list[0:pass_len])

    print(f'Password generated!\nYour password is {pass_generated}')
