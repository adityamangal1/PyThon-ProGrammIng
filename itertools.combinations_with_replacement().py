from itertools import combinations_with_replacement

word, num = input().split()
n = int(num)
s = sorted(word)

a = list(combinations_with_replacement(s,n))
a = sorted(a)
for i in range(len(a)):
    print(''.join(a[i]))

