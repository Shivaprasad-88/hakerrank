def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        small = i
        for j in range(i + 1, n):
            if arr[j] < arr[small]:
                small = j
        arr[i], arr[small] = arr[small], arr[i]
    return arr
