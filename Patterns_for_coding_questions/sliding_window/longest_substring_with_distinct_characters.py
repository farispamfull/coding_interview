def non_repeat_substring(strng):
    last_index = {}
    result = 0
    start = 0
    for i in range(len(strng)):
        if strng[i] in last_index:
            start = max(start, last_index[strng[i]] + 1)
        result = max(result, i - start + 1)
        last_index[strng[i]] = i
    return result


print(non_repeat_substring('aaaaacf'))
