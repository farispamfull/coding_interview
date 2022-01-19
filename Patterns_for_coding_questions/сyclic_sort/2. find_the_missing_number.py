def cyclic_sort(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1


def find_missing_number(nums):
    cyclic_sort(nums)
    for i in range(len(nums)):
        if nums[i] != i:
            return i


print(find_missing_number([4, 0, 3, 1]))
