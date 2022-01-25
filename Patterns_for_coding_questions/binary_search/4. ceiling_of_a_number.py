def search_ceiling_of_a_number(arr, key):
    left = 0
    right = len(arr) - 1

    if arr[left] > key:
        return -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < key:
            left = mid + 1
        elif arr[mid] > key:
            right = mid - 1
        else:
            return mid

    return right


def test():
    assert search_ceiling_of_a_number([4, 6, 10], 6) == 1
    assert search_ceiling_of_a_number([1, 3, 8, 10, 15], 12) == 3
    assert search_ceiling_of_a_number([4, 6, 10], 17) == 2
    assert search_ceiling_of_a_number([4, 6, 10], -1) == -1


if __name__ == '__main__':
    test()
