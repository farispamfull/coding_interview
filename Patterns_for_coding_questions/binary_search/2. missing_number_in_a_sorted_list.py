def missing_number(lst):
    left = 0
    right = len(lst) - 1

    if lst[left] != 1:
        return 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid - 1] == mid and lst[mid] != mid + 1:
            return mid + 1

        if lst[mid] != mid + 1:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def test():
    assert missing_number([1, 2, 4]) == 3
    assert missing_number([1, 2, 3, 4, 6]) == 5
    assert missing_number([2, 3, 4, 5, 6]) == 1
    assert missing_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1


if __name__ == '__main__':
    test()
