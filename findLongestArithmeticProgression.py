def findLongestArithmeticProgression(arr, k):
    s = set(arr)
    count = 0

    for x in s:
        if x - k not in s:
            length = 1
            while x + length * k in s:
                length += 1
            count = max(count, length)

    return count
