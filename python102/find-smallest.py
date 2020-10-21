def smallest(numbers):
    for number in numbers:
        last_number = numbers[0]
        if number < last_number:
            last_number = number
        else:
            last_number = last_number
    return last_number

print(smallest([2,2,3,4,5,6,7,78]))