# Длина самой длинной подстроки без повторяющихся символов

def longestUniqueSubsttr(strng):
    result = 0
    last_index = {}
    start = 0

    for i in range(len(strng)):

        if strng[i] in last_index:

            char_index = last_index[strng[i]]
            start = max(char_index + 1, start)

        result = max(result, i - start + 1)

        last_index[strng[i]] = i
    return result

print(longestUniqueSubsttr('abcddafvadc'))
# 4 12 20 5
# 0 4 16 36 41
