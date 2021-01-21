from collections import namedtuple

user  = int(input())
data = namedtuple('data', input().split())

# print(data(*input().split().MARKS))

s = sum(int(data(*input().split()).MARKS) for _ in range(user))
print(s/user)

