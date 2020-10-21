def leetspeak():
    phrase = (input("Input to translate:  ").upper())
    new_phrase = ""
    letter = [""]
    i = 0
    j = 0
    while i < len(phrase):
        while j < len(letter):
            if phrase[i] == letter[j]:
                new_phrase.append(number[j]) 
            else:
                new_phrase[i] = phrase[i]
            j += 1
        i += 1
    return new_phrase

print(leetspeak()) 