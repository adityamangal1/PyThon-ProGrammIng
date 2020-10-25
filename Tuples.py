if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))

    print(integer_list)
    a = tuple(integer_list)
    print(a)
    print(hash(a))

    
