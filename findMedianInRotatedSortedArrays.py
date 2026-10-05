def findMedianInRotatedSortedArrays(A, B):
    arr = sorted(A + B)
    return arr[(len(arr) - 1) // 2]
