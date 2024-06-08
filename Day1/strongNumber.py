def factorial(n):
    if n < 0:
        return 1
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    return n * factorial(n-1)

n = int(input())
temp = n

sum = 0

while(n != 0):
    i = n % 10
    n = n // 10
    sum += factorial(int(i))

if(sum == temp):
    print(True)
else:
    print(False)