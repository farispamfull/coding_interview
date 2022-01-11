def make_squares(arr):
    start = 0
    end = len(arr) - 1
    result = [0] * len(arr)
    current_cursor = len(arr) - 1
    while start <= end:
        if abs(arr[start]) > abs(arr[end]):
            result[current_cursor] = arr[start] * arr[start]
            start += 1
        else:
            result[current_cursor] = arr[end] * arr[end]
            end -= 1
        current_cursor -= 1

    return result


print(make_squares([-2, -1, 0, 2, 3]))
