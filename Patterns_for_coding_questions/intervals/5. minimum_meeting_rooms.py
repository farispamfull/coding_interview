# https://medium.com/@edward.zhou/leetcode-253-meeting-rooms-ii-explained-python3-solution-3f8869612df
from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.end < other.end


def min_meeting_rooms(meetings):
    meetings.sort()

    minRooms = 0
    minHeap = []
    for meeting in meetings:
        # если отрезок не пересекается с минимальным, мы его выталкиваем из кучи
        # все благодаря сортирови по [0][0] и [0][1]
        # следующие отрезки будут обладать большим временем начала
        # и большим временем конца
        if len(minHeap) > 0 and meeting[0] >= minHeap[0]:
            heappop(minHeap)
        # добавляем текущий end в кучу
        heappush(minHeap, meeting[1])
        # обновляем количество активных комнат
        minRooms = max(minRooms, len(minHeap))
    return minRooms


min_meeting_rooms(
    [[4, 5], [2, 3], [2, 4], [3, 5]])
