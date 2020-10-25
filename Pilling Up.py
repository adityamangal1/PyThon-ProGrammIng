def pillingup():
    user_in = int(input())
    user_list = list(map(int, input().split()))
    if len(user_list) % 2 == 0:
        print('Yes')
    else:
        print('No')


user = int(input())
for i in range(user):
    pillingup()
