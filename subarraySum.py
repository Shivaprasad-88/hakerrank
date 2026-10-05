def subarraySum(nums, k):
    count = 0
    total = 0
    seen = {0: 1}

    for x in nums:
        total += x
        count += seen.get(total - k, 0)
        seen[total] = seen.get(total, 0) + 1

    return count
