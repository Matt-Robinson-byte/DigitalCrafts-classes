my_array = [1,2,4,0,8,0,6,9,0,9,4,5,6,0,3]
my_new_array = []
i  = 0
val = True
while i < len(my_array):
    if my_array[i] != 0:
        my_new_array.append(my_array[i])
    i += 1
while val:
    if len(my_new_array) < len(my_array):
        my_new_array.append(0)
    else:
        val = False
print(f"This was the array {my_array}")
print(f"This is the rearranged array {my_new_array}")