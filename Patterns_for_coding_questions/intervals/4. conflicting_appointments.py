def can_attend_all_appointments(intervals):
    intervals.sort(key=lambda x: x[0])
    start, end = intervals[0][0], intervals[0][1]
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval[0] < end:
            return False
        else:
            start = interval[0]
            end = interval[1]
    return True


def can_attend_all_appointments2(intervals):
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i - 1][1] > intervals[i][0]:
            return False

    return True


def test():
    arr = [[6, 7], [2, 4], [8, 12]]
    assert can_attend_all_appointments(arr) is True
    arr = [[1, 4], [2, 5], [7, 9]]
    assert can_attend_all_appointments(arr) is False
    arr = [[4, 5], [2, 3], [3, 6]]
    assert can_attend_all_appointments(arr) is False


if __name__ == '__main__':
    test()
