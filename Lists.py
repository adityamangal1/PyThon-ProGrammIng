if __name__ == "__main__":

    final_list = []
    n = int(input())
    for i in range(n):

        user_input = input().split()

        if user_input[0] == 'insert':
            final_list.insert(int(user_input[1]), int(user_input[2]))
        elif user_input[0] == 'print':
            print(final_list)
        elif user_input[0] == 'pop':
            final_list.pop()
        elif user_input[0] == 'sort':
            final_list.sort()

        elif user_input[0] == 'remove':
            final_list.remove(int(user_input[1]))

        elif user_input[0] == 'append':
            final_list.append(int(user_input[1]))

        elif user_input[0] == 'reverse':
            final_list.reverse()

        else:
            print('Something gone wrong!')
