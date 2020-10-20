lista = ["dog", "cat","hat","pants","dog","shirt","hat"]
new_list = []
for item in lista:
    if not item in new_list:
        new_list.append(item)
    
print(new_list)