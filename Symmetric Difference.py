usrer_in = int(input())
set1 = set(list(map(int, input().split())))
usrer_in2 = int(input())
set2 = set(list(map(int, input().split())))
a = sorted(set1.difference(set2))
b = sorted(set2.difference(set1))
final_list = [a[i] for i in range(len(a))]
for i in range(len(b)):
    final_list.append(b[i])

final_list = sorted(final_list)
for i in range(len(final_list)):
    print(final_list[i])
