def maxDistinctSubstringLengthInSessions(sessionString):
    longest = 0

    for s in sessionString.split("*"):
        seen = set()
        start = 0

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[start])
                start += 1

            seen.add(s[i])
            longest = max(longest, i - start + 1)

    return longest
