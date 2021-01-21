num1, num2 = list(map(int, input().split()))

userlist1 = []
for _ in range(num2):
    user_list = list(map(float, input().split()))
    userlist1.append(user_list)

zipped = list(zip(*userlist1))
print(zipped)
for i in zipped:
    print(sum(i)/num2)


