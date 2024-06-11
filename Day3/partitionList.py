# Write a program to partition a list around a given value such that all elements less than the given value come before it 
# and all elements greater than the given value come after it

def partitionList(lst, pivot):
    less_than = [x for x in lst if x < pivot]
    equal_to = [x for x in lst if x == pivot]
    greater_than = [x for x in lst if x > pivot]

    return less_than + equal_to + greater_than

n = int(input())
p = int(input())
my_list = []
for i in range(n):
    my_list.append(int(input()))

print(partitionList(my_list, p))