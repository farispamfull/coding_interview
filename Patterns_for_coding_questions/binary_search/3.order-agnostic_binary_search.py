def binary_search(arr, key):
    flag = False
    left = 0
    right = len(arr) - 1

    if arr[left] > arr[right]:
        flag = True

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        if flag:
            if arr[mid] < key:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < key:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def test():
    assert binary_search([4, 6, 10], 10) == 2
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 5) == 4
    assert binary_search([10, 6, 4], 10) == 0
    assert binary_search([10, 6, 4], 4) == 2


if __name__ == '__main__':
    test()
