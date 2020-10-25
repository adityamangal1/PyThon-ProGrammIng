# !/bin/python3

import math
import os
import random
import re
import sys


def solve(s):
    # list1 = []
    for i in range(len(s)):
        # list1.append(s[i].capitalize())
        list1 = [word.capitalize() for word in s.split(' ')]
    a = (' '.join(list1))
    return a


if __name__ == '__main__':
    fptr = open(os.environ['hello'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
