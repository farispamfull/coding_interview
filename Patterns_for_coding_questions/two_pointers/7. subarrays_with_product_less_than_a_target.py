from collections import deque


def find_subarrays(arr, target):
    count = 0
    pre_target_sum = 1
    start = 0
    end = 0
    while end < len(arr):
        pre_target_sum *= arr[end]

        while end > start and pre_target_sum >= target:
            pre_target_sum //= arr[start]
            start += 1
        if pre_target_sum < target:
            count += end - start + 1

        end += 1
    return count


print(find_subarrays([1, 2, 3, 50,1,2], 10))


def find_subarrays(arr, target):
    result = []
    product = 1
    left = 0
    for right in range(len(arr)):
        product *= arr[right]
        while product >= target and left < len(arr):
            product /= arr[left]
            left += 1
        temp_list = deque()
        for i in range(right, left - 1, -1):
            print(arr[i])
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))
    return result
