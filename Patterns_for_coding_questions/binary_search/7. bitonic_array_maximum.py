def find_max_in_bitonic_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return arr[left]


def test():
    assert find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]) == 12
    assert find_max_in_bitonic_array([3, 8, 3, 1]) == 8
    assert find_max_in_bitonic_array([1, 3, 8, 12]) == 12
    assert find_max_in_bitonic_array([10, 9, 8]) == 10


if __name__ == '__main__':
    test()
