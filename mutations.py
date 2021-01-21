def mutate_string(string, position, character):
    print(string)
    return string[:position] + character + string[position + 1:]


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    print(int(i))
    print(c)
    s_new = mutate_string(s, int(i), c)
    print(s_new)
