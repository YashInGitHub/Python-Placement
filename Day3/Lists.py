l1 = ["apple", "banana", "cherry", "mango"]
l2 = [10, 20, 30, 40, 50]
l3 = [True, False]
l4 = list(("Jack"))
l5 = list(("Jack", "John"))

print(l4) #prints list l4
print(l5) #prints list l5
print(l1[0]) #prints "apple"
print(l1[0:4]) #prints all elements in l1
print(l1[:4])
print(l1[0:])
print(l1[:])
print(l1[-4:-1])
print(l1[-1:-4])

x = len(l1)
print(x)

print(type(l1))
print(type(l1[0]))

if "apple" in l1:
    print("Exists")

l1[1] = "Kiwi"
print(l1)

l1[1:3] = ["Pineapple", "Dates", "x"]
print(l1)

list = ["apple", "banana", "cherry"]
list.insert(2, "watermelon")
print(list)

list.append("orange")
print(list)

list2 = ["mango", "papaya", "pineapple"]
list.extend(list2)
print(list)

list.pop(1)
print(list)

del list[0]
del l1

list2.clear()
print(list2)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])

i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

#List comprehension: basically execute lines of codes in a single line

for i in range(len(thislist)):
    if thislist[i] == "apple":
        print(thislist[i])
# or
thislist = ["apple", "banana", "cherry"]
[print(thislist[i]) for i in range(len(thislist)) if thislist[i] == "apple"]


def fun(n):
    return abs(n - 50)

newList = [100, 50, 65, 82, 23]
newList.sort(key = fun)
print(newList)

#sort the list ignoring the case sensitivity

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#swapping the first and last element of a list

def swapList(l1):
    temp = l1[0]
    l1[0] = l1[len(l1) - 1]
    l1[len(l1) - 1] = temp

    return l1

l1 = [12, 34, 9, 56, 24]
print(swapList(l1))

L = [4, 5, 1, 2, 9, 7, 10, 8]
max = 0
for i in L:
    if i > max:
        max = i
min = max
for i in L:
    if i < min:
        min = i
print(max, min)