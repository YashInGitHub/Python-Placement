n = int(input())

powN = n**2

sum = 0
while(powN != 0):
    i = powN % 10
    powN = powN // 10
    sum += int(i)

if sum == n:
    print(True)
else:
    print(False)