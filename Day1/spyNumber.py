n = int(input()) 

sum = 0
product = 1

while(n != 0):
    i = n % 10
    n = n // 10
    sum += i
    product *= int(i)

if sum == product:
    print(True)
else:
    print(False)