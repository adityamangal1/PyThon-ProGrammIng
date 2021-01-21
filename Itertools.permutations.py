
'''
Author: Aditya Mangal 
Date:  5 october,2020
Purpose: python practise problem

'''

from itertools import permutations

x = word, num = input().split()
a = list(permutations(word, int(num)))

b = list(map(list, a))

final_list = [''.join(item) for item in b]
a = sorted(final_list)  # sorted function
for i in range(len(a)):
    print(a[i])
