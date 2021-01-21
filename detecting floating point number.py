import re
user = int(input())
regex = r'^[+-]?[0-9]*\.[0-9]+$'
for _ in range(user):
    a1 = input()
    print(bool(re.search(regex, a1)))


