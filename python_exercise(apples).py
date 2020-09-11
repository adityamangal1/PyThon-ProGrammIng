user_input = int(input("How many apples do you have?\n"))
min_range = int(input('How many minimum students are there?\n'))
max_range = int(input('How many maximum students are there?\n'))

for i in range(min_range, max_range+1):
    if user_input % i == 0:
        print(f"{i} is divisible by {user_input}.")
        i += 1

    elif user_input % i != 0:
        print(f"{i} is not divisible by {user_input}.")
        i += 1

    else:
        print('Something Wrong Please check!')
