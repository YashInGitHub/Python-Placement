list1 = [1, 2, 3, 4, 5]
list2 = [1, 3, 5, 7, 9]

union = []
intersection = []

print("Union: ", list(set(list1) | set(list2)))
print("Intersection: ", list(set(list1) & set(list2)))


