'''
Author: Aditya Mangal 
Date:  5 october,2020
Purpose: python practise problem

'''
import re

user = int(input())
for i in range(user):

    try:

        print(bool(re.compile(input())))
    except re.error as e:
        print("False")
