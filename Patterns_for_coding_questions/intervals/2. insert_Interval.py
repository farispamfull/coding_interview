def insert(intervals, new_interval):
    merged = []
    i = 0
    start, end = new_interval
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        merged.append([intervals[i][0], intervals[i][1]])
        i += 1
    while i < len(intervals) and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1
    merged.append([start, end])

    merged.extend(intervals[i:])
    return merged


def test():
    assert insert([[2, 3], [5, 7]], [1, 4]) == [[1, 4], [5, 7]], ''
    assert insert([[1, 3], [5, 7], [8, 12]], [4, 10]) == [[1, 3], [4, 12]]


if __name__ == '__main__':
    test()
