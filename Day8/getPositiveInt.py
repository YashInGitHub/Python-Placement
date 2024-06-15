def get_positive_integer():
    while True:
        try:
            number = int(input("Enter a positive integer: "))
            if number <= 0:
                raise ValueError("Not a positive integer !!!")
            return number
        except ValueError as e:
            print("Error: ", e)
positiveInt = get_positive_integer()
print("You entered: ", positiveInt)