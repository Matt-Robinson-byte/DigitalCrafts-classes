width = int(input("Enter a width: "))
space = int(width/2)
star = 1
while star <= width:
    print(' '*(space + 2) + "*" * star)
    space -= 1
    star += 2
    
