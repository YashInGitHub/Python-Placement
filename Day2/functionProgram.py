def fn(n):
    print(n)
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fn(n-1) + fn(n-2)

n = int(input())
print(fn(n))