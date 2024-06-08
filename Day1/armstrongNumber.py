m = input()
n = len(m)

m = int(m)
temp = m

sum = 0
while(m != 0):
    i = m % 10
    m = m // 10
    sum += int(i) ** n

if sum == temp:
    print(True)
else:
    print(False) 