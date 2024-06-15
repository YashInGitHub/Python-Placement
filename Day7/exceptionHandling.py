try: 
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1/num2
    print(result)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("No exception")
finally:
    print("End of program")
