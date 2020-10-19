import random
answer = True
play_again = True
while play_again:
    print("I am thinking of a number between 1 and 10")
    secret_num = random.randint(1, 10)
    guess_number = 1
    guess_counter = 0 
    while guess_number != secret_num and guess_counter < 5:
        while True:
            try:
                guess_number = int(input("What's the number? "))
                break
            except ValueError:
                print("Oh no!! That's not a number!")
        guess_counter += 1
        if guess_number > secret_num:
            print(f"{guess_number} is to high.")
        elif guess_number < secret_num:
            print(f"{guess_number} is to low.")
        else:
            print("Yes!! You Win!!")
        if guess_counter < 5 and guess_number != secret_num:
            print(f"You have {5 - guess_counter} guesses left")
        elif guess_counter and guess_number != secret_num:
            print("You have no guesses left")
    while answer != 'Y' or answer != 'N':
        answer = input("Do you want to play again? (any key to play or N to quit)")
        if answer == 'N':
            play_again = False
            break
        elif answer == 'Y':
            play_again = True
            break
        else:
            print("I didn't get that")
