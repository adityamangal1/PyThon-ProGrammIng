'''
Author: Aditya Mangal 
Date:  5 october,2020
Purpose: python practise problem

'''

from collections import Counter

user = int(input())
l1 = list(map(int, input().split()))

# print()
dict = Counter(l1)
userin = int(input())
p = 0
print(dict)
for _ in range(userin):
    shoe, cost = list(map(int, input().split()))
    if dict[shoe]:
        dict[shoe] -= 1
        p += cost
        print(dict)


print(p)
