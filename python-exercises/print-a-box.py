height = int(input("Enter a height: "))
width = int(input("Enter a width: "))
print("*" * width)
while height - 2 > 0:
    print("*" + ' ' * (width - 2) + "*")
    height -= 1
print("*" * width)