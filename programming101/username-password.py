username = "Matthew"
password = "Robinson"
name = ""
pwd = ""
counter = 0
while name != username and pwd != password and counter != 3:
    name = input("Please enter your username:\n")
    pwd = input("Please enter your password:\n")
    counter += 1
    if counter == 3:
        print("You have exhausted your chances!!")
print("You have entered chosen wisely!!")

