from itertools import zip_longest


# хороший вариант, когда хотим сохранить состояние и передать управление
def backspace_compare(str1, str2):
    first = get_next_valid_char_index(str1)
    last = get_next_valid_char_index(str2)

    return all(i == j for i, j in zip_longest(first, last))


def get_next_valid_char_index(strng):
    backspace_count = 0
    for i in range(len(strng) - 1, -1, -1):
        if strng[i] == '#':
            backspace_count += 1
        elif backspace_count:
            backspace_count -= 1
        else:
            yield strng[i]


# без генератора получается примерно так же.
# разделение ответственности для читаемости
def backspace_compare(str1, str2):
    index1 = len(str1) - 1
    index2 = len(str2) - 1
    while index1 >= 0 or index2 >= 0:
        i1 = get_next_valid_char_index(str1, index1)
        i2 = get_next_valid_char_index(str2, index2)

        if i1 < 0 and i2 < 0:
            return True

        if i1 < 0 or i2 < 0:
            return False

        if str1[i1] != str2[i2]:
            return False

        index1 = i1 - 1
        index2 = i2 - 1

    return True


def get_next_valid_char_index(strng, index):
    backspace_count = 0
    flag = True
    while index >= 0 and flag is True:
        if strng[index] == '#':
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            return index

        index -= 1

    return index
