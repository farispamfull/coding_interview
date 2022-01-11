from collections import defaultdict


def length_of_longest_substring(strng, k):
    hash_map = defaultdict(int)
    max_letter = 0
    max_length = 0
    start_window = 0
    for i, j in enumerate(strng):
        hash_map[j] += 1
        max_letter = max(max_letter, hash_map[j])

        current_len = i - start_window + 1
        while current_len - max_letter > k:
            hash_map[strng[start_window]] -= 1
            start_window += 1
            current_len -= 1

        max_length = max(max_length, current_len)
    return max_length

print(length_of_longest_substring('abccde',1))