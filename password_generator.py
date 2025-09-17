while True:
    pass_length = input("Enter length of password: ")
    
    if pass_length.isdigit():  # check if input is all digits
        pass_int = int(pass_length)
    else:
        print("Please give a valid number, not a letter or symbol")

print("Final password length:", pass_int)