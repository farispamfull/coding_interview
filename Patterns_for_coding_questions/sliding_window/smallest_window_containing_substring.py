from collections import defaultdict


def find_substring(strng, pattern):
    set_pattern = set(pattern)
    count_map = defaultdict(int)
    start_window = 0
    result_start = 0
    result_end = len(strng) - 1
    for i, j in enumerate(strng):
        if j in set_pattern:
            count_map[strng[i]] += 1

        if len(count_map) == len(set_pattern):
            while count_map[strng[start_window]] - 1 != 0:
                if strng[start_window] in set_pattern:
                    count_map[strng[start_window]] -= 1
                start_window += 1
            if i - start_window + 1 < result_end - result_start + 1:
                result_end = i
                result_start = start_window
    if len(count_map) < len(set_pattern):
        return ''
    return strng[result_start:result_end + 1]


String = "abdbca"
Pattern = "abc"
print(find_substring(String, Pattern))


def find_substring_2(strng, pattern):
    set_pattern = set(pattern)
    part_index = []
    hash_map = {}
    result_start = 0
    result_end = len(strng) - 1
    for i, j in enumerate(filter(lambda x: x in set_pattern, strng)):
        if len(hash_map) == len(set_pattern):
            part_index.remove(hash_map[j])
            if result_end - result_start + 1 > i - part_index[-1] + 1:
                result_start = part_index[-1]
                result_end = i
        hash_map[j] = i
        part_index.append(i)
    if len(hash_map) < len(set_pattern):
        return ''
    return strng[result_start:result_end + 1]

print(find_substring(String, Pattern))