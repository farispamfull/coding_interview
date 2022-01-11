# Самая длинная подстрока, содержащая не более K символов из заданного набора символов

def maxNormalSubstring(strng, q, k):
    longest = 0
    pattern = set(q)
    count = 0
    start = 0

    for i in range(len(strng)):
        if strng[i] in pattern:
            count += 1

        while count > k:
            if strng[start] in pattern:
                count -= 1
            start += 1
        longest = max(longest, i - start + 1)

    return longest


print(maxNormalSubstring('abcdeccd', 'adbc', 2))

