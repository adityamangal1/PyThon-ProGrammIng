def number_guess(num_of_guesses, num):

    while(num_of_guesses != 9):

        guess = int(input("ENTER THE NUMBER TO GUESS :-\n"))
        if guess > num:

            num_of_guesses += 1
            print("LOWER NUMBER PLEASE!")
            print("BE PATIENT, TRY AGAIN!")
            print("YOU USED YOUR", num_of_guesses, "LIFE.")

        elif guess < num:

            num_of_guesses += 1
            print("HIGHER NUMBER PLEASE!")
            print("BE PATIENT, TRY AGAIN!")
            print("YOU USED YOUR", num_of_guesses, "LIFE.")
        else:
            print("HURRAY! YOU GUESSED THE NUMBER. ")
            print("THE NUMBER YOUR OPPONENT CHOOSES IS ", num)
            print("YOU GUESSED THE NUMBER IN", num_of_guesses + 1, "ATTEMPTS ")
            break

        if num_of_guesses == 9:
            print("GAME OVER!")
            print("YOU LOSE! BETTER LUCK NEXT TIME.")
            # break

    restart_game()


def restart_game():
    print("WANT TO PLAY AGAIN?\nType y for yes and n for no : ")

    again_play = input()
    if again_play == "y":

        number_guess(num_of_guesses, num)
    else:

        print("THANK YOU FOR PLAYING!!\nCOME BACK SOON.")


print("\tWELCOME BUDDY!!\n\t\t\t*****THIS IS A NUMBER GUESSING QUIZ*****\t\t\t\t")
print("\t\t\t  --TO WIN THIS YOU HAVE ONLY 9 LIFES-- ")
num = 30
num_of_guesses = 0
number_guess(num_of_guesses, num)
