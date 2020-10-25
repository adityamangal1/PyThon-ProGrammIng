'''
Author: Aditya Mangal 
Date:  5 october,2020
Purpose: python practise problem

'''
user = input()
user2 = int(input())

subsequent = int(len(user)//user2)
for i in range(subsequent):

    slicing = user[i * user2:(i + 1) * user2]

    u = ""
    for c in slicing:
        if c not in u:
            u += c

    print(u)


# print(dict.fromkeys(list))
