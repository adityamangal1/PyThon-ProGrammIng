if __name__ == "__main__":
    user_inpu = int(input())
    user_list = list(map(int, input().split()))
    user_list = set(user_list)
    n = int(input())
    for _ in range(n):
        user_input = input().split()
        if user_input[0] == 'intersection_update':
            new_list = list(map(int, input().split()))
            user_list.intersection_update(new_list)
        elif user_input[0] == 'symmetric_difference_update':
            new_list2 = list(map(int, input().split()))
            user_list.symmetric_difference_update(new_list2)
        elif user_input[0] == 'difference_update':
            new_list3 = list(map(int, input().split()))
            user_list.difference_update(new_list3)
        elif user_input[0] == 'update':
            new_list4 = list(map(int, input().split()))
            user_list.update(new_list4)
        else:
            print('Something gone wrong!')

    a = sum(user_list)
    print(a)
