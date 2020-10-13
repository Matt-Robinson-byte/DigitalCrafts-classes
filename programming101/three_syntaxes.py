person = "Matt"
today = "Tuesday"
emotion = "Happy"
print(f"""Hello {person}, 
I hope that your {today} is going well. 
I'm personally really {emotion}.""")
print("Hello "+ person+ " \nI hope that your "+today+" is going well.\nI'm personally really "+ emotion)
print("Hello %s,\nI hope that your %s is going well.\nI'm personally really %s" % (person,today,emotion))