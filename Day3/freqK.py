# Write a program to extract elements with a frequency greater than k

li = [8, 9, 8, 8, 8, 5, 5, 4, 5]
k = 2
newl = []

for i in li:
    freq = li.count(i)
    if(freq > k and i not in newl):
        newl.append(i)
print(newl)