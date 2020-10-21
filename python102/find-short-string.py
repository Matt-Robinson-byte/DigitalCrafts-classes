def shortest(strings):
    length = len(strings[0])
    shortest = ''
    for string in strings:
        if len(string) < length:
            length = len(string)
            shortest = string
    return shortest

print(shortest(["this","is","something"]))

