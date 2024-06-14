#Brute force method
def power(n, p):
    if p == 0:
        return 1
    
    return (n * power(n, p-1))


#Optimal Approach
def OptimalPower(n, p):
    if p <= 1:
        return n
    temp = OptimalPower(n, p//2)
    if p % 2 != 0:
        return n * temp * temp
    return temp * temp


n = int(input())
p = int(input())

print(OptimalPower(n, p))


