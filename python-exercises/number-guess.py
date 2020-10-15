import random

play_again = True
print("I am thinking of a number between 1 and 10")
while play_again:
    secret_num = random.randint(1, 10)
    guess_number = 0
    guess_counter = 0 
    while guess_number != secret_num and guess_counter < 5:
        guess_number = int(input("What's the number? "))
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
    answer = input("Do you want to play again? (Y or N)")
    if answer == 'N':
        play_again = False
