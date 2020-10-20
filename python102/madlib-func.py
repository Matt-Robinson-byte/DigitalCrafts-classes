def madlib_func(name,subject):
    try:
        return f"{name} loves to study {subject}!"
    except TypeError:
        print(f"Santa loves to study Toy-making!")
print (madlib_func())