
user = int(input())
user_list = set(list(map(int, input().split())))
user2 = int(input())
user_list2 = set(list(map(int, input().split())))
print(len(user_list.symmetric_difference(user_list2)))
