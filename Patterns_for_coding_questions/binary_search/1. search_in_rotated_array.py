def search_rotated_array(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == key:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] >= key < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[right] >= key > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1


def req_search_rotated_array(arr, left, right, key):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= key < arr[mid]:
                return req_search_rotated_array(arr, left, mid - 1, key)
            return req_search_rotated_array(arr, mid + 1, right, key)

        if arr[right] >= key > arr[mid]:
            return req_search_rotated_array(arr, mid + 1, right, key)
        return req_search_rotated_array(arr, left, mid - 1, key)


def test():
    assert search_rotated_array([10, 15, 1, 3, 8], 15) == 1
    assert search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10) == 4
    assert req_search_rotated_array([10, 15, 1, 3, 8], 0, 4, 15) == 1
    assert req_search_rotated_array([4, 5, 7, 9, 10, -1, 2], 0, 6, 10) == 4


if __name__ == '__main__':
    test()
