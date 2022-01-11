def max_sub_array_of_size_k(k: int, arr: list) -> int:
    start = 0
    corrent_sum = 0
    result_sum = 0
    for i in range(len(arr)):
        if i >= k:
            result_sum = max(result_sum, corrent_sum)
            corrent_sum -= arr[start]
            start += 1
        corrent_sum += arr[i]
    return result_sum


arr = [2, 3, 4, 1, 5]
k = 2
print(max_sub_array_of_size_k(k=k, arr=arr))
