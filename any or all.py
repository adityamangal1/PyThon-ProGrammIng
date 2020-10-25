user = int(input())
user_list = input().split()

print(all(int(i) > 0 for i in user_list)
      and any(j == j[::-1] for j in user_list))
