def find_window(arr):
    left, right = 0, len(arr) - 1

    while left < len(arr) - 1 and arr[left] < arr[left + 1]:
        left += 1
    while right > 0 and arr[right] > arr[right - 1]:
        right -= 1

    return left, right


def shortest_window_sort(arr):
    left, right = find_window(arr)
    # если массив отсортирован
    if left == len(arr) - 1:
        return 0

    minimum = arr[left]
    maximum = arr[left]
    for i in range(left, right + 1):
        minimum = min(minimum, arr[i])
        maximum = max(maximum, arr[i])

    while left > 0 and arr[left - 1] > minimum:
        left -= 1
    while right < len(arr) - 1 and arr[right + 1] < maximum:
        right += 1

    return right - left + 1


print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
