# ALGORITHM SELECTION SORT:
# Selection sort repeatedly finds the minimum element from the unsorted part. It then swaps with the first unsorted element
# Time complexity : O(n^2)

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_ind = i
        for j in range(i+1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    print(arr)

selectionSort([1,2,3,5,4])



