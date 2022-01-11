# Наименьшее окно, содержащее все символы самой строки
from collections import defaultdict


def findSubString(strr):
    pattern = len(set(list(strr)))
    start = 0
    end = 0
    result_map = defaultdict()
    result_start = 0
    result_end = len(strr)
    while end < len(strr):

        result_map[strr[map]] += 1

        if pattern == len(result_map):

            while result_map[strr[start]] > 1:
                result_map[strr[start]] -= 1
                start += 1
            if result_end - result_start > end - start:
                result_end = end
                result_start = start
        end += 1
    return strr[result_start:result_end+1]
