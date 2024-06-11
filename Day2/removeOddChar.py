# WAP to read a string from user and implement the logic to remove the characters which are at the odd number index

s = input()
a = ""
for i in range(len(s)):
    if i % 2 != 0:
        a = a+s[i]
print(a)