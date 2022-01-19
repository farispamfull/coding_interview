def remove_duplicates(arr):
    result = len(arr)
    for i in range(1, result):
        if arr[i - 1] == arr[i]:
            result -= 1
    return result


print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))


# возвращаем такой массив
def remove_duplicates(arr):
    non_duble = 1
    i = 1
    while i < len(arr):
        if arr[non_duble - 1] != arr[i]:
            arr[non_duble] = arr[i]
            non_duble += 1
        i += 1
    return arr[:non_duble]


def remove_duplicates(arr):
    next_duble = 1
    for i in range(1, len(arr)):
        if arr[next_duble - 1] != arr[i]:
            arr[next_duble] = arr[i]
            next_duble += 1
    return arr[:next_duble]


print(remove_duplicates([2, 3, 3, 3, 6, 9, 9, 9, 9, 12]))


