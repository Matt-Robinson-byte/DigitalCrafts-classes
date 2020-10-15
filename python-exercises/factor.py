number = int(input("Enter a number to factor: "))
dividor = 1
while dividor <= number:
    if (number % dividor) == 0:
        print (dividor)
    dividor += 1