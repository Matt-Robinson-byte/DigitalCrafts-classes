pet_name = input("Enter a pet's name:\n")
petname_length = len(pet_name)
if petname_length > 3:
    if pet_name == "Daisy":
        print("Good Dog!")
    elif pet_name == "Shadow":
        print("El Gato Diablo!")
    else:
        print(f"AWWW sweet {pet_name}")
else:
    print(f"Sorry!, {petname_length} is two short!")