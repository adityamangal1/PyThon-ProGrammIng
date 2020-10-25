from collections import Counter
user = int(input())
list1 = []
for i in range(user):
    user1 = input()
    list1.append(user1)

a = Counter(list1)
print(len(a))
for i in a.values():
    print(i, end=" ")