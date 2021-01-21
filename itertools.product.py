
'''
Author: Aditya Mangal 
Date:  5 october,2020
Purpose: python practise problem

'''
from itertools import product


def product_lists(A, B):

    a = list(product(A, B))
    convert_list = list(map(str, a))
    return ' '.join(convert_list)


x = a1, *a2 = input().split()
y = b1, *b2 = input().split()
A = list(map(int, x))
B = list(map(int, y))

final_ans = product_lists(A, B)
print(final_ans)
