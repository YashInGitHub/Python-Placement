#Given an array of integers and a number k find the count of distinct elements in every window of size k in the array

def findKDistinct(arr, k):
    l = 0;
    res = []
    while(l+k <= len(arr)):
        dup = set(arr[l:l+k])
        count = len(dup)
        res.append(count)
        l+=1
    print(res)


n = int(input())
k = int(input())  
arr = []

for i in range(n):
    arr.append(int(input()))

findKDistinct(arr, k)

