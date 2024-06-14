#   Print the pattern using recursion
#   5 4 3 2 1
#   5 4 3 2
#   5 4 3
#   5 4
#   5

def pattern(n, t):
    if t == n+1:
        return
    for i in range(n, t-1, -1):
        print(i, end=" ")
    print()
    pattern(n, t+1)


n = int(input())
pattern(n, 1)

