# Produce the pattern

#     1 2 3 4
#     5 6 7 8
#     9 10 11 12
#     13 14 15 16

n = int(input())
count = 1

for i in range(n):
    for j in range(n):
        print(count, end=" ")
        count += 1
    print()