def merge(intervals):
    intervals.sort()
    merged = []
    start = intervals[0][0]
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval[0] <= end:
            end = max(interval[1], end)
        else:
            merged.append([start, end])
            start = interval[0]
            end = interval[1]
    merged.append([start, end])
    return merged


def merge2(intervals):
    intervals.sort()
    merged = [[intervals[0][0], intervals[0][1]]]

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval[0] <= merged[-1][1]:
            merged[-1][1] = max(interval[1], merged[-1][1])
        else:
            merged.append([interval[0], interval[1]])
    return merged


def test():
    assert merge([[6, 7], [2, 4], [5, 9]]) == [[2, 4], [5, 9]]
    assert merge([[1, 4], [2, 6], [3, 5]]) == [[1, 6]]


def test2():
    assert merge2([[6, 7], [2, 4], [5, 9]]) == [[2, 4], [5, 9]]
    assert merge2([[1, 4], [2, 6], [3, 5]]) == [[1, 6]]


if __name__ == '__main__':
    test()
    test2()
