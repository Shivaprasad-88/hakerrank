def plusMinus(arr):
    n = len(arr)
    print(f"{sum(x > 0 for x in arr) / n:.6f}")
    print(f"{sum(x < 0 for x in arr) / n:.6f}")
    print(f"{sum(x == 0 for x in arr) / n:.6f}")
