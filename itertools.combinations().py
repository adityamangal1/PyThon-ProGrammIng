from itertools import combinations


def combinations_l(num1):
    b = 1

    while True:

        final = sorted(combinations(word, b))
        a1 = []
        for i in final:
            a = ''.join(sorted(i))
            a1.append(a)
            final = sorted(a1)
        for i in final:
            print(i)
        b += 1
        if b > int(num1):
            break


word, num = input().split()
sorted_list = sorted(word)
b = int(num)
combinations_l(num)
