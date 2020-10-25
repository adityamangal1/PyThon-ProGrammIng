# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

user = int(input())
user_list = set(list(map(int, input().split())))
user2 = int(input())
user_list2 = set(list(map(int, input().split())))
print(len(user_list.union(user_list2)))
