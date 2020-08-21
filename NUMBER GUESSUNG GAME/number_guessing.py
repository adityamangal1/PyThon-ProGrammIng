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
            print("YOU LOSE! BETTER LUCK NEXT TIME. ")
            break


print("WELCOME!\n\t\t\tTHIS IS A NUMBER GUESSING QUIZ AND \b YOU HAVE ONLY 9 LIFE TO WIN.\t\t\t\t  ")
num = 30
num_of_guesses = 0
number_guess(num_of_guesses,num)
print("WANT TO PLAY AGAIN?\nType y for yes and n for no : ")
again = input()

if again == "y":
# while ag ain=='y':

    number_guess(num_of_guesses,num)
    again.capitalize()
    # number_guess(num_of_guesses,num)
else:
    again.capitalize()
    print("THANK YOU FOR PLAYING!!\nCOME BACK SOON.")    