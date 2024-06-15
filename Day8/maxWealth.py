#You are given an mxn integer grid accounts where accounts[i][j] is the amount of money the ith customer has in jth bank. 
#The customers wealth is the amount of money they hav in all their bank accounts. The richest customer is the customer that has the maximum wealth.
#lst = [[1, 5], [7, 3], [3, 5]]
#o/p = 10

def customerWealth(lst):
    maxWealth = 0
    for a in lst:
        wealth = sum(a)
        maxWealth = max(maxWealth, wealth)
    return maxWealth

# m = int(input())
# n = int(input())

#lst = []
#for i in range(m):
#    bank = []
#    for j in range(n):
#        bank.append(int(input()))
#    lst.append(bank)

print(customerWealth([[1, 5], [7, 3], [3, 5]]))

