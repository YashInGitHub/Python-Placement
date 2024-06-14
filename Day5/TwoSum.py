# Given an array of n numbers and another number x the task is to check whether or not there exist 2 elements in the array whose exact sum
# is x

def TwoSum(x, numbers):
    for i in numbers:
        num = x - i
        if num in numbers and num != i:
            return True
    return False

def OptimalTwoSum(x, numbers):
    numbers.sort()
    l = 0
    r = len(numbers) - 1

    while(l < r):
        sum = numbers[l] + numbers[r]
        if sum < x:
            l+=1
        elif sum > x:
            r -= 1
        else:
            return True
    return False

n = int(input())
x = int(input())

numbers = []

for i in range(n):
    numbers.append(int(input()))
print(OptimalTwoSum(x, numbers))


