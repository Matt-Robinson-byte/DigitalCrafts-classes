run = True
coins = 0
while run:
    print(f"You have {coins} coins.")
    add = input("Do you want a coin? ")
    if add == 'yes':
        coins += 1
    elif add == 'no':
        print("Bye")
        run = False