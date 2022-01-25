def low_local(arr, key):
    left, right = 0, len(arr) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if arr[mid] < key:
            left = mid
        else:
            right = mid
    return right


def hight_local(arr, key):
    left, right = 0, len(arr) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if arr[mid] > key:
            right = mid
        else:
            left = mid
    return left


def find_range(arr, key):
    low = low_local(arr, key)
    if arr[low] != key:
        return [-1, -1]
    hight = hight_local(arr, key)
    return [low, hight]


def test():
    assert find_range([4, 6, 6, 6, 9], 6) == [1, 3]
    assert find_range([1, 3, 8, 10, 15], 10) == [3, 3]
    assert find_range([1, 3, 8, 10, 15], 12) == [-1, -1]


if __name__ == '__main__':
    test()
