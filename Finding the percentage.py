marksheet = []
scores = []
dict1 = {}
user = int(input())
for _ in range(user):
    x = name, *score = input().split()
    b = list(map(float, score))
    dict1[name] = b

user_input = input()
li = dict1[user_input]
a = sum(li)/3
print('{0:.2f}'.format(a))
