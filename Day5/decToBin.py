def dTob(d):
    if d == 0:
        return "0"
    b = ""
    while d > 0:
        b = str(d % 2) + b
        d = d // 2
    return b

n = int(input())
print(dTob(n))
