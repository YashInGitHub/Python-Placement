#An equilibrium index is an index such that its sum of elements at lower indicies is equal to sum of elements at higher indicies
#arr = [-7, 1, 5, 2, -4, 3, 0]
#o/p = 3
#else if no such point exists

def equillibriumIndex(arr):
    for i in range(len(arr)):
        lsum = sum(arr[:i])
        rsum = sum(arr[i+1:])
        if lsum == rsum:
            return i
    return -1
    
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

print("Position found at: ", equillibriumIndex(arr))