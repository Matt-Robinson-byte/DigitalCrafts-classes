numbers = [-10,1,2,9,8,6,45,3,4,5,6,-9]
last_number = 0
for number in numbers:
    if number < last_number:
        last_number = number
    else:
        last_number = last_number
print(last_number)