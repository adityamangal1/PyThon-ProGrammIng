marksheet = []
scores = []
n = int(input())
for _ in range(n):
    name = input()
    score = float(input())
    marksheet += [[name, score]]
    scores += [score]

li = sorted(set(scores))[1]

for n, s in marksheet:
    if s == li:
        print(n)
