
def create_tuples():
    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = ('a', 'b', 'c', 'd', 'e')
    tuple3 = ("apple", "banana", "cherry")

    return tuple1, tuple2, tuple3

def access_tuple_items(tuple1, tuple2):
    print("Tuple 1: ", tuple1)
    print("First element of Tuple 1: ", tuple1[0])
    print("Last element of Tuple 1: ", tuple1[-1])
    print("Tuple 2: ", tuple2)
    print("Second element of Tuple 2: ", tuple2[1])
    print("Second last element of Tuple 2: ", tuple2[-2])
    print("Elements from index 0 to 5: ", tuple1[0:5])

def unpacking_tuple1(tuple3):
    (green, yellow, red) = tuple3

    print(green)
    print(yellow)
    print(red)

def unpacking_tuple2():
    fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
    (green, yellow, *red) = fruits

    print(green)
    print(yellow)
    print(red)

def change_tuples(tuple1, tuple2):
    list1 = list(tuple1)
    list2 = list(tuple2)
    list1.append(6)
    list2.remove('c')
    tuple1 = tuple(list1)
    tuple2 = tuple(list2)

    return tuple1, tuple2

def loop_through_tuple(tuple1):
    print("Looping through tuple 1 using for loop: ")
    for item in tuple:
        print(item)
    print("\nLooping using while loop and index numbers: ")
    ind = 0
    while ind < len(tuple1):
        print(tuple1[ind])
        ind+=1

def join_tuples(tuple1, tuple2):
    tuple3 = tuple1 + tuple2
    return tuple3

tuple1, tuple2, tuple3 = create_tuples()
access_tuple_items(tuple1, tuple2)
print()

unpacking_tuple1(tuple3)
print()

unpacking_tuple2()
print()

tuple1, tuple2 = change_tuples(tuple1, tuple2)
print("After making changes: ")
access_tuple_items(tuple1, tuple2)
print()

tuple3 = join_tuples(tuple1, tuple2)
print("Joined tuple: ", tuple3)

my_tuple = (1, 2, 3)
another_tuple = tuple([4, 5, 6])
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:3])

combined_tuple = my_tuple + another_tuple
print(combined_tuple)

repeated_tuple = my_tuple * 3
print(repeated_tuple)

print(2 in my_tuple) #Output: True
print(4 not in my_tuple)

print(len(my_tuple))

for item in my_tuple:
    print(item)

string_to_tuple = tuple("hello")
print(string_to_tuple)

list_to_tuple = tuple([1, 2, 3])
print(list_to_tuple)

print(my_tuple.count(2)) #Output: 1
print(my_tuple.index(3)) #Output: 2

tuple_of_integers = (5, 3, 6, 8, 1, 3)
sorted_tuple = tuple(sorted(tuple_of_integers))
print("Sorted Tuple: ", sorted_tuple)

#using lambda to sort nested tuples
#sorts the nested tuple according to the 2nd element in each inner tuple
tuple_in_tuple = ((1, 'apple'), (3, 'orange'), (2, 'banana'))
sorted_tuples = sorted(tuple_in_tuple, key=lambda x : x[1])
print(sorted_tuple)

squares_tuple = tuple(x ** 2 for x in range(1, 6))
print(squares_tuple)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped_tuple = tuple(zip(list1, list2))
print(zipped_tuple) 

from collections import namedtuple
import math

Point = namedtuple('Point', ['x', 'y'])

point1 = Point(2, 3)
point2 = Point(4, 6)

print(math.sqrt((point2.y - point1.y)**2 + (point2.x - point1.x)**2))

original_tuple = (1, 2, 3, 4, 5)
filtered_tuple = tuple(filter(lambda x : x % 2 == 0, original_tuple))
print(filtered_tuple)

from functools import reduce

def add (x, y):
    return x + y

original_tuple1 = (1, 2, 3, 4, 5)

result = reduce((add, original_tuple1))

print(result)