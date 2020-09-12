import random

# print(rand_num)


def guess_game_player1(n):

    user_input = input(
        'Its layer1 turn first to play.\nType start to start the game.\n')
    if user_input == 'start':

        number_of_guesses = 1
        # number_of_guesses2 = 1
        user_num = ()
        print('layer1: \n')

        while(user_num != n):

            user_num = int(input('Guess any number between 1 to 100\n'))

            if user_num > n:

                print('Wrong Guessed.\nYour number is greater than the actual number.\n')
                number_of_guesses += 1

            elif user_num < n:
                print('Wrong Guessed.\nYour number is shorter than the actual number.\n')
                number_of_guesses += 1

            else:
                print(f'Congratulations!! Yoy guessed it.')
                # print(f'You guessed it in {number_of_guesses} times.')

        return number_of_guesses

    elif user_input == 'exit':
        exit()

    else:
        print('Wrong input!\nGive correct input or type exit to exit.\n ')
        num = random.randint(1, 100)
        guess_game_player1(num)


def guess_game_player2(n):

    user_input = input(
        'Its player2 turn now to play.\nType start to start the game.\n')
    if user_input == 'start':

        number_of_guesses2 = 1
        user_num2 = ()
        print('Player2: \n')
        user_num2 = ()
        while(user_num2 != n):

            user_num2 = int(
                input('Guess any number between 1 to 100\n'))

            if user_num2 > n:

                print('Wrong Guessed.\nYour number is greater than the actual number.\n')
                number_of_guesses2 += 1

            elif user_num2 < n:
                print('Wrong Guessed.\nYour number is shorter than the actual number.\n')
                number_of_guesses2 += 1

            else:
                print(f'Congratulations!! Yoy guessed it.')
                # print(f'You guessed it in {number_of_guesses2} times.')

        return number_of_guesses2

    elif user_input == 'exit':
        exit()

    else:
        print('Wrong input!\nGive correct input or type exit to exit.\n ')
        num2 = random.randint(1, 100)
        guess_game_player2(num2)


if __name__ == "__main__":
    print('\t\t **Number Guessing Game** \n')
    rand_num = random.randint(1, 100)
    print(rand_num)
    Player_1 = guess_game_player1(rand_num)
    rand_num2 = random.randint(1, 100)
    print(rand_num2)
    Player_2 = guess_game_player2(rand_num2)

    if Player_1 > Player_2:
        print(
            f'Player2 is winner as he guessed number earlier in {Player_2}.\n')

    elif Player_1 < Player_2:
        print(
            f'Player1 is winner as he guessed number earlier in {Player_1}.\n')

    elif Player_2 > Player_1:
        print(
            f'Player1 is winner as he guessed number earlier in {Player_1}.\n')

    elif Player_2 < Player_1:
        print(
            f'Player2 is winner as he guessed number earlier in {Player_2}.\n')

    elif Player_1 == Player_2:
        print('Match Draw.\n')
        print(f'Player1 guessed it in {Player_1}.\n')
        print(f'Player2 guessed it in {Player_2}.\n')

    else:
        print('Something Gone Wrong.\n')
print('Hope You Enjoyed.')
