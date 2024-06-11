# Write a program to count the unique values in a list

n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
print()
print(len(set(num)))