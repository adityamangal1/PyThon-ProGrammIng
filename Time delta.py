import os
from datetime import datetime

def time_delta(t1, t2):
    time_format = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, time_format)
    t2 = datetime.strptime(t2, time_format)
    return str(int(abs(t1-t2).total_seconds()))


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        t = int(input())

        for _ in range(t):
            t1 = input()

            t2 = input()

            delta = time_delta(t1, t2)

            fptr.write(delta + '\n')

