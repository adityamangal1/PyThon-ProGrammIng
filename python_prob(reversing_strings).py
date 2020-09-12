user_input = int(input("How many numbers are their in list?\n"))
input_list = []

# i = 1
for i in range(user_input):
    # i = 1
    user_input2 = int(input(f'Enter your {i + 1} number in the list.\n'))
    # i = i + 1
    input_list.append(user_input2)
    # i += 1

print("Your given list is", input_list)
reverse = input_list[::]
reverse.reverse()
print("The reverse of your list is", reverse)
# print(input_list)

reverse2 = input_list[::-1]
print("The reverse of your list is", reverse2)

reverse3 = input_list[:]
for i in range(len(reverse3)//2):
    reverse3[i], reverse3[len(reverse3) - i -
                          1] = reverse3[len(reverse3) - i - 1], reverse3[i]

print("The reverse of your list is", reverse3)
