def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]

    while end > start:
        if array[start] < pivot:
            array[start], array[end] = array[end], array[start]
            end -= 1


def partition2(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


def kthSmallest(arr, l, r, k):
    if 0 < k <= r - l + 1:
        positions = partition2(arr, l, r)
        if positions - l == k - 1:
            return arr[positions]
        if positions - l > k - 1:
            return kthSmallest(arr, l, positions - 1, k)

        return kthSmallest(arr, positions + 1, r, k - positions + l - 1)

    return False


# k = 3
# pos = 4 l = 2+3 5 - 4 1 - 1 0
#  3 - 5 + 2 - 1 = -1
# k + l - positions + 1

a = [12, 3, 5, 7, 2, 19, 4]
l = 0
r = len(a) - 1
print(partition2(a, l, r))
print(kthSmallest(a, 0, len(a) - 1,100))


