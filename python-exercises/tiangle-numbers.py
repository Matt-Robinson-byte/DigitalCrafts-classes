counter = 0
last_counted = 1
i = 0
while i < 100:
    print(counter + last_counted)
    counter += 1
    last_counted += counter 
    i += 1