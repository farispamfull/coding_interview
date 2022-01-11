def length_of_longest_substring(arr, k):
    max_length = 0
    max_one_letter = 0
    start_window = 0
    for i, j in enumerate(arr):
        if j == 1:
            max_one_letter += 1
        current_len = i - start_window + 1

        if current_len - max_one_letter > k:
            if arr[start_window] == 1:
                max_one_letter -= 1
            current_len -= 1
            start_window += 1
        max_length = max(max_length, current_len)
    return max_length


print(
    length_of_longest_substring([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],k = 2))
