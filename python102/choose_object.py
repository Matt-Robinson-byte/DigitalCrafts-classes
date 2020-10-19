four_things = ["phone", "mask", "desk", "window"]
four_pithy_messages = ["calling people", "Bane", "writing", "fresh air"]
choice = int(input("Choose a number from 0-3: "))
if choice >= 0 and choice < len(four_things):
    print(f"You chose {four_things[choice]}, you must love {four_pithy_messages[choice]}")
else:
    print("Your choice is invalid!")