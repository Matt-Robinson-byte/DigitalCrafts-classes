def mult_two_numbers(number1,number2):
    try:
        print(number1*number2)
    except NameError:
        print("Not a valid argument")
    except:
        print("something is wrong")

mult_two_numbers(9,5)
mult_two_numbers(2,4)
mult_two_numbers(2,p)