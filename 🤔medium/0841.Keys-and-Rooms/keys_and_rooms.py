# 841. Keys and Rooms
# https://leetcode.com/problems/keys-and-rooms/

from collections import defaultdict

LOCKED = False
OPENED = True


class Solution:

    def searchOpenedRoom(self, key, rooms, status):

        for k in rooms[key]:
            if status[k] == OPENED:
                continue
            status[k] = OPENED
            self.searchOpenedRoom(k, rooms, status)

    def canVisitAllRooms(self, rooms: 'List[List[int]]') -> 'bool':

        status = defaultdict(bool)
        # room 0 is not locked
        status[0] = OPENED
        for key in range(len(rooms)):
            if status[key] == OPENED:
                self.searchOpenedRoom(key, rooms, status)

        return all(status.values())


if __name__ == '__main__':
    sol = Solution()
    assert sol.canVisitAllRooms([[1], [2], [3], []]) is True
    assert sol.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]) is False
