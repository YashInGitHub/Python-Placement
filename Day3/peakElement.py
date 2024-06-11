# Find a peak element in a list of integers. (Peak element is an element that is greater than or equal to its neighbours)

n = int(input())
myList = []
for i in range(n):
    myList.append(int(input()))
peakElements = []
for i in range(1, len(myList)-1):
    if myList[i] > myList[i-1] and myList[i] > myList[i+1]:
        peakElements.append(myList[i])
print(peakElements)
