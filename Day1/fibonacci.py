n = int(input())

a = 0
b = 1

print(str(a) + "  " + str(b), end="")

n = n - 2
while(n):
    c = a + b
    print(" ", c, end="")
    a = b
    b = c
    n -= 1