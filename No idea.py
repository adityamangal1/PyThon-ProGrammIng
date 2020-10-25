n, m = list(map(int, input().split()))
array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(sum((i in A) - (i in B) for i in array))


