def search_next_letter(letters, key):
    n = len(letters)

    start, end = 0, n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key < letters[mid]:
            end = mid - 1
        else:  # key >= letters[mid]:
            start = mid + 1

    # если все удачно start > key,
    # если key больше letters[n-1], то start = end + 1
    return letters[start % n]


def test():
    assert search_next_letter(['a', 'c', 'f', 'h'], 'f') == 'h'
    assert search_next_letter(['a', 'c', 'f', 'h'], 'b') == 'c'
    assert search_next_letter(['a', 'c', 'f', 'h'], 'm') == 'a'


if __name__ == '__main__':
    test()
