def next_greater_element(arr):
    result = [-1] * len(arr)
    stack = []

    for i in range(len(arr) - 1, -1, -1):
        while stack and arr[i] >= stack[-1]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result


def test():
    assert next_greater_element([4, 6, 3, 2, 8, 1]) == [6, 8, 8, 8, -1, -1]

