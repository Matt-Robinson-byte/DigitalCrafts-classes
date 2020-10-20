def movie(dictionary):
    i = 1
    for item in dictionary:
        print(f"{i}. {item} : {dictionary[item]}")
        i += 1

movie({"Title" : "Goonies","Genre" : "Family","Year" : 1986})