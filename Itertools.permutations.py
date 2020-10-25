
'''
Author: Aditya Mangal 
Date:  5 october,2020
Purpose: python practise problem

'''
from itertools import permutations

x = word, num = input().split()
a = list(permutations(word, int(num)))

b = list(map(list, a))

final_list = []
for i in range(len(b)):
    final_list.append(''.join(b[i]))

a = sorted(final_list)  # sorted function
for i in range(len(a)):
    print(a[i])
