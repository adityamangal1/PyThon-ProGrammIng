def checking_subset():
    user_in = int(input())
    set1 = set(list(map(int, input().splitl())))
    user_in2 = int(input())
    set2 = set(list(map(int, input().splitl())))
    print(set1.issubset(set2))


user = int(input())
for i in range(user):
    checking_subset()
