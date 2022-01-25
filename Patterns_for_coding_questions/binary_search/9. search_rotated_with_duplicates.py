def search_rotated_with_duplicates(arr, left, right, key):
    if left <= right:
        mid = (left + right) // 2

        if arr[mid] == key:
            return mid

        if arr[mid] == arr[left] == arr[right]:
            left += 1
            right -= 1
        if arr[left] <= arr[mid]:
            if arr[left] <= key < arr[mid]:
                return search_rotated_with_duplicates(arr, left, mid - 1,
                                                      key)
            return search_rotated_with_duplicates(arr, mid + 1, right,
                                                  key)
        else:
            if arr[mid] < key <= arr[right]:
                return search_rotated_with_duplicates(arr, mid + 1, right,
                                                      key)
            return search_rotated_with_duplicates(arr, left, mid - 1,
                                                  key)
