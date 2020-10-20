people = [
{
    "name": "Matthew Robinson",
    "phone": 123456778,
    "email": "matt@email.com"
},
{
    "name": "Michelle Robinson",
    "phone": 123123478,
    "email": "michelle@email.com"
},
{
    "name": "Natalia Robinson",
    "phone": 123888878,
    "email": "natalia@email.com"
}
]
j = 1
i = 1
for person in people:
    print("\n")
    for item in person:
        print(f"    {j}.{person[item]}")
        j += 1
    j = 1
