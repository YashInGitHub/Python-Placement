# Count the number of occurances of a given item in the list

n = int(input())
k = int(input())

num = []

count = 0
for i in range(n):
    if int(input()) == k:
        count+=1

print(count)
