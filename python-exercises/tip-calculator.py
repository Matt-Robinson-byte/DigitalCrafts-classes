total = int(input("Enter bill total: "))
level_service = (input("Enter level of Service: "))
service_list = ["good","fair","bad"]
index = service_list.index(level_service)
perc = 0
if index == 0:
    perc = 0.20
elif index == 1:
    perc = 0.15
else:
    perc = 0.10
tip = total*perc
print("Tip amount: $" + str(tip))
print("Total amount: $" + str(total + tip))