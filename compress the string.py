from itertools import groupby

user = input()
for key, group in groupby(user):
    a = len(list(group)), int(key)
    print(tuple(a))
