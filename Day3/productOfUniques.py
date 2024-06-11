# Find out the duplicate removal list product using list comprehension

test_list = [1, 3, 4, 5, 6 ,3, 6, 1]
res = list(set(test_list))
pro = 1
[pro := x * pro for x in res]
print(pro)