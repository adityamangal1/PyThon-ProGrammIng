from collections import namedtuple

user  = int(input())
data = namedtuple('data', input().split())

# print(data(*input().split().MARKS))

s = 0
for i in range(user):
    s += int(data(*input().split()).MARKS)

print(s/user)

