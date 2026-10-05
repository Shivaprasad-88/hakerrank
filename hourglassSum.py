def hourglassSum(arr):
    maximum = float("-inf")
    for i in range(4):
        for j in range(4):
            total = (
                arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
                + arr[i + 1][j + 1]
                + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            )
            maximum = max(maximum, total)
    return maximum
