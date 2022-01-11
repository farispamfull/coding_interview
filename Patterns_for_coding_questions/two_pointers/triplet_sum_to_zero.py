def search_triplets(arr):
    arr.sort()
    result = []
    search_tuple(arr=arr, x=arr[0], index=0 + 1, result=result)
    for i in range(1, len(arr) - 1):
        if arr[i] != arr[i - 1]:
            search_tuple(arr=arr, x=arr[i], index=i + 1, result=result)
    return result


def search_tuple(arr, x, index, result):
    start = index
    end = len(arr) - 1
    while start < end:
        if arr[start] + arr[end] == -x:
            result.append((x, arr[start], arr[end]))
            start += 1
            end -= 1

            while start < end and arr[start - 1] == arr[start]:
                start += 1
            while start < end and arr[end + 1] == arr[end]:
                end -= 1
        elif arr[start] + arr[end] > -x:
            end -= 1
        else:
            start += 1
print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
