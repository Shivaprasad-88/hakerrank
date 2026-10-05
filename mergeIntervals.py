def mergeIntervals(intervals):
    intervals.sort()
    result = []

    for x in intervals:
        if not result or x[0] > result[-1][1]:
            result.append(x)
        else:
            result[-1][1] = max(result[-1][1], x[1])

    return result
