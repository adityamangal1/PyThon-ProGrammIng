if __name__ == "__main__":
    user_inpu = int(input())
    user_list = list(map(int, input().split()))
    user_list = set(user_list)
    n = int(input())
    for _ in range(n):
        user_input = input().split()
        if user_input[0] == 'pop':      
            user_list.pop()
        elif user_input[0] == 'discard':
            user_list.discard(int(user_input[1]))
        elif user_input[0] == 'remove':
            user_list.remove(int(user_input[1]))
        else:
            print('Something gone wrong!')

    a = sum(user_list)
    print(a)




