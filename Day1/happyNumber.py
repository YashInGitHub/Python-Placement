import sys

n = int(input())
temp = n

if n == 1 or n == 4:
    print(False)
    sys.exit()

flag = False

sum = 0
while(sum != n):
    while(temp != 0):
        i = temp % 10
        temp = temp // 10
        sum += i**2
    temp = sum
    sum = 0

    if temp == 1:
        print(True)
        break
    elif temp == n or temp == 4:
        print(False)
        break
