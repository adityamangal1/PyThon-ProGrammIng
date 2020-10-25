from collections import Counter

user = sorted(input())
a = Counter(user).most_common(3)

for key, value in a:
    print(key, value)
