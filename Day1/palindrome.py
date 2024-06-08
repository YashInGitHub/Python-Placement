n = int(input())
temp = n
reverse = 0
while temp != 0:
    remain = temp % 10
    reverse = (reverse * 10) + remain
    temp = temp // 10

if n == reverse:
    print(True)
else:
    print(False)