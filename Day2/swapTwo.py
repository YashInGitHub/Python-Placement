# WAP to swap 2 numbers using a variable and without using a variable
a = int(input())
b = int(input())

def with3(a, b):
    temp = a
    a = b
    b = temp
    print(a, b)

def without(a, b):
    a = a + b
    b = a - b
    a = a - b
    print(a, b)

with3(a, b)
without(a, b)
