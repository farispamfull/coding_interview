from collections import defaultdict


def fruits_into_baskets(fruits):
    result = 0
    hash_map = defaultdict(int)
    start = 0
    for i in range(len(fruits)):
        hash_map[fruits[i]] += 1

        while len(hash_map) > 2:
            char = fruits[start]
            hash_map[char] -= 1
            if hash_map[char] == 0:
                del hash_map[char]
            start += 1

        result = max(result, i - start + 1)

    return result

Fruit = ['A', 'B', 'C', 'B', 'B', 'C']
