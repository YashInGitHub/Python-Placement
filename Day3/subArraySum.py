# Find the largest sub array sum of a given list

def subArraySum(lst):
    maxSum = curSum = lst[0]
    for num in lst[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(curSum, maxSum)
    return maxSum

n = int(input())
my_list = []

for i in range(n):
    my_list.append(int(input()))

print(subArraySum(my_list))

