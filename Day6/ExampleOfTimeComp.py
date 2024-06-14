# O(1)
def access_element(arr, index):
    return arr[index]

arr = [10, 20, 30, 40, 50]
index = 2
print("Example of O(1) time complexity: ")
print("Array: ", arr)
print("Index: ", index)
print("Element at index: ",access_element(arr, index))

# O(log n)
def binary_search(array, key):
    l = 0
    r = len(array) - 1

    while(l <= r):
        mid = l + ((r - l) // 2)
        if array[mid] == key:
            return [True, mid]
        if array[mid] > key:
            r = mid - 1
        else:
            l = mid + 1
    return [False, None]

def binary_search_recursion(arr, key, l, r):
    mid = l + ((r - l)//2)
    if l > r:
        return False
    if arr[mid] == key:
        return True
    if arr[mid] > key:
        return binary_search_recursion(arr, key, l, mid-1)
    else:
        return binary_search_recursion(arr, key, mid+1, r)

array = [10, 20, 30, 40, 50]
key = 2
print("Example of O(log n) time complexity: ")
print("\nSorted Array: ", array)
print("Key: ", key)
ans = binary_search_recursion(array, key, 0, len(array))
print("Key element found status: ", ans)

# O(n)
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return [True, i]
    return [False, None]

array = [10, 20, 30, 40, 50]
key = 20
print("Example of O(n) time complexity: ")
print("\nArray: ", array)
print("Key: ", key)
ans = linear_search(array, key)
print("Key element found status: ", ans[0], "\nKey at: ", ans[1])

# O(n^2)

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] >= arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

bubbleSort([9, 8, 7, 6, 5, 4, 3, 2, 1])