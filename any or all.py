user = int(input())
user_list = input().split()

print(all(int(i) > 0 for i in user_list) and j[::-1] in user_list)
