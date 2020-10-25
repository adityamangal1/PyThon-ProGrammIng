from collections import defaultdict
user_in = list(map(int, input().split()))
n, m = user_in[0], user_in[1]
userdict = defaultdict(list)

for i in range(1, n+1):
    userdict[input()].append(i)

a = []
for j in range(m):
    us = input()
    a.append(us)

for k in a:
    if k in userdict.keys():
        print(*userdict[k])
    else:
        print('-1')

