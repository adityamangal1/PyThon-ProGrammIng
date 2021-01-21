user_input = input().swapcase()
user_list = user_input.split()
string = ''.join(user_list[i]+' ' for i in range(len(user_list) - 1, -1, -1))
print(string)