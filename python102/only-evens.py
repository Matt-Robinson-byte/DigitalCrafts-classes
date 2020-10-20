def is_even(number):
    if number%2 == 0:
        return True
    else:
        return False

def only_evens(lista):
    new_list = []
    for element in lista:
        if is_even(element):
            new_list.append(element)
    return new_list
print (only_evens([1,2,3,4,5,6,7,8]))