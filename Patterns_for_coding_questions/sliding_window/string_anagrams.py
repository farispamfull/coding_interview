from collections import Counter, defaultdict


def find_string_anagrams(strng, pattern):
    len_pattern = len(pattern)
    pattern = Counter(pattern)
    window_map = defaultdict(int)
    window_start = 0
    result = []
    for i in range(len(strng)):
        window_map[strng[i]] += 1

        if i - window_start + 1 == len_pattern:
            if window_map == pattern:
                result.append(window_start)
            current_start = strng[window_start]
            window_map[current_start] -= 1
            if not window_map[current_start]:
                del window_map[current_start]
            window_start += 1
    return result
