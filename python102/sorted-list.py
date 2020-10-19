list_title = ["meat","veggies", "other"]
i = 0
j = 0
index = 1
list_of_lists = [
    ["chicken","beef","pork"],
    ["tomatoes", "potatos","carrots"],
    ['milk','eggs','cheese','yogurt']
]
for element in list_title:
    print(index,element)
    index += 1
    for element in list_of_lists[j]:
        print(i + 1,element)
        i += 1
    j += 1
    i = 0
j = 0
