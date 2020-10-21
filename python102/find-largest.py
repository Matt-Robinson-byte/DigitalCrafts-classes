
def largest(numbers):
    last_number = numbers[0]
    for number in numbers:
        if number > last_number:
            last_number = number
        else:
            last_number = last_number
    return last_number

print(largest([65,1,2,9,8,6,45,3,4,5,6,89]))