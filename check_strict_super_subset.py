set1 = set(list(map(int, input().split())))
user = int(input())
new_list =[]
for _ in range(user):
    set2 = set(list(map(int, input().split())))
    new_list.append(set2)

for i in range(len(new_list)):
    new_list[i] = set(new_list[i])

a = new_list[0]
b = new_list[1]

a1 = set1.issuperset(a)
b1 = set1.issuperset(b)

if a1 is True and b1 is True:
    print('True')
else:
    print('False')


