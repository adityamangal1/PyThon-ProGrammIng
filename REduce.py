from fractions import Fraction
from functools import reduce


def product(fracs):
    print(fracs)
    t = reduce(lambda x, y: x * y, fracs)
    print(t)
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = [Fraction(*map(int, input().split())) for _ in range(int(input()))]
    result = product(fracs)
    print(*result)
