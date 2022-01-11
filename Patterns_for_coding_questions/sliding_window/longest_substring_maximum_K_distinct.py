from collections import defaultdict


def longest_substring_with_k_distinct(str1, k):
    result = 0
    start = 0
    hash_map = defaultdict(int)
    for i in range(len(str1)):
        hash_map[str1[i]] += 1
        while len(hash_map) > k:
            hash_map[str1[start]] -= 1
            if hash_map[str1[start]] == 0:
                del hash_map[str1[start]]
            start += 1
        result = max(result, i - start + 1)
    return result
