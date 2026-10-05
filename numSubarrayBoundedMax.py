def numSubarrayBoundedMax(nums, left, right):
    count = 0
    last_invalid = -1
    last_valid = -1

    for i, x in enumerate(nums):
        if x > right:
            last_invalid = i

        if x >= left:
            last_valid = i

        count += max(0, last_valid - last_invalid)

    return count
