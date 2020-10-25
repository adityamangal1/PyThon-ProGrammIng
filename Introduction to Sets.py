
'''
Author: Aditya Mangal 
Date:  3 october,2020
Purpose: python practise problem

'''


def average(array):

    a = set(array)
    b = (sum(a))/len(a)
    return b


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
