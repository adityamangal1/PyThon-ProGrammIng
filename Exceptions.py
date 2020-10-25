'''
Author: Aditya Mangal 
Date:  5 october,2020
Purpose: python practise problem

'''

user_in = int(input())

for i in range(user_in):
    first, secound = list(map(str, input().split()))

    try:
        a = int(first) // int(secound)
        print(a)

    except ValueError as f:
        print("Error Code:", f)

    except ZeroDivisionError as e:

        print("Error Code:", e)


