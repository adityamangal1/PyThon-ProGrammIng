# !/bin/python3

import math
import os
import random
import re
import sys


def solve(s):
    # list1 = []
    for _ in range(len(s)):
        # list1.append(s[i].capitalize())
        list1 = [word.capitalize() for word in s.split(' ')]
    return (' '.join(list1))


if __name__ == '__main__':
    with open(os.environ['hello'], 'w') as fptr:
        s = input()

        result = solve(s)

        fptr.write(result + '\n')
