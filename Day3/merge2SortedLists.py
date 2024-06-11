# Write a program to merge 2 sorted lists into a single sorted list
list1 = [2, 4, 6, 8, 10]
list2 = [1, 3, 5, 7, 9]

maxLen = max(len(list1), len(list2))
mergedList = list1 + list2
mergedList.sort()
print(mergedList)
