def pair_with_targetsum(arr, target_sum):
    start = 0
    end = len(arr) - 1
    while end > start:
        if arr[start] + arr[end] > target_sum:
            end -= 1
        elif arr[start] + arr[end] < target_sum:
            start += 1
        else:
            return [start, end]
    return []


arr = [2, 5, 9, 11]
target = 11
print(pair_with_targetsum(arr, target))


def pair_with_targtetsum2(arr, target_sum):
    hash_map = {}
    for i, j in enumerate(arr):
        if target_sum - j in hash_map:
            return [hash_map[target_sum - j], i]
        hash_map[j] = i
    return []

arr = [2, 5, 9, 11]
target = 11
print(pair_with_targtetsum2(arr, target))