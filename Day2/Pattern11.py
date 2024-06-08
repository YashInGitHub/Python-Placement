# Produce the pattern

#     A A A A A
#     A A A A A 
#     A A A A A
#     A A A A A
#     A A A A A

n = int(input())
a = input()
print()
for i in range(n):
    for j in range(n):
        print(a, end=" ")
    print()