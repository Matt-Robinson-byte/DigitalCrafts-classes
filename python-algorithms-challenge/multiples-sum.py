i = 1 
total = 0
while i <= 1000:
    if i % 3 == 0 or i % 5 == 0:
        total = total + i
        print(total)
    i += 1