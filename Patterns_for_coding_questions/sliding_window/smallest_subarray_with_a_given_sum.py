def smallest_subarray_with_given_sum(s: int, arr: list) -> int:
    result = len(arr)
    start = 0
    corrent_sum = 0
    for i in range(len(arr)):
        corrent_sum += arr[i]
        while corrent_sum >= s:
            result = min(result, i - start + 1)

            corrent_sum -= arr[start]
            start += 1
    return result
