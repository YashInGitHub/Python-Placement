#Given an array of size (n-1) such that it only contains distinct integers in the range of 1 to n. Find the missing element
#i/p = 10
# lst = [6, 1, 2, 8, 3, 4, 7, 10, 5]

def distinctElements(arr):
    arrSums = sum(arr)
    n = len(arr)
    sums = (n * (n+1))//2

    if arrSums != sums:
        return False
    else:
        return True

print(distinctElements([6, 1, 2, 8, 3, 4, 7, 10, 5, 9]))