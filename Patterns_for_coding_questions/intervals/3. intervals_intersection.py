def merge(intervals_a, intervals_b):
    result = []
    i = 0
    j = 0
    while i < len(intervals_a) and j < len(intervals_b):
        if (intervals_a[i][0] <= intervals_b[j][1] and intervals_a[i][1] >=
                intervals_b[j][0]):
            start = max(intervals_a[i][0], intervals_b[j][0])
            end = min(intervals_a[i][1], intervals_b[j][1])

            result.append([start, end])

        if intervals_b[j][1] > intervals_a[i][1]:
            i += 1
        else:
            j += 1
    return result


def test():
    arr1 = [[1, 3], [5, 7], [9, 12]]
    arr2 = [[5, 10]]
    assert merge(arr1, arr2) == [[5, 7], [9, 10]]

    arr1 = [[1, 3], [5, 6], [7, 9]]
    arr2 = [[2, 3], [5, 7]]
    assert merge(arr1, arr2) == [[2, 3], [5, 6], [7, 7]]


if __name__ == '__main__':
    test()
