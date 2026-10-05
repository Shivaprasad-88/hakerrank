def countResponseTimeRegressions(responseTimes):
    count = 0
    total = 0
    for i in range(len(responseTimes)):
        if i > 0 and responseTimes[i] > total / i:
            count += 1
        total += responseTimes[i]
    return count
