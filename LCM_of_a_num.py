'''
Author: Aditya Mangal 
Date:  20 september,2020
Purpose: python practise problem

'''
user = int(input('Enter your number\n'))
user_2 = int(input('Enter the secound number\n'))

maxnum = max(user,user_2)
# print(maxnum)

while True:
    if(maxnum%user == 0 and maxnum%user_2 == 0):
        break

    maxnum +=1

print(f'LCM is {maxnum}')

