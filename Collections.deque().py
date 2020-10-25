from collections import deque
if __name__ == "__main__":

    final_list = deque()
    n = int(input())
    for i in range(n):

        user_input = input().split()

        if user_input[0] == 'append':
            final_list.append(int(user_input[1]))
        elif user_input[0] == 'appendleft':
            final_list.appendleft(int(user_input[1]))
        elif user_input[0] == 'pop':
            final_list.pop()
        elif user_input[0] == 'popleft':
            final_list.popleft()

        else:
            print('Something gone wrong!')

    for i in range(len(final_list)):
        print(final_list[i],end=" ")


