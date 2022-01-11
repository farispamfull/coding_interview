from collections import Counter, defaultdict
from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    pattern = Counter(p)
    window_dict = defaultdict(int)
    len_pattern = len(p)
    result = []
    start = 0
    end = len_pattern - 1
    if end < len(s):
        for i in range(end):
            window_dict[s[i]] += 1

    while end < len(s):
        window_dict[s[end]] += 1
        end += 1

        if window_dict == pattern:
            result.append(start)

        window_dict[s[start]] -= 1
        if not window_dict[s[start]]:
            del [window_dict[s[start]]]
        start += 1

    return result


def findAnagrams2(s: str, p: str) -> List[int]:
    pattern = Counter(p)
    window_dict = defaultdict(int)
    len_pattern = len(p)
    result = []
    start = 0
    for i in range(len(s)):
        char = s[i]
        window_dict[char] += 1

        if i - start == len_pattern - 1:
            if pattern == window_dict:
                result.append(start)
            char = s[start]
            window_dict[char] -= 1

            if window_dict[char] == 0:
                del window_dict[char]
            start += 1
    return result


print(findAnagrams2(s='abccdaabc', p='abc'))
