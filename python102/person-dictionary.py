person = {
    "first_name": "Matthew",
    "last_name": "Robinson",
    "age": 36,
    "hair_color":"blonde"
}
for item in person:
    print(person[item])
print(f"Hello {person['first_name']} {person['last_name']}.  Since you are {person['age']}, you can ride this ride.  You have awesome {person['hair_color']} hair")