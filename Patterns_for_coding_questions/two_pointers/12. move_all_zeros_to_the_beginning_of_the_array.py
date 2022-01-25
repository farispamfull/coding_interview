def move_zeros_to_left(arr):
    low = len(arr) - 1
    current_non_zero = len(arr) - 1
    while low >= 0:
        if arr[low] != 0:
            arr[current_non_zero] = arr[low]
            current_non_zero -= 1
        low -= 1
    while current_non_zero >= 0:
        arr[current_non_zero] = 0
        current_non_zero -= 1
    return arr


def test(arr):
    assert move_zeros_to_left(arr) == [0, 0, 1, 10, -1, 11, 5, -7, 25, -35]


if __name__ == '__main__':
    arr = [1, 10, -1, 11, 5, 0, -7, 0, 25, -35]
    test(arr)
