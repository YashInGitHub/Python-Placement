# Write a python program to find the best of 2 test average marks out of 3 test marks accepted from the user.

marks = []

for i in range(3):
    marks.append(int(input()))

marks.sort()
print()
print(marks[2], " ", marks[1])