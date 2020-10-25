
# find the secound runner up
user2 = list(map(int, input().split()))
print(user2)
list = [i for i in user2 if i != max(user2)]
print(max(list))

user = list(map(int, input().split()))
print(user)


marksheet = []
scorelist = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet += [[name, score]]
        scorelist += [score]
    # b = sorted(list(set(scorelist)))[1]

    # for n, s in sorted(marksheet):
    #     if s == b:
    #         print(n)
