n = int(input())

i = 2
flag = True
while(i < n/2):
    if(n % i == 0):
        flag = False
        break
    i+=1

if flag:
    print(True)
else:
    print(False)