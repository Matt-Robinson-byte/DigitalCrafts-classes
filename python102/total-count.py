def total_counts(strings):
    list_length = len(strings)
    total_length = 0
    for item in strings:
        total_length = total_length + len(item)
    return({"List length" : list_length, "Total characters" : total_length})
print(total_counts(["hi", "my", "name", "is", "matt"]))