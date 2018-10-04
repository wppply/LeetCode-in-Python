# sort algorithm

arr = [8,7,6,5,2,3,1,10]
"""
Insertion sort
    use two pointers
    time: n^2
    space: 1
"""


def insertSort(arr):
    for i in range(len(arr)):
        minn = i
        for j in range(i, len(arr)):
            minn = j if arr[j] < arr[minn] else minn
        arr[minn], arr[i] = arr[i], arr[minn]

    return arr


print("Insertion sort:", insertSort(arr))

"""
Bubble sort
    same with 2 pointers
    time: n^2
    space: 1 
"""


def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr

print("Bubble Sort:", bubbleSort(arr))

"""
Merge sort
time: nlgn
space: n 
"""

def merge(arr1, arr2):
    res = [0] * (len(arr1)+len(arr2))
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res[i+j] = arr1[i]
            i += 1
        else:
            res[i+j] = arr2[j]
            j += 1
    if not arr1:
        arr1, arr2 = arr2, arr1
        i, j = j, i

    while i+j < len(res):
        res[i+j] = arr[i]
        i += 1
    return res

def mergeSort(arr):
    # base case
    if len(arr) == 1:
        return arr

    m = len(arr)//2
    left = mergeSort(arr[:m])
    right = mergeSort(arr[m:])
    return merge(left, right)
print("MergeSort:", mergeSort(arr))

"""
Quick sort
"""
def quickSort(arr):
    if len(arr) < 2: return arr
    pivot = arr[0]
    return quickSort([x for x in arr if x < pivot]) + \
           [x for x in arr if x == pivot] + \
           quickSort([x for x in arr if x > pivot])
print("quickSort:", quickSort(arr))