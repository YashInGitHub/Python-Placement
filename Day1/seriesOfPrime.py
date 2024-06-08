m = int(input())
o = int(input())

for n in range(m, o+1):
    i = 2
    flag = True
    while(i <= n/2):
        if(n % i == 0):
            flag = False
            break
        i+=1

    if flag:
        print(str(n), end=" ")
