# Найдите самую длинную подстроку строки, содержащей k различных символов
from collections import defaultdict


def findLongestSubstring(strng: str, k: int) -> str:
    start = 0
    end = 0
    result_start = 0
    result_end = 0
    count_map = defaultdict(int)
    while end < len(strng):
        char = strng[end]
        count_map[char] += 1

        while len(count_map) > k:
            char = strng[start]
            count_map[char] -= 1
            if count_map[char] == 0:
                del count_map[char]
            start += 1
        if end - start > result_end - result_start:
            result_end = end
            result_start = start
        end += 1

    return strng[result_start:result_end + 1]


print(findLongestSubstring('abcccaad', 2))
