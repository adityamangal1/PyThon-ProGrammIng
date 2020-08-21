print("WELCOME!\nTHIS IS A NUMBER GUESSING QUIZ ")
num = 30
num_of_guesses = 1
guess = input("ARE YOU A KID?\n")

while(guess != num):
    guess = int(input("ENTER THE NUMBER TO GUESS\n"))
    if guess > num:

        print("NOT CORRECT")
        print("LOWER NUMBER PLEASE!")
        num_of_guesses += 1

    elif guess < num:
        print("NOT CORRECT")
        print("HIGHER NUMBER PLEASE!")
        num_of_guesses += 1 

    else:
        print("CONGRATULATION! YOU GUESSED THE NUMBER ")
        print("THE NUMBER IS ", num)
        print(num_of_guesses, "ATTEMPTS YOU USED TO ARIVE AT THE NUMBER ")
