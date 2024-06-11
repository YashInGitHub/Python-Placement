# Write a program to test if list contains elements in the range

n = int(input())
myList = []

for i in range(n):
    myList.append(int(input()))

i = int(input())
j = int(input())

flag = True
for num in myList:
    if num < i or num > j:
        flag = False
        break
print(flag)

