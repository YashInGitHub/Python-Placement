def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        sub_arr1 = arr[:mid]
        sub_arr2 = arr[mid:]

        mergeSort(sub_arr1)
        mergeSort(sub_arr2)

        i = j = k = 0

        while i < len(sub_arr2) and j < len(sub_arr2):
            if sub_arr1[i] < sub_arr2[j]:
                arr[k] = sub_arr1[i]
                i+=1
            else:
                arr[k] = sub_arr2[j]
                j+=1
            k+=1
