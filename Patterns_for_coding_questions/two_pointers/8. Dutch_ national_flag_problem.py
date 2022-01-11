# 1 2 2 2 1 2 1
def dutch_flag_sort(arr):
    start = 0
    end = len(arr) - 1
    midlle = len(arr) - 1
    while start < midlle:
        while arr[start] == 0 or (start >= end and arr[start] == 1):
            start += 1

        while end > start and (arr[end] == 1 or arr[end] == 2):
            end -= 1
        while midlle > 0 and arr[midlle] == 2:
            midlle -= 1

        if start < midlle:
            if arr[start] == 1:
                arr[start], arr[end] = arr[end], arr[start]
            else:
                arr[start], arr[midlle] = arr[midlle], arr[start]


a = [0, 0, 2, 1, 2, 1, 1]
dutch_flag_sort(a)


def dutch_flag_sort(arr):
    low, high = 0, len(arr) - 1
    i = 0
    while i <= high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            i += 1
            low += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1


print(a)
